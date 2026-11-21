const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await (await b.newContext()).newPage();await p.route('**/cdn.jsdelivr.net/**',r=>r.abort());
await p.goto('file://'+process.cwd()+'/out/_app_axiom/apex/index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{const d=document.createElement('div');d.id='mt';d.textContent='Slope is \\(\\frac{y_2-y_1}{x_2-x_1}\\), area \\(\\pi r^{2}\\), root \\(\\sqrt{x^2+1}\\), \\[\\int_0^1 x^2\\,dx \\le \\frac{1}{3}\\] and $$a\\cdot b \\ne 0$$ costs $5.';document.getElementById('main').appendChild(d)});
await p.waitForTimeout(7500);console.log(await p.textContent('#mt'));
console.log(await p.evaluate(()=>plainTeX('\\vec{v}=\\text{rate}\\times t, x_{n+1}=\\frac{x_n}{2}, \\sqrt[3]{8}')));await b.close()})()
