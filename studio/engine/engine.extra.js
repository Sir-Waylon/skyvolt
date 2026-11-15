/* ===== study, help, cosmetics ===== */
var STUDY=P.study||null;
if(!S.lr)S.lr={};if(!S.cos)S.cos={own:{},on:{av:'a0',th:'t0',ti:'i0'}};
var stu={t:null,i:0,gl:false};
function cardsOf(t){return(STUDY&&STUDY.cards[t])||[]}
function fmtC(c){return '<h3>'+esc(c[0])+'</h3><p class="lc">'+esc(c[1])+'</p>'+(c[2]?'<div class="fml">'+esc(c[2])+'</div>':'')}
function drawStudy(){
 var h='';
 if(!STUDY){$('v-study').innerHTML='<p class="mute">No study cards in this pack.</p>';return}
 if(!stu.t){
  var tot=0,got=0;P.topics.forEach(function(t){var cs=cardsOf(t.id);tot+=cs.length;cs.forEach(function(_,i){if(S.lr[t.id+i])got++})});
  h+='<div class="head"><h2>Study</h2><span class="small mute">'+got+' / '+tot+' cards learned</span></div><p class="mute small">Short lessons. One idea per card. Tap Got it, then try a quick check.</p><div class="grid">';
  P.topics.forEach(function(t){var cs=cardsOf(t.id);if(!cs.length)return;var d=cs.filter(function(_,i){return S.lr[t.id+i]}).length;
   h+='<button class="card skill" data-st="'+t.id+'" style="text-align:left"><div class="t"><div><h3>'+esc(t.name)+'</h3><span class="small mute">'+cs.length+' cards · '+d+' done</span></div></div><div class="xpbar"><i style="width:'+(100*d/cs.length)+'%"></i></div></button>'});
  h+='</div><div class="row" style="margin-top:14px"><button class="btn alt" data-st="__gl">Glossary</button></div>';
 }else if(stu.t==='__gl'){
  h+='<div class="head"><h2>Glossary</h2><button class="btn ghost sm" data-st="">Back</button></div><dl class="gl">'+STUDY.glossary.map(function(g){return '<dt>'+esc(g[0])+'</dt><dd>'+esc(g[1])+'</dd>'}).join('')+'</dl>';
 }else{
  var cs=cardsOf(stu.t),c=cs[stu.i],tp=TOP[stu.t];
  h+='<div class="head"><h2>'+esc(tp.name)+'</h2><button class="btn ghost sm" data-st="">All topics</button></div><div class="card lesson"><span class="small mute">Card '+(stu.i+1)+' of '+cs.length+'</span><div class="xpbar"><i style="width:'+(100*(stu.i+1)/cs.length)+'%"></i></div>'+fmtC(c)+'</div><div class="row" style="margin-top:12px">'+(stu.i>0?'<button class="btn alt" data-sn="-1">Back</button>':'')+(stu.i<cs.length-1?'<button class="btn" data-sn="1">'+(S.lr[stu.t+stu.i]?'Next':'Got it')+'</button>':'<button class="btn" data-sn="2">Got it · quick check</button>')+'</div>';
 }
 $('v-study').innerHTML=h;
}
$('v-study').addEventListener('click',function(e){
 var a=e.target.closest('[data-st]');
 if(a){stu.t=a.dataset.st||null;stu.i=0;drawStudy();window.scrollTo(0,0);return}
 var n=e.target.closest('[data-sn]');
 if(n){var k=stu.t+stu.i;if(!S.lr[k]){S.lr[k]=1;dq().l++;S.xp+=2;S.dxp[today()]=(S.dxp[today()]||0)+2;S.days[today()]=1;save();hud()}
  var d=+n.dataset.sn;
  if(d===2){var ids=pick([stu.t],5,['mcq','short']).ids;var easy=QS.filter(function(q){return q.t===stu.t&&q.l===1&&(q.type==='mcq'||q.type==='short')}).map(function(q){return q.id});ids=shuf(easy).slice(0,5);var t0=stu.t;stu.t=null;start({mode:'learn',ids:ids,label:'Quick check'});return}
  stu.i=Math.max(0,stu.i+d);drawStudy();window.scrollTo(0,0)}
});
/* help: 3 steps, costs half XP on this question, no coins */
function helpHTML(it){
 var q=it.q,cs=cardsOf(q.t),h='<div class="help"><b>Help</b>',n=it.help;
 h+='<p class="small"><b>Step 1.</b> '+esc(STUDY.stuck[0])+' '+esc(STUDY.stuck[1])+'</p>';
 if(n>=2){var c=helpCard(q,cs);h+='<p class="small"><b>Step 2. Review this idea.</b></p>'+(c?'<div class="lesson card">'+fmtC(c)+'</div>':'<p class="small">Open the Study tab for this topic.</p>')}
 if(n>=3)h+='<p class="small"><b>Step 3.</b> '+(q.type==='mcq'?'Two wrong choices are removed. ':'')+esc(STUDY.stuck[2])+'</p>';
 return h+'<p class="small mute">Using help halves the XP for this question.</p></div>'}
