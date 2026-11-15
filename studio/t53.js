const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:900}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.stack.split('\n').slice(0,3).join(' | ')));await p.goto('file://'+process.cwd()+'/out/_app_axiom/geometry/index.html');await p.waitForTimeout(400);
for(const t of ['balance','machine','mistake']){await p.evaluate(t=>{const q=QS.find(q=>q.type===t);startSess({kind:'review',title:'t',steps:[{k:'try',it:mkItem(q.id)}],remed:true})},t);await p.waitForTimeout(700);
 if(t==='balance'){await p.click('[data-bo="tx"]');await p.click('[data-bm="n+"]');await p.waitForTimeout(100)}
 if(t==='machine'){await p.evaluate(()=>{const el=document.querySelector('input[data-mc="m"]');el.value=2;el.dispatchEvent(new Event('input',{bubbles:true}))})}
 if(t==='mistake'){await p.click('[data-mst="2"]')}
 await p.waitForTimeout(150);await p.screenshot({path:'shots/gm_'+t+'.png'});await p.evaluate(()=>closeSess());await p.waitForTimeout(700)}
console.log(e);await b.close();process.exit(0)})()
