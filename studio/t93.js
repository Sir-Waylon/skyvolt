const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const dark=process.argv[2]==='dark';
const p=await (await b.newContext({viewport:{width:390,height:844},colorScheme:dark?'dark':'light'})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
for(const [app,labs] of [['_app_axiom/quanta',['div','skate','string','dopp','orbit','lens','incline','bread','myst']],['_app_skyvolt/meteorology',['sea','storm']]]){
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
for(const l of labs){await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(120);await p.evaluate(()=>document.querySelector('[data-nav="lib:labs"]').click());await p.waitForTimeout(150);await p.evaluate(l=>document.querySelector('[data-lab="'+l+'"]').click(),l);await p.waitForTimeout(900);
 if(l==='sea'){await p.evaluate(()=>{const i=document.querySelector('[data-ls="h"]');i.value=15;i.dispatchEvent(new Event('input',{bubbles:true}))});await p.waitForTimeout(300)}
 await p.screenshot({path:'shots/t93'+(dark?'d':'')+'_'+l+'.png'})}}
console.log(E);await b.close()})()
