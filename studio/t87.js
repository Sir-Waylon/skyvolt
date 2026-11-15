const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const want=process.argv.slice(2);
for(const [app,labs] of [['_app_skyvolt/circuit',['myst','bread','div']],['_app_skyvolt/meteorology',['storm','sea']],['_app_axiom/quanta',['orbit','myst','proj','lens','ripple','incline','bread','div','skate','string','dopp']]]){
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();p.setDefaultTimeout(3000);const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/'+app+'/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
const go=async()=>{await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(150);await p.evaluate(()=>document.querySelector('[data-nav="lib:labs"]').click());await p.waitForTimeout(200)};
await go();console.log(app,await p.$$eval('[data-lab]',a=>a.map(x=>x.dataset.lab).join(',')));
for(const l of labs){if(want.length&&!want.includes(l))continue;await go();const ex=await p.$('[data-lab="'+l+'"]');if(!ex){console.log('  missing',l);continue}await ex.evaluate(e=>e.click());await p.waitForTimeout(700);
 for(const sel of await p.$$('[data-ls]')){await sel.evaluate(e=>{e.value=e.max;e.dispatchEvent(new Event('input',{bubbles:true}))});}
 for(const c of (await p.$$('#labroot [data-lc]')).slice(0,8)){await c.evaluate(e=>e.click())}
 for(const c of (await p.$$('#labroot [data-la]')).slice(0,3)){await c.evaluate(e=>e.click())}
 await p.waitForTimeout(900);
 console.log('  ',l,await p.evaluate(()=>((document.querySelector('#labroot .labr')||{innerText:''}).innerText).slice(0,150)));await p.screenshot({path:'shots/t87_'+app.split('/')[1]+'_'+l+'.png'})}
console.log(E);await p.close()}
await b.close()})()
