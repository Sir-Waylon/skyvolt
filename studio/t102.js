const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:360,height:740}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{startLesson('hist','hist-L1')});await p.waitForTimeout(500);
console.log(await p.evaluate(()=>JSON.stringify(Z.steps.slice(0,4).map(s=>[s.k,s.c&&s.c.h,!!(s.c&&s.c.dd)]))));await p.evaluate(()=>{Z.i=2;drawSess()});for(let i=0;i<0;i++){const has=await p.$('details.dd');if(has)break;await p.evaluate(()=>{var e=document.getElementById('go');e&&e.click()});await p.waitForTimeout(150)}
const d=await p.$('details.dd');console.log('dd',!!d,E);if(d){await d.scrollIntoViewIfNeeded();await p.click('details.dd summary');await p.waitForTimeout(200);await p.screenshot({path:'shots/t102.png'})}
await b.close()})()
