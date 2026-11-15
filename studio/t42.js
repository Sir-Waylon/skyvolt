const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const pg=await (await b.newContext({viewport:{width:1100,height:900}})).newPage();const e=[];pg.on('pageerror',x=>e.push(x.message));
const apps={voltaic:'_app_skyvolt/circuit',stratus:'_app_skyvolt/meteorology',vertex:'_app_axiom/geometry',apex:'_app_axiom/apex',quanta:'_app_axiom/quanta'};
for(const [k,v] of Object.entries(apps)){await pg.goto('file://'+process.cwd()+'/out/'+v+'/index.html');await pg.waitForTimeout(300);
 await pg.evaluate(()=>{const d=document.createElement('div');d.id='sheet';d.style.cssText='position:fixed;inset:0;background:#fff;z-index:99999;display:flex;flex-wrap:wrap;gap:4px;padding:6px;overflow:auto';
  d.innerHTML=AV.map(a=>'<div style="text-align:center;font:10px sans-serif">'+mascot(a[0],'happy',130)+'<br>'+a[1]+' r'+a[6]+'</div>').join('');document.body.appendChild(d)});
 await pg.waitForTimeout(200);await pg.screenshot({path:'shots/ppl_'+k+'.png'});
 await pg.evaluate(()=>{document.getElementById('sheet').innerHTML=AV.slice(0,12).map(a=>mascot(a[0],'happy',56)).join('')});await pg.screenshot({path:'shots/ppl_'+k+'_s.png',clip:{x:0,y:0,width:900,height:90}});}
console.log(e);await b.close()})()
