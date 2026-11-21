const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const site of ['_app_skyvolt/circuit','_app_axiom/apex']){
for(const g of ['gold','boss','run']){
const p=await (await b.newContext({viewport:{width:390,height:780}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.clock.install();await p.goto('file://'+process.cwd()+'/out/'+site+'/index.html');await p.clock.runFor(800);
await p.evaluate(g=>{S.stat=S.stat||{};openArcade(g)},g);let n=0,shot=false,qs=0;
for(let i=0;i<400;i++){await p.clock.runFor(250);
 if(await p.$('#ar .ogdone'))break;
 const tile=await p.$('#arq .ogtile:not([disabled])');
 if(tile){qs++;const ok=(qs%3!==0);const sel=ok?'#arq .ogtile[data-aro="0"]':'#arq .ogtile:not([data-aro="0"])';
  if(!shot&&g!=='gold'||(!shot&&qs===2)){await p.screenshot({path:`ar_${g}_q.png`});shot=true}
  await p.click(sel+':not([disabled])',{force:true,timeout:2000}).catch(()=>{});continue}
 const cont=await p.$('#arcont');if(cont){await cont.click();continue}
 const ch=await p.$('button[data-arc]');if(ch){await ch.click();continue}
 const st=await p.$$('.arstar');if(st.length&&g==='run'){await st[0].click({force:true}).catch(()=>{});
  if(!shot){await p.screenshot({path:'ar_run_stage.png'});shot=true}}}
const done=await p.$('#ar .ogdone');console.log(site,g,'finished:',!!done,'questions',qs,done?(await done.textContent()).slice(0,110):'', errs.slice(0,2));
if(done)await p.screenshot({path:`ar_${g}_end.png`});await p.close()}}
await b.close()})()
