const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [app,lab] of [['_app_axiom/quanta','orbit'],['_app_axiom/quanta','myst'],['_app_axiom/quanta','ohm'],['_app_skyvolt/meteorology','front']]){
for(const vp of [{width:360,height:640},{width:390,height:700}]){
const p=await (await b.newContext({viewport:vp})).newPage();p.setDefaultTimeout(3000);
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(150);await p.evaluate(()=>document.querySelector('[data-nav="lib:labs"]').click());await p.waitForTimeout(200);
await p.evaluate(l=>document.querySelector('[data-lab="'+l+'"]').click(),lab);await p.waitForTimeout(500);
await p.evaluate(()=>window.scrollTo(0,document.documentElement.scrollHeight));await p.waitForTimeout(200);
const r=await p.evaluate(()=>{const n=document.querySelector('.nav').getBoundingClientRect();const m=document.querySelector('main');const kids=[...m.querySelectorAll('*')].filter(e=>e.getBoundingClientRect().height>0);const lastB=Math.max(...kids.map(e=>e.getBoundingClientRect().bottom));return {navTop:Math.round(n.top),lastBottom:Math.round(lastB),vh:innerHeight}});
console.log(app,lab,vp.width,JSON.stringify(r));await p.close()}}
await b.close()})()