function helpCard(q,cs){
 if(!cs.length)return null;var words=(q.q+' '+(q.o||[]).join(' ')).toLowerCase().replace(/[^a-z0-9 ]/g,' ').split(/\s+/),best=null,bs=0;
 cs.forEach(function(c){var s=0,t=(c[0]+' '+c[1]).toLowerCase();words.forEach(function(w){if(w.length>3&&t.indexOf(w)>-1)s++});if(s>bs){bs=s;best=c}});
 return best||cs[0]}
/* cosmetics: characters, hats, themes, titles. Coins buy looks only. */
var AV=[['a0','Volt',0,'#ff8a1f','#fff0dc','spark'],['a1','Gizmo',60,'#3f8cff','#e1eeff','bot'],['a2','Hoot',60,'#8a5cf6','#eee6ff','owl'],['a3','Fennec',120,'#f2603c','#ffe5dd','fox'],['a4','Capa',250,'#18b58a','#d9f5ec','cat'],['a5','Rex',400,'#5aa83a','#e5f4d9','dino']];
var AC=[['c0','No hat',0],['c1','Cap',40],['c2','Goggles',90],['c3','Headphones',150],['c4','Crown',300]];
var TH=[['t0','Indigo',0,'#5b4bff'],['t1','Ocean',80,'#0f8fd8'],['t2','Mint',80,'#12a67a'],['t3','Berry',150,'#c43b8a'],['t4','Sunset',200,'#e8582a']];
var TI=[['i0','Rookie',0,1],['i1','Volt Chaser',50,1],['i2','Ohm Hero',120,1],['i3','Diode Duke',200,1],['i4','Gate Keeper',300,1]];
function avOf(id){return AV.filter(function(x){return x[0]===id})[0]||AV[0]}
function mascot(id,mood,s,hat){
 var a=avOf(id),m=a[3],l=a[4],k=a[5];s=s||40;hat=hat===undefined?(S.cos&&S.cos.on.ac):hat;
 var b='<rect width="40" height="40" rx="12" fill="'+l+'"/><path d="M6 40c1-9 6-12 14-12s13 3 14 12z" fill="'+m+'"/>';
 if(k==='spark')b+='<path d="M20 1l-5 7h4l-2 5 7-8h-4z" fill="#ffd23c" stroke="#b8860b" stroke-width=".6"/>';
 if(k==='bot')b+='<rect x="19" y="3" width="2" height="6" fill="#33415c"/><circle cx="20" cy="3" r="2.4" fill="#ff5c5c"/><rect x="3.5" y="17" width="4" height="9" rx="2" fill="#33415c"/><rect x="32.5" y="17" width="4" height="9" rx="2" fill="#33415c"/>';
 if(k==='owl')b+='<path d="M7 12l3-9 6 7zM33 12l-3-9-6 7z" fill="'+m+'"/>';
 if(k==='fox')b+='<path d="M6 17L8 2l9 8zM34 17L32 2l-9 8z" fill="'+m+'"/><path d="M9 11l.8-5 3.7 3zM31 11l-.8-5-3.7 3z" fill="#fff"/>';
 if(k==='cat')b+='<path d="M7 16L8 3l8 6zM33 16L32 3l-8 6z" fill="'+m+'"/>';
 if(k==='dino')b+='<path d="M12 9l2-5 3 4 3-6 3 6 3-4 2 5z" fill="#2f7a1d"/>';
 b+=(k==='bot'?'<rect x="7" y="9" width="26" height="22" rx="7" fill="'+m+'"/><rect x="10" y="14" width="20" height="12" rx="5" fill="#fff"/>':'<ellipse cx="20" cy="21" rx="14" ry="13" fill="'+m+'"/><ellipse cx="20" cy="25" rx="9" ry="7" fill="#fff" opacity=".85"/>');
 if(k==='owl')b+='<circle cx="14" cy="20" r="6" fill="#fff"/><circle cx="26" cy="20" r="6" fill="#fff"/><path d="M18.5 25l1.5 3 1.5-3z" fill="#ffb02e"/>';
 var e='',o='#1b2038';
 if(mood==='happy'||mood==='cheer'){e='<path d="M11 21q3-4 6 0M23 21q3-4 6 0" stroke="'+o+'" stroke-width="2" fill="none" stroke-linecap="round"/>'}
 else if(mood==='oops'){e='<circle cx="14" cy="21" r="2" fill="'+o+'"/><circle cx="26" cy="21" r="2" fill="'+o+'"/><path d="M10 17l5 1.5M30 17l-5 1.5" stroke="'+o+'" stroke-width="1.4"/>'}
 else if(mood==='think'){e='<circle cx="14" cy="21" r="2" fill="'+o+'"/><circle cx="26" cy="21" r="2" fill="'+o+'"/><path d="M23 16.5l6-1.5" stroke="'+o+'" stroke-width="1.4"/>'}
 else e='<circle cx="14" cy="21" r="2.1" fill="'+o+'"/><circle cx="26" cy="21" r="2.1" fill="'+o+'"/>';
 var mo=mood==='cheer'?'<path d="M15 27q5 7 10 0z" fill="#7a1f2e"/>':mood==='oops'?'<path d="M16 30q4-3 8 0" stroke="'+o+'" stroke-width="1.6" fill="none" stroke-linecap="round"/><path d="M33 14q2 3 0 5q-2-2 0-5z" fill="#6cc6ff"/>':mood==='think'?'<path d="M17 29h6" stroke="'+o+'" stroke-width="1.6" stroke-linecap="round"/>':'<path d="M16 28q4 4 8 0" stroke="'+o+'" stroke-width="1.8" fill="none" stroke-linecap="round"/>';
 b+=e+mo+(k==='cat'?'<path d="M5 24h6M5 28l6-2M35 24h-6M35 28l-6-2" stroke="'+o+'" stroke-width=".9"/>':'')+(mood==='cheer'||mood==='happy'?'<circle cx="9.5" cy="26" r="2.2" fill="#ff9aa8" opacity=".6"/><circle cx="30.5" cy="26" r="2.2" fill="#ff9aa8" opacity=".6"/>':'');
 if(hat==='c1')b+='<path d="M9 12q11-11 22 0z" fill="#e23d3d"/><rect x="7" y="11" width="26" height="3" rx="1.5" fill="#b92b2b"/>';
 if(hat==='c2')b+='<rect x="8" y="16" width="24" height="9" rx="4.5" fill="#222" opacity=".85"/><circle cx="14" cy="20.5" r="3.4" fill="#9fe3ff"/><circle cx="26" cy="20.5" r="3.4" fill="#9fe3ff"/>';
 if(hat==='c3')b+='<path d="M7 22q0-15 13-15t13 15" stroke="#333" stroke-width="2.4" fill="none"/><rect x="4.5" y="19" width="5" height="9" rx="2.4" fill="#333"/><rect x="30.5" y="19" width="5" height="9" rx="2.4" fill="#333"/>';
 if(hat==='c4')b+='<path d="M10 11l-1-9 6 5 5-7 5 7 6-5-1 9z" fill="#ffc83d" stroke="#b8860b" stroke-width=".8"/>';
 return '<svg class="mas '+(mood||'')+'" width="'+s+'" height="'+s+'" viewBox="0 0 40 40" aria-hidden="true">'+b+'</svg>'}
