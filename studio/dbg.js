const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:400,height:800}});await p.goto('file://'+process.argv[2]);await p.waitForTimeout(500);
console.log(await p.evaluate(()=>[document.querySelectorAll('[data-to]').length,document.querySelector('.lessons').innerHTML.slice(-400)]));await b.close()})();
