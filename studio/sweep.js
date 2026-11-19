// Graphics sweep: node sweep.js [quick]  -> prints problems per screen; screenshots in shots/sweep
const {chromium}=require('playwright');const quick=process.argv[2]==='quick';
const APPS=[['circuit','_app_skyvolt/circuit'],['meteo','_app_skyvolt/meteorology'],['apex','_app_axiom/apex'],['quanta','_app_axiom/quanta']];
const VPS=quick?[[390,780]]:[[360,740],[768,1024],[1280,800]];const THEMES=quick?['light']:['light','dark'];
const METRICS=()=>{const vw=innerWidth,out=[];const de=document.documentElement;
 if(de.scrollWidth>vw+1)out.push('hscroll '+de.scrollWidth+'>'+vw);
 const bad=[];document.querySelectorAll('body *').forEach(e=>{if(e.closest('svg')&&e.tagName!=='svg')return;const r=e.getBoundingClientRect();if(r.width<1||r.height<1)return;const cs=getComputedStyle(e);if(cs.visibility==='hidden'||cs.display==='none'||cs.position==='fixed'&&false)return;
  if(r.right>vw+2&&!e.closest('[data-scroll],.scroll,pre,.tbl,table,.hs,.chips,.rail,.snap')){const p=e.parentElement;const ps=p&&getComputedStyle(p);if(!ps||!/(auto|scroll|hidden)/.test(ps.overflowX))bad.push(e.tagName+'.'+(e.className&&e.className.baseVal===undefined?String(e.className).slice(0,24):'')+' r='+Math.round(r.right))}});
 if(bad.length)out.push('overflow '+bad.length+': '+bad.slice(0,3).join(' ; '));
 const small=[];document.querySelectorAll('button,a,[role=button],input[type=checkbox],input[type=radio],select').forEach(e=>{const r=e.getBoundingClientRect();if(r.width<2||r.height<2)return;const cs=getComputedStyle(e);if(cs.visibility==='hidden'||cs.opacity==='0')return;if(e.closest('[hidden]'))return;if(r.height<32||r.width<32)small.push((e.textContent||e.getAttribute('aria-label')||e.className||'').toString().trim().slice(0,14)+' '+Math.round(r.width)+'x'+Math.round(r.height))});
 if(small.length)out.push('small-targets '+small.length+': '+small.slice(0,4).join(' | '));
 const svgs=[...document.querySelectorAll('svg')].filter(s=>{const r=s.getBoundingClientRect();return r.width>8&&r.height>8&&(r.width<10||r.height<10)});
 const imgs=[...document.querySelectorAll('img')].filter(i=>i.complete&&i.naturalWidth===0);if(imgs.length)out.push('broken img '+imgs.length);
 return out}
;(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});let total=0;
for(const [nm,dir] of APPS)for(const vp of VPS)for(const th of THEMES){
 const ctx=await b.newContext({viewport:{width:vp[0],height:vp[1]},colorScheme:th});const p=await ctx.newPage();const E=[];p.on('pageerror',x=>E.push(x.message));p.on('console',m=>{if(m.type()==='error'&&!/jsdelivr|net::ERR|Failed to load resource|file:\/\/\/api/.test(m.text()))E.push('console:'+m.text().slice(0,100))});
 await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
 await p.goto('file://'+process.cwd()+`/out/${dir}/index.html`);await p.waitForTimeout(500);
 await p.evaluate(t=>{document.documentElement.dataset.theme=t;S.dgr={};ALL.forEach((x,i)=>S.dgr[x]=i%2);S.dg=today();S.cu=null;route()},th);await p.waitForTimeout(300);
 const tabs=await p.evaluate(()=>[...document.querySelectorAll('#nav button')].map(b=>b.dataset.t));
 const shots=[];
 for(const t of tabs){await p.evaluate(t=>document.querySelector('#nav button[data-t="'+t+'"]').click(),t);await p.waitForTimeout(350);shots.push(['tab-'+t,await p.evaluate(METRICS)])
  if(!quick||t===tabs[0])await p.screenshot({path:`shots/sweep/${nm}_${vp[0]}_${th}_${t}.png`,fullPage:false})}
 // lesson card, then practice items of each type
 const les=await p.evaluate(()=>{const un=UN.find(u=>u.lessons[0]&&u.lessons[0].cards.some(c=>c.fig||c.f))||UN[0];const l=un.lessons[0];startSess({kind:'lesson',title:l.title,unit:un,lesson:l,steps:l.cards.map(c=>({k:'card',c:c,ut:un.title}))});return l.cards.length});await p.waitForTimeout(400);
 shots.push(['lesson',await p.evaluate(METRICS)]);await p.screenshot({path:`shots/sweep/${nm}_${vp[0]}_${th}_lesson.png`});
 for(const ty of ['mcq','short','order','match','multi']){const ok=await p.evaluate(ty=>{const q=QS.find(x=>x.type===ty&&!x.compass);if(!q)return 0;q.keep=true;startSess({kind:'practice',title:'Practice',steps:[{k:'try',it:mkItem(q.id)}]});return 1},ty);if(!ok)continue;await p.waitForTimeout(350);shots.push(['q-'+ty,await p.evaluate(METRICS)]);if(!quick||ty==='order')await p.screenshot({path:`shots/sweep/${nm}_${vp[0]}_${th}_q-${ty}.png`})}
 for(const [k,m] of shots)if(m.length){total+=m.length;console.log(nm,vp[0],th,k,'=>',m.join(' || '))}
 if(E.length){total+=E.length;console.log(nm,vp[0],th,'ERRORS',E.slice(0,3))}
 await ctx.close()}
console.log('sweep done; issue lines:',total);await b.close()})()
