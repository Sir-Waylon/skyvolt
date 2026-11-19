const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext({viewport:{width:360,height:740}})).newPage();await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
await p.goto('file://'+process.cwd()+`/out/_app_axiom/apex/index.html`);await p.waitForTimeout(400);
console.log(await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route();const un=UN[0],l=un.lessons[0];startSess({kind:'lesson',title:l.title,unit:un,lesson:l,steps:[{k:'card',c:l.cards[0],ut:un.title}]});
 const s=document.getElementById('sess'),sb=s.querySelector('.s-body'),o=[];s.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();if(r.right>361&&r.width>0)o.push(e.tagName+'.'+String(e.className&&e.className.baseVal!==undefined?'':e.className).slice(0,30)+' right='+Math.round(r.right)+' w='+Math.round(r.width)+' pos='+getComputedStyle(e).position)});
 return JSON.stringify({sw:sb.scrollWidth,cw:sb.clientWidth,ox:getComputedStyle(sb).overflowX,o:o.slice(0,8)})}));await b.close()})()
