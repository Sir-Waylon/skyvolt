// custom a11y audit: names, contrast, target size, landmarks, labels. usage: node a11y.js <url> [themes]
const {chromium}=require('playwright');
const CHECK=()=>{
const out=[];const vis=e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e);return r.width>0&&r.height>0&&s.visibility!=='hidden'&&s.display!=='none'&&s.opacity!=='0'};
const parse=c=>{const m=c.match(/rgba?\(([^)]+)\)/);if(!m)return null;const p=m[1].split(/[ ,\/]+/).map(Number);return{r:p[0],g:p[1],b:p[2],a:p[3]===undefined?1:p[3]}};
const lin=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};const L=c=>.2126*lin(c.r)+.7152*lin(c.g)+.0722*lin(c.b);
const over=(f,b)=>({r:f.r*f.a+b.r*(1-f.a),g:f.g*f.a+b.g*(1-f.a),b:f.b*f.a+b.b*(1-f.a),a:1});
const bgOf=e=>{const st=[];let n=e;while(n&&n.nodeType===1){const s=getComputedStyle(n);const c=parse(s.backgroundColor);if(s.backgroundImage&&s.backgroundImage!=='none')st.push('IMG');if(c&&c.a>0){st.push(c);if(c.a>=1)break}n=n.parentElement}
 let base={r:255,g:255,b:255,a:1};if(st.includes('IMG'))return null;for(let i=st.length-1;i>=0;i--)base=over(st[i],base);return base};
const name=e=>{let n=e.getAttribute('aria-label');if(n)return n.trim();const lb=e.getAttribute('aria-labelledby');if(lb){const t=lb.split(' ').map(i=>document.getElementById(i)).filter(Boolean).map(x=>x.textContent).join(' ').trim();if(t)return t}
 if(e.labels&&e.labels.length)return [...e.labels].map(l=>l.textContent).join(' ').trim();const t=(e.innerText||e.textContent||'').trim();if(t)return t;const im=e.querySelector('img[alt],svg[aria-label],[aria-label]');if(im)return (im.getAttribute('alt')||im.getAttribute('aria-label')||'').trim();return e.getAttribute('title')||''};
document.querySelectorAll('button,a[href],input:not([type=hidden]),select,textarea,[role=button],[role=tab],[role=switch],[tabindex]').forEach(e=>{if(!vis(e))return;
 if(!name(e)&&!(e.type==='range'&&e.getAttribute('aria-label')))out.push(['noname',e.tagName+'#'+e.id+'.'+(e.className||'')+' '+e.outerHTML.slice(0,80)]);
 const r=e.getBoundingClientRect();if((r.width<24||r.height<24)&&e.tagName!=='A'&&e.type!=='range'&&e.type!=='checkbox'&&e.type!=='radio')out.push(['small',Math.round(r.width)+'x'+Math.round(r.height)+' '+e.outerHTML.slice(0,70)]);
 if(e.tabIndex>0)out.push(['postabindex',e.outerHTML.slice(0,60)])});
const seen=new Set();document.querySelectorAll('body *').forEach(e=>{if(!vis(e))return;let own='';e.childNodes.forEach(n=>{if(n.nodeType===3)own+=n.textContent});own=own.trim();if(!own)return;
 const s=getComputedStyle(e),fg=parse(s.color),bg=bgOf(e);if(!fg||!bg)return;const f=over(fg,bg);const a=L(f),b=L(bg);const ratio=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);const px=parseFloat(s.fontSize),bold=+s.fontWeight>=700;const need=(px>=24||(px>=18.66&&bold))?3:4.5;
 if(ratio<need){const k=e.className+'|'+s.color+'|'+JSON.stringify(bg);if(!seen.has(k)){seen.add(k);out.push(['contrast',ratio.toFixed(2)+'<'+need+' "'+own.slice(0,30)+'" '+e.tagName+'.'+e.className+' fg='+s.color+' bg=rgb('+Math.round(bg.r)+','+Math.round(bg.g)+','+Math.round(bg.b)+')'])}}});
document.querySelectorAll('img:not([alt])').forEach(e=>out.push(['imgalt',e.outerHTML.slice(0,60)]));
document.querySelectorAll('svg[role=img]:not([aria-label]):not([aria-labelledby])').forEach(e=>{if(vis(e))out.push(['svgname',e.getAttribute('class')])});
const ids={};document.querySelectorAll('[id]').forEach(e=>{ids[e.id]=(ids[e.id]||0)+1});Object.keys(ids).forEach(k=>{if(ids[k]>1)out.push(['dupid',k])});
if(!document.documentElement.lang)out.push(['lang','missing']);if(!document.title)out.push(['title','missing']);
if(!document.querySelector('main,[role=main]'))out.push(['landmark','no main']);if(!document.querySelector('h1'))out.push(['h1','none']);
if(!document.querySelector('[aria-live],[role=status],[role=alert]'))out.push(['live','no live region']);
return out};
module.exports={CHECK};
if(require.main===module)(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const url=process.argv[2];const views=(process.argv[3]||'learn,practice,library,me').split(',');
for(const cs of ['light','dark']){const c=await b.newContext({viewport:{width:390,height:844},colorScheme:cs});const p=await c.newPage();await p.goto(url);await p.waitForTimeout(500);
 for(const v of views){await p.evaluate(v=>go(v),v);await p.waitForTimeout(250);const r=await p.evaluate(CHECK);const g={};r.forEach(x=>{(g[x[0]]=g[x[0]]||[]).push(x[1])});
  console.log('==',cs,v,Object.entries(g).map(([k,a])=>k+':'+a.length).join(' '));if(process.env.V)Object.entries(g).forEach(([k,a])=>a.slice(0,+process.env.V).forEach(x=>console.log('  ',k,x)))}
 await c.close()}await b.close()})();
