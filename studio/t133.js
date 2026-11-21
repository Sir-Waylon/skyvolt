const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const ctx=await b.newContext({viewport:{width:390,height:800}});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://skyvolt.localhost:8791/');await p.waitForSelector('#gate #acg');await p.click('[data-am="up"]');
await p.fill('#email','sync1@example.com');await p.fill('#username','syncer');await p.fill('#password','correct horse 99');await p.click('#acg');await p.waitForFunction(()=>!document.getElementById('gate'));
// earn xp on this trainer, push, then simulate progress on another trainer (meteorology-b) via the API
await p.evaluate(()=>{S.dgr={};ALL.forEach((x,i)=>S.dgr[x]=i%2);S.dg=today();S.xp=500;S.total=20;save();});
const r1=await p.evaluate(async()=>{const ck=()=>document.cookie.split('; ').find(c=>c.startsWith('__Host-csrf='))?.slice(12);
 const post=(path,b)=>fetch('/api/'+path,{method:'POST',credentials:'same-origin',headers:{'content-type':'application/json','x-csrf':ck()},body:JSON.stringify(b)}).then(r=>r.status);
 const a=await post('sync',{pack:'circuit-lab-b',state:{xp:500,total:20}});const m=await post('sync',{pack:'meteorology-b',state:{xp:400,total:15}});return [a,m]});
console.log('sync statuses',r1);
await p.evaluate(()=>{window.__ACC.me&&0});
await p.evaluate(()=>{go('me');window.__V.me=null;route()});
// trigger refresh by visibilitychange after bypassing the 45s throttle
await p.waitForTimeout(500);await p.evaluate(()=>{Object.defineProperty(document,'hidden',{value:false,configurable:true});document.dispatchEvent(new Event('visibilitychange'))});await p.waitForTimeout(1500);
console.log('combined level:',await p.evaluate(()=>JSON.stringify(vxLevel())));
console.log('me line:',await p.evaluate(()=>document.querySelector('.prof2 .small').textContent));
console.log('header ring title:',await p.evaluate(()=>document.getElementById('lvr').title));
console.log('sister row:',await p.evaluate(()=>{const a=[...document.querySelectorAll('a.rw2')].find(x=>/Axiom/.test(x.textContent));return a?a.textContent.trim().slice(0,60)+' -> '+a.href:'none'}));
await p.evaluate(()=>{window.__V.me='profile';route()});await p.waitForTimeout(300);console.log('profile card:',await p.evaluate(()=>(document.querySelector('.allx')||{}).textContent));
console.log('errors',errs);await b.close()})()
