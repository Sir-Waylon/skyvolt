const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext()).newPage();p.on('pageerror',x=>console.log('ERR',x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/geometry/index.html');await p.waitForTimeout(500);
const r=await p.evaluate(()=>{function ids(f){f();var a=Z.steps.map(s=>s.it&&s.it.id).join();closeSess();return a}
 var d=[ids(()=>document.getElementById('dgs').click()),ids(()=>document.getElementById('dgs').click()),ids(()=>document.getElementById('dgs').click())],u=[ids(()=>startUnitTest(UN[0].id)),ids(()=>startUnitTest(UN[0].id))];return {diagDistinct:new Set(d).size,unitDistinct:new Set(u).size}});
console.log(r);await b.close();process.exit(0)})()