function avSVG(id,s){return mascot(id,'happy',s)}
function applyCos(){var t=TH.filter(function(x){return x[0]===S.cos.on.th})[0]||TH[0],r=document.documentElement.style;r.setProperty('--pri',t[3]);r.setProperty('--pri-ink','#fff');r.setProperty('--pri-soft','color-mix(in srgb,'+t[3]+' 14%,var(--surface))');var h=$('mav');if(h)h.innerHTML=mascot(S.cos.on.av,'happy',34)}
if(!S.cos.on.ac)S.cos.on.ac='c0';
function shopHTML(){
 function sec(name,list,key,render){return '<h3>'+name+'</h3><div class="shop">'+list.map(function(x){var own=S.cos.own[x[0]]||x[2]===0,on=S.cos.on[key]===x[0];
  return '<div class="up">'+render(x)+'<b>'+x[1]+'</b><button class="btn sm" data-cos="'+x[0]+'|'+key+'"'+(on?' disabled':(!own&&S.coins<x[2]?' disabled':''))+'>'+(on?'Equipped':own?'Equip':'Buy · '+x[2])+'</button></div>'}).join('')+'</div>'}
 return '<div class="head" style="margin-top:20px"><h2>Cosmetics</h2><span class="small mute">'+S.coins+' coins · looks only, no advantages</span></div>'+sec('Characters',AV,'av',function(x){return mascot(x[0],'happy',56,S.cos.on.ac)})+sec('Hats',AC,'ac',function(x){return mascot(S.cos.on.av,'happy',56,x[0])})+sec('Themes',TH,'th',function(x){return '<i class="sw" style="background:'+x[3]+'"></i>'})+sec('Titles',TI,'ti',function(){return ''})}
