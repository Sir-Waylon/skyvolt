const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:900}});const e=[];p.on('pageerror',x=>e.push(x.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(400);
await p.evaluate(()=>{S.coins=900;save();document.getElementById('app').innerHTML='<div class="wrap">'+shopHTML()+'</div>'});
await p.waitForTimeout(300);await p.screenshot({path:'ck/shop.png',fullPage:true});console.log('errs',e);await b.close()})()
