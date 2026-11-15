#!/usr/bin/env python3
"""build.py <pack.json> <out.html> : generic scioly engine build (any event pack)"""
import json,sys,os
d=os.path.dirname(os.path.abspath(__file__))+'/engine/'
pack=json.load(open(sys.argv[1],encoding='utf8'))
css=open(d+'engine.css',encoding='utf8').read()+open(d+'engine.theme.css',encoding='utf8').read();body=open(d+'engine.body.html',encoding='utf8').read()
js=''.join(open(d+f,encoding='utf8').read()+'\n' for f in ['engine.core.js','engine.fig.js','engine.quiz.js','engine.views.js','engine.extra.js'])
js=js.replace('__PACK__',json.dumps(pack,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
m=pack['meta']
out=f'''<title>{m['title']} {m['division']} Trainer</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap">
<style>
{css}
</style>
{body}
<script>
{js}
</script>
'''
open(sys.argv[2],'w',encoding='utf8').write(out);print(len(out)//1024,'KB')
