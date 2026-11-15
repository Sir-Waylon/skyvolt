const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:820}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(400);
await p.evaluate(()=>{sub.lib='proofs';go('library')});await p.waitForTimeout(300);
await p.evaluate(()=>{document.querySelector('details').open=true});await p.click('[data-rv="1"]').catch(()=>{});await p.click('[data-rv="1"]').catch(()=>{});await p.waitForTimeout(400);await p.screenshot({path:'ck/g_proof.png'});
await p.evaluate(()=>{const q=QS.find(q=>q.svg&&q.type==='short');startFromIds([q.id])});await p.waitForTimeout(500);await p.screenshot({path:'ck/g_q.png'});
const d=await b.newPage({viewport:{width:1280,height:800}});await d.goto('file://'+process.argv[2]);await d.waitForTimeout(500);await d.screenshot({path:'ck/g_desk.png'});
console.log(errs);await b.close()})();
