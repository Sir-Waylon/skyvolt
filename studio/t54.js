const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:900}})).newPage();let last='';p.on('pageerror',x=>console.log('ERR after',last,x.stack.split('\n').slice(0,2).join('|')));await p.goto('file://'+process.cwd()+'/out/_app_axiom/geometry/index.html');await p.waitForTimeout(400);
for(const t of ['balance','machine','mistake']){last='start '+t;await p.evaluate(t=>{const q=QS.find(q=>q.type===t);startSess({kind:'review',title:'t',steps:[{k:'try',it:mkItem(q.id)}],remed:true})},t);await p.waitForTimeout(500);
 if(t==='balance'){last='bo';await p.click('[data-bo="tx"]');last='bm';await p.click('[data-bm="n+"]')}
 if(t==='machine'){last='mach';await p.evaluate(()=>{const el=document.querySelector('input[data-mc="m"]');el.value=2;el.dispatchEvent(new Event('input',{bubbles:true}))})}
 if(t==='mistake'){last='ml';await p.click('[data-mst="2"]')}
 last='close';await p.evaluate(()=>closeSess());await p.waitForTimeout(500)}
await b.close();process.exit(0)})()
