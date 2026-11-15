const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const apps=['out/skyvolt/app/circuit','out/skyvolt/app/meteorology','out/axiom/app/geometry','out/axiom/app/apex','out/axiom/app/quanta'];let tot=0;
for(const a of apps){const p=await (await b.newContext({viewport:{width:380,height:900}})).newPage();const errs=[];p.on('pageerror',x=>errs.push(x.message));
await p.goto('file://'+process.cwd()+'/'+a+'/index.html');await p.waitForTimeout(400);
const r=await p.evaluate(()=>{const res=[];const root=document.createElement('div');root.id='wt';document.body.appendChild(root);
 P.units.forEach(u=>u.lessons.forEach(L=>L.cards.forEach(c=>{if(c.lab&&typeof c.lab==='object'){const d=document.createElement('div');d.className='lab';root.appendChild(d);try{labInit(d,c.lab);
  // answer predict
  const pb=d.querySelector('.wpre button');if(pb)pb.click();
  d.querySelectorAll('input[type=range]').forEach(s=>{[s.min,s.max,s.value].forEach(v=>{s.value=v;s.dispatchEvent(new Event('input'))})});
  d.querySelectorAll('.wtog,.wbit,.wstep').forEach(x=>{try{x.click()}catch(e){}});
  const bad=/NaN|undefined|–/.test(d.innerText)&&!/undefined \(/.test(d.innerText);
  res.push([u.id,c.h,d.innerText.length<8?'EMPTY':(bad?'BADTXT':'ok'),bad?d.innerText.slice(0,160):''])}catch(e){res.push([u.id,c.h,'ERR '+e.message,''])}}})));return res});
const bad=r.filter(x=>x[2]!=='ok');tot+=r.length;console.log(a,r.length,'bad:',JSON.stringify(bad),errs.slice(0,3));
await p.evaluate(()=>{document.getElementById('wt').style.cssText='position:fixed;inset:0;z-index:999;background:#fff;overflow:auto;padding:8px'});await p.screenshot({path:'shots/wid_'+a.split('/').pop()+'.png'});}
console.log('total',tot);await b.close()})()
