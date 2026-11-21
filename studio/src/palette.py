import json
# Brand palettes: single source is src/brand.json (AA contrast checked in mksite.py)
PAL=json.load(open('src/brand.json'))['trainers']
for k,v in PAL.items():
    f='events/%s/pack.json'%k
    try:p=json.load(open(f,encoding='utf8'))
    except Exception:continue
    sk=k in('circuit-lab-b','meteorology-b');p['meta']['site']='Skyvolt' if sk else 'Axiom';p['meta']['sister']='Axiom' if sk else 'Skyvolt';p['meta']['sisterDesc']='Math and Physics trainers' if sk else 'Circuit Lab and Meteorology trainers'
    p['meta']['accent']=v;json.dump(p,open(f,'w'),ensure_ascii=False,separators=(',',':'))
print('palette applied')
