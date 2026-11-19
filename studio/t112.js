const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
async function run(app,tp,ty,wrong,tag){const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+`/out/${app}/index.html`);await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
const qid=await p.evaluate(a=>{const q0=QS.find(x=>x.t===a[0]&&x.type===a[1]&&(a[1]!=='short'||x.num));q0.keep=true;startSess({kind:'practice',title:'Practice',steps:[{k:'try',it:mkItem(q0.id)}]});return q0.id},[tp,ty]);console.log(tag,qid);await p.waitForTimeout(300);
const q=await p.evaluate(i=>QS.find(x=>x.id===i),qid);
if(q.type==='short'){await p.fill('#sv',wrong);await p.click('#chk')}else{await p.evaluate(()=>{const o=[...document.querySelectorAll('#sess [data-o],#sess .opt,#sess .choice')];o.length&&o[o.length-1].click()});await p.click('#chk').catch(()=>{})}
await p.waitForTimeout(1700);
const r=await p.evaluate(()=>({deep:!!document.querySelector('.deepx'),h:(document.querySelector('.card.explain h2')||{}).textContent,dg:(document.querySelector('.wdg')||{}).textContent,anim:document.querySelectorAll('.wv animate,.wv animateTransform,.wv animateMotion').length,mode:(document.querySelector('.deepx')||{dataset:{}}).dataset.m}));
console.log(tag,JSON.stringify(r),E);await p.screenshot({path:`shots/t112_${tag}.png`});
if(tag==='apex'){await p.click('[data-lp=visual]');await p.waitForTimeout(300);console.log(' after Picture',await p.evaluate(()=>document.querySelector('.deepx').dataset.m+' anim:'+document.querySelectorAll('.wv animate').length));await p.screenshot({path:'shots/t112_apex_vis.png'})}
await p.close()}
await run('_app_axiom/apex','ti','short','0.123','apex');
await run('_app_axiom/apex','tg','mcq','','tgm');
await run('_app_axiom/quanta','kin','short','999','quanta');
await run('_app_skyvolt/circuit','circ','mcq','','circ');
await b.close()})()
