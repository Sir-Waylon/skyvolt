const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const bad=[];const M=()=>{const m=document.getElementById('main');const o=[];[...m.children].forEach(c=>{const r=c.getBoundingClientRect();if(r.width<2||getComputedStyle(c).position==='fixed')return;const l=r.left,rr=innerWidth-r.right;if(Math.abs(l-rr)>3&&r.width<innerWidth-40)o.push((c.className||c.tagName).toString().slice(0,28)+' L'+Math.round(l)+' R'+Math.round(rr));if(r.right>innerWidth+1||r.left<-1)o.push('OVERFLOW '+(c.className||c.tagName).toString().slice(0,28))});return o.slice(0,3)};
for(const site of ['_app_skyvolt/circuit','_app_axiom/apex']){for(const w of [390,820,1280]){
const p=await (await b.newContext({viewport:{width:w,height:800}})).newPage();await p.goto('file://'+process.cwd()+'/out/'+site+'/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{S.dgr={};ALL.forEach((x,i)=>S.dgr[x]=i%2);S.dg=today();S.cu=null;route()});await p.waitForTimeout(300);
const tabs=await p.evaluate(()=>[...document.querySelectorAll('#nav button')].map(b=>b.dataset.t));
for(const t of tabs){await p.evaluate(t=>document.querySelector('#nav button[data-t="'+t+'"]').click(),t);await p.waitForTimeout(250);
 let r=await p.evaluate(M);if(r.length)bad.push(site+' w'+w+' '+t+': '+r.join('; '));
 if(t==='me'){const rows=await p.evaluate(()=>[...document.querySelectorAll('#main [data-nav^="me:"]')].map(x=>x.dataset.nav));
  for(const rw of rows){await p.evaluate(x=>{go('me');window.__V.me=null;route();document.querySelector('[data-nav="'+x+'"]').click()},rw);await p.waitForTimeout(250);r=await p.evaluate(M);if(r.length)bad.push(site+' w'+w+' '+rw+': '+r.join('; '))}}}
await p.close()}}
console.log(bad.length?bad.join('\n'):'all main blocks symmetric, no overflow');await b.close()})()
