const {chromium}=require('playwright');const {spawn}=require('child_process');const fs=require('fs');
(async()=>{const s='axiom',port=8881;const hdr={};fs.readFileSync('out/'+s+'/_headers','utf8').split('\n\n')[0].split('\n').slice(1).forEach(l=>{const i=l.indexOf(':');if(i>0)hdr[l.slice(0,i).trim().toLowerCase()]=l.slice(i+1).trim()});
const sv=spawn('node',['server.mjs','../../out/'+s,String(port)],{cwd:'backend/test',stdio:'ignore'});await new Promise(r=>setTimeout(r,900));
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});const ctx=await b.newContext();const bad=[],reqs=[];
await ctx.route('**/*',async r=>{const u=r.request().url();if(!u.includes('.localhost')){bad.push('EXTERNAL '+u);return r.abort()}reqs.push(u.split('/').slice(-2).join('/'));const f=await r.fetch({url:u.replace(/[a-z]+\.localhost/,'127.0.0.1'),headers:{...r.request().headers(),host:new URL(u).host}});r.fulfill({response:f,headers:{...f.headers(),...hdr}})});
const p=await ctx.newPage();p.on('console',m=>{if(/Content Security|Refused|violat/i.test(m.text()))bad.push(m.text().slice(0,150))});
await p.goto('http://axiom.localhost:'+port+'/app/apex/');await p.waitForTimeout(1500);
await p.evaluate(()=>{const d=document.createElement('div');d.id='mt';d.textContent='Solve \\(x=\\frac{-b\\pm\\sqrt{b^2-4ac}}{2a}\\) and $$\\int_0^1 x^2dx$$';document.body.appendChild(d);window.typeset(d)});
await p.waitForTimeout(2500);
console.log('katex nodes',await p.evaluate(()=>document.querySelectorAll('#mt .katex').length),'fontsLoaded',await p.evaluate(()=>[...document.fonts].filter(f=>f.status==='loaded'&&/KaTeX/.test(f.family)).length));
console.log(reqs.filter(x=>/katex|woff2/.test(x)).join(' '));console.log('BAD',bad.join('|'));sv.kill();await b.close()})()
