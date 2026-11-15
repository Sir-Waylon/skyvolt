const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const app of ['_app_skyvolt/circuit','_app_skyvolt/meteorology','_app_axiom/geometry','_app_axiom/apex','_app_axiom/quanta']){
const p=await (await b.newContext({viewport:{width:400,height:820},deviceScaleFactor:2})).newPage();p.on('pageerror',x=>console.log('ERR',app,x.message));
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;S.stat[ALL[0]]=[16,20];S.stat[ALL[1]]=[3,5];route()});
const n=app.split('/')[1];await p.screenshot({path:'shots/t60_'+n+'_today.png'});
await p.evaluate(()=>go('course'));await p.waitForTimeout(300);await p.click('.chead');await p.waitForTimeout(200);
console.log(n,await p.evaluate(()=>[document.querySelectorAll('.cunit').length,document.querySelector('.cseg').children.length,document.querySelector('.cprog i').style.width,document.querySelector('#nav button').innerHTML.length]));
await p.screenshot({path:'shots/t60_'+n+'_course.png'})}
await b.close();process.exit(0)})()
