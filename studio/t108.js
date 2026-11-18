const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [u,n] of [['_app_skyvolt/circuit','c'],['_app_skyvolt/meteorology','m'],['_app_axiom/apex','a'],['_app_axiom/quanta','q']]){
const p=await (await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:1})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+`/out/${u}/index.html`);await p.waitForTimeout(700);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});await p.waitForTimeout(400);
console.log(n,await p.evaluate(()=>getComputedStyle(document.documentElement).getPropertyValue('--pri')+' '+document.querySelector('link[rel=icon]').getAttribute('href')),E);
await p.screenshot({path:`shots/t108_${n}.png`});await p.close()}
await b.close()})()
