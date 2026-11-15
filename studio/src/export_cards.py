import json,sys,os
# exports lesson cards for deep-dive authoring: audit/lessons/<event>_<unit>.txt
out='../audit/lessons';os.makedirs(out,exist_ok=True)
ev=sys.argv[1];p=json.load(open('events/%s/pack.json'%ev,encoding='utf8'));Q={q['id']:q for q in p['questions']}
for u in p['units']:
    L=[]
    for les in u['lessons']:
        L.append('## LESSON %s: %s'%(les['id'],les['title']))
        for i,c in enumerate(les['cards']):
            q=Q.get(c.get('q'));L.append('KEY %s#%d | %s | %s%s%s'%(les['id'],i,c['h'],c['t'],(' | FORMULA: '+c['f']) if c.get('f') else '',(' | CHECK Q: '+q['q'][:140]) if q else ''))
    open('%s/%s_%s.txt'%(out,ev.split('-')[0],u['id']),'w').write('\n'.join(L))
print(ev,len(p['units']),'units')
