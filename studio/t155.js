const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const sv=spawn('python3',['-m','http.server','8812'],{cwd:process.cwd()+'/out/_app_axiom/quanta',stdio:'ignore'});await new Promise(r=>setTimeout(r,1000));
const b=await chromium.launch({args:['--no-sandbox']});const p=await b.newPage({viewport:{width:390,height:800}});const err=[];p.on('pageerror',e=>err.push(e.message));
await p.goto('http://127.0.0.1:8812/');await p.waitForTimeout(1500);
const r=await p.evaluate(()=>{try{S.pro=null;S.stat={};var t=UN[0].id;startPractice([t],5);var m=document.querySelector('.pmx');return {t:t,modal:!!m,h:m&&m.querySelector('h3').textContent,btns:m&&[].map.call(m.querySelectorAll('button'),b=>b.textContent)}}catch(e){return 'ERR '+e.message}});
console.log(JSON.stringify(r));await p.screenshot({path:'shots/primer.png'});
if(r.modal){await p.click('#prsk');await p.waitForTimeout(500);console.log('after skip sess',await p.evaluate(()=>!!document.getElementById('sess')&&!document.querySelector('.pmx')))}
console.log(err);await b.close();sv.kill()})();
