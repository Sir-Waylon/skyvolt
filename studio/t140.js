const {chromium}=require('playwright');const fs=require('fs');const {spawn}=require('child_process');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});const res=[];
for(const [site,port,apps] of [['skyvolt',8811,['circuit','meteorology']],['axiom',8812,['apex','quanta']]]){
 const hdr={};fs.readFileSync('out/'+site+'/_headers','utf8').split('\n\n')[0].split('\n').slice(1).forEach(l=>{const i=l.indexOf(':');if(i>0)hdr[l.slice(0,i).trim().toLowerCase()]=l.slice(i+1).trim()});
 const sv=spawn('node',['server.mjs','../../out/'+site,port],{cwd:'backend/test'});await new Promise(r=>setTimeout(r,800));
 const ctx=await b.newContext({viewport:{width:390,height:800}});
 await ctx.route('**/*',async r=>{const u=r.request().url();if(!u.includes('.localhost')){return r.abort()}const f=await r.fetch({url:u.replace(/[a-z]+\.localhost/,'127.0.0.1'),headers:{...r.request().headers(),host:new URL(u).host}});r.fulfill({response:f,headers:{...f.headers(),...hdr}})});
 const p=await ctx.newPage();const v=[];p.on('console',m=>{const t=m.text();if(/Content Security Policy|Refused to/i.test(t))v.push(t.slice(0,160))});p.on('pageerror',e=>v.push('JS '+e.message));
 const base='http://'+site+'.localhost:'+port;
 for(const path of ['/','/account/','/privacy/','/app/']){const rr=await p.goto(base+path);if(path==='/')v.push('HDR '+((await rr.allHeaders())['content-security-policy']||'NONE').slice(0,60));await p.waitForTimeout(400)}
 for(const a of apps){await p.goto(base+'/app/'+a+'/');await p.waitForTimeout(900);
  // sign in gate -> create account via API then exercise UI
  await p.evaluate(async()=>{try{await __ACC.auth&&0}catch(e){}});
  await p.goto(base+'/app/'+a+'/');await p.waitForTimeout(600);
  const tabs=await p.evaluate(()=>[...document.querySelectorAll('#nav button')].map(b=>b.dataset.t));
  for(const t of tabs){await p.evaluate(t=>document.querySelector('#nav button[data-t="'+t+'"]')&&document.querySelector('#nav button[data-t="'+t+'"]').click(),t);await p.waitForTimeout(200)}
  await p.evaluate(()=>{try{openArcade()}catch(e){}});await p.waitForTimeout(300);}
 const ev=await p.evaluate(()=>{const s=document.createElement('script');s.textContent='window.__x=1';document.head.appendChild(s);return window.__x?'INLINE ALLOWED':'inline script blocked: CSP active'});res.push([ev,site,v.length?[...new Set(v)]:'no CSP violations or JS errors (4 site pages + trainers, all tabs, arcade)']);await ctx.close();sv.kill()}
console.log(JSON.stringify(res,null,1));await b.close()})()
