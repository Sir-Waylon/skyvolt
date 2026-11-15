const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:400,height:860}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));await p.goto('file://'+process.cwd()+'/out/_app_axiom/quanta/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{const q=QS.find(q=>q.type==='frbal');startSess({kind:'review',title:'t',steps:[{k:'try',it:mkItem(q.id)}],remed:true})});await p.waitForTimeout(300);
const r=await p.evaluate(()=>Z.steps[0].it.q.fr.sol);await p.fill('input[data-fr="0"]',String(r[0])).catch(()=>{});
await p.evaluate(s=>{[0,1].forEach(i=>{const el=document.querySelector('input[data-fr="'+i+'"]');el.value=s[i];el.dispatchEvent(new Event('input',{bubbles:true}))})},r);
await p.click('[data-frt]');await p.waitForTimeout(300);await p.screenshot({path:'shots/bld_fr.png'});
console.log('ok state',await p.evaluate(()=>IT.frbal.ok(Z.steps[0].it)),e);await b.close();process.exit(0)})()
