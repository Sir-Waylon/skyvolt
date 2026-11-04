const V='tr-16fbfb7c-22348f';
const PRE=["./", "icon.svg", "manifest.webmanifest", "hub.css", "reg.js", "circuit/", "circuit/app.3882fffd.js", "circuit/app.16fbfb7c.css", "meteorology/", "meteorology/app.cf8aafc2.js", "meteorology/app.16fbfb7c.css"];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(PRE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==V).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin||new URL(r.url).pathname.startsWith('/api/'))return;
e.respondWith(caches.match(r).then(h=>{const n=fetch(r).then(x=>{if(x.ok){const y=x.clone();caches.open(V).then(c=>c.put(r,y))}return x}).catch(()=>h);return h||n}))});