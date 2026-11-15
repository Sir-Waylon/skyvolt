const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();p.setDefaultTimeout(4000);const E=[];p.on('pageerror',x=>E.push(x.message));
await p.goto('file://'+process.cwd()+'/out/_app_skyvolt/circuit/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;
 const ids=QS.slice(0,40).map(q=>q.id);ids.slice(0,6).forEach((id,i)=>{S.mem[id]=[i%3,dayN()-2+BOX[i%3],2]});route()});
await p.evaluate(()=>startMission());await p.waitForTimeout(400);
const info=await p.evaluate(()=>({n:Z.steps.length,locks:Z.steps.filter(s=>s.lock).length,first:Z.steps[0].lock||0,mains:Z.mains}));console.log(info);
console.log('tag:',await p.evaluate(()=>(document.querySelector('#sess .tag')||{}).textContent),'conf:',await p.evaluate(()=>document.querySelectorAll('[data-cf]').length));
await p.screenshot({path:'shots/t94_a.png'});
// answer wrong with Sure on each try step, count
let guard=0;while(guard++<40){const st=await p.evaluate(()=>{if(!Z||Z.fin)return 'fin';const s=Z.steps[Z.i];return s.k+':'+(s.lock||0)});if(st==='fin')break;
 if(st.startsWith('card')){await p.evaluate(()=>document.getElementById('go').click());continue}
 if(st.startsWith('explain')){await p.evaluate(()=>{const e=document.querySelector('#exf,#exb,#exs,#exq,#exn');e&&e.click()});continue}
 await p.evaluate(()=>{const it=Z.steps[Z.i].it;const q=it.q;const cf=document.querySelector('[data-cf="s"]');cf&&cf.click();
 });
 // choose first option then check
 await p.evaluate(()=>{const st=Z.steps[Z.i],it=st.it,q=it.q;if(q.type==='mcq'){const btn=document.querySelector('[data-sq]');btn&&btn.click()}else if(q.type==='short'){const inp=document.getElementById('sv');if(inp){inp.value='0';inp.dispatchEvent(new Event('input',{bubbles:true}))}}});
 await p.evaluate(()=>{const c=document.getElementById('chk');if(c&&!c.disabled)c.click()});
 await p.evaluate(()=>{const n=document.getElementById('nx');n&&n.click();const e2=document.getElementById('exp');if(e2){document.getElementById('nx')&&document.getElementById('nx').click()}});await p.waitForTimeout(40)}
console.log('hyper',await p.evaluate(()=>Object.keys(S.hyper).length),'cal',await p.evaluate(()=>JSON.stringify(S.cal)),'retests',await p.evaluate(()=>Z.steps.filter(s=>s.lock===2).length));
await p.screenshot({path:'shots/t94_b.png'});console.log(E.slice(0,4));await b.close()})()
