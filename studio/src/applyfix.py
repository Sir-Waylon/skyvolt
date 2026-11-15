import json,sys,os
p=json.load(open(sys.argv[1],encoding="utf8"));fx=json.load(open(sys.argv[2])) if os.path.exists(sys.argv[2]) else {};n=0
for q in p["questions"]:
    f=fx.get(q["id"])
    if f:
        for k,v in f.items():q[k]=v
        n+=1
json.dump(p,open(sys.argv[1],"w"),ensure_ascii=False,separators=(",",":"));print("fixes",sys.argv[2],n)
