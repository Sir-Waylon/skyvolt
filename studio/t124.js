const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const site of ['_app_skyvolt/circuit','_app_skyvolt/meteorology']){const p=await (await b.newContext()).newPage();await p.goto('file://'+process.cwd()+'/out/'+site+'/index.html');await p.waitForTimeout(400);
console.log(site,JSON.stringify(await p.evaluate(()=>UN.map(u=>u.id+'='+u.title+'|'+u.lessons.map(l=>l.title).join('/')))));await p.close()}await b.close()})()
