const {chromium}=require('playwright');const fs=require('fs');const {spawn}=require('child_process');
const axe=fs.readFileSync('node_modules/axe-core/axe.min.js','utf8');
const PAGES=['/','/account/','/privacy/','/terms/','/accessibility/','/ai-disclosure/','/404.html','/app/'];
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const ext=new Set(),issues=[];let pages=0,links=0;
for(const [site,port] of [['skyvolt',8801],['axiom',8802]]){
 const sv=spawn('node',['server.mjs','../../out/'+site,port],{cwd:'backend/test'});await new Promise(r=>setTimeout(r,800));
 const base='http://'+site+'.localhost:'+port;
 const extra=fs.readdirSync('out/'+site+'/app').filter(d=>fs.existsSync('out/'+site+'/app/'+d+'/index.html')).map(d=>'/app/'+d+'/');
 for(const path of PAGES.concat(extra)){
  for(const w of [360,768,1280]){
   const ctx=await b.newContext({viewport:{width:w,height:800}});const p=await ctx.newPage();const errs=[];
   p.on('pageerror',e=>errs.push('JS '+e.message));p.on('console',m=>{if(m.type()==='error'&&!/jsdelivr|gsi|ERR_|Failed to load resource/.test(m.text()))errs.push('console '+m.text().slice(0,100))});
   await p.goto(base+path,{waitUntil:'load'});await p.waitForTimeout(500);pages++;
   const tag=site+path+'@'+w;
   const info=await p.evaluate(()=>{const d=document.documentElement;const o={ow:d.scrollWidth>innerWidth+1,title:document.title,lang:d.lang,h1:document.querySelectorAll('h1').length,main:document.querySelectorAll('main,[role=main]').length,skip:!!document.querySelector('a[href^="#"]'),vp:!!document.querySelector('meta[name=viewport]'),desc:!!document.querySelector('meta[name=description]')};
    const hs=[...document.querySelectorAll('h1,h2,h3,h4')].map(h=>+h.tagName[1]);o.skipLvl=hs.some((v,i)=>i&&v>hs[i-1]+1);
    const wrap=document.querySelector('.wrap,main');if(wrap){const r=wrap.getBoundingClientRect();o.asym=Math.abs(r.left-(innerWidth-r.right))>2}
    o.small=[...document.querySelectorAll('a,button,input,select,summary')].filter(e=>{const r=e.getBoundingClientRect();return r.width&&r.height&&(r.height<24||r.width<24)&&getComputedStyle(e).visibility!=='hidden'&&!e.closest('p,li,.doc')}).length;
    o.hrefs=[...document.querySelectorAll('a[href],link[href],script[src],img[src]')].map(e=>e.getAttribute('href')||e.getAttribute('src'));return o});
   if(info.ow)issues.push(tag+' horizontal overflow');if(!info.title||info.title.length<8)issues.push(tag+' weak title');if(!info.lang)issues.push(tag+' no lang');
   if(path!=='/404.html'&&info.h1!==1)issues.push(tag+' h1 count '+info.h1);if(!info.vp)issues.push(tag+' no viewport');if(info.asym)issues.push(tag+' content not centered');if(info.skipLvl)issues.push(tag+' heading level skip');
   if(info.small&&w===360)issues.push(tag+' '+info.small+' tiny targets');
   if(w===1280){await p.addScriptTag({content:axe});const r=await p.evaluate(()=>axe.run(document,{runOnly:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa','best-practice']}));
     for(const v of r.violations)issues.push(tag+' axe '+v.id+' ('+v.impact+') x'+v.nodes.length+' '+v.nodes[0].target.join(' ').slice(0,60));
     for(const h of info.hrefs){if(!h||h.startsWith('#')||h.startsWith('mailto:')||h.startsWith('data:'))continue;links++;
       if(/^https?:/.test(h)&&!h.includes('.localhost')){ext.add(h);continue}
       const u=new URL(h,base+path);if(u.hostname.includes('localhost')){const st=await p.evaluate(x=>fetch(x).then(r=>r.status).catch(()=>0),u.href.split('#')[0]);if(st>=400||!st)issues.push(tag+' BROKEN '+h+' '+st)}}}
   errs.forEach(e=>issues.push(tag+' '+e));await ctx.close()}}
 sv.kill()}
console.log('pages loaded',pages,'internal links checked',links);console.log('external links:',[...ext].join('\n  '));console.log('ISSUES',issues.length);console.log([...new Set(issues)].join('\n'));await b.close()})()
