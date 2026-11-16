import json,os
P='/tmp/claude-0/-home-claude/bdb1ee03-0916-54eb-a354-ea75cf26b960/scratchpad/kit/src/dd/dd_meteorology.json'
def save(d):
    cur=json.load(open(P)) if os.path.exists(P) else {}
    cur.update(d)
    json.dump(cur,open(P,'w'),ensure_ascii=False,indent=1)
    print(len(cur))
def E(why,pic,an,ways,q,steps,trap,tip):
    return dict(why=why,pic=pic,analogy=an,ways=[list(w) for w in ways],ex=dict(q=q,steps=steps),trap=trap,tip=tip)
