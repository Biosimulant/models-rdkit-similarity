import base64
import csv
import hashlib
import io
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB / 'models/search'))
from src.search import MolecularSimilarity, search, PARAMETERS, MAX_BYTES
from rdkit import Chem, DataStructs, rdBase
from rdkit.Chem import AllChem
from PIL import Image

FIXTURE = (LAB / 'fixtures/example.csv').read_text()


def csv_for(rows):
    stream = io.StringIO()
    writer = csv.writer(stream, lineterminator='\n')
    writer.writerow(['molecule_id', 'smiles'])
    writer.writerows(rows)
    return stream.getvalue()


def test_independent_complete_ranking_and_scores_A1():
    # Independent legacy upstream function, not the wrapper's generator.
    query = Chem.MolFromSmiles('CCO')
    with rdBase.BlockLogs():
        query_fp = AllChem.GetMorganFingerprintAsBitVect(query, 2, nBits=2048, useChirality=True)
        expected = []
        for i, row in enumerate(csv.DictReader(io.StringIO(FIXTURE))):
            mol = Chem.MolFromSmiles(row['smiles'])
            if mol is None or mol.GetNumAtoms() == 0:
                continue
            fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048, useChirality=True)
            expected.append((float(DataStructs.TanimotoSimilarity(query_fp, fp)), row['molecule_id'], i))
    expected.sort(key=lambda x: (-x[0], x[1], x[2]))
    report = search('CCO', FIXTURE, top_k=100)
    assert [(h['molecule_id'], h['row_index']) for h in report['hits']] == [(e[1], e[2]) for e in expected]
    assert [h['score'] for h in report['hits']] == pytest.approx([e[0] for e in expected], abs=1e-12, rel=0)
    assert all(0 <= h['score'] <= 1 for h in report['hits'])
    assert report['hits'][0]['score'] == 1.0


def test_duplicate_equivalent_invalid_counts_checksums_A2_A4():
    report = search('CCO', FIXTURE, top_k=100)
    exact = [h for h in report['hits'] if h['exact_match']]
    assert [(h['molecule_id'], h['row_index']) for h in exact] == [('ethanol', 0), ('ethanol', 2), ('ethanol-equivalent', 1)]
    assert all(h['score'] == 1 for h in exact)
    assert [(r['molecule_id'], r['row_index']) for r in report['invalid_rows']] == [('invalid', 11), ('blank', 12)]
    r = report['receipt']
    assert (r['collection_rows'], r['valid_entries'], r['searched_entries'], r['invalid_entries']) == (13, 11, 11, 2)
    assert r['collection_sha256'] == hashlib.sha256(FIXTURE.encode()).hexdigest()
    assert r['query_sha256'] == hashlib.sha256(b'CCO').hexdigest()
    assert r['fingerprint_parameters'] == PARAMETERS
    assert len({h['row_index'] for h in report['hits']}) == 11


def test_threshold_top_k_ties_no_matches_A2():
    full = search('CCO', FIXTURE, top_k=100)['hits']
    boundary = full[3]['score']
    result = search('CCO', FIXTURE, top_k=100, minimum_similarity=boundary)
    assert result['hits'] == [h for h in full if h['score'] >= boundary]
    assert search('CCO', FIXTURE, top_k=1)['hits'] == full[:1]
    empty = search('CCO', csv_for([('x', 'c1ccccc1')]), minimum_similarity=1)
    assert empty['hits'] == [] and empty['receipt']['threshold_hit_count'] == 0
    tied = search('CCO', csv_for([('é', 'CCO'), ('Z', 'CCO'), ('a', 'CCO'), ('Z', 'OCC')]), top_k=100)
    assert [(h['molecule_id'], h['row_index']) for h in tied['hits']] == [('Z', 1), ('Z', 3), ('a', 2), ('é', 0)]


def test_chirality_setting_A3():
    left, right = 'N[C@@H](C)C(=O)O', 'N[C@H](C)C(=O)O'
    result = search(left, csv_for([('left', left), ('right', right)]), top_k=100)
    assert result['hits'][0]['score'] == 1 and result['hits'][0]['exact_match']
    opposite = result['hits'][1]
    assert opposite['score'] < 1 and not opposite['exact_match']
    with rdBase.BlockLogs():
        fps = [AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(s), 2, nBits=2048, useChirality=True) for s in [left, right]]
        assert opposite['score'] == pytest.approx(DataStructs.TanimotoSimilarity(*fps), abs=1e-12, rel=0)
        control = [AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(s), 2, nBits=2048, useChirality=False) for s in [left, right]]
        assert DataStructs.TanimotoSimilarity(*control) == 1
    assert result['receipt']['fingerprint_parameters']['includeChirality'] is True


