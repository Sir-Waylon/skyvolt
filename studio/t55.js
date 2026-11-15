const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const app of ['_app_axiom/apex','_app_skyvolt/circuit','_app_axiom/quanta']){
const p=await (await b.newContext({viewport:{width:400,height:900}})).newPage();p.on('pageerror',x=>console.log('ERR',app,x.stack.split('\n').slice(0,2).join('|')));
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(500);
console.log(app,'gate:',await p.evaluate(()=>!!document.querySelector('.gate')),'nav:',await p.evaluate(()=>document.querySelector('#nav button span').textContent));
await p.click('#dgs');await p.waitForTimeout(600);console.log(' sess open',await p.evaluate(()=>!!document.getElementById('sess')));
// answer diag by simulating finish
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>{S.dgr[t]=i%3===0?1:i%3===1?0:0});S.dg=today();closeSess&&closeSess()});
await p.evaluate(()=>{S.cu=null;route()});await p.waitForTimeout(300);
console.log(' today:',await p.evaluate(()=>[!!document.querySelector('.prc'),!!document.querySelector('#msn'),!!document.querySelector('.plc'),document.querySelectorAll('details.unit').length,document.body.innerText.match(/learning category: [^\n]*/)]));
await p.click('#msn');await p.waitForTimeout(700);console.log(' mission steps',await p.evaluate(()=>Z&&Z.steps.length));
await p.screenshot({path:'shots/t55_'+app.split('/')[1]+'.png'});}
await b.close();process.exit(0)})()
