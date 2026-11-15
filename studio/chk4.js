const {chromium}=require('playwright');
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:800}});
const errs=[];p.on('pageerror',e=>errs.push('PAGE '+e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(300);
console.log('typo',await p.evaluate(()=>gradeShort({text:['neutral']},'netural').ok));
// order correct via UI: click pool items in correct order
await p.evaluate(()=>{start({mode:'learn',ids:QS.filter(q=>q.type==='order').map(q=>q.id).slice(0,2)})});
for(let r=0;r<2;r++){
 const n=await p.evaluate(()=>Z.items[Z.i].q.items.length);
 for(let k=0;k<n;k++){const txt=await p.evaluate((k)=>Z.items[Z.i].q.items[k],k);await p.click('[data-po]:has-text("'+txt.replace(/"/g,'\\"')+'")').catch(async()=>{await p.evaluate((k)=>{document.querySelector('[data-po="'+k+'"]').click()},k)});}
 await p.click('#chk');
 console.log('order ok?',await p.evaluate(()=>Z.items[Z.i].ok));
 await p.click('#nx').catch(()=>{});await p.waitForTimeout(80);
}
// match correct
await p.evaluate(()=>{start({mode:'learn',ids:QS.filter(q=>q.type==='match').map(q=>q.id).slice(0,1)})});
const n=await p.evaluate(()=>Z.items[0].q.pairs.length);
for(let i=0;i<n;i++){await p.click('[data-ml="'+i+'"]');await p.click('[data-mr="'+i+'"]');}
await p.click('#chk');console.log('match ok?',await p.evaluate(()=>Z.items[0].ok));await p.screenshot({path:'ck/match_q.png'});
// multi
await p.evaluate(()=>{start({mode:'learn',ids:QS.filter(q=>q.type==='multi').map(q=>q.id).slice(0,1)})});
const a=await p.evaluate(()=>Z.items[0].q.a);
for(const oi of a)await p.click('[data-oi="'+oi+'"]');
await p.click('#chk');console.log('multi ok?',await p.evaluate(()=>Z.items[0].ok));
// short via UI numeric with unit
await p.evaluate(()=>{start({mode:'learn',ids:['virpe-027']})});
console.log(await p.evaluate(()=>Z.items[0].q.q+' | '+shortAnswer(Z.items[0].q)));
// test mode
await p.evaluate(()=>go('test'));await p.waitForTimeout(100);
await p.click('.dots button:nth-child(3)');await p.click('#fin');await p.waitForTimeout(100);
console.log('test finished',await p.isVisible('#again'));
// export/import
await p.evaluate(()=>{show('stats')});const ex=await p.inputValue('#ex');await p.fill('#im',ex);await p.click('#ip');
console.log('errors',errs);await b.close()})();
