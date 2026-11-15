const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:420,height:900}});const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/axiom/app/index.html');await p.waitForTimeout(500);
await p.screenshot({path:'ck/learn0.png'});
console.log(await p.evaluate(()=>{const u=[...document.querySelectorAll('.unit h3')].map(x=>x.textContent);return [u.length,u.slice(0,3),!!document.querySelector('.dgc'),document.querySelector('.pace')&&document.querySelector('.pace').textContent]}));
await p.click('#dgs');await p.waitForTimeout(300);
const n=await p.evaluate(()=>{return Z.steps.length});console.log('diag steps',n);
// answer: correct for geometry topics, wrong for algebra
await p.evaluate(()=>{Z.steps.forEach(s=>{const it=s.it,t=it.q.t;const alg=['eq','lin','sys','exp','fac','rad','qdr'].includes(t);
 if(it.q.type==='mcq'){it.sel=[alg?it.perm.findIndex(x=>x!==0):it.perm.indexOf(0)]}else{it.val=alg?'zz':String(it.q.ans||it.q.a||'1')}});finishSess();Z.sumDone=1;drawSess()});
await p.waitForTimeout(500);await p.screenshot({path:'ck/diag.png'});
await p.evaluate(()=>closeSess());await p.waitForTimeout(500);
console.log(await p.evaluate(()=>{const u=[...document.querySelectorAll('.unit h3')].map(x=>x.textContent);return [u.length,u.slice(0,4),Object.keys(S.dgr).length,JSON.stringify(S.dgr)]}));
await p.screenshot({path:'ck/learn1.png'});console.log(e);await b.close()})()
