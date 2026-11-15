const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const mk=async()=>{const c=await b.newContext({viewport:{width:420,height:900}});const p=await c.newPage();p.on('pageerror',x=>console.log('ERR',x.message));return p};
const A=await mk(),B=await mk();
async function signup(p,em,un){await p.goto('http://localhost:8791/');await p.waitForTimeout(600);await p.evaluate(()=>{sub.me='friends';go('me')});await p.waitForTimeout(500);
 await p.click('[data-am=up]');await p.fill('#email',em);await p.fill('#username',un);await p.fill('#password','a long passphrase 42');await p.click('#acg');await p.waitForTimeout(900)}
await signup(A,'a@x.com','alice_1');await signup(B,'b@x.com','bob_2');
await A.evaluate(()=>{S.xp=120;save()});await A.waitForTimeout(4600);
await A.fill('#fru','bob_2');await A.click('#fra');await A.waitForTimeout(500);
await B.evaluate(()=>friends&&0).catch(()=>{});await B.reload();await B.waitForTimeout(900);await B.evaluate(()=>{sub.me='friends';go('me')});await B.waitForTimeout(900);
await B.screenshot({path:'ck/fr_b.png'});
await B.click('[data-fa=alice_1]');await B.waitForTimeout(700);await B.screenshot({path:'ck/fr_b2.png'});
console.log(await B.evaluate(()=>document.querySelector('.card:nth-of-type(3)')&&[...document.querySelectorAll('.lg')].map(x=>x.textContent.replace(/\s+/g,' '))));
// cloud restore: fresh browser context logs in as alice
const C=await mk();await C.goto('http://localhost:8791/');await C.waitForTimeout(500);await C.evaluate(()=>{sub.me='friends';go('me')});await C.waitForTimeout(400);
await C.fill('#email','alice_1');await C.fill('#password','a long passphrase 42');await C.click('#acg');await C.waitForTimeout(1500);
console.log('restored xp',await C.evaluate(()=>S.xp));
await b.close()})()
