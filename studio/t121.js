const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const site of ['_app_axiom/apex','_app_skyvolt/circuit','_app_skyvolt/meteorology','_app_axiom/quanta']){
const p=await (await b.newContext()).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.cwd()+'/out/'+site+'/index.html');await p.waitForTimeout(600);
const r=await p.evaluate(()=>{const out={};const u=UN[1]||UN[0],L=u.lessons[0];
 const kinds=m=>lessonSteps(u,L,m).map(s=>s.k+(s.solo?'*':'')+(s.refresh?'r':'')).join(',');
 S.stat={};S.un={};out.fresh=lessonMode(u,L);out.freshSteps=kinds(lessonMode(u,L));
 S.stat[u.id]=[6,10];out.mid=lessonMode(u,L);
 S.stat[u.id]=[18,20];out.hi=lessonMode(u,L);out.hiSteps=kinds('review');
 S.stat={};S.un[u.id]={d:{[L.id]:1}};out.done=lessonMode(u,L);
 // run a review lesson: answer wrong first try -> refresher card inserted
 S.un={};S.stat[u.id]=[18,20];startLesson(u.id,L.id);const z=Z;out.zmode=z.lmode;out.first=z.steps[0].k;
 const it=z.steps[0].it;it.done=true;it.ok=false;const n0=z.steps.length;advance();out.afterWrong=Z.steps[Z.i].k+'/'+Z.steps[Z.i].ut+' len+'+(Z.steps.length-n0);
 closeSess();S.stat={};startLesson(u.id,L.id);out.newKinds=Z.steps.map(s=>s.k).join(',');
 const ex=Z.steps.findIndex(s=>s.solo);if(ex>-1){Z.i=ex;drawSess();out.exBtn=document.querySelector('#sess .sheet button').textContent;document.querySelector('#sess .sheet button').click();out.afterEx=Z.steps[Z.i].k;}
 return out});
console.log(site,JSON.stringify(r),errs.slice(0,2));await p.close()}await b.close()})()
