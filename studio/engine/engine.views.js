/* ===== views ===== */
var TABS=[['home','Home'],['plan','Plan'],['study','Study'],['notes','Notes'],['play','Practice'],['cards','Cards'],['bench','Stations'],['stats','Progress']];
var cur='home';
function show(v){
 cur=v;
 [].forEach.call(document.querySelectorAll('.view'),function(e){e.classList.toggle('on',e.id==='v-'+v)});
 [].forEach.call(document.querySelectorAll('#tabs button'),function(b){b.setAttribute('aria-current',b.dataset.v===v?'true':'false')});
 if(v==='home')drawHome();else if(v==='plan')drawPlan();else if(v==='play'){if(!Z)drawPlay()}else if(v==='cards')drawCards();else if(v==='study')drawStudy();else if(v==='stats')drawStats();
 try{history.replaceState(null,'','#'+v)}catch(e){}
 window.scrollTo(0,0);
}
$('tabs').innerHTML=TABS.map(function(t){return '<button data-v="'+t[0]+'">'+t[1]+'</button>'}).join('');
$('tabs').addEventListener('click',function(e){var b=e.target.closest('button');if(b){if(b.dataset.v==='play'&&Z&&Z.fin)Z=null;show(b.dataset.v)}});
$('ttl').textContent=P.meta.title+' '+P.meta.division;$('org').textContent=P.meta.org+' · '+P.meta.year;

/* ---- home ---- */
function drawHome(){
 var dx=S.dxp[today()]||0,goal=60,p=Math.min(100,100*dx/goal),L=lvInfo(),seen=cnt(S.seen),miss=cnt(S.miss);
 var h='<div class="hero"><div class="card goal"><div class="ring" style="--p:'+p+'"><span>'+dx+'/'+goal+'</span></div><div><h2>Daily goal</h2><p class="mute small">'+(dx>=goal?'Goal met. Keep going.':(goal-dx)+' XP to go')+' · '+L.to+' XP to level '+(L.l+1)+'</p></div></div>';
 h+='<div class="card"><h3>'+QS.length+' questions</h3><p class="mute small">'+seen+' seen · '+(QS.length-seen)+' new · '+miss+' to review</p><div class="row" style="margin-top:8px"><button class="btn" data-go="learn">Continue learning</button></div></div></div><div class="facts" style="margin-top:12px">'+P.meta.facts.map(function(f){return '<span><b>'+esc(f[0])+'</b>'+esc(f[1])+'</span>'}).join('')+'</div>';
 h+='<div class="modes"><button class="mode" data-go="blitz"><b>Blitz</b><span>60 s, earn coins for cosmetics</span></button><button class="mode" data-go="test"><b>Mock test</b><span>30 questions, timed, graded at end</span></button><button class="mode" data-go="review"'+(miss?'':' disabled style="opacity:.5"')+'><b>Review misses</b><span>'+miss+' waiting</span></button><button class="mode" data-go="match"><b>Match game</b><span>Race the clock with cards</span></button></div>';
 [['core','Core topics'],['adjacent','Adjacent topics']].forEach(function(g){
  var ts=P.topics.filter(function(t){return t.tier===g[0]});if(!ts.length)return;
  h+='<div class="head"><h2>'+g[1]+'</h2><span class="small mute">'+(g[0]==='core'?'Tested on the current rules':'Listed in other years or by other states')+'</span></div><div class="grid">';
  ts.forEach(function(t){var m=mastery(t.id),n=QS.filter(function(q){return q.t===t.id}).length;
   h+='<div class="card skill"><div class="t"><div><h3>'+esc(t.name)+'</h3><span class="small mute">'+(t.area&&t.area!=='adj'?'Area '+t.area+' · ':'')+n+' questions</span></div><span class="tag '+(m.lv>=4?'ok':'')+'">'+MN[m.lv]+'</span></div><div class="pips'+(g[0]==='adjacent'?' adj':'')+'">'+[1,2,3,4].map(function(k){return '<i class="'+(m.lv>=k?'on':'')+'"></i>'}).join('')+'</div><div class="row"><button class="btn sm" data-topic="'+t.id+'">Practice</button><button class="btn ghost sm" data-note="'+t.note+'">Notes</button></div></div>'});
  h+='</div>'});
 var sc=P.meta.scope;
 if(sc){h+='<details class="card" style="margin-top:16px"><summary><b>Scope and sources</b></summary><div class="in" style="border:0"><h3>Core areas</h3><ul>'+sc.core.map(function(a){return '<li><b>'+a[0]+'.</b> '+esc(a[1])+'</li>'}).join('')+'</ul><h3>Adjacent</h3><p>'+sc.adjacent.map(esc).join(' · ')+'</p><h3>Not tested</h3><p>'+sc.skip.map(esc).join(' · ')+'</p><h3>Hands-on stations</h3><p>'+sc.stations.map(esc).join(' · ')+'</p><p class="small mute">'+esc(P.meta.intro)+' Sources: '+sc.sources.map(function(s){return '<a href="'+s[1]+'" target="_blank" rel="noopener">'+esc(s[0])+'</a>'}).join(', ')+'.</p></div></details>'}
 $('v-home').innerHTML=h;
}
$('v-home').addEventListener('click',function(e){
 var g=e.target.closest('[data-go]'),t=e.target.closest('[data-topic]'),n=e.target.closest('[data-note]');
 if(g&&!g.disabled)go(g.dataset.go);
 if(t)start({mode:'learn',topics:[t.dataset.topic],n:10});
 if(n)openNote(n.dataset.note);
});
var ALL=P.topics.map(function(t){return t.id});
function go(m){
 if(m==='learn')start({mode:'learn',topics:ALL,n:10});
 else if(m==='blitz')start({mode:'blitz',topics:ALL,n:20,types:['mcq','short']});
 else if(m==='test')start({mode:'test',topics:P.topics.filter(function(t){return t.tier==='core'}).map(function(t){return t.id}),n:30,min:35});
 else if(m==='review')start({mode:'learn',ids:shuf(Object.keys(S.miss).filter(function(i){return QI[i]!==undefined})).slice(0,20)});
 else if(m==='match'){show('cards');startMatch()}
}
function openNote(id){show('notes');var el=$('n-'+id);if(el){el.open=true;el.scrollIntoView()}else if(id==='bench')show('bench')}

