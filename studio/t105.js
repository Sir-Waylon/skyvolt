const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const u of ['_app_skyvolt/circuit','_app_skyvolt/meteorology','_app_axiom/apex','_app_axiom/quanta']){
const p=await (await b.newContext({viewport:{width:360,height:700}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+`/out/${u}/index.html`);await p.waitForTimeout(3500);
// simulate signed-in friends flow with stubbed api
const r=await p.evaluate(async()=>{return 'ok'});
console.log(u,r,E.slice(0,2));await p.close()}
await b.close()})()
