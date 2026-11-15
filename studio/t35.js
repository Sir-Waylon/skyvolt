const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:420,height:900}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/axiom/app/geometry/index.html');await p.waitForTimeout(600);
await p.evaluate(()=>{S.coins=900;cur='me';sub.me='shop';route()});await p.waitForTimeout(400);
await p.screenshot({path:'shots/vertex_shop.png'});console.log(e,await p.title());await b.close()})()
