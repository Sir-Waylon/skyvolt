#!/usr/bin/env python3
"""build3.py <pack.json> <out.html> : engine v3 plain build (globals kept for tests)"""
import json,sys,os
d=os.path.dirname(os.path.abspath(__file__))+'/engine3/'
pack=json.load(open(sys.argv[1],encoding='utf8'))
css=open(d+'app.css',encoding='utf8').read()+open(d+'roster.css',encoding='utf8').read()+open(d+'widgets.css',encoding='utf8').read()
js=''.join(open(d+f,encoding='utf8').read()+'\n' for f in ['core.js','fig.js','char.js','roster1.js','people.js','session.js','brain.js','app.js','roster2.js','labs.js','audio.js','itypes.js','itypes2.js','interact.js','rewards.js','window.js','online.js','widgets.js','tools.js','sims.js','builders.js','builders2.js','goals.js','physdemo.js','games.js','rw.js','personal.js','style.js','accounts.js','refs.js','stn_core.js','stn_circ1.js','stn_circ2.js','stn_met1.js','stn_met2.js','extras.js','tracks.js','shorts.js','metacog.js','curric.js','today.js','lock.js','icons.js','course.js','a11y.js','print.js','ctl.js','dive.js','order.js','ui2.js','flash.js','play.js','sandbox.js','labs2.js','labs3.js','labs4.js','graph.js','dev.js'])
js=js.replace('__PACK__',json.dumps(pack,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
m=pack['meta']
out=f'''<!doctype html><html lang="en" data-theme="auto"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>{m['title']} {m['division']}</title><style>{css}</style></head><body class="ok"><script>
{js}
</script></body></html>'''
open(sys.argv[2],'w',encoding='utf8').write(out);print(len(out)//1024,'KB')
