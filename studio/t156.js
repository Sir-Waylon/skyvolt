const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const out={};const b=await chromium.launch({args:['--no-sandbox']});
for(const [site,port] of [['axiom',8821],['skyvolt',8822]]){const sv=spawn('python3',['-m','http.server',String(port)],{cwd:process.cwd()+'/out/'+site,stdio:'ignore'});await new Promise(r=>setTimeout(r,800));
 for(const w of [1280,390]){const p=await b.newPage({viewport:{width:w,height:900}});const err=[];p.on('pageerror',e=>err.push(e.message));p.on('console',m=>{if(m.type()==='error'&&!/favicon|404/.test(m.text()))err.push(m.text())});
 await p.goto('http://127.0.0.1:'+port+'/');await p.waitForTimeout(600);
 const info=await p.evaluate(()=>{const c=[...document.querySelectorAll('.tqd')];return c.map(x=>({d:x.dataset.demo,svg:!!x.querySelector('svg'),sl:x.querySelectorAll('input[type=range]').length,sel:x.querySelectorAll('select').length,ro:[...x.querySelectorAll('.dro div')].map(e=>e.textContent).join(' | ')}))});
 const total=await p.evaluate(()=>document.querySelectorAll('.tq').length);
 // exercise: move first slider of every demo and read outputs
 const res=await p.evaluate(()=>{const o=[];document.querySelectorAll('.tqd').forEach(c=>{const r=c.querySelector('input[type=range]');if(!r)return;const before=c.querySelector('.dro').textContent;r.value=r.max;r.dispatchEvent(new Event('input',{bubbles:true}));o.push([c.dataset.demo,before!==c.querySelector('.dro').textContent,c.querySelector('.dro').textContent])});return o});
 const ov=await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
 if(w===390){await p.evaluate(()=>{const l=document.querySelector('.trylist');const c=[...document.querySelectorAll('.tqd')][0];l.scrollTo({left:c.offsetLeft-l.firstElementChild.offsetLeft})});await p.waitForTimeout(400);await p.screenshot({path:'shots/demo_'+site+'.png'})}
 out[site+w]={total,info:info.length,res,ov,err};await p.close()}
 sv.kill()}
console.log(JSON.stringify(out,null,1));await b.close()})();
