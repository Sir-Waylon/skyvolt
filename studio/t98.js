const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:360,height:740}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.click('#nav button[data-t="library"]');await p.waitForTimeout(300);
await p.click('[data-nav="lib:stations"]');await p.waitForTimeout(400);
console.log('btns',await p.evaluate(()=>[...document.querySelectorAll('button')].map(b=>b.textContent.trim().slice(0,30)).slice(0,25)));
await p.screenshot({path:'shots/t98_a.png'});
for(const nm of ['LED and resistor','Logic from a truth table','Three-way switch']){const bt=p.locator('button',{hasText:nm}).first();await bt.click();await p.waitForTimeout(400);console.log(nm,'segs',await p.evaluate(()=>document.querySelectorAll('.segs').length),'sel',await p.evaluate(()=>document.querySelectorAll('select').length));await p.screenshot({path:'shots/t98_'+nm[0]+'.png'});await p.goBack().catch(()=>{});const bk=await p.$('[data-back]');if(bk)await bk.click();await p.waitForTimeout(300)}
console.log('segs',await p.evaluate(()=>document.querySelectorAll('.segs').length),'selects',await p.evaluate(()=>document.querySelectorAll('select').length));
await p.screenshot({path:'shots/t98_b.png'});console.log(E)
await b.close()})()
