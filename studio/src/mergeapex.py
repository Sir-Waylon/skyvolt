"""mergeapex.py <vertex pack> <apex pack> <out>  -> one pack: Algebra 1 -> Geometry readiness first, then Apex. meta.id stays 'apex-math'."""
import json,sys
a=json.load(open(sys.argv[1]));b=json.load(open(sys.argv[2]))
o=json.loads(json.dumps(b))
for k in ['topics','notes','cards','written','bench','safety','checklist','questions','proofs','units']:
    o[k]=(a.get(k) or [])+(b.get(k) or [])
pl=[]
for i,w in enumerate((a.get('plan') or [])+(b.get('plan') or [])):
    w=dict(w);w['t']='Week %d'%(i+1);pl.append(w)
o['plan']=pl
o['study']={}
for k in set(a['study'])|set(b['study']):
    x,y=a['study'].get(k),b['study'].get(k)
    o['study'][k]=({**(x or {}),**(y or {})} if isinstance(x or y,dict) else (x or [])+(y or []))
m=o['meta']
m.update(title='Apex',division='',brand='Apex',tagline='Algebra 1 to Calculus III',tag='Algebra 1 to Calculus III',
  refresh=a['meta'].get('refresh'),target=a['meta'].get('target'),accent=b['meta'].get('accent'))
ids=[t['id'] for t in o['topics']];assert len(ids)==len(set(ids)),'topic id clash'
qs=[q['id'] for q in o['questions']];assert len(qs)==len(set(qs)),'question id clash'
json.dump(o,open(sys.argv[3],'w'),ensure_ascii=False,separators=(',',':'))
print('merged',len(ids),'topics',len(qs),'questions')
