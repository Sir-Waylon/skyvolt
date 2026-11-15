const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:860}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/geometry/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>go('learn'));await p.waitForTimeout(200);
await p.click('#dgs');await p.waitForTimeout(400);console.log('skip btn',!!(await p.$('#dkip')));await p.screenshot({path:'shots/diag.png'});
let n=0;while(await p.$('#dkip')&&n<80){await p.click('#dkip');await p.waitForTimeout(40);n++}
console.log('skipped',n,'fin',await p.evaluate(()=>Z&&Z.fin),e);await p.screenshot({path:'shots/diag2.png'});await b.close()})()
