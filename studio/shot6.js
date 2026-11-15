const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:700,height:260}});await p.goto('file://'+process.argv[2]);await p.waitForTimeout(300);
await p.evaluate(()=>{document.body.innerHTML='<div style="display:flex;gap:6px;flex-wrap:wrap;padding:10px;background:#fff">'+AV.map(a=>mascot(a[0],'happy',100,null)).join('')+AV.map(a=>mascot(a[0],'cheer',60,null)).join('')+'</div>'});
await p.screenshot({path:'ck/av.png'});await b.close()})();
