const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();p.on('pageerror',x=>console.log('ERR',x.message));
await p.goto('file://'+process.cwd()+'/out/_app_axiom/apex/index.html');await p.waitForTimeout(500);
console.log(await p.evaluate(()=>{startSess({kind:'practice',title:'P',steps:[{k:'try',it:mkItem('ti-xh1001')}]});const s=document.getElementById('sess');return [(s.innerHTML.match(/<input[^>]*>/g)||[]).join(' ').slice(0,300),(s.innerHTML.match(/<button[^>]*id="[a-z]*"/g)||[]).join(' '),QS.some(q=>q.id==='ti-xh1001')]}));
await b.close()})()
