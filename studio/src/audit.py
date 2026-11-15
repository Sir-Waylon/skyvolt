import json,re,sys,collections
P=json.load(open(sys.argv[1],encoding='utf8'));Q=P['questions']
STOP=set('the a an of to in is are and or for on with as at by from that this which what when be it its not than into does do'.split())
def words(s):return {w for w in re.findall(r"[a-z0-9]+",s.lower()) if w not in STOP and len(w)>2}
flag=collections.defaultdict(list)
for q in Q:
    if q['type'] not in('mcq','multi'):
        if q['type']=='short' and q.get('text'):
            for a in q['text']:
                if len(re.sub(r'\W','',a))>=4 and re.sub(r'\W','',a.lower()) in re.sub(r'\W','',q['q'].lower()):flag['short_ans_in_stem'].append(q['id'])
        continue
    co=[q['o'][i] for i in (q['a'] if q['type']=='multi' else [0])];wr=[x for i,x in enumerate(q['o']) if i not in(q['a'] if q['type']=='multi' else [0])]
    if q['type']=='mcq':
        c=q['o'][0];L=sorted((len(x) for x in q['o']),reverse=True)
        if len(c)==L[0] and len(c)>=1.25*L[1] and len(c)>16:flag['correct_much_longer'].append(q['id'])
        sw=words(q['q']);ov=[len(words(x)&sw) for x in q['o']]
        if ov[0]>=2 and ov[0]>max(ov[1:])+1:flag['correct_echoes_stem'].append(q['id'])
        if re.search(r'\b(always|never|only|none|cannot|impossible|every)\b',' '.join(wr),re.I) and not re.search(r'\b(always|never|only|none|cannot|impossible|every)\b',c,re.I):flag['absolute_in_wrong_only'].append(q['id'])
        if len(set(x.lower() for x in q['o']))<4:flag['dup_options'].append(q['id'])
        if any(re.search(r'all of the above|none of the above|both of the above',x,re.I) for x in q['o']):flag['all_none_above'].append(q['id'])
    for a in co:
        n=re.sub(r'[^a-z0-9]','',a.lower())
        if len(n)>=4 and not n.isdigit() and n in re.sub(r'[^a-z0-9]','',q['q'].lower()):flag['answer_in_stem'].append(q['id'])
st=[q['q'] for q in Q]
if len(set(st))!=len(st):flag['dup_stem'].append('x')
m=sum(1 for q in Q if q['type']=='mcq')
print('total',len(Q),'mcq',m)
for k,v in flag.items():print(' ',k,len(v),v[:6])
json.dump({k:v for k,v in flag.items()},open('src/audit_flags.json','w'))
