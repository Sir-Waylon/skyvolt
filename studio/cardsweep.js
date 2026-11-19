const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
let tot=0;
for(const [nm,dir] of [['circuit','_app_skyvolt/circuit'],['meteo','_app_skyvolt/meteorology'],['apex','_app_axiom/apex'],['quanta','_app_axiom/quanta']]){
 const p=await (await b.newContext({viewport:{width:360,height:740}})).newPage();const E=[];p.on('pageerror',x=>E.push(x.message));await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
 await p.goto('file://'+process.cwd()+`/out/${dir}/index.html`);await p.waitForTimeout(400);
 await p.evaluate(()=>{S.dgr={};ALL.forEach((t,i)=>S.dgr[t]=i%2);S.dg=today();S.cu=null;route()});
 await p.addStyleTag({content:'*,*::before,*::after{animation:none!important;transition:none!important}'});const res=await p.evaluate(async()=>{const bad=[];let n=0,figs=0;
  for(const un of UN)for(const l of un.lessons)for(let i=0;i<l.cards.length;i++){const c=l.cards[i];
   try{startSess({kind:'lesson',title:l.title,unit:un,lesson:l,steps:[{k:'card',c:c,ut:un.title}]});}catch(e){bad.push([un.id,i,'throw '+e.message]);continue}
   n++;const s=document.getElementById('sess');if(!s){bad.push([un.id,i,'no sess']);continue}
   const h=s.innerHTML;if(/NaN|undefined|\[object|null%/.test(h.replace(/data-[a-z]+="[^"]*"/g,'')))bad.push([un.id,i,'bad text '+(h.match(/.{20}(NaN|undefined|\[object).{20}/)||[''])[0]]);
   s.querySelectorAll('svg').forEach(v=>{figs++;const r=v.getBoundingClientRect();if(r.width>0&&r.width<24&&!v.closest('button,.ti,.ic'))bad.push([un.id,i,'tiny svg '+Math.round(r.width)]);if(/NaN/.test(v.outerHTML))bad.push([un.id,i,'NaN in svg'])});
   const sb=s.querySelector('.s-body');if(sb&&sb.scrollWidth>sb.clientWidth+2)bad.push([un.id,i,'hscroll '+sb.scrollWidth+'>'+sb.clientWidth]);
   if(window.closeSess)try{closeSess()}catch(e){}}
  return {n,figs,bad:bad.slice(0,12),nbad:bad.length}});
 console.log(nm,JSON.stringify(res),E.slice(0,2));tot+=res.nbad;await p.close()}
console.log('card sweep issues',tot);await b.close()})()
