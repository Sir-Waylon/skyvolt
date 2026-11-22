const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const sv=spawn('node',['server.mjs','../../out/skyvolt',8841],{cwd:'backend/test',env:{...process.env,TEST_MAIL:'1'}});await new Promise(r=>setTimeout(r,900));
const base='http://skyvolt.localhost:8841';const res=[];const ok=(n,c)=>{res.push((c?'ok   ':'FAIL ')+n)};
const ctx=await b.newContext({viewport:{width:390,height:844}});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto(base+'/app/circuit/');await p.waitForTimeout(1200);
ok('gate shown',await p.evaluate(()=>!!document.getElementById('gate')));
await p.click('[data-am="up"]');await p.waitForTimeout(200);
ok('password checklist visible',await p.evaluate(()=>document.querySelectorAll('#pwr li').length===3));
await p.fill('#email','kid@x.com');await p.fill('#username','kid_one');await p.fill('#password','abc');
ok('checklist reacts (0 done)',await p.evaluate(()=>document.querySelectorAll('#pwr li.ok').length===0));
await p.fill('#password','correct horse 42 battery');
ok('checklist all done',await p.evaluate(()=>document.querySelectorAll('#pwr li.ok').length===3));
await p.click('#acg');await p.waitForTimeout(900);
ok('verify screen',await p.evaluate(()=>/Check your email/.test(document.getElementById('gate').textContent)));
ok('email masked',await p.evaluate(()=>/ki\*\*\*@x\.com/.test(document.getElementById('gate').textContent)));
await p.fill('#code','000000');await p.click('#acv');await p.waitForTimeout(500);
ok('wrong code keeps gate',await p.evaluate(()=>/Check your email/.test(document.getElementById('gate').textContent)));
const code=await p.evaluate(async()=>(await fetch('/__lastcode')).text());
await p.fill('#code',code);await p.click('#acv');await p.waitForTimeout(1200);
ok('verified -> gate gone',await p.evaluate(()=>!document.getElementById('gate')));
// 2FA from Me > Friends
await p.evaluate(()=>{window.__V&&(window.__V.me=null);document.querySelector('#nav button[data-t="me"]').click()});await p.waitForTimeout(300);
await p.evaluate(()=>{[...document.querySelectorAll('#main button,#main [role=button],#main a')].find(e=>/Friends and account/.test(e.textContent)).click()});await p.waitForTimeout(600);
ok('security card present',await p.evaluate(()=>!!document.getElementById('tfn')));
console.log(res.join('\n'));console.log(await p.evaluate(()=>JSON.stringify({tf:__ACC.tf,me:__ACC.me&&{v:__ACC.me.verified,c:__ACC.me.canTfa,t:__ACC.me.tfa},sub:sub.me,cur:cur,html:document.querySelector('#main')&&document.querySelector('#main').textContent.slice(0,200)})));await p.click('#tfn');await p.waitForTimeout(600);
let c2=code;for(let i=0;i<20&&c2===code;i++){await p.waitForTimeout(300);c2=await p.evaluate(async()=>(await fetch('/__lastcode')).text())}
await p.fill('#tfc',c2);await p.click('#tfy');await p.waitForTimeout(600);
console.log('DBG2',c2,'verifycode',code,await p.evaluate(()=>JSON.stringify({v:(document.getElementById('tfc')||{}).value,t:[...document.querySelectorAll('.toast,[role=status],#toast')].map(e=>e.textContent)})));ok('2fa on',await p.evaluate(()=>!!document.getElementById('tff')));
// sign out and sign in again -> code step
await p.evaluate(()=>document.querySelector('[data-so]').click());await p.waitForTimeout(700);
await p.fill('#email','kid_one');await p.fill('#password','correct horse 42 battery');await p.click('#acg');await p.waitForTimeout(900);
console.log('DBG',await p.evaluate(()=>(document.getElementById('gate')||document.body).textContent.slice(0,300)));ok('login asks for code',await p.evaluate(()=>!!document.getElementById('gate')&&/sign-in code/i.test(document.getElementById('gate').textContent)));
let c3=c2;for(let i=0;i<20&&c3===c2;i++){await p.waitForTimeout(300);c3=await p.evaluate(async()=>(await fetch('/__lastcode')).text())}
await p.fill('#code',c3);await p.click('#act');await p.waitForTimeout(1200);
ok('2fa login works',await p.evaluate(()=>!document.getElementById('gate')&&__ACC.me&&__ACC.me.username==='kid_one'));
await p.screenshot({path:'../shots/gate-after.png'});
console.log(res.join('\n'),errs.length?'\nJS ERRORS '+errs:'');sv.kill();await b.close()})()
