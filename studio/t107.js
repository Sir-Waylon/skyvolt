const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:800}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));const F=[];p.on('requestfailed',r=>F.push(r.url().slice(-30)));
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(900);
console.log(await p.evaluate(async()=>{await document.fonts.ready;return [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+f.weight).join(',')+' | body='+getComputedStyle(document.body).fontFamily.slice(0,30)+' h2='+getComputedStyle(document.querySelector('h2')||document.body).fontFamily.slice(0,20)}),E,F);
await p.screenshot({path:'shots/t107.png'});await b.close()})()
