const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:1100,height:800}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8792/');const t=async()=>p.evaluate(()=>[...document.querySelectorAll('.btn')].map(x=>x.textContent.trim()).join(' | '));
console.log('signed out:',await t());
await p.evaluate(async()=>{const c=await (await fetch('/api/config')).json();const r=await fetch('/api/signup',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({email:'a1@example.com',username:'lander1',password:'correct horse 99'})});return r.status});
await p.reload();await p.waitForTimeout(800);console.log('signed in :',await t());
await p.screenshot({path:'landing.png'});console.log(errs);await b.close()})()
