(function(){"use strict";
function $(i){return document.getElementById(i)}function n(i){var v=parseFloat($(i).value);return isFinite(v)?v:0}
function t(i,s){$(i).textContent=s}function f(x,d){return isFinite(x)?x.toFixed(d):"–"}
function score(){var c=$("sc_c").value==="1",rt=n("sc_t"),tt=Math.max(n("sc_tt"),0.1),d=c?0:Math.min(Math.max(n("sc_d"),0),185),R=Math.min(Math.max(n("sc_r"),0),4)+($("sc_h").value==="1"?0.5:0),N=Math.min(Math.max(n("sc_n"),0),20),ramp=$("sc_p").value==="1";
var ds=c?40:40*(185-d)/185;if(ramp)ds*=0.5;var ts=c?Math.max(0,40*(1-Math.abs(rt-tt)/tt)):0;var ms=ramp?0:(4*R+0.1*N)*(185-d)/185;
var k=Math.pow(0.8,Math.max(0,n("sc_cv")))*Math.pow(0.9,Math.max(0,n("sc_pv")))*($("sc_m").value==="1"?0.7:1);ds*=k;ts*=k;ms*=k;
t("o_ds",f(ds,1));t("o_ts",f(ts,1));t("o_ms",f(ms,1));t("o_rs",f(ds+ts+ms,1));t("o_g",ramp?"0 g (ramp)":f(R*200+N*5,0)+" g")}
function lift(){var m=n("lf_m")+n("lf_n")+n("lf_d"),a=n("lf_a")/10000;t("lf_w",f(m,0));t("lf_f",f(m/1000*9.81,2));t("lf_p",a>0?f(m/1000*9.81/a,0):"–")}
function batt(){var s=Math.max(1,n("bt_s")),v=s*n("bt_v"),i=n("bt_l")+n("bt_t")*Math.min(Math.max(n("bt_d"),0),100)/100,r=i>0?n("bt_c")/1000/i*60:NaN;t("bt_vo",f(v,1));t("bt_i",f(i,2));t("bt_r",f(r,1));t("bt_ok",v<=12.0001?"OK ("+f(v,1)+" V)":"Too high")}
function relay(){var V=n("rl_v"),R1=n("rl_r"),Rc=n("rl_c"),C=n("rl_u")/1e6,Vp=n("rl_p"),Vd=n("rl_d"),msg="";
var Rth=R1*Rc/(R1+Rc),Vth=V*Rc/(R1+Rc),a=(Vth-Vp)/(Vth-Vd);var tc=NaN;
if(Vd<=0||Vp<=Vd){msg="Pull-in voltage must be higher than drop-out voltage."}else if(Vth<=Vp){msg="With these values the capacitor can never reach the pull-in voltage (V_Th "+f(Vth,2)+" V is not above "+f(Vp,2)+" V), so the relay will not cycle. Lower R1 or raise the battery voltage."}else{tc=-Rth*C*Math.log(a)*1000}
var td=-Rc*C*Math.log(Vd/Vp)*1000,per=tc+td;
t("rl_tc",f(tc,1));t("rl_td",f(td,1));t("rl_f",per>0?f(1000/per,1):"–");t("rl_du",per>0?f(td/per*100,0)+"%":"–");t("rl_ip",R1>0?f((V-Vd)/R1,2):"–");$("rl_msg").textContent=msg}
var map={sc:score,lf:lift,bt:batt,rl:relay};Object.keys(map).forEach(function(k){var fm=$(k);if(!fm)return;fm.addEventListener("input",map[k]);fm.addEventListener("submit",function(e){e.preventDefault()});map[k]()})})();
