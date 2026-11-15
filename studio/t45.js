const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const apps=['_app_axiom/apex','_app_axiom/geometry','_app_axiom/quanta','_app_skyvolt/circuit','_app_skyvolt/meteorology'];
for(const a of apps){const p=await (await b.newContext({viewport:{width:400,height:860}})).newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.cwd()+'/out/'+a+'/index.html');await p.waitForTimeout(400);
const r=await p.evaluate(()=>{const c={};QS.forEach(q=>{const v=virtQ(q);const k=v?v.type:q.type;c[k]=(c[k]||0)+1});return c});
// play a few of each interactive type end to end
const res=await p.evaluate(async()=>{const out=[];for(const ty of ['tune','swipe','yn','short']){const q=QS.find(q=>{const v=virtQ(q);return (v?v.type:q.type)===ty});if(!q)continue;
 startSess({kind:'practice',title:'t',steps:[{k:'try',it:mkItem(q.id)}]});await new Promise(r=>setTimeout(r,200));
 const it=Z.steps[0].it;out.push(ty+':'+it.q.type+':'+(document.querySelector('.qtext')?'q':'noq'));
 if(ty==='tune'){const n=it.q.num;const s=it.q.tn;const k=Math.round(n.v/s.step);document.getElementById('tnr').value=k;document.getElementById('tnr').dispatchEvent(new Event('input',{bubbles:true}));}
 if(ty==='swipe'){document.querySelectorAll('[data-sw]').length;for(let i=0;i<it.jd.length;i++){const oi=it.ord[it.cs];document.querySelector('[data-swj="'+(oi===0?1:0)+'"]').click();await new Promise(r=>setTimeout(r,30))}}
 if(ty==='yn'){const ans=/^(yes|true)/i.test(it.q.text[0])?'yes':'no';document.querySelector('[data-yn="'+ans+'"]').click()}
 await new Promise(r=>setTimeout(r,100));const chk=document.getElementById('chk');out.push('chk:'+(chk&&!chk.disabled));if(chk){chk.click();await new Promise(r=>setTimeout(r,200));out.push('ok:'+it.ok)}
 closeSess&&closeSess()}return out});
console.log(a.split('/').pop(),JSON.stringify(r),res.join(' '),e.slice(0,2));if(a.includes('geometry')){await p.evaluate(()=>{const q=QS.find(q=>virtQ(q)&&virtQ(q).type==='tune');startSess({kind:'practice',title:'t',steps:[{k:'try',it:mkItem(q.id)}]})});await p.waitForTimeout(300);await p.screenshot({path:'shots/tune.png'});await p.evaluate(()=>{closeSess();const q=QS.find(q=>virtQ(q)&&virtQ(q).type==='swipe');startSess({kind:'practice',title:'t',steps:[{k:'try',it:mkItem(q.id)}]})});await p.waitForTimeout(300);await p.screenshot({path:'shots/swipe.png'})}}
await b.close()})()
