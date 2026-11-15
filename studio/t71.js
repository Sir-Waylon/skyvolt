const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();p.setDefaultTimeout(3000);
await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
console.log(await p.evaluate(()=>[...document.querySelectorAll('#nav button')].map(b=>b.dataset.t+'|'+b.textContent.trim())));
console.log(await p.evaluate(()=>[...document.body.children].map(e=>e.id+'.'+e.className+':'+e.innerText.length).join(' ')));
await p.screenshot({path:'shots/t71.png'});await b.close()})()
