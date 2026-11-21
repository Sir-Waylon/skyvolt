const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const ctx=await b.newContext({viewport:{width:390,height:780}});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8791/');await p.waitForSelector('#gate .gcard #acg',{timeout:6000});
console.log('gate shown; inert',await p.evaluate(()=>[...document.body.children].filter(n=>n.hasAttribute('inert')).length));
const box=await p.evaluate(()=>{const r=document.querySelector('#gate .gcard').getBoundingClientRect();return [Math.round(r.left),Math.round(innerWidth-r.right),Math.round(r.top),Math.round(innerHeight-r.bottom)]});console.log('card margins L,R,T,B',box);
await p.screenshot({path:'gate.png'});
await p.click('[data-am="up"]');console.log('switched:',await p.textContent('#gt'));
await p.fill('#email','kid1@example.com');await p.fill('#username','kid_one');await p.fill('#password','correct horse 99');await p.click('#acg');
await p.waitForFunction(()=>!document.getElementById('gate'),null,{timeout:6000});console.log('signed up -> gate gone');
const ck=(await ctx.cookies()).filter(c=>c.name.startsWith('__Host-'));console.log('cookies',ck.map(c=>c.name+' expires='+c.expires));
await p.evaluate(()=>{go('me');window.__V.me=null;route()});await p.waitForTimeout(300);
console.log('sign-out visible:',await p.evaluate(()=>!!document.querySelector('[data-so]')));
await p.click('[data-so]');await p.waitForSelector('#gate #acg');console.log('signed out -> gate back; title',await p.textContent('#gt'));
await p.fill('#email','kid_one');await p.fill('#password','correct horse 99');await p.click('#acg');await p.waitForFunction(()=>!document.getElementById('gate'));console.log('sign in ok');
// new browser context = browser closed -> no cookie -> must sign in again
const p2=await (await b.newContext()).newPage();await p2.goto('http://localhost:8791/');await p2.waitForSelector('#gate #acg');console.log('fresh browser -> gate');
console.log('errors',errs);await b.close()})()
