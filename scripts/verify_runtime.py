"""Local composed-runtime evidence, distinct from managed or hosted checks."""
import csv, hashlib, io, json, subprocess, sys, tempfile, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LAB=ROOT/'labs/molecular-similarity'

def main():
    fixture=(LAB/'fixtures/example.csv').read_text()
    cases=[('example-text',{'query_smiles':'CCO','collection_csv':fixture,'top_k':100},11),
           ('example-upload',{'query_smiles':'CCO','collection_file':str(LAB/'fixtures/example.csv'),'top_k':100},11),
           ('strict-threshold',{'query_smiles':'CCO','collection_csv':fixture,'minimum_similarity':0.6,'top_k':100},3),
           ('no-matches',{'query_smiles':'CCO','collection_csv':'molecule_id,smiles\nbenzene,c1ccccc1\n','minimum_similarity':1.0},0),
           ('chiral-pair',{'query_smiles':'N[C@@H](C)C(=O)O','collection_csv':'molecule_id,smiles\nleft,N[C@@H](C)C(=O)O\nright,N[C@H](C)C(=O)O\n','top_k':2},2)]
    records=[];roots=[]
    with tempfile.TemporaryDirectory() as temp:
        for label,inputs,count in cases:
            run_input=Path(temp)/'input.json';result_file=Path(temp)/'results.json'
            run_input.write_text(json.dumps({'parameters':{'initial_inputs':{'search.'+k:v for k,v in inputs.items()}}}))
            start=time.monotonic()
            result=subprocess.run([str(Path(sys.executable).with_name('biosimulant')),'--no-open','labs','run',str(LAB),'--no-install-deps','--require-local-capability','--run-input-file',str(run_input),'--results-file',str(result_file),'--json'],cwd=ROOT,capture_output=True,timeout=120)
            assert result.returncode==0,(label,result.stderr.decode(),result.stdout.decode()[:1500])
            payload=json.loads(result_file.read_text());outputs=payload['outputs']['search']
            assert len(outputs)==7
            report=outputs['report']['value'];hits=report['hits']
            assert len(hits)==count,(label,len(hits))
            assert json.loads(Path(outputs['rankings_json']['value']).read_text())==report
            assert len(list(csv.DictReader(Path(outputs['rankings_csv']['value']).open())))==count
            visuals=payload['visuals'][0]['visuals'];renders={v['render'] for v in visuals}
            assert renders==({'image','text','table','bar'} if count else {'image','text'})
            if count:
                bars=next(v for v in visuals if v['render']=='bar')['data']['items']
                assert [v['value'] for v in bars]==[h['score'] for h in hits]
            artifacts=[]
            for port in ['rankings_csv','rankings_json','invalid_csv','receipt_file','drawings']:
                p=Path(outputs[port]['value']);raw=p.read_bytes();artifacts.append({'port':port,'size_bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
            roots.append(Path(outputs['drawings']['value']).parent)
            records.append({'case':label,'status':'PASS','elapsed_seconds':time.monotonic()-start,'returned_hits':count,'eligible_hits':outputs['hit_count']['value'],'typed_outputs':7,'renders':sorted(renders),'artifacts':artifacts})
            if label=='example-text':
                (ROOT/'reports/local-example-results.json').write_text(json.dumps(payload,indent=2))
                import shutil
                shutil.copy2(outputs['drawings']['value'],ROOT/'reports/example-molecules.png')
        assert len(set(roots))==len(roots)
    evidence={'scope':'Local composed CLI from dedicated staging source; no managed Run, hosted deployment or end-to-end platform staging evidence','python':sys.version,'cases':records,'output_directory_isolation':'PASS'}
    (ROOT/'reports/local-runtime-verification.json').write_text(json.dumps(evidence,indent=2)+'\n')
    print(f'{len(records)} composed cases pass with seven outputs, exact downloads, visuals and isolation')
if __name__=='__main__':main()
