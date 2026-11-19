const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [app,unit] of [['_app_axiom/apex','tg'],['_app_axiom/quanta','sho'],['_app_skyvolt/circuit',null]]){
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+`/out/${app}/index.html`);await p.waitForTimeout(500);
const r=await p.evaluate(u=>{const un=u?UN.find(x=>x.id===u):UN[0];const l=un.lessons[0];startSess({kind:'lesson',title:l.title,unit:un,lesson:l,steps:l.cards.map(c=>({k:'card',c:c,ut:un.title}))});const s=document.querySelector('#sess .dd');return s?s.querySelector('summary').textContent+' | vis:'+!!s.querySelector('.wv'):'none'},unit);console.log(app,r,E);
await p.evaluate(()=>{const d=document.querySelector('#sess .dd');d&&(d.open=true)});await p.screenshot({path:'shots/t114_'+app.split('/')[1]+'.png'});await p.close()}
await b.close()})()