/* ---- plan ---- */
function drawPlan(){
 var tot=0,done=0;P.plan.forEach(function(d,i){d.tasks.forEach(function(t,k){tot++;if(S.plan['d'+i+'-'+k])done++})});
 var h='<div class="head"><h2>7-day plan</h2><span class="small mute">'+done+'/'+tot+' tasks</span></div><div class="pbar"><i style="width:'+(100*done/tot)+'%"></i></div><p class="small mute">About 75 min a day. Short on time: Days 3, 5, 6, then 7.</p>';
 P.plan.forEach(function(d,i){var c=0;d.tasks.forEach(function(t,k){if(S.plan['d'+i+'-'+k])c++});
  h+='<details class="day"'+(i===(S.openDay||0)?' open':'')+' data-day="'+i+'"><summary><span style="display:flex;gap:10px;align-items:center;min-width:0"><span class="dn">'+(i+1)+'</span><span>'+esc(d.t)+'<br><small class="mute" style="font-weight:500">'+esc(d.focus)+'</small></span></span><span class="tag '+(c===d.tasks.length?'ok':'')+'">'+c+'/'+d.tasks.length+'</span></summary><div class="in">';
  d.tasks.forEach(function(t,k){var id='d'+i+'-'+k;h+='<label class="task"><input type="checkbox" data-t="'+id+'"'+(S.plan[id]?' checked':'')+'><span><span class="tag">'+t[0]+'</span>'+esc(t[1])+'</span></label>'});
  h+='<div class="row" style="margin-top:6px"><button class="btn sm" data-drill="'+i+'">'+(d.drill.mode==='t'?'Start mock':'Drill · '+d.drill.n)+'</button>'+d.learn.map(function(n){return '<button class="btn ghost sm" data-note="'+n+'">Note '+n.slice(1)+'</button>'}).join('')+'</div></div></details>'});
 $('v-plan').innerHTML=h;
}
$('v-plan').addEventListener('change',function(e){if(e.target.dataset.t){S.plan[e.target.dataset.t]=e.target.checked;save();var o=[].map.call(document.querySelectorAll('.day'),function(d){return d.open});drawPlan();[].forEach.call(document.querySelectorAll('.day'),function(d,i){d.open=o[i]})}});
$('v-plan').addEventListener('click',function(e){
 var d=e.target.closest('[data-drill]'),n=e.target.closest('[data-note]');
 if(d){var dd=P.plan[+d.dataset.drill].drill;start({mode:dd.mode==='t'?'test':'learn',topics:dd.topics,n:dd.n,min:dd.min})}
 if(n)openNote(n.dataset.note)});

