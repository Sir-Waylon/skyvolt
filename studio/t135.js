const {chromium}=require('playwright');
const CHECK=()=>{function parse(c){const m=c.match(/rgba?\(([^)]+)\)/);if(!m)return null;const p=m[1].split(/[ ,\/]+/).filter(Boolean).map(Number);return{r:p[0],g:p[1],b:p[2],a:p.length>3?p[3]:1}}
 function lum(c){const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(c.r)+.7152*f(c.g)+.0722*f(c.b)}
 function bgOf(el){let layers=[];for(let e=el;e;e=e.parentElement){const cs=getComputedStyle(e);const c=parse(cs.backgroundColor);if(c&&c.a>0)layers.push(c);if(c&&c.a>=1)break}
  let base={r:255,g:255,b:255};if(!layers.length||layers[layers.length-1].a<1){const bb=parse(getComputedStyle(document.body).backgroundColor);if(bb&&bb.a>0)base=bb}
  for(let i=layers.length-1;i>=0;i--){const l=layers[i];base={r:l.r*l.a+base.r*(1-l.a),g:l.g*l.a+base.g*(1-l.a),b:l.b*l.a+base.b*(1-l.a)}}return base}
 const out=[],seen=new Set();const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;
 while((n=w.nextNode())){const t=n.nodeValue.trim();if(t.length<2)continue;const el=n.parentElement;if(!el||seen.has(el))continue;const cs=getComputedStyle(el);if(cs.visibility==='hidden'||cs.display==='none'||+cs.opacity===0)continue;const r=el.getBoundingClientRect();if(r.width<2||r.height<2||r.bottom<0||r.top>innerHeight*3)continue;
  if(el.closest('[hidden],svg,script,style,[inert]'))continue;seen.add(el);const fg=parse(cs.color);if(!fg)continue;const bg=bgOf(el);const a=fg.a;const f2={r:fg.r*a+bg.r*(1-a),g:fg.g*a+bg.g*(1-a),b:fg.b*a+bg.b*(1-a)};
  const L1=lum(f2),L2=lum(bg),ratio=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);const size=parseFloat(cs.fontSize),bold=+cs.fontWeight>=700;const large=size>=24||(size>=18.66&&bold);
  if(ratio<(large?3:4.5)&&!el.disabled)out.push((ratio.toFixed(2))+' '+size+'px "'+t.slice(0,32)+'" '+(el.className||el.tagName).toString().slice(0,24))}
 return out.slice(0,6)};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});const rep={};
for(const site of ['_app_skyvolt/circuit','_app_skyvolt/meteorology','_app_axiom/apex','_app_axiom/quanta']){for(const th of ['light','dark']){
const p=await (await b.newContext({viewport:{width:390,height:800}})).newPage();await p.goto('file://'+process.cwd()+'/out/'+site+'/index.html');await p.waitForTimeout(500);
await p.evaluate(t=>{document.documentElement.dataset.theme=t;S.dgr={};ALL.forEach((x,i)=>S.dgr[x]=i%2);S.dg=today();S.cu=null;route()},th);await p.waitForTimeout(300);
const tabs=await p.evaluate(()=>[...document.querySelectorAll('#nav button')].map(b=>b.dataset.t));
const views=[];for(const t of tabs){await p.evaluate(t=>document.querySelector('#nav button[data-t="'+t+'"]').click(),t);await p.waitForTimeout(250);views.push([t,await p.evaluate(CHECK)])}
await p.evaluate(()=>{openArcade&&openArcade()});await p.waitForTimeout(200);views.push(['arcade',await p.evaluate(CHECK)]);await p.evaluate(()=>{document.getElementById('ar')&&document.getElementById('ar').remove();openOnline()});await p.waitForTimeout(200);views.push(['online',await p.evaluate(CHECK)]);
for(const [v,o] of views)if(o.length)rep[site+' '+th+' '+v]=o;await p.close()}}
const keys=Object.keys(rep);console.log(keys.length?keys.map(k=>k+'\n   '+rep[k].join('\n   ')).join('\n'):'no contrast failures found');await b.close()})()
