const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [w,h] of [[360,640],[320,568],[1100,760]]){
const p=await (await b.newContext({viewport:{width:w,height:h}})).newPage();p.setDefaultTimeout(4000);const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;QS.slice(0,6).forEach((q,i)=>{S.mem[q.id]=[i%3,dayN()-2+BOX[i%3],2]});route();startMission()});await p.waitForTimeout(900);
// advance to first try
for(let g=0;g<20;g++){const k=await p.evaluate(()=>Z.steps[Z.i].k);if(k==='try')break;await p.evaluate(()=>{const e=document.querySelector('#go,#exf,#exb,#exs,#exq,#exn');e&&e.click()});await p.waitForTimeout(80)}
const geo=()=>p.evaluate(()=>{const f=document.querySelector('.sheet'),s=document.getElementById('sess').getBoundingClientRect(),r=f&&f.getBoundingClientRect(),b=document.querySelector('.s-body').getBoundingClientRect();return JSON.stringify({vh:innerHeight,footBottom:r&&r.bottom,footTop:r&&r.top,bodyBottom:b.bottom,cls:f&&f.className})});
console.log(w,'pre',await geo());
await p.screenshot({path:`shots/t96_${w}_a.png`});
await p.click('#smn');await p.waitForTimeout(100);await p.screenshot({path:`shots/t96_${w}_m.png`});
console.log('menu items',await p.evaluate(()=>document.querySelectorAll('.smenu .mi,.smenu .cfd').length));
await p.keyboard.press('Escape');await p.waitForTimeout(100);
// skip
const id0=await p.evaluate(()=>Z.steps[Z.i].it.id),n0=await p.evaluate(()=>Z.steps.length);
const hasSkip=await p.$('#skp');if(hasSkip){await p.click('#skp');await p.waitForTimeout(100);console.log('skipped',id0!==await p.evaluate(()=>Z.steps[Z.i].it.id),await p.evaluate(()=>Z.steps.filter(s=>s.skipped).length),n0===await p.evaluate(()=>Z.steps.length))}
// answer wrong/right then explain
await p.evaluate(()=>{const s=Z.steps[Z.i];if(s.k!=='try')return;const q=s.it.q;if(q.type==='mcq'){document.querySelector('[data-oi]').click()}else{const i=document.getElementById('sv');if(i){i.value='0';i.dispatchEvent(new Event('input',{bubbles:true}))}}const c=document.getElementById('chk');c&&!c.disabled&&c.click()});await p.waitForTimeout(200);
console.log(w,'post',await geo());await p.screenshot({path:`shots/t96_${w}_b.png`});
const ex=await p.$('#exp');if(ex){await p.click('#exp');await p.waitForTimeout(200);console.log('explain',await p.evaluate(()=>document.querySelector('.explain h2')?.textContent+' | '+document.querySelectorAll('.explain .step').length));await p.screenshot({path:`shots/t96_${w}_c.png`});const d=await p.$('#exd');if(d){await d.click();await p.waitForTimeout(150);console.log('back',await p.evaluate(()=>Z.steps[Z.i].k+' rq3='+JSON.stringify(Z.rq3)))}}
console.log(E.slice(0,3));await p.close()}
await b.close()})()
