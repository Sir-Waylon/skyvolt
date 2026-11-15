const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:900,height:300}});
for(const [n,f] of [['ax','axiom/index.html'],['vo','skyvolt/circuit/index.html'],['st','skyvolt/meteorology/index.html']]){
await p.goto('file://'+process.cwd()+'/out/'+f);await p.waitForTimeout(300);
await p.evaluate(()=>{document.body.innerHTML='<div style="display:flex;gap:10px;padding:10px;background:#fff">'+['a6','a7','a8','a9','a10'].map(i=>mascot(i,'happy',150,'c0')).join('')+'</div>'});
await p.screenshot({path:'ck/el_'+n+'.png'})}
await b.close()})()
