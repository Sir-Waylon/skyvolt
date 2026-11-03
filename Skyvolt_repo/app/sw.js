const V='tr-bb9c9f3a-9e99f6';
const PRE=["./", "icon.svg", "manifest.webmanifest", "hub.css", "reg.js", "circuit/", "circuit/app.91adcc57.js", "circuit/app.bb9c9f3a.css", "meteorology/", "meteorology/app.9d4fbfb3.js", "meteorology/app.bb9c9f3a.css"];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(PRE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==V).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin||new URL(r.url).pathname.startsWith('/api/'))return;
e.respondWith(caches.match(r).then(h=>{const n=fetch(r).then(x=>{if(x.ok){const y=x.clone();caches.open(V).then(c=>c.put(r,y))}return x}).catch(()=>h);return h||n}))});