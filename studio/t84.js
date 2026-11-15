const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const app of ['_app_skyvolt/circuit','_app_skyvolt/meteorology','_app_axiom/apex','_app_axiom/quanta']){
const p=await (await b.newContext({viewport:{width:1100,height:760}})).newPage();
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});await p.waitForTimeout(300);
const info=await p.evaluate(()=>({tabs:[...document.querySelectorAll('#nav button')].map(b=>b.dataset.t).join(','),hdr:[...document.querySelectorAll('header *')].filter(e=>e.children.length===0&&e.innerText).map(e=>e.className+':'+e.innerText.trim().slice(0,18)).join(' | '),tracks:document.querySelectorAll('.tracks button, .tracks a').length,main:[...document.getElementById('main').children].map(e=>e.className.split(' ')[0]||e.tagName).join(',')}));
console.log(app,JSON.stringify(info));await p.screenshot({path:'shots/t84_'+app.split('/')[1]+'.png'});await p.close()}
await b.close()})()
