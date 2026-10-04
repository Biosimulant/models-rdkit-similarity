"""Fetch MCP-authorized bytes; never persist or print temporary capability URLs."""
import base64,hashlib,json,sys,urllib.request
from pathlib import Path
request=json.load(sys.stdin);data=request['data'];destination=Path(sys.argv[1]);destination.parent.mkdir(parents=True,exist_ok=True)
try:
    if data.get('content_base64'):raw=base64.b64decode(data['content_base64'],validate=True)
    elif data.get('content',{}).get('base64'):raw=base64.b64decode(data['content']['base64'],validate=True)
    else:
        req=urllib.request.Request(request['links']['download'],headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=40) as response:raw=response.read(data['size_bytes']+1024)
    record={'artifact_id':data.get('artifact_id'),'declared_size_bytes':data['size_bytes'],'actual_size_bytes':len(raw),'declared_sha256':data['sha256'],'actual_sha256':hashlib.sha256(raw).hexdigest()}
    record['verified']=record['actual_size_bytes']==record['declared_size_bytes'] and record['actual_sha256']==record['declared_sha256']
    destination.write_bytes(raw);destination.with_name(destination.name+'.verification.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record))
except urllib.error.HTTPError as exc:
    print(json.dumps({'artifact_id':data.get('artifact_id'),'verified':False,'download_http_status':exc.code,'error':'MCP artifact capability download failed'}));sys.exit(1)