@pytest.mark.parametrize('kwargs', [{'top_k':0},{'top_k':101},{'top_k':1.5},{'top_k':True},
    {'minimum_similarity':-0.1},{'minimum_similarity':1.1},{'minimum_similarity':float('nan')},
    {'minimum_similarity':float('inf')},{'minimum_similarity':True}])
def test_invalid_options(kwargs):
    with pytest.raises(ValueError):
        search('CCO', FIXTURE, **kwargs)


@pytest.mark.parametrize('query', ['', 'not-smiles', '*', 'CO(C)C', 'C'*257, 'C'*8193])
def test_query_rejection(query):
    with pytest.raises(ValueError):
        search(query, FIXTURE)


@pytest.mark.parametrize('text', ['id,smiles\nx,CCO\n', 'molecule_id,smiles\n',
    'molecule_id,smiles\nx,CCO,extra\n', 'molecule_id,smiles\n"unterminated,CCO\n', 'x'* (MAX_BYTES+1)])
def test_csv_rejection(text):
    with pytest.raises(ValueError):
        search('CCO', text)


def test_per_row_structure_and_id_errors():
    result = search('CCO', csv_for([('', 'CCO'), ('long', 'C'*257), ('wildcard', '*'), ('valence', 'CO(C)C'), ('ok', '[Na+].[Cl-]')]))
    assert len(result['invalid_rows']) == 4
    assert [r['error_code'] for r in result['invalid_rows']] == ['id_limit', 'structure_limit', 'unsupported_structure', 'sanitize_error']
    assert result['hits'][0]['canonical_smiles'] == '[Cl-].[Na+]'


def test_file_input_exact_bytes_and_oversize_rows(tmp_path):
    path = tmp_path / 'collection.csv'
    raw = b'\xef\xbb\xbf' + FIXTURE.replace('\n','\r\n').encode()
    path.write_bytes(raw)
    result = search('CCO', collection_file=str(path), top_k=100)
    assert result['receipt']['collection_sha256'] == hashlib.sha256(raw).hexdigest()
    assert result['receipt']['collection_size_bytes'] == len(raw)
    with pytest.raises(ValueError):
        search('CCO', FIXTURE, collection_file=str(path))
    with pytest.raises(ValueError):
        search('CCO', csv_for([(str(i), 'CCO') for i in range(10001)]))


def test_computed_visuals_downloads_no_hits_and_isolation(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    component = MolecularSimilarity()
    inputs = lambda **values: {k: SimpleNamespace(value=v) for k,v in values.items()}
    output = component.execute(inputs(query_smiles='CCO', collection_csv=FIXTURE, top_k=100), context=None)
    report = output['report']
    visuals = component.visualize()
    assert {v['render'] for v in visuals} == {'image','bar','table','text'}
    bar = next(v for v in visuals if v['render']=='bar')
    assert [i['value'] for i in bar['data']['items']] == [h['score'] for h in report['hits']]
    assert json.loads(Path(output['rankings_json']).read_text()) == report
    assert len(list(csv.DictReader(Path(output['rankings_csv']).open()))) == len(report['hits'])
    assert json.loads(Path(output['receipt_file']).read_text()) == report['receipt']
    Image.open(output['drawings']).verify()
    image = next(v for v in visuals if v['render']=='image')
    Image.open(io.BytesIO(base64.b64decode(image['data']['src'].split(',',1)[1]))).verify()
    second = component.execute(inputs(query_smiles='CCO', collection_csv=csv_for([('benzene', 'c1ccccc1')]), minimum_similarity=1), context=None)
    assert second['report']['hits'] == []
    assert len(component.visualize()) == 2
    assert output['rankings_json'] != second['rankings_json']
    assert 'ethanol' not in Path(second['rankings_json']).read_text()


def test_csv_formula_safety_preserves_json(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    module = MolecularSimilarity()
    output = module.execute({'query_smiles':SimpleNamespace(value='CCO'), 'collection_csv':SimpleNamespace(value=csv_for([('=danger', 'CCO')]))},context=None)
    assert output['report']['hits'][0]['molecule_id'] == '=danger'
    assert list(csv.DictReader(Path(output['rankings_csv']).open()))[0]['molecule_id'] == "'=danger"
