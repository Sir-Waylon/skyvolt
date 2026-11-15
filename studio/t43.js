const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:800}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/apex/index.html');await p.waitForTimeout(500);
console.log(await p.evaluate(()=>{const o={};const t=new Date(2026,10,2,16),n=new Date(2026,10,2,23),d=new Date(2026,10,2,10);o.aft=studyWindow(t).pct;o.night=studyWindow(n).pct;o.morn=studyWindow(d).pct;
 S.hr={9:[18,20],10:[9,12],16:[10,20],17:[12,20],20:[8,10]};o.best=studyWindow(d).best;o.pk=studyWindow(new Date(2026,10,2,9)).tag;return o}));
await p.evaluate(()=>go('learn'));await p.waitForTimeout(200);console.log(await p.evaluate(()=>!!document.querySelector('.swchip')));
await p.click('.swchip');await p.screenshot({path:'shots/sw.png'});console.log(e);await b.close()})()
