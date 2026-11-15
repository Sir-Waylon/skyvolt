#!/usr/bin/env python3
"""build_secure.py <pack.json> <outdir> [passcode] : encrypted single-file trainer + hosting files"""
import json,sys,os,gzip,base64,hashlib,secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
d=os.path.dirname(os.path.abspath(__file__))+'/engine/'
pack=json.load(open(sys.argv[1],encoding='utf8'));out=sys.argv[2];os.makedirs(out,exist_ok=True)
words=['volt','amp','ohm','gate','diode','spark','coil','node','relay','logic','fuse','wire']
pw=sys.argv[3] if len(sys.argv)>3 else '-'.join([secrets.choice(words) for _ in range(3)])+'-'+str(secrets.randbelow(90)+10)
pack['_sec']=base64.b64encode(secrets.token_bytes(32)).decode()
raw=gzip.compress(json.dumps(pack,ensure_ascii=False,separators=(',',':')).encode(),9)
salt=secrets.token_bytes(16);iv=secrets.token_bytes(12);IT=600000
key=PBKDF2HMAC(hashes.SHA256(),32,salt,IT).derive(pw.strip().lower().encode())
ct=AESGCM(key).encrypt(iv,raw,None)
b=lambda x:base64.b64encode(x).decode()
enc={'id':pack['meta']['id'],'s':b(salt),'n':b(iv),'i':IT,'c':b(ct)}
rd=lambda f:open(d+f,encoding='utf8').read()
eng=''.join(rd(f)+'\n' for f in ['engine.core.js','engine.fig.js','engine.quiz.js','engine.views.js','engine.extra.js']).replace('var P=__PACK__;','var P=P0;')
loader=rd('secure.loader.js').replace('__ENC__',json.dumps(enc)).replace('__ENGINE__',eng)
h=hashlib.sha256(loader.encode()).digest();hs="'sha256-"+b(h)+"'"
csp=f"default-src 'none'; script-src {hs}; style-src 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src data:; connect-src 'none'; base-uri 'none'; form-action 'none'"
m=pack['meta']
lock='<div id="lock" hidden style="max-width:380px;margin:12vh auto;padding:24px"><div class="card"><h2>'+m['title']+' '+m['division']+'</h2><p class="mute small">Enter the class passcode from your coach.</p><form id="lf"><input id="lp" type="password" autocomplete="off" style="width:100%;border:1.5px solid var(--line);border-radius:10px;padding:12px;font-size:1.1rem;background:var(--surface);color:inherit" aria-label="Class passcode"><label class="small" style="display:block;margin:10px 0"><input type="checkbox" id="lr"> Remember on this device</label><button class="btn" id="lb" type="submit">Unlock</button><p id="le" class="small" role="alert"></p></form></div></div>'
css=rd('engine.css')+rd('engine.theme.css')+'body:not(.ok) .app{display:none}'
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta http-equiv="Content-Security-Policy" content="{csp}"><meta name="referrer" content="no-referrer"><title>{m['title']} {m['division']} Trainer</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap"><style>{css}</style></head><body>{lock}{rd('engine.body.html')}<script>{loader}</script></body></html>'''
open(out+'/index.html','w',encoding='utf8').write(page)
open(out+'/_headers','w').write("/*\n  Content-Security-Policy: "+csp+"; frame-ancestors 'none'\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: no-referrer\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Strict-Transport-Security: max-age=31536000\n  Cross-Origin-Opener-Policy: same-origin\n")
open(out+'/PASSCODE.txt','w').write(pw+'\n');print(len(page)//1024,'KB passcode:',pw)
