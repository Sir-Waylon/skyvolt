const {chromium}=require('playwright');const fs=require('fs');const axe=fs.readFileSync('node_modules/axe-core/axe.min.js','utf8');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});let tot=0;
for(const [nm,dir] of [['circuit','_app_skyvolt/circuit'],['meteo','_app_skyvolt/meteorology'],['apex','_app_axiom/apex'],['quanta','_app_axiom/quanta']])for(const th of ['light','dark']){
 const p=await (await b.newContext({viewport:{width:430,height:900}})).newPage();await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
 await p.goto('file://'+process.cwd()+`/out/${dir}/index.html`);await p.waitForTimeout(400);
 await p.evaluate(t=>{document.documentElement.setAttribute('data-theme',t);S.dgr={};ALL.forEach((x,i)=>S.dgr[x]=i%2);S.dg=today();S.cu=null;route()},th);
 const chk=async(label)=>{await p.addScriptTag({content:axe});const r=await p.evaluate(()=>axe.run(document,{runOnly:['color-contrast']}));const v=r.violations.flatMap(x=>x.nodes.map(n=>n.target.join(' ')+' '+n.html.slice(0,50)+' | '+(n.any[0]&&n.any[0].message||'').slice(0,90)));if(v.length){console.log(nm,th,label,v.length,v.slice(0,3));tot+=v.length}};
 await p.evaluate(()=>{const u=UN[1]||UN[0];startLesson(u.id,u.lessons[0].id)});await p.waitForTimeout(600);await chk('lesson1');
 await p.evaluate(()=>{const b=[...document.querySelectorAll('button')].find(x=>/^(Continue)/i.test(x.textContent.trim()));b&&b.click()});await p.waitForTimeout(500);await chk('lesson2');
 await p.reload();await p.waitForTimeout(400);await p.evaluate(t=>{document.documentElement.setAttribute('data-theme',t);S.dgr={};ALL.forEach((x,i)=>S.dgr[x]=i%2);S.dg=today();S.cu=null;route()},th);
 await p.evaluate(()=>document.querySelector('#nav button[data-t="library"]').click());await p.waitForTimeout(200);await p.evaluate(()=>{const e=document.querySelector('[data-nav="lib:labs"]');e&&e.click()});await p.waitForTimeout(250);
 await p.evaluate(()=>{const e=document.querySelector('[data-lab]');e&&e.click()});await p.waitForTimeout(700);await chk('lab');await p.close()}
console.log('contrast issues',tot);await b.close()})()
