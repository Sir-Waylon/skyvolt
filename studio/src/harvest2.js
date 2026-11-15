const vm=require('vm'),fs=require('fs');
const U='/root/.claude/uploads/bdb1ee03-0916-54eb-a354-ea75cf26b960/';
const out=JSON.parse(fs.readFileSync('harvest.json'));
function stub(){const f=function(){};return new Proxy(f,{get:(t,k)=>k===Symbol.toPrimitive?()=>'':k==='length'?0:(k==='then'?undefined:stub()),apply:()=>stub(),construct:()=>stub(),set:()=>true})}
for(const f of ['975f009b-Circuit_Lab_B_Mastery_Test.html','a8f23d04-Circuit_Lab_B_Week_1_Mastery_Test.html']){
 const html=fs.readFileSync(U+f,'utf8');let sc=[...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(m=>m[1]).sort((a,b)=>b.length-a.length)[0];
 const names=[...new Set([...sc.matchAll(/function (gen\d+_\d+)\s*\(/g)].map(m=>m[1]))];
 const sn=(sc.match(/var strandNames\s*=\s*(\[[^\]]*\])/)||[])[1];
 // expose generators: inject before last closing of IIFE
 sc=sc.replace(/\}\)\(\);?\s*$/,'globalThis.__G={'+names.map(n=>n+':'+n).join(',')+'};})();');
 const ctx=vm.createContext({document:stub(),window:stub(),localStorage:{getItem:()=>null,setItem(){},removeItem(){}},setTimeout:()=>0,setInterval:()=>0,clearInterval(){},console,Math,JSON,Date,location:{hash:''},navigator:stub(),history:stub(),matchMedia:()=>({matches:false,addEventListener(){}}),requestAnimationFrame:()=>0});
 try{vm.runInContext(sc,ctx,{timeout:8000})}catch(e){console.error(f,'err',e.message.slice(0,150))}
 const G=ctx.__G;if(!G){console.error(f,'no G');continue}
 const strands=sn?JSON.parse(sn):[];const seen=new Set(),rows=[];
 for(const n of names){const si=+n.match(/gen(\d+)_/)[1];
  for(let i=0;i<300;i++){let q;try{q=G[n]()}catch(e){break}
   if(!q||!q.q||!q.choices)continue;if(seen.has(q.q))continue;seen.add(q.q);
   rows.push({cat:'s'+si,catname:strands[si]||('strand '+si),q:q.q,o:q.choices,a:q.correct,t:q.tip||'',h:''})}}
 out[f]=rows;console.error(f,'rows',rows.length,'gens',names.length);
}
fs.writeFileSync('harvest.json',JSON.stringify(out));
