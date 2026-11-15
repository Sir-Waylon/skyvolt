import json,sys,glob
# merges deep-dive data into lesson cards: files map "<lessonId>#<cardIndex>" -> dd object
pf=sys.argv[1];p=json.load(open(pf,encoding='utf8'));dd={}
for f in sorted(glob.glob(sys.argv[2])):dd.update(json.load(open(f,encoding='utf8')))
n=0
for u in p.get('units',[]):
    for L in u.get('lessons',[]):
        for i,c in enumerate(L['cards']):
            k='%s#%d'%(L['id'],i)
            if k in dd:c['dd']=dd[k];n+=1
json.dump(p,open(pf,'w'),ensure_ascii=False,separators=(',',':'));print('applydd',pf.split('/')[1],n)
