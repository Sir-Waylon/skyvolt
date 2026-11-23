const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});const p=await b.newPage();
await p.goto('file://'+process.cwd()+'/out/skyvolt/app/circuit/index.html');await p.waitForTimeout(1000);
for(const k of ['7p7p-993a-2wz9-9zgf','7P7P-993A-2WZ9-9ZGF',' 7p7p-993a-2wz9-9zgf ','wrong'])console.log(JSON.stringify(k),await p.evaluate(k=>window.__sha256('voltaxis-dev-de9724ad'+k.trim().toUpperCase())==='770c8da0c76b543a740a8e0cb4c4cdacfe0ed11dbf26178f00c6277841f3a47b',k));
await b.close()})()
