const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();p.setDefaultTimeout(2500);p.on('pageerror',x=>console.log('PE',x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.click('[data-og="solo"]');await p.click('[data-solo="blitz"]');await p.waitForTimeout(500);
await p.screenshot({path:'shots/t73a.png'});
await p.click('#sx');await p.waitForTimeout(400);console.log(await p.evaluate(()=>document.body.innerText.slice(0,200).replace(/\n/g,' / ')));
console.log(await p.evaluate(()=>document.getElementById('main').innerText.slice(0,300)+' | modals='+document.querySelectorAll('.modal').length+' og='+document.querySelectorAll('[data-og]').length));
await p.screenshot({path:'shots/t73b.png'});await b.close()})()
