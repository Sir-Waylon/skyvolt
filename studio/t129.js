const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [w,h,n] of [[390,800,'m'],[1280,800,'d']]){const p=await (await b.newContext({viewport:{width:w,height:h}})).newPage();await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(600);
await p.evaluate(()=>openOnline());await p.waitForTimeout(300);await p.screenshot({path:'om_'+n+'.png'});
console.log(n,'menu centered offsets',await p.evaluate(()=>{const c=document.querySelector('.ogmenu').getBoundingClientRect();return [Math.round(c.left),Math.round(innerWidth-c.right)]}));
await p.evaluate(()=>{document.getElementById('og').remove();openArcade()});await p.waitForTimeout(300);await p.screenshot({path:'am_'+n+'.png'});await p.close()}await b.close()})()
