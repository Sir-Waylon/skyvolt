const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:820}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(300);
await p.screenshot({path:'ck/h1.png'});
// start first lesson
await p.click('.cont .btn');await p.waitForTimeout(300);await p.screenshot({path:'ck/l1.png'});
for(let g=0;g<6;g++){const k=await p.evaluate(()=>Z.steps[Z.i].k);if(k==='card'){await p.click('#go');await p.waitForTimeout(150)}else break}
await p.waitForTimeout(300);
// answer wrong deliberately
const isMcq=await p.evaluate(()=>Z.steps[Z.i].it.q.type==='mcq');
console.log('try step type',await p.evaluate(()=>Z.steps[Z.i].k+':'+Z.steps[Z.i].it.q.type));
if(isMcq){const wrong=await p.evaluate(()=>{const it=Z.steps[Z.i].it;return it.perm.find(x=>x!==0)});await p.click('.opt[data-oi="'+wrong+'"]');}
else{await p.fill('#sv','12345.5');await p.click('#chk')}
await p.waitForTimeout(300);await p.screenshot({path:'ck/l2.png'});
await p.click('#exp');await p.waitForTimeout(300);await p.screenshot({path:'ck/l3.png'});
await p.click('#exn').catch(()=>{});
for(let k=0;k<4;k++){const s=await p.$('#exs');if(s){await s.click();await p.waitForTimeout(100)}}
await p.screenshot({path:'ck/l4.png'});
await p.click('#exf');await p.waitForTimeout(300);
console.log('follow step',await p.evaluate(()=>Z.steps[Z.i].k+':'+!!Z.steps[Z.i].follow));
// answer follow correctly
const t=await p.evaluate(()=>Z.steps[Z.i].it.q.type);
if(t==='mcq'){await p.click('.opt[data-oi="0"]')}else{const a=await p.evaluate(()=>shortAnswer(Z.steps[Z.i].it.q));await p.fill('#sv',String(a));await p.click('#chk')}
await p.waitForTimeout(300);await p.screenshot({path:'ck/l5.png'});
await p.click('#nx');
// finish rest of lesson via evaluate loop
for(let g=0;g<30;g++){const k=await p.evaluate(()=>Z&&!Z.fin?Z.steps[Z.i].k:'x');if(k==='x')break;
 console.log('k',k,await p.evaluate(()=>!!document.getElementById('go')+':'+Z.i+'/'+Z.steps.length));if(k==='card'){await p.click('#go',{timeout:3000})}else if(k==='try'){const ty=await p.evaluate(()=>Z.steps[Z.i].it.q.type);if(ty==='mcq')await p.click('.opt[data-oi="0"]');else{await p.evaluate(()=>{const it=Z.steps[Z.i].it,q=it.q;if(q.type==='short')it.val=String(shortAnswer(q));else if(q.type==='order')it.seq=q.items.map((_,i)=>i);else if(q.type==='match')q.pairs.forEach((_,i)=>it.mp[i]=i);else if(q.type==='multi')it.sel=q.a.slice();drawSess()});await p.click('#chk')}
  await p.waitForTimeout(80);await p.click('#nx')}else break}
await p.waitForTimeout(400);await p.screenshot({path:'ck/l6.png'});
console.log('lesson fin',await p.evaluate(()=>Z&&Z.fin),await p.evaluate(()=>JSON.stringify(S.un)));
await p.click('#done');await p.waitForTimeout(200);
// unit test
await p.evaluate(()=>startUnitTest('eq'));
for(let g=0;g<12;g++){const f=await p.evaluate(()=>Z&&Z.fin);if(f)break;const ty=await p.evaluate(()=>Z.steps[Z.i].it.q.type);
 if(ty==='mcq')await p.click('.opt[data-oi="0"]');else{await p.evaluate(()=>{const it=Z.steps[Z.i].it,q=it.q;if(q.type==='short')it.val=String(shortAnswer(q));else if(q.type==='order')it.seq=q.items.map((_,i)=>i);else if(q.type==='match')q.pairs.forEach((_,i)=>it.mp[i]=i);else if(q.type==='multi')it.sel=q.a.slice();drawSess()})}
 await p.click('#nx')}
await p.waitForTimeout(300);await p.screenshot({path:'ck/u1.png'});console.log('unit',await p.evaluate(()=>Z.pct+' '+JSON.stringify(S.un.virpe)));
await p.evaluate(()=>{document.querySelectorAll('.modal').forEach(m=>m.remove())});await p.click('#done');
for(const t of ['practice','library','me']){await p.click('#nav [data-t='+t+']');await p.waitForTimeout(250);await p.screenshot({path:'ck/t_'+t+'.png'})}
await p.click('#thm');await p.click('#nav [data-t=learn]');await p.waitForTimeout(300);await p.screenshot({path:'ck/dark.png'});
await p.evaluate(()=>startPractice(ALL,5));await p.waitForTimeout(200);console.log('adaptive step',await p.evaluate(()=>Z.steps.length+':'+Z.steps[0].k));
console.log('errs',errs);await b.close()})();
