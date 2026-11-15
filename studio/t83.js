const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(200);
await p.evaluate(()=>document.querySelector('[data-nav="lib:labs"]').click());await p.waitForTimeout(200);
const labs=await p.$$eval('[data-lab]',a=>a.map(x=>x.dataset.lab));console.log('labs',labs.join(','));
const pos=()=>p.evaluate(()=>{const c=document.querySelector('#lsv circle[fill="#5b4bff"]');return c?c.getAttribute('cx')+','+c.getAttribute('cy'):'none'});
await p.evaluate(()=>document.querySelector('[data-lab="proj"]').click());await p.waitForTimeout(300);
console.log('bar',await p.$('.labbar')!==null);
await p.evaluate(()=>{document.querySelector('[data-lc="h:30"]').click()});await p.click('[data-la="fire"]');await p.waitForTimeout(300);const a=await pos();
await p.click('[data-lk="pp"]');await p.waitForTimeout(150);const b1=await pos();await p.waitForTimeout(600);const b2=await pos();
console.log('paused frozen',b1===b2,'btn',await p.$eval('[data-lk="pp"]',e=>e.textContent));
await p.click('[data-lk="pp"]');await p.waitForTimeout(500);const c1=await pos();console.log('resumed moves',c1!==b2,a,b2,c1);
await p.click('[data-lk="sp:0.25"]');console.log('speed on',await p.$eval('[data-lk="sp:0.25"]',e=>e.className));
for(const l of ['swing','coll','bulb']){await p.evaluate(()=>document.querySelector('[data-lab=""]').click());await p.waitForTimeout(150);await p.evaluate(l=>document.querySelector('[data-lab="'+l+'"]').click(),l);await p.waitForTimeout(500);
 await p.click('[data-lk="pp"]');await p.waitForTimeout(200);await p.click('[data-lk="pp"]');await p.click('[data-lk="rs"]');await p.waitForTimeout(300);console.log(l,'ok bar',!!(await p.$('.labbar')),(await p.evaluate(()=>document.getElementById('labroot').innerHTML.length)))}
await p.screenshot({path:'shots/t83.png'});console.log(E);await b.close()})()
