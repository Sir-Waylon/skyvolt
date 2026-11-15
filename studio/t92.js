const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
const open=async l=>{await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(120);await p.evaluate(()=>document.querySelector('[data-nav="lib:labs"]').click());await p.waitForTimeout(150);await p.evaluate(l=>document.querySelector('[data-lab="'+l+'"]').click(),l);await p.waitForTimeout(500)};
await open('ripple');await p.locator('#rtc').screenshot({path:'shots/t92_ripple.png'});
await open('incline');await p.evaluate(()=>{document.querySelector('[data-lc="fa:1"]').click();document.querySelector('[data-la="go"]').click()});await p.waitForTimeout(900);await p.locator('#lsvw').screenshot({path:'shots/t92_incline.png'});console.log(await p.evaluate(()=>document.querySelector('#lro').innerText));
await open('lens');await p.evaluate(()=>{const i=document.querySelector('[data-ls="f"]');i.value=5;i.dispatchEvent(new Event('input',{bubbles:true}))});await p.waitForTimeout(200);await p.locator('#lsvw').screenshot({path:'shots/t92_lens.png'});console.log(await p.evaluate(()=>document.querySelector('#lro').innerText));
console.log(E);await b.close()})()
