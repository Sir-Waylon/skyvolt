const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/axiom/app/index.html');await p.waitForTimeout(500);
const ids=await p.evaluate(()=>{const o={};QS.forEach(q=>{if(!o[q.type])o[q.type]=q.id});return o});
const go=id=>p.evaluate(i=>{startSess({kind:'practice',title:'Practice',steps:[{k:'try',it:mkItem(i)}]})},id);
// angle by keyboard
await go(ids.angle);await p.waitForTimeout(100);await p.focus('#angsv');for(let i=0;i<20;i++)await p.keyboard.press('ArrowRight');
console.log('angle val',await p.evaluate(()=>Z.steps[0].it.val),await p.getAttribute('#angsv','aria-valuenow'),'focused',await p.evaluate(()=>document.activeElement.id));
await p.fill('#angin','42');console.log('typed',await p.evaluate(()=>Z.steps[0].it.val));
// point alt
await go(ids.point);await p.waitForTimeout(100);await p.click('details.alt summary');await p.fill('#ptx','3');await p.fill('#pty','-2');await p.click('#ptset');await p.waitForTimeout(100);console.log('point',await p.evaluate(()=>Z.steps[0].it.pt),'live:',await p.textContent('#live'));
// chips keyboard
await go(ids.chips);await p.waitForTimeout(100);await p.focus('.ch');await p.keyboard.press('Enter');await p.waitForTimeout(100);console.log('chip filled',await p.evaluate(()=>Z.steps[0].it.bl),'focus',await p.evaluate(()=>document.activeElement.className));
// mcq: select with space, check, announce
await go(ids.mcq);await p.focus('.opt');await p.keyboard.press('Space');await p.waitForTimeout(100);console.log('mcq focus kept',await p.evaluate(()=>document.activeElement.className));
// voice stub
await p.evaluate(()=>{window.__sp=[];window.speechSynthesis.speak=u=>__sp.push(u.text);});await p.click('.speak');console.log('spoken',await p.evaluate(()=>window.__sp.slice(0,2)));
console.log('dialog',await p.getAttribute('#sess','role'),'inert',await p.evaluate(()=>document.getElementById('shell').inert),e);await b.close()})()
