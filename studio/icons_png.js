// Renders PNG icons (180 apple-touch, 192/512 manifest) from each icon.svg. usage: node icons_png.js <appdir>...
const {chromium}=require('playwright'),fs=require('fs'),path=require('path');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
for(const root of process.argv.slice(2)){
 const dirs=[root,...fs.readdirSync(root).map(d=>path.join(root,d)).filter(d=>fs.existsSync(path.join(d,'icon.svg')))];
 for(const d of dirs){const svg=fs.readFileSync(path.join(d,'icon.svg'),'utf8');
  for(const s of [180,192,512]){const p=await b.newPage({viewport:{width:s,height:s}});
   await p.setContent('<style>html,body{margin:0;background:transparent}svg{width:'+s+'px;height:'+s+'px;display:block}</style>'+svg);
   await p.screenshot({path:path.join(d,s===180?'apple-touch-icon.png':'icon-'+s+'.png'),omitBackground:true});await p.close()}}}
await b.close()})()
