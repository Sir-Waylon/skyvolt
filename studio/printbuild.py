#!/usr/bin/env python3
"""printbuild.py <pack.json> <outdir> : builds B/W US-Letter PDFs for any scioly pack"""
import json,sys,os,subprocess
d=os.path.dirname(os.path.abspath(__file__))+'/engine/'
pack=json.load(open(sys.argv[1],encoding='utf8'));out=sys.argv[2];os.makedirs(out,exist_ok=True)
css=open(d+'print.css',encoding='utf8').read()
js=open(d+'engine.fig.js',encoding='utf8').read()+'\n'+open(d+'print.js',encoding='utf8').read()
js='var P='+json.dumps(pack,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+';\n'+js
html=f'<!doctype html><meta charset="utf-8"><style>{css}</style><body><script>{js}</script></body>'
open(out+'/_print.html','w',encoding='utf8').write(html)
names=[('notes','Study_Notes'),('quick','Quick_Reference'),('plan','Plan_Stations_Checklist'),('testA','Practice_Test_A'),('keyA','Practice_Test_A_KEY'),('testB','Practice_Test_B'),('keyB','Practice_Test_B_KEY'),('cards','Flashcards_Print_Duplex')]
json.dump({'html':out+'/_print.html','docs':[[a,f'{out}/{b}.pdf'] for a,b in names]},open(out+'/_jobs.json','w'))
subprocess.check_call(['node',d+'pdf.js',out+'/_jobs.json'],env={**os.environ,'NODE_PATH':subprocess.check_output(['npm','root','-g']).decode().strip()})
