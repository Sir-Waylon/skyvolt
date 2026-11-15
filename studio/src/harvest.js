const vm=require('vm'),fs=require('fs');
const U='/root/.claude/uploads/bdb1ee03-0916-54eb-a354-ea75cf26b960/';
function stub(){const f=function(){};return new Proxy(f,{get:(t,k)=>k===Symbol.toPrimitive?()=>'':k==='length'?0:(k==='then'?undefined:stub()),apply:()=>stub(),construct:()=>stub(),set:()=>true})}
function run(file){
 const html=fs.readFileSync(U+file,'utf8');const scripts=[...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(m=>m[1]).filter(s=>s.includes('cats'));
 if(!scripts.length)return null;
 const ctx=vm.createContext({document:stub(),window:stub(),localStorage:{getItem:()=>null,setItem(){},removeItem(){}},setTimeout:()=>0,setInterval:()=>0,clearInterval(){},console,Math,JSON,Date,location:{hash:''},navigator:stub(),history:stub(),matchMedia:()=>({matches:false,addEventListener(){}}),requestAnimationFrame:()=>0});
 try{vm.runInContext(scripts[0],ctx,{timeout:5000})}catch(e){console.error(file,'run err',e.message.slice(0,120))}
 return ctx;
}
const out={};
for(const f of ['a60274eb-Circuit_Lab_B_Hub.html','975f009b-Circuit_Lab_B_Mastery_Test.html','a8f23d04-Circuit_Lab_B_Week_1_Mastery_Test.html']){
 const c=run(f);if(!c){console.error('no ctx',f);continue}
 let cats;try{cats=vm.runInContext('typeof cats!=="undefined"?cats:null',c)}catch(e){}
 if(!cats){console.error(f,'no cats');continue}
 const seen=new Set(),rows=[];
 cats.forEach(cat=>{const g=cat.g;(Array.isArray(g)?g:[]).forEach(fn=>{
   const reps=typeof fn==='function'?120:1;
   for(let i=0;i<reps;i++){let q;try{q=typeof fn==='function'?fn():fn}catch(e){break}
     if(!q||!q.q||!q.o||q.a===undefined)continue;
     const key=q.q;if(seen.has(key))continue;seen.add(key);
     rows.push({cat:cat.id,catname:cat.n,tip:cat.tip,q:q.q,o:q.o,a:q.a,t:q.t||'',h:q.h||''})}})});
 out[f]=rows;console.error(f,'rows',rows.length,'cats',cats.map(c=>c.id).join(','));
}
fs.writeFileSync('harvest.json',JSON.stringify(out));