document.addEventListener('click',function(e){var b=e.target.closest('[data-cos]');if(!b)return;var p=b.dataset.cos.split('|'),all=AV.concat(AC,TH,TI),it=all.filter(function(x){return x[0]===p[0]})[0];
 if(!S.cos.own[p[0]]&&it[2]>0){if(S.coins<it[2])return;S.coins-=it[2];S.cos.own[p[0]]=1}S.cos.on[p[1]]=p[0];save();hud();applyCos();if(cur==='play')drawPlay()});
/* header: avatar + settings */
(function(){var hud=document.querySelector('.hud');if(!hud)return;
 hud.insertAdjacentHTML('beforeend','<button class="iconbtn" id="mav" aria-label="My character"></button><button class="iconbtn" id="gear" aria-label="Display settings"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/></svg></button>')})();
var A11={};try{A11=JSON.parse(localStorage.getItem('scioly:ui')||'{}')}catch(e){}
function applyUI(){var c=document.documentElement.classList;c.toggle('xl',A11.xl==1);c.toggle('xxl',A11.xl==2);c.toggle('rm',!!A11.rm);c.toggle('hc',!!A11.hc);c.toggle('dys',!!A11.dys);c.toggle('focus',!!A11.focus)}
function saveUI(){try{localStorage.setItem('scioly:ui',JSON.stringify(A11))}catch(e){}applyUI()}
applyUI();
document.addEventListener('click',function(e){
 if(e.target.closest('#gear')){var p=$('uip');if(p){p.remove();return}
  var d=document.createElement('div');d.id='uip';d.className='card';d.innerHTML='<h3>Display</h3><label class="small">Text size <select id="u-xl"><option value="0">Normal</option><option value="1">Large</option><option value="2">Extra large</option></select></label><label><input type="checkbox" id="u-rm"> Reduce motion</label><label><input type="checkbox" id="u-hc"> High contrast</label><label><input type="checkbox" id="u-dys"> Easy-read font and spacing</label><label><input type="checkbox" id="u-focus"> Focus mode (hide extras while answering)</label><button class="btn sm" id="u-x">Done</button>';
  document.body.appendChild(d);$('u-xl').value=A11.xl||0;$('u-rm').checked=!!A11.rm;$('u-hc').checked=!!A11.hc;$('u-dys').checked=!!A11.dys;$('u-focus').checked=!!A11.focus;return}
 if(e.target.id==='u-x'){$('uip').remove()}
 if(e.target.closest('#mav')){show(SEC&&SEC.share?'me':'stats')}});
