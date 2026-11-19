const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [n,u] of [['m','_app_skyvolt/meteorology'],['a','_app_axiom/apex']]){const p=await (await b.newContext({viewport:{width:1000,height:900}})).newPage();
await p.goto('file://'+process.cwd()+`/out/${u}/index.html`);await p.waitForTimeout(500);await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});await p.waitForTimeout(300);
const el=await p.$('.play2');await el.scrollIntoViewIfNeeded();await el.screenshot({path:`shots/t116_${n}.png`});await p.close()}await b.close()})()
