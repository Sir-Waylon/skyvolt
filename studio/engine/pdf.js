const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const j=JSON.parse(fs.readFileSync(process.argv[2]));
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const [name,out] of j.docs){const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+j.html);await p.evaluate(n=>render(n),name);
 await p.pdf({path:out,format:'Letter',printBackground:false,preferCSSPageSize:true});
 console.log(name,errs.length?errs:'ok');await p.close()}
await b.close()})();