/* ---- notes ---- */
function drawNotes(){
 var h='<div class="head"><h2>Notes</h2><button class="btn alt sm" id="opn">Expand all</button></div>';
 P.notes.forEach(function(n,i){h+='<details id="n-'+n.id+'"'+(i===0?' open':'')+'><summary>'+esc(n.title)+'</summary><div class="in">'+n.html+'</div></details>'});
 $('v-notes').innerHTML=h;
 $('opn').onclick=function(){var d=document.querySelectorAll('#v-notes details'),o=!d[0].open;[].forEach.call(d,function(x){x.open=o});this.textContent=o?'Collapse all':'Expand all'}}

/* ---- practice setup + shop ---- */
function drawPlay(){
 var h='<div class="head"><h2>Practice</h2><span class="small mute">'+QS.length+' questions · '+cnt(S.seen)+' seen</span></div><div class="card setup"><div><b>Mode</b><div class="topics" id="pm">'+[['learn','Learn'],['test','Mock test'],['blitz','Blitz']].map(function(m,i){return '<label class="pill"><input type="radio" name="pm" value="'+m[0]+'"'+(i===0?' checked':'')+'>'+m[1]+'</label>'}).join('')+'</div></div>';
 h+='<div><div class="row" style="justify-content:space-between"><b>Topics</b><span><button class="btn ghost sm" id="ta">All</button><button class="btn ghost sm" id="tn">None</button></span></div><div class="topics">'+P.topics.map(function(t){return '<label class="pill"><input type="checkbox" class="tc" value="'+t.id+'" checked>'+esc(t.name)+(t.tier==='adjacent'?' ◇':'')+'</label>'}).join('')+'</div></div>';
 h+='<div class="row"><label>Questions <select id="pn"><option>10</option><option selected>20</option><option>30</option><option>40</option></select></label><label>Minutes <input type="number" id="pt" value="35" min="5" max="90" style="width:64px;border:1.5px solid var(--line);border-radius:8px;padding:4px 6px;background:var(--surface)"></label></div><div class="row"><button class="btn" id="pg">Start</button><button class="btn alt" id="pr">Reset seen history</button></div></div>';
 h+=shopHTML();
 $('v-play').innerHTML=h;
}
$('v-play').addEventListener('click',function(e){
 if(Z)return;var t=e.target;
 if(t.id==='ta'||t.id==='tn')[].forEach.call(document.querySelectorAll('.tc'),function(c){c.checked=t.id==='ta'});
 if(t.id==='pg'){var tp=[].filter.call(document.querySelectorAll('.tc'),function(c){return c.checked}).map(function(c){return c.value});if(!tp.length){toast('Pick a topic');return}var m=document.querySelector('input[name=pm]:checked').value;start({mode:m,topics:tp,n:+$('pn').value,min:+$('pt').value,types:m==='blitz'?['mcq','short']:null})}
 if(t.id==='pr'){if(t.dataset.arm){S.seen={};save();t.textContent='Reset seen history';delete t.dataset.arm;toast('Seen history cleared')}else{t.dataset.arm=1;t.textContent='Tap again to confirm'}}
});

