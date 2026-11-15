const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:360,height:640}})).newPage();
await p.goto('file://'+process.cwd()+'/out/_app_axiom/apex/index.html');await p.waitForTimeout(400);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
await p.evaluate(()=>startPractice(ALL,12));await p.waitForTimeout(500);
await p.evaluate(()=>{const st=Z.steps[Z.i];if(st.it&&!st.it.done){try{if(st.it.q.type==='mcq')st.it.sel=[0];resolveIt(st.it)}catch(x){}}});await p.waitForTimeout(700);
console.log(await p.evaluate(()=>{const s=document.getElementById('sess');s.scrollTo(0,s.scrollHeight);const b=s.querySelector('.s-body'),sh=document.querySelector('.sheet');
 const arr=[...b.querySelectorAll('*')].filter(e=>e.getBoundingClientRect().height>0&&!e.closest('.sheet')).map(e=>[e.tagName+'.'+e.className,Math.round(e.getBoundingClientRect().bottom),getComputedStyle(e).position]).sort((a,c)=>c[1]-a[1]).slice(0,4);
 return JSON.stringify({pad:b.style.paddingBottom,shTop:sh&&sh.getBoundingClientRect().top,shH:sh&&sh.getBoundingClientRect().height,scrollH:s.scrollHeight,client:s.clientHeight,top:arr,shParent:sh&&sh.parentElement.id+'.'+sh.parentElement.className})}));
await b.close()})()
