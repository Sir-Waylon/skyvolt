const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?(e.name.startsWith('_')||e.name==='app'?[]:walk(path.join(d,e.name))):e.name.endsWith('.html')?[path.join(d,e.name)]:[])}
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});const bad=[];let n=0;
for(const root of ['out/skyvolt','out/axiom']){for(const f of walk(root)){for(const w of [390,1280]){const p=await (await b.newContext({viewport:{width:w,height:800}})).newPage();await p.goto('file://'+process.cwd()+'/'+f);await p.waitForTimeout(150);n++;
const r=await p.evaluate(()=>{const o=[];if(document.documentElement.scrollWidth>innerWidth+1)o.push('hscroll '+document.documentElement.scrollWidth);document.querySelectorAll('.wrap,main>section>.wrap,h1,.cta').forEach(c=>{const r=c.getBoundingClientRect();if(r.width<2)return;const l=r.left,rr=innerWidth-r.right;if(Math.abs(l-rr)>3&&!c.closest('nav,header,footer')&&getComputedStyle(c).textAlign!=='left'&&c.matches('.cta,h1'))o.push(c.tagName+'.'+c.className+' L'+Math.round(l)+' R'+Math.round(rr))});return o.slice(0,3)});
if(r.length)bad.push(f+' w'+w+': '+r.join('; '));await p.close()}}}
console.log(n+' page views;',bad.length?'\n'+bad.slice(0,20).join('\n'):'no overflow');await b.close()})()
