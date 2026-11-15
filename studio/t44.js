const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const mk=async()=>{const c=await b.newContext({viewport:{width:420,height:860}});const p=await c.newPage();p.errs=[];p.on('pageerror',x=>p.errs.push(x.message));await p.goto('http://localhost:8791/');await p.waitForTimeout(400);return p};
const H=await mk(),A=await mk(),B=await mk();
const open=async p=>{await p.evaluate(()=>go('practice'));await p.click('[data-og]');};
await open(H);await H.fill('#ognick3','Teacher');await H.click('#oghost');await H.waitForSelector('.ogbig');
const code=(await H.textContent('.ogbig')).trim();console.log('code',code);
for(const [p,n] of [[A,'Ada'],[B,'Ben']]){await open(p);await p.fill('#ogcode',code);await p.fill('#ognick',n);await p.click('#ogjoin');await p.waitForSelector('.oglobby')}
await H.waitForTimeout(1800);console.log('players in lobby',(await H.$$('.ogchip')).length);
await H.screenshot({path:'shots/og_lobby.png'});
await H.click('#ogstart');
for(let r=0;r<2;r++){await A.waitForSelector('.ogtile',{timeout:8000});await B.waitForSelector('.ogtile');await H.waitForSelector('.ogtile');
 if(r===0)await A.screenshot({path:'shots/og_q.png'});
 await A.click('.ogtile');await B.click('.ogtile');await H.click('.ogtile');
 await A.waitForSelector('.ogres',{timeout:8000});if(r===0)await A.screenshot({path:'shots/og_rev.png'});
 await H.click('#ognext')}
console.log('A row',await A.textContent('.ogldr li.me').catch(()=>'none'));
console.log('errs',[H,A,B].map(p=>p.errs));
const V=await mk();await open(V);await V.fill('#ognick2','Vee');await V.click('#ogvs');await V.waitForSelector('#ogbot',{timeout:15000});await V.click('#ogbot');await V.waitForSelector('.ogvs',{timeout:10000});await V.waitForSelector('.ogtile',{timeout:10000});await V.screenshot({path:'shots/og_vs.png'});
console.log('vs ok',V.errs);await b.close();process.exit(0)})()
