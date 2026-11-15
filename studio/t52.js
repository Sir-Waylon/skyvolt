const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:900}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(400);
const ids=await p.evaluate(()=>{const s={};QS.filter(q=>q.type==='lab').forEach(q=>{if(!s[q.lab.id])s[q.lab.id]=q.id});return s});
for(const [k,id] of Object.entries(ids)){await p.evaluate(id=>{const it=mkItem(id);it.v=Object.assign({},it.q.lab.sv);it.t=true;startSess({kind:'review',title:'t',steps:[{k:'try',it:it}],remed:true})},id);await p.waitForTimeout(150);await p.evaluate(()=>window.scrollTo(0,0));await p.screenshot({path:'shots/lab_'+k+'.png',clip:{x:0,y:60,width:400,height:620}});await p.evaluate(()=>closeSess())}
console.log(Object.keys(ids).join(','),e);await b.close();process.exit(0)})()
