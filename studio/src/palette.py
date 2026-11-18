import json
# Brand palettes: single source is src/brand.json (AA contrast checked in mksite.py)
PAL=json.load(open('src/brand.json'))['trainers']
for k,v in PAL.items():
    f='events/%s/pack.json'%k
    try:p=json.load(open(f,encoding='utf8'))
    except Exception:continue
    p['meta']['accent']=v;json.dump(p,open(f,'w'),ensure_ascii=False,separators=(',',':'))
print('palette applied')
