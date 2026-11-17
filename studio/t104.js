const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:360,height:700}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{startFromIds(['circ-044'],'t')});await p.waitForTimeout(500);
await p.screenshot({path:'shots/t104.png'});console.log(await p.evaluate(()=>document.querySelector('.s-body').innerHTML.slice(0,600)));console.log(await p.evaluate(()=>JSON.stringify(Z.steps.map(s=>[s.k,s.it&&s.it.id,s.it&&s.it.q.type]))),await p.evaluate(()=>QS.filter(q=>q.id==='circ-044').map(q=>q.type+'|'+q.q.slice(0,60))),E);
await b.close()})()
