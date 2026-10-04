"""Measure 100-row pilot before upper-bound benchmark; local staging evidence."""
import csv,io,json,resource,sys,time,tempfile,os
from pathlib import Path
from types import SimpleNamespace
ROOT=Path(__file__).resolve().parents[1];LAB=ROOT/'labs/molecular-similarity'
sys.path.insert(0,str(LAB/'models/search'))
from src.search import MolecularSimilarity

def invoke(n):
    data=io.StringIO();w=csv.writer(data);w.writerow(['molecule_id','smiles'])
    compounds=['CCO','CCCO','CCCCO','CCN','CC(=O)O','c1ccccc1','N[C@@H](C)C(=O)O','N[C@H](C)C(=O)O','CC(=O)[O-].[Na+]']
    for i in range(n):w.writerow([f'molecule-{i:05}',compounds[i%len(compounds)]])
    module=MolecularSimilarity();started=time.monotonic()
    output=module.execute({k:SimpleNamespace(value=v) for k,v in {'query_smiles':'CCO','collection_csv':data.getvalue(),'top_k':100}.items()},context=None)
    elapsed=time.monotonic()-started
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform!='darwin':peak*=1024
    receipt=output['report']['receipt']
    assert receipt['searched_entries']==n and receipt['invalid_entries']==0
    assert elapsed<=120 and peak<=512*1024*1024
    return {'rows':n,'status':'PASS','calculation_seconds':receipt['calculation_seconds'],'total_seconds':elapsed,'process_peak_rss_bytes':peak,'returned_hits':len(output['report']['hits']),'collection_bytes':receipt['collection_size_bytes'],'allocation_limit_bytes':512*1024*1024}
if __name__=='__main__':
    records=[]
    with tempfile.TemporaryDirectory() as temp:
        os.chdir(temp)
        for n in [100,10000]:
            record=invoke(n);records.append(record);print(json.dumps(record),flush=True)
    (ROOT/'reports/local-benchmark.json').write_text(json.dumps({'scope':'Local staging process; not Modal/hosted evidence','python':sys.version,'pilot_before_upper_bound':True,'records':records},indent=2)+'\n')
