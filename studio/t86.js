const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const app of ['_app_skyvolt/circuit','_app_axiom/apex']){
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();p.setDefaultTimeout(2500);const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(500);
console.log(app,'gate before:',await p.evaluate(()=>/placement/i.test(document.getElementById('main').innerText)||document.getElementById('main').innerText.slice(0,40)));
await p.evaluate(()=>document.querySelector('#nav button[data-t="me"]').click());await p.waitForTimeout(200);
await p.evaluate(()=>document.querySelector('[data-nav="me:dev"]').click());await p.waitForTimeout(200);
await p.fill('#devk','WRONG-CODE');await p.click('[data-dev="unlock"]');console.log('wrong:',await p.$eval('#devmsg',e=>e.textContent));
await p.fill('#devk','VX-EXP3-KUC2-55XK-BN9V');await p.click('[data-dev="unlock"]');await p.waitForTimeout(300);
console.log('unlocked:',await p.evaluate(()=>!!S.dev),'chip',!!(await p.$('#devchip')),'panel',await p.evaluate(()=>[...document.querySelectorAll('#main h3')].map(h=>h.textContent).join('|')));
console.log('plans:',await p.evaluate(()=>[...document.querySelectorAll('#main summary')].map(s=>s.innerText).join(' || ')));
await p.click('[data-dev="skip:gap"]');await p.waitForTimeout(300);
await p.evaluate(()=>document.querySelector('#nav button[data-t="learn"]').click());await p.waitForTimeout(300);
console.log('gate after skip:',await p.evaluate(()=>document.getElementById('main').innerText.slice(0,60).replace(/\n/g,' / ')));
await p.evaluate(()=>document.querySelector('#nav button[data-t="me"]').click());await p.evaluate(()=>document.querySelector('[data-nav="me:dev"]').click());await p.waitForTimeout(200);
const before=await p.evaluate(()=>Object.keys(S.cos.own).length);await p.click('[data-dev="cos"]');await p.click('[data-dev="coins"]');await p.waitForTimeout(200);
console.log('cosmetics',before,'->',await p.evaluate(()=>Object.keys(S.cos.own).length),'coins',await p.evaluate(()=>S.coins));
await p.click('[data-dev="off"]');await p.waitForTimeout(200);console.log('off: dev',await p.evaluate(()=>S.dev),'cos',await p.evaluate(()=>Object.keys(S.cos.own).length),'coins',await p.evaluate(()=>S.coins),'chip',!!(await p.$('#devchip')));
console.log(E);await p.close()}
await b.close()})()
