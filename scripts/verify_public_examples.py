import hashlib,json,urllib.request,urllib.error
from pathlib import Path
r=Path(__file__).resolve().parents[1]/'reports'
api='https://api.biosimulant.com/api'
def get(route):
 with urllib.request.urlopen(urllib.request.Request(api+route,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as f:return f.read(),f.status
checks=[]
for prefix,run in [('managed-pilot','0850f12f-e803-4876-8f98-1df512b2e7fd'),('managed-threshold-low','1169e304-181a-44ad-b089-8d252145cd41'),('managed-threshold-high','e4b31111-37b1-4faa-aead-323bcd0b54a5')]:
 raw,status=get('/runs/'+run); data=json.loads(raw);assert data['is_public'] is True
 checks.append({'run_id':run,'anonymous_status':status,'is_public':True})
 metadata=json.loads((r/(prefix+'-status.json')).read_text())['data']
 for a in metadata['artifacts']:
  if a['role']=='report':continue
  raw,code=get('/runs/'+run+'/artifacts/'+a['artifact_id']); h=hashlib.sha256(raw).hexdigest();assert len(raw)==a['size_bytes'] and h==a['sha256']
  checks.append({'run_id':run,'artifact_id':a['artifact_id'],'role':a['role'],'anonymous_status':code,'bytes':len(raw),'sha256':h,'verified':True})
raw,status=get('/labs/f0291213-a063-4aeb-8981-8e0e739f665d/runs');listing=json.loads(raw)
checks.append({'public_lab_runs_status':status,'public_lab_runs_count':listing['total'] if isinstance(listing,dict) else len(listing)})
(r/'public-examples-verification.json').write_text(json.dumps({'scope':'Anonymous requests; no owner credentials; only original deliberately shareable fixtures','checks':checks},indent=2)+'\n')
print('Anonymous example run and non-HTML artifact bytes all verified:',len(checks),'checks')
