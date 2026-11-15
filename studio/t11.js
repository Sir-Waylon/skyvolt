const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [n,f] of [['ax','axiom/index.html'],['vo','skyvolt/app/circuit/index.html'],['st','skyvolt/app/meteorology/index.html']]){
const p=await b.newPage({viewport:{width:420,height:900}});const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/'+f);await p.waitForTimeout(400);
await p.evaluate(()=>{S.coins=1200;S.xp=3000;document.body.insertAdjacentHTML('beforeend','<div style="position:fixed;inset:0;background:#fff;overflow:auto;padding:12px;z-index:99">'+shopHTML()+'</div>')});
await p.waitForTimeout(300);await p.screenshot({path:'ck/shop_'+n+'.png',fullPage:false});
await p.reload();await p.waitForTimeout(300);
const r=await p.evaluate(()=>{const u=UN[0],L=u.lessons[0];startLesson(u.id,L.id);let g=0;while(Z&&!Z.fin&&g++<80){const st=Z.steps[Z.i];if(st.k==='card'){advance();continue}const it=st.it;if(!it){advance();continue}
 if(it.q.type==='mcq'){it.sel=[it.perm.indexOf(0)];}else{break}
 resolveIt(it);advance()}
 finishSess();drawSess();return [Z&&Z.fin,S.coins,Z.earned]});
await p.waitForTimeout(2200);await p.screenshot({path:'ck/sum_'+n+'.png'});console.log(n,r,e);await p.close()}
await b.close()})()
