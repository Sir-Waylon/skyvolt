import json,re,sys,collections
NUM=re.compile(r'-?\d+(?:\.\d+)?')
def nums(s):
    out=set()
    for m in NUM.findall(str(s).replace('−','-').replace(',','')):
        try:out.add(round(float(m),6))
        except:pass
    return out
tot=collections.Counter();flag=collections.defaultdict(list)
for slug in sys.argv[1:]:
    P=json.load(open(f'events/{slug}/pack.json'))
    for q in P['questions']:
        t=q.get('type','mcq');i=q['id'];tot[slug]+=1
        txt=' '.join(map(str,q.get('sol',[])))+' '+str(q.get('w',''))
        if t in('mcq','short') and q.get('o'):
            o=q['o']
            if len(set(map(str,o)))!=len(o):flag[slug,'dup-options'].append(i)
            if not q.get('sol') and not q.get('w'):flag[slug,'no-solution'].append(i)
            a=nums(o[0])
            if a and txt.strip() and not (a & nums(txt)) and len(txt)>25 and not any(w in q['q'].lower() for w in('which','why')):
                flag[slug,'answer-num-not-in-solution'].append(i)
        if q.get('num') and 'v' in q['num']:
            v=q['num']['v']
            if txt.strip() and len(nums(txt))>0:
                tn=nums(txt)
                if not any(abs(v-x)<=max(abs(v)*0.02,0.006) for x in tn) and not any(abs(v)<1e-3 for _ in[0]):
                    flag[slug,'num-v-not-in-solution'].append(i)
        if t=='mcq' and len(q.get('o',[]))<3:flag[slug,'few-options'].append(i)
        if len(q.get('q',''))>420:flag[slug,'long-stem'].append(i)
for k,v in sorted(flag.items()):print(k,len(v),v[:8])
print(dict(tot))