document.addEventListener('change',function(e){var t=e.target;if(t.id==='u-xl')A11.xl=+t.value;else if(t.id==='u-rm')A11.rm=t.checked;else if(t.id==='u-hc')A11.hc=t.checked;else if(t.id==='u-dys')A11.dys=t.checked;else if(t.id==='u-focus')A11.focus=t.checked;else return;saveUI()});
/* wrong-answer learn card */
function learnHTML(q){var c=STUDY&&helpCard(q,cardsOf(q.t));if(!c)return '';return '<div class="learn">'+mascot(S.cos.on.av,'think',44)+'<div><b>Quick lesson</b>'+fmtC(c)+'<button class="btn alt sm" data-st="'+q.t+'" data-go-study="1">More on this topic</button></div></div>'}
/* home greeting */
function greet(){var dx=S.dxp[today()]||0,st=dayStreak(),L=lvInfo(),m;
 if(!S.total)m='Hi! I am '+avOf(S.cos.on.av)[1]+'. Tap Study for a short lesson, or jump into a quiz.';
 else if(dx>=60)m='Daily goal done! Every extra answer is bonus XP.';
 else if(st>=3)m=st+' days in a row. Keep the streak alive today.';
 else m=(60-dx)+' XP to hit today\'s goal. A 5-question quiz gets you close.';
 return '<div class="hero2">'+mascot(S.cos.on.av,dx>=60?'cheer':'happy',72)+'<div class="bubble">'+esc(m)+'<div class="small mute">Level '+L.l+' · '+esc(L.name)+'</div></div></div>'}
