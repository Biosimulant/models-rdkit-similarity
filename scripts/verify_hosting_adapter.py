"""Execute candidate through a staging adapter with real isolated RDKit children."""
import base64,csv,hashlib,io,json,sys,tempfile,time
from pathlib import Path
from uuid import uuid4
from curated_serving.runner import execute
from curated_serving.spec import spec_digest

ROOT=Path(__file__).resolve().parents[1]
REPORTS=ROOT/'reports'
config=json.loads((REPORTS/'hosting-staging-candidate-spec.json').read_text())
archive=REPORTS/'rdkit-molecular-similarity-v011-candidate.bsilab'
fixture=(ROOT/'labs/molecular-similarity/fixtures/example.csv').read_bytes()
records=[]
with tempfile.TemporaryDirectory(prefix='similarity-hosting-adapter-') as temp:
 scratch=Path(temp)
 for label,payload,upload,threshold in [('pasted-example',fixture,False,0),('uploaded-example',b'\xef\xbb\xbf'+fixture.replace(b'\n',b'\r\n'),True,0.6)]:
  parameters={'query_smiles':'CCO','top_k':100,'minimum_similarity':threshold};file_contents=None
  if upload:
   parameters['collection_file']={'kind':'stored_file','file_id':str(uuid4()),'sha256':hashlib.sha256(payload).hexdigest(),'size_bytes':len(payload),'format':'csv'};file_contents={'collection_file':payload}
  else:parameters['collection_csv']=payload.decode()
  started=time.monotonic();result=execute(archive,config,parameters=parameters,file_contents=file_contents,invocation_id=label,expected_config_digest=spec_digest(config),scratch_parent=scratch)
  out=result['outputs']['search'];report=out['report']['value'];receipt=report['receipt'];assert receipt['collection_sha256']==hashlib.sha256(payload).hexdigest();assert (receipt['collection_rows'],receipt['valid_entries'],receipt['invalid_entries'])==(13,11,2)
  assert out['hit_count']['value']==(3 if upload else 11);assert len(out)==7
  visuals=result['visuals'][0]['visuals'];assert {v['render'] for v in visuals}=={'image','text','bar','table'}
  artifacts=[]
  for f in result['files']:
   raw=base64.b64decode(f['content']['base64'],validate=True);assert len(raw)==f['bytes'] and hashlib.sha256(raw).hexdigest()==f['sha256'];artifacts.append({k:f[k] for k in ['port','format','bytes','sha256']})
  assert len(artifacts)==5 and list(scratch.iterdir())==[]
  if upload:assert result['input_files']['collection_file']['sha256']==receipt['collection_sha256']
  records.append({'case':label,'status':'PASS','original_bytes_preserved':True,'returned_hits':len(report['hits']),'eligible_hits':out['hit_count']['value'],'elapsed_seconds':time.monotonic()-started,'typed_outputs':7,'renders':[v['render'] for v in visuals],'files':artifacts,'scratch_cleaned':True})
result={'scope':'Local isolated adapter built from synchronized staging; real Python3.12 RDKit child processes; not deployed core staging, managed compute or live hosted evidence','python':sys.version,'package_sha256':config['hub']['sha256'],'spec_sha256':spec_digest(config),'cases':records,'production':'Modal unchanged; no remote resources created'}
(REPORTS/'hosting-staging-adapter-verification.json').write_text(json.dumps(result,indent=2)+'\n');print('Two real-child hosting-adapter cases pass with original-byte identity, seven outputs, four visuals and five exact downloads')
