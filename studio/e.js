const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/apex/index.html');await p.waitForTimeout(500);console.log(e.slice(0,4),await p.evaluate(()=>typeof virtQ+typeof IT));await b.close()})()