/* ---- cards ---- */
var fc={i:0,flip:false,order:[],hide:false},mg=null,mtm=null;
function fcList(){var l=P.cards.map(function(_,i){return i});return fc.hide?l.filter(function(i){return !S.known[i]}):l}
function drawCards(){
 if(mg){return drawMatch()}
 var l=fcList(),h='<div class="head"><h2>Flashcards</h2><span class="small mute">'+cnt(S.known)+' / '+P.cards.length+' known</span></div>';
 if(!l.length){h+='<div class="card">All known. <button class="btn sm" id="fa">Show all</button></div>'}
 else{if(fc.i>=l.length)fc.i=0;var id=fc.order.length?fc.order[fc.i%fc.order.length]:l[fc.i];if(l.indexOf(id)<0)id=l[fc.i%l.length];var c=P.cards[id];
  h+='<div class="fc"><div class="fcard'+(fc.flip?' back':'')+'" id="fcard" tabindex="0" role="button" aria-label="Flip card">'+esc(fc.flip?c[1]:c[0])+'</div></div><div class="small mute" style="text-align:center">'+(fc.i+1)+' / '+l.length+'</div><div class="row" style="justify-content:center;margin-top:8px"><button class="btn alt" id="fpv">Back</button><button class="btn alt" id="fst">Still learning</button><button class="btn" id="fkn">Know it</button><button class="btn alt" id="fnx">Next</button></div><div class="row" style="justify-content:center;margin-top:8px"><button class="btn ghost sm" id="fsh">Shuffle</button><label class="small"><input type="checkbox" id="fhd"'+(fc.hide?' checked':'')+'> Hide known</label></div>';
  fc.cur=id}
 h+='<div class="head" style="margin-top:24px"><h2>Match game</h2></div><div class="card"><p class="small mute">Pair 6 terms with definitions as fast as you can. Best: '+(S.mbest?S.mbest+' s':'–')+'</p><button class="btn" id="mst">Start</button></div>';
 $('v-cards').innerHTML=h;
}
function fcMove(d){var l=fcList();fc.i=(fc.i+d+l.length)%Math.max(1,l.length);fc.flip=false;drawCards()}
$('v-cards').addEventListener('click',function(e){
 var t=e.target,id=t.id||(t.closest('[id]')||{}).id;
 if(mg){var b=t.closest('[data-m]');if(b)matchTap(+b.dataset.m);if(t.id==='mq'){mg=null;clearInterval(mtm);drawCards()}return}
 if(id==='fcard'){fc.flip=!fc.flip;drawCards()}
 else if(id==='fnx')fcMove(1);else if(id==='fpv')fcMove(-1);
 else if(id==='fkn'){S.known[fc.cur]=1;save();fcMove(0)}
 else if(id==='fst'){delete S.known[fc.cur];save();fcMove(1)}
 else if(id==='fsh'){fc.order=shuf(P.cards.map(function(_,i){return i}));fc.i=0;fc.flip=false;drawCards()}
 else if(id==='fhd'){fc.hide=t.checked;fc.i=0;drawCards()}
 else if(id==='fa'){fc.hide=false;drawCards()}
 else if(id==='mst')startMatch();
});
$('v-cards').addEventListener('keydown',function(e){if(e.target.id==='fcard'&&(e.key==='Enter'||e.key===' ')){e.preventDefault();fc.flip=!fc.flip;drawCards();$('fcard').focus()}});
function startMatch(){
 var ids=shuf(P.cards.map(function(_,i){return i})).slice(0,6),t=[];
 ids.forEach(function(i){t.push({k:i,s:P.cards[i][0],side:0});t.push({k:i,s:P.cards[i][1],side:1})});
 mg={tiles:shuf(t),sel:null,left:6,t0:Date.now(),pen:0,wrong:-1};
 clearInterval(mtm);mtm=setInterval(function(){var e=$('mt');if(e&&mg)e.textContent=((Date.now()-mg.t0)/1000+mg.pen).toFixed(1)},100);
 show('cards');drawMatch();
}
function drawMatch(){
 var h='<div class="head"><h2>Match</h2><span class="timer" id="mt">0.0</span></div><div class="mg">';
 mg.tiles.forEach(function(t,i){h+='<button data-m="'+i+'" class="'+(t.gone?'gone':'')+(mg.sel===i?' sel':'')+(mg.wrong===i?' wrong':'')+'">'+esc(t.s)+'</button>'});
 h+='</div><p><button class="btn ghost" id="mq">Quit</button></p>';
 $('v-cards').innerHTML=h;
}
function matchTap(i){
 var t=mg.tiles[i];if(t.gone)return;mg.wrong=-1;
 if(mg.sel===null){mg.sel=i}else if(mg.sel===i){mg.sel=null}else{
  var a=mg.tiles[mg.sel];
  if(a.k===t.k&&a.side!==t.side){a.gone=t.gone=true;mg.left--;mg.sel=null;
   if(!mg.left){clearInterval(mtm);var sec=(Date.now()-mg.t0)/1000+mg.pen;var best=!S.mbest||sec<S.mbest;if(best)S.mbest=Math.round(sec*10)/10;var xp=best?30:15;S.xp+=xp;S.coins+=10;S.dxp[today()]=(S.dxp[today()]||0)+xp;S.days[today()]=1;checkBadges();save();hud();
    $('v-cards').innerHTML='<div class="card"><div class="score">'+sec.toFixed(1)+' s</div><p class="mute">'+(best?'New best. ':'')+'+'+xp+' XP · +10 coins</p><div class="row"><button class="btn" id="mst">Again</button><button class="btn alt" id="mx">Done</button></div></div>';mg=null;$('mx').onclick=function(){drawCards()};return}}
  else{mg.pen+=2;mg.wrong=i;mg.sel=null}}
 drawMatch();
}