/* ---- Me: profile, quests, friends (signed share codes) ---- */
var QU=[['Answer 10 questions',function(){return dq().a},10,15],['Get 7 right',function(){return dq().r},7,15],['Learn 3 cards',function(){return dq().l},3,10]];
if(SEC&&SEC.share){TABS.splice(TABS.length-1,0,['me','Me']);$('tabs').innerHTML=TABS.map(function(t){return '<button data-v="'+t[0]+'">'+t[1]+'</button>'}).join('');$('tabs').insertAdjacentHTML('afterend','')}
if(!S.fr)S.fr={};if(!S.nm)S.nm='';
function myCard(){var L=lvInfo();return{n:S.nm||'Player',x:S.xp,l:L.l,s:dayStreak(),a:S.cos.on.av,ti:S.cos.on.ti,t:Date.now()}}
function drawMe(){
 var L=lvInfo(),q=dq(),h='<div class="head"><h2>Me</h2></div><div class="card"><div class="row">'+mascot(S.cos.on.av,'happy',64)+'<div><b>'+esc(S.nm||'Player')+'</b><div class="small mute">'+esc((TI.filter(function(x){return x[0]===S.cos.on.ti})[0]||TI[0])[1])+' · Lv '+L.l+' · '+dayStreak()+' day streak</div></div></div><div class="row" style="margin-top:10px"><input id="nm" maxlength="14" placeholder="Nickname (no real name)" value="'+esc(S.nm)+'" style="border:1.5px solid var(--line);border-radius:8px;padding:8px;background:var(--surface);color:inherit"><button class="btn sm" id="nms">Save</button></div></div>';
 h+='<div class="head" style="margin-top:16px"><h2>Today\'s quests</h2></div><div class="card">'+QU.map(function(u){var v=Math.min(u[2],u[1]()),dn=v>=u[2];return '<div class="bar2"><span>'+u[1]+(dn?' ✓':'')+'</span><span class="tr"><i style="width:'+100*v/u[2]+'%"></i></span><span>'+v+'/'+u[2]+'</span></div>'}).join('')+'<p class="small mute">One missed day in a week will not break your streak after 7 days in a row.</p></div>';
 h+='<div class="head" style="margin-top:16px"><h2>Friends</h2></div><div class="card"><p class="small mute">Share your code. Paste a friend\'s code to add them. Codes cannot be faked and hold no personal info.</p><textarea id="mc" readonly rows="3"></textarea><div class="row"><button class="btn sm" id="mcp">Copy my code</button></div><textarea id="fc" rows="2" placeholder="Paste a friend code (SCI1...)"></textarea><div class="row"><button class="btn sm alt" id="fadd">Add friend</button></div></div><div id="lb"></div>';
 $('v-me').innerHTML=h;
 SEC.share(myCard()).then(function(t){$('mc').value=t});
 var rows=Object.keys(S.fr).map(function(k){return S.fr[k]}).concat([Object.assign(myCard(),{me:1})]).sort(function(a,b){return b.x-a.x});
 $('lb').innerHTML='<div class="head" style="margin-top:16px"><h2>Leaderboard</h2></div><div class="card">'+rows.map(function(r,i){return '<div class="row" style="padding:6px 0;'+(r.me?'font-weight:800':'')+'"><span>'+(i+1)+'</span>'+avSVG(r.a,30)+'<span style="flex:1">'+esc(r.n)+' <span class="small mute">Lv '+r.l+' · '+r.s+'d</span></span><b>'+r.x+' XP</b></div>'}).join('')+'<p class="small mute">Friend scores update when they send a new code.</p></div>'}
document.addEventListener('click',function(e){var id=e.target.id;
 if(id==='nms'){S.nm=$('nm').value.replace(/[<>&"]/g,'').slice(0,14);save();drawMe()}
 if(id==='mcp'){var ta=$('mc');ta.select();try{navigator.clipboard.writeText(ta.value);toast('Copied')}catch(x){document.execCommand('copy')}}
 if(id==='fadd'){SEC.open($('fc').value).then(function(o){if(typeof o.x!=='number'||o.x<0||o.x>1e6)throw 0;var k=String(o.n).slice(0,14);var old=S.fr[k];if(!old||o.t>=old.t){S.fr[k]={n:k,x:o.x|0,l:o.l|0,s:o.s|0,a:String(o.a),ti:String(o.ti),t:o.t|0}}save();drawMe();toast('Friend added')},function(){toast('That code is not valid for this class')})}});
if(!document.getElementById('v-me')){var _s=document.createElement('section');_s.className='view';_s.id='v-me';$('v-stats').parentNode.insertBefore(_s,$('v-stats'))}
var _show=show;show=function(v){_show(v);if(v==='me'&&SEC&&SEC.share)drawMe();if(v==='home')$('v-home').insertAdjacentHTML('afterbegin',greet())};
if(cur==='me')show('me');
if(cur==='study')drawStudy();applyCos();show(cur);
document.addEventListener('click',function(e){var g=e.target.closest('[data-go-study]');if(!g)return;stu.t=g.dataset.st;stu.i=0;show('study')});
