const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:900}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(500);
console.log(await p.evaluate(()=>{const c={};QS.filter(q=>q.type==='sbx').forEach(q=>c[q.sbx.id]=(c[q.sbx.id]||0)+1);return JSON.stringify(c)+' proj:'+QS.filter(q=>/^lab-(proj|cart)/.test(q.id)).length}));
for(const d of ['drop','shot','crash']){const id=await p.evaluate(d=>QS.find(q=>q.sbx&&q.sbx.id===d).id,d);
 await p.evaluate(id=>startSess({kind:'review',title:'t',steps:[{k:'try',it:mkItem(id)}],remed:true}),id);await p.waitForTimeout(300);
 await p.click('[data-sbx="run"]');await p.waitForTimeout(700);await p.screenshot({path:'shots/t57_'+d+'.png'});await p.waitForTimeout(4000);
 console.log(d,await p.evaluate(()=>document.getElementById('sbxr').innerText));
 await p.evaluate(()=>closeSess());await p.waitForTimeout(200)}
console.log('errs',e);await b.close();process.exit(0)})()
