const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:900}})).newPage();p.on('pageerror',x=>console.log('ERR',x.stack.split('\n').slice(0,4).join('|')));
for(const app of ['_app_skyvolt/circuit','_app_axiom/geometry']){await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
console.log(app,await p.evaluate(()=>{var b=document.querySelector('[data-plan="go"]');b.click();return Z&&Z.kind+':'+Z.mains}));await p.waitForTimeout(300);await p.evaluate(()=>closeSess())}
await b.close();process.exit(0)})()
