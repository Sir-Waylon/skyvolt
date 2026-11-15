const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const c=await b.newContext({viewport:{width:390,height:700},colorScheme:'light'});const p=await c.newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('http://localhost:8801/app/circuit/');await p.waitForTimeout(600);await p.screenshot({path:'ck/trk_circ.png'});
await p.click('.tracks a:nth-child(2)');await p.waitForTimeout(700);console.log(p.url());await p.screenshot({path:'ck/trk_met.png'});
await p.goto('http://localhost:8801/app/');await p.waitForTimeout(300);await p.screenshot({path:'ck/trk_hub.png'});console.log(e);await b.close()})()