/* ---- stations ---- */
function drawBench(){
 var h='<div class="head"><h2>Hands-on stations</h2></div>';
 P.bench.forEach(function(b){h+='<div class="card"><h3>'+esc(b[0])+'</h3><p>'+b[1]+'</p></div>'});
 if(P.safety)h+='<div class="card" style="border-color:var(--bad)"><h3>Safety</h3><ul>'+P.safety.map(function(s){return '<li>'+esc(s)+'</li>'}).join('')+'</ul></div>';
 if(P.checklist)h+='<div class="card"><h3>Test-day checklist</h3><ul>'+P.checklist.map(function(s){return '<li>'+esc(s)+'</li>'}).join('')+'</ul></div>';
 if(P.written&&P.written.length){h+='<div class="head" style="margin-top:20px"><h2>Written drill</h2><span class="small mute">Write first, then reveal</span></div>';P.written.forEach(function(w){h+='<details class="card" style="margin-top:8px"><summary><b>'+esc(w[0])+'</b></summary><p class="mute">'+esc(w[1])+'</p></details>'})}
 $('v-bench').innerHTML=h;
}

/* ---- progress ---- */
function drawStats(){
 var h='<div class="head"><h2>Progress</h2><span class="small mute">'+S.right+' correct of '+S.total+' · best streak ×'+S.best+'</span></div><div class="card"><div class="bars">';
 P.topics.forEach(function(t){var st=S.stat[t.id]||[0,0],p=st[1]?100*st[0]/st[1]:0;h+='<div class="bar2"><span>'+esc(t.name)+'</span><span class="tr"><i style="width:'+p+'%"></i></span><span>'+(st[1]?Math.round(p)+'%':'–')+'</span></div>'});
 h+='</div></div><div class="head" style="margin-top:16px"><h2>Badges</h2></div><div class="badges">'+BADGES.map(function(b){return '<div class="bdg'+(S.badges[b[0]]?' on':'')+'"><b>'+b[1]+'</b><small>'+b[2]+'</small></div>'}).join('')+'</div>';
 h+='<div class="head" style="margin-top:16px"><h2>Save and restore</h2></div><div class="card"><p class="small mute">Copy this code to keep your progress. Paste it back to restore on any device.</p><textarea id="ex" readonly></textarea><div class="row" style="margin:8px 0"><button class="btn sm" id="cp">Copy</button></div><textarea id="im" placeholder="Paste saved progress here"></textarea><div class="row" style="margin-top:8px"><button class="btn sm" id="ip">Restore</button><button class="btn alt sm" id="rs">Reset all</button></div></div>';
 $('v-stats').innerHTML=h;if(SEC&&SEC.pack)SEC.pack(S).then(function(t){$('ex').value=t});else $('ex').value=JSON.stringify(S);
}
$('v-stats').addEventListener('click',function(e){var id=e.target.id;
 if(id==='cp'){var ta=$('ex');ta.select();try{navigator.clipboard.writeText(ta.value).then(function(){toast('Copied')},function(){document.execCommand('copy');toast('Copied')})}catch(x){try{document.execCommand('copy');toast('Copied')}catch(y){}}}
 if(id==='ip'){var txt=$('im').value.trim();var done=function(o){if(!o||typeof o.xp!=='number')throw 0;for(var k in o)S[k]=o[k];save();hud();drawStats();toast('Restored')};
  try{if(SEC&&SEC.unpack)SEC.unpack(txt).then(done,function(){toast('Code is not valid for this class')});else done(JSON.parse(txt))}catch(x){toast('Not valid progress text')}}
 if(id==='rs'){if(e.target.dataset.arm){if(SEC)SEC.clear();else try{localStorage.removeItem(KEY)}catch(x){}setTimeout(function(){location.reload()},200)}else{e.target.dataset.arm=1;e.target.textContent='Tap again to confirm'}}});

/* ---- init ---- */
drawNotes();drawBench();hud();
var h0=(location.hash||'').slice(1);show(TABS.some(function(t){return t[0]===h0})?h0:'home');
