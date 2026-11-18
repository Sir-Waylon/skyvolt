import json
# Brand palettes (coolors.co-style harmonies, each primary checked for AA contrast with white text)
PAL={'circuit-lab-b':['#2D6A4F','#D8F3DC'],'meteorology-b':['#0077B6','#CAF0F8'],'apex-math':['#BC4749','#F7E9D7'],'apex-merged':['#BC4749','#F7E9D7'],'quanta-physics':['#0F4C5C','#FFE9D2']}
for k,v in PAL.items():
    f='events/%s/pack.json'%k
    try:p=json.load(open(f,encoding='utf8'))
    except Exception:continue
    p['meta']['accent']=v;json.dump(p,open(f,'w'),ensure_ascii=False,separators=(',',':'))
print('palette applied')
