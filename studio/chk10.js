const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:820}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(400);
const lab=process.argv[3]||'par';
// lab lesson
const found=await p.evaluate(l=>{for(const u of UN)for(const L of u.lessons)for(const c of L.cards)if(c.lab===l){startLesson(u.id,L.id);const i=Z.steps.findIndex(s=>s.k==='card'&&s.c.lab===l);Z.i=i;drawSess();return [u.id,L.id,i]}},lab);
await p.waitForTimeout(500);const lb=await p.evaluate(()=>{const l=document.querySelector('.lab');if(!l)return 'nolab';const s=l.querySelector('input[type=range]');s.value=s.max;s.dispatchEvent(new Event('input'));return l.querySelector('.out').textContent.slice(0,80)});
console.log('lab',found,lb);await p.screenshot({path:'ck/lab_'+lab+'.png'});
// resume
await p.evaluate(()=>{Z.i=0;drawSess();advance();advance();});await p.evaluate(()=>closeSess());await p.waitForTimeout(200);
console.log('rs',await p.evaluate(()=>JSON.stringify(S.rs)),'btn',await p.evaluate(()=>!!document.getElementById('rsm')));
await p.click('#rsm');await p.waitForTimeout(300);console.log('resumed at',await p.evaluate(()=>Z.i));await p.evaluate(()=>closeSess());
// test out
await p.evaluate(()=>{window.solve=function(it){var q=it.q;if(q.type==='mcq')it.sel=[0];else if(q.type==='multi')it.sel=q.a.slice();else if(q.type==='short')it.val=shortAnswer(q);else if(q.type==='order')it.seq=q.items.map(function(_,i){return i});else if(q.type==='match')q.pairs.forEach(function(_,i){it.mp[i]=i})}});
const u0=await p.evaluate(()=>UN[0].id);
await p.evaluate(u=>{startTestOut(u);Z.steps.forEach(s=>solve(s.it));finishSess()},u0);await p.waitForTimeout(300);
console.log('testout',await p.evaluate(()=>JSON.stringify({pass:S.un[UN[0].id].pass,sk:S.un[UN[0].id].skipped,n:Object.keys(S.un[UN[0].id].d).length,of:UN[0].lessons.length})));
await p.evaluate(()=>closeSess());await p.waitForTimeout(100);
await p.evaluate(()=>startEndless());
await p.evaluate(()=>{for(var g=0;g<24;g++){var it=Z.steps[Z.i].it;solve(it);resolveIt(it);advance();document.querySelectorAll('.modal').forEach(function(m){m.remove()})}});
console.log('endless seen',await p.evaluate(()=>Z&&Z.seenQ.length),'skill?',await p.evaluate(()=>Z.steps.filter(s=>s.it&&s.it.skill).length),'mains',await p.evaluate(()=>Z.mains));
await p.evaluate(()=>window.__brk());await p.waitForTimeout(200);console.log('break modal',await p.evaluate(()=>!!document.querySelector('.modal #bt')));await p.screenshot({path:'ck/brk.png'});
console.log('errs',errs.slice(0,4));await b.close()})();
