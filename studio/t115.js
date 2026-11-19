const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:800}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));
await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
await p.goto('file://'+process.cwd()+'/out/_app_axiom/apex/index.html');await p.waitForTimeout(600);
console.log('offline ok, errors:',E);
// stub KaTeX to prove the observer wiring
await p.evaluate(()=>{window.katex={};window.__calls=0;window.renderMathInElement=function(el,o){window.__calls++;el.innerHTML=el.innerHTML.replace(/\\\((.*?)\\\)/g,'<span class="katex">[$1]</span>')}});
await p.evaluate(()=>{const d=document.createElement('p');d.id='mt';d.textContent='Solve \\(x^2=4\\) now';document.body.appendChild(d)});await p.waitForTimeout(500);
console.log(await p.evaluate(()=>[document.getElementById('mt').innerHTML,window.__calls]));
await p.evaluate(()=>{document.getElementById('mt').textContent='no math here'});await p.waitForTimeout(300);
console.log('calls after plain text',await p.evaluate(()=>window.__calls),E);
await b.close()})()
