#!/usr/bin/env python3
"""dropunknown.py <pack.json>: remove questions whose topic is not in the pack's topic list (left over from removed advanced topics)."""
import json,sys
p=sys.argv[1];d=json.load(open(p));ids={t['id'] for t in d['topics']}
n=len(d['questions']);d['questions']=[q for q in d['questions'] if q['t'] in ids]
for k in ('cards',):
    pass
json.dump(d,open(p,'w'),ensure_ascii=False,separators=(',',':'));print('dropunknown',p,n-len(d['questions']),'removed')
