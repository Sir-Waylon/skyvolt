const V='tr-7acc3e2c-447d4f';
const PRE=["./", "icon.svg", "manifest.webmanifest", "hub.css", "reg.js", "circuit/", "circuit/app.37f4344d.js", "circuit/app.7acc3e2c.css", "meteorology/", "meteorology/app.54e6623e.js", "meteorology/app.7acc3e2c.css"];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(PRE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==V).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin||new URL(r.url).pathname.startsWith('/api/'))return;
e.respondWith(caches.match(r).then(h=>{const n=fetch(r).then(x=>{if(x.ok){const y=x.clone();caches.open(V).then(c=>c.put(r,y))}return x}).catch(()=>h);return h||n}))});