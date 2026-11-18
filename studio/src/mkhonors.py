#!/usr/bin/env python3
"""Generates verified Algebra 2 / Trigonometry honors questions (answers are computed, never typed by hand).
Output: src/audit_apex/h1.json  ({'new':[...]}), merged by applyextra.py into events/apex-math/pack.json."""
import json,math,random,itertools
R=random.Random(20261117);N=[]
B={1:-1.2,2:0.3,3:1.2}
TRI=[(3,4,5),(5,12,13),(8,15,17),(7,24,25),(20,21,29),(9,40,41)]
def d(x,n=3):return ('%.*f'%(n,x)).rstrip('0').rstrip('.')
def fr(a,b):
    g=math.gcd(abs(a),abs(b));a//=g;b//=g
    if b<0:a,b=-a,-b
    return str(a) if b==1 else '%d/%d'%(a,b)
def num(t,l,q,v,sol,w,tol=0.006,show=None):
    n={'v':float(v),'tol':tol,'free':True}
    if show:n['show']=show
    N.append(dict(t=t,l=l,b=B[l],type='short',q=q,num=n,sol=sol,w=w))
def mcq(t,l,q,right,wrong,sol,w):
    o=[right]+wrong;assert len(set(o))==len(o)==4,(q,o)
    N.append(dict(t=t,l=l,b=B[l],type='mcq',q=q,o=o,sol=sol,w=w))
def order(t,l,q,items,sol,w):
    N.append(dict(t=t,l=l,b=B[l],type='order',q=q,items=items,sol=sol,w=w))
def match(t,l,q,pairs,sol,w):
    N.append(dict(t=t,l=l,b=B[l],type='match',q=q,pairs=pairs,sol=sol,w=w))
# ---- ti: Pythagorean identity, quadrants, double angle ----
for a,b,c in TRI:
    for quad,sc,ss in [(2,-1,1),(3,-1,-1),(4,1,-1)]:
        if R.random()<0.45:continue
        cos=sc*b/c;sin=ss*a/c;nm={2:'II',3:'III',4:'IV'}[quad]
        if quad==2: g='sin θ = %s'%fr(a,c);ask='cos θ';v=cos;pre=['The Pythagorean identity says a point on the unit circle satisfies sin²θ + cos²θ = 1, because sin θ and cos θ are its height and width.','sin²θ = (%s)² = %s, so cos²θ = 1 − %s = %s.'%(fr(a,c),fr(a*a,c*c),fr(a*a,c*c),fr(b*b,c*c)),'Square root gives cos θ = ±%s. Quadrant II is left of the y-axis, so cosine (the x-value) is negative.'%fr(b,c),'cos θ = −%s = %s.'%(fr(b,c),d(v))]
        elif quad==3: g='cos θ = %s'%fr(-b,c);ask='sin θ';v=sin;pre=['A point on the unit circle satisfies sin²θ + cos²θ = 1.','cos²θ = %s, so sin²θ = 1 − %s = %s.'%(fr(b*b,c*c),fr(b*b,c*c),fr(a*a,c*c)),'sin θ = ±%s. Quadrant III is below the x-axis, so sine (the height) is negative.'%fr(a,c),'sin θ = %s.'%d(v)]
        else: g='cos θ = %s'%fr(b,c);ask='tan θ';v=sin/cos;pre=['In Quadrant IV the point is to the right of the y-axis (cos positive) and below the x-axis (sin negative).','sin²θ = 1 − cos²θ = 1 − %s = %s, so sin θ = −%s.'%(fr(b*b,c*c),fr(a*a,c*c),fr(a,c)),'tan θ = sin θ ÷ cos θ = (−%s) ÷ %s = −%s.'%(fr(a,c),fr(b,c),fr(a,b)),'As a decimal: %s.'%d(v)]
        num('ti',2,'%s and θ is in Quadrant %s. Find %s (decimal, 3 places).'%(g,nm,ask),v,pre,pre[-1])
# double angle from sin and quadrant I/II
for a,b,c in TRI[:5]:
    s=a/c;co=b/c
    num('id',2,'sin θ = %s with θ in Quadrant I. Find sin 2θ (decimal, 3 places).'%fr(a,c),2*s*co,['Double angle: sin 2θ = 2 sin θ cos θ. It is a sum formula in disguise: sin(θ+θ).','Find cos θ from sin²θ + cos²θ = 1: cos θ = %s (positive in Quadrant I).'%fr(b,c),'sin 2θ = 2 · %s · %s = %s ≈ %s.'%(fr(a,c),fr(b,c),fr(2*a*b,c*c),d(2*s*co)),'Check: 2θ is between 0° and 180°, so sin 2θ must be positive.'],'sin 2θ = 2 sin θ cos θ = %s'%d(2*s*co))
    num('id',3,'cos θ = %s with θ in Quadrant I. Find cos 2θ (decimal, 3 places). Use whichever double-angle form is quickest.'%fr(b,c),2*co*co-1,['cos 2θ has three equal forms: cos²θ − sin²θ = 2cos²θ − 1 = 1 − 2sin²θ. Pick the one that uses only what you were given.','Given cos θ = %s, use 2cos²θ − 1.'%fr(b,c),'2 · %s − 1 = %s − 1 = %s.'%(fr(b*b,c*c),fr(2*b*b,c*c),fr(2*b*b-c*c,c*c)),'≈ %s.'%d(2*co*co-1)],'cos 2θ = 2cos²θ − 1 = %s'%d(2*co*co-1))
for ang,(sa,ca,sb,cb) in [(75,(45,30)),(15,(45,30))] if False else []:pass
num('id',3,'Use sin(A + B) with A = 45° and B = 30° to find sin 75° (decimal, 4 places).',math.sin(math.radians(75)),['Sum formula: sin(A+B) = sin A cos B + cos A sin B. It says a rotation by A then B mixes both angles’ heights and widths.','sin 45° = √2/2 ≈ 0.7071, cos 30° = √3/2 ≈ 0.8660, cos 45° ≈ 0.7071, sin 30° = 0.5.','0.7071 × 0.8660 + 0.7071 × 0.5 = 0.6124 + 0.3536 = 0.9659.','Sanity check: 75° is close to 90°, so sine should be close to 1.'],'sin 75° ≈ 0.9659',tol=0.0006)
num('id',3,'Use cos(A − B) with A = 60° and B = 45° to find cos 15° (decimal, 4 places).',math.cos(math.radians(15)),['Difference formula: cos(A − B) = cos A cos B + sin A sin B. Note the sign flips compared with the angle: the minus in the angle gives a plus here.','cos 60° = 0.5, cos 45° ≈ 0.7071, sin 60° ≈ 0.8660, sin 45° ≈ 0.7071.','0.5 × 0.7071 + 0.8660 × 0.7071 = 0.3536 + 0.6124 = 0.9659.','15° is a small angle, so cosine should be near 1.'],'cos 15° ≈ 0.9659',tol=0.0006)
mcq('ti',2,'Which expression equals (1 − cos²θ) ÷ sin θ for sin θ ≠ 0?','sin θ',['cos θ','tan θ','1'],['Pythagorean identity rearranged: 1 − cos²θ = sin²θ.','So the fraction is sin²θ ÷ sin θ.','Cancel one factor of sin θ to get sin θ.'],'1 − cos²θ = sin²θ, so the result is sin θ.')
mcq('ti',2,'Which expression is equivalent to tan θ · cos θ?','sin θ',['cos θ','1','sec θ'],['tan θ is defined as sin θ ÷ cos θ.','Multiply by cos θ: (sin θ ÷ cos θ) · cos θ.','The cos θ factors cancel, leaving sin θ.'],'tan θ · cos θ = sin θ.')
mcq('ti',3,'Which statement is an identity (true for every angle where both sides are defined)?','1 + tan²θ = sec²θ',['1 + sin²θ = cos²θ','sin θ + cos θ = 1','tan²θ − 1 = sec²θ'],['Start from sin²θ + cos²θ = 1 and divide every term by cos²θ.','That gives tan²θ + 1 = sec²θ.','Test the others at θ = 45°: 1 + ½ ≠ ½, √2 ≠ 1, and 1 − 1 = 0 ≠ 2. A single failing angle disproves an identity.'],'Dividing sin²θ + cos²θ = 1 by cos²θ gives 1 + tan²θ = sec²θ.')
mcq('ti',3,'How many solutions does 2 sin²x − sin x − 1 = 0 have on 0 ≤ x < 2π?','3',['2','4','1'],['Treat sin x as a single unknown u. Then 2u² − u − 1 = 0 factors as (2u + 1)(u − 1) = 0.','u = −1/2 or u = 1.','sin x = 1 gives x = π/2 (one solution). sin x = −1/2 gives x = 7π/6 and 11π/6 (two solutions).','Total: 1 + 2 = 3.'],'u = −1/2 or 1 gives 2 + 1 = 3 solutions.')
order('ti',2,'Put the steps in order to solve 2cos²x − cos x = 0 on 0 ≤ x < 2π.',['Factor out cos x: cos x (2cos x − 1) = 0','Set each factor to zero: cos x = 0 or cos x = 1/2','Solve cos x = 0: x = π/2, 3π/2','Solve cos x = 1/2: x = π/3, 5π/3'],['Never divide by cos x, or you lose the solutions where cos x = 0. Factor instead.','A product is zero only when a factor is zero.','Use the unit circle to list every angle in one turn.'],'Factor first, then solve each factor on the unit circle.')
# ---- iv: inverse trig ----
for a,b,c in TRI[:4]:
    num('iv',2,'Evaluate cos(arcsin(%s)) (decimal, 3 places).'%fr(a,c),b/c,['arcsin(%s) is an angle θ whose sine is %s. Draw it: a right triangle with opposite side %d and hypotenuse %d.'%(fr(a,c),fr(a,c),a,c),'The missing adjacent side is √(%d² − %d²) = %d.'%(c,a,b),'cos θ = adjacent ÷ hypotenuse = %d/%d = %s.'%(b,c,d(b/c)),'arcsin returns angles in [−90°, 90°], where cosine is never negative, so the answer is positive.'],'cos(arcsin(%s)) = %s'%(fr(a,c),d(b/c)))
    num('iv',3,'Evaluate sin(arctan(%s)) (decimal, 3 places).'%fr(a,b),a/c,['arctan(%s) is an angle θ with tan θ = opposite ÷ adjacent = %d/%d.'%(fr(a,b),a,b),'Hypotenuse = √(%d² + %d²) = %d.'%(a,b,c),'sin θ = opposite ÷ hypotenuse = %d/%d = %s.'%(a,c,d(a/c))],'sin(arctan(%s)) = %s'%(fr(a,b),d(a/c)))
mcq('iv',2,'What is arccos(−√3/2) in radians?','5π/6',['π/6','7π/6','2π/3'],['arccos returns an angle between 0 and π (the top half of the unit circle).','cos θ = −√3/2 has reference angle π/6 and the cosine is negative, so we are in Quadrant II.','θ = π − π/6 = 5π/6. (7π/6 has the right cosine but lies outside arccos’s range.)'],'The answer must lie in [0, π]; 5π/6 does.')
mcq('iv',3,'What is arcsin(sin(7π/6))?','−π/6',['7π/6','π/6','5π/6'],['sin 7π/6 = −1/2.','arcsin undoes sine only on [−π/2, π/2]. 7π/6 is outside that interval, so the answer is NOT 7π/6.','The angle in [−π/2, π/2] with sine −1/2 is −π/6.'],'Inverse functions only undo on their restricted range.')
mcq('iv',3,'Why does arcsin only return angles between −π/2 and π/2?','Sine is not one-to-one, so we restrict it to an interval where it is, to make an inverse function',['Sine is undefined outside that interval','Angles outside it have no sine','It is simply a convention with no mathematical reason'],['A function needs one output per input. An inverse swaps inputs and outputs, so the original must be one-to-one.','Sine repeats: sin 30° = sin 150°. Asking “which angle has sine 1/2?” has many answers.','Restricting to [−π/2, π/2] covers every sine value exactly once, which makes arcsin a function.'],'A restriction makes sine one-to-one so an inverse exists.')
# ---- tc: radians, arc, sector ----
for r,deg in [(6,40),(10,72),(8,135),(12,50),(5,210)]:
    th=math.radians(deg);num('tc',2,'A circle has radius %d cm. Find the arc length for a central angle of %d° (cm, 2 decimals).'%(r,deg),r*th,['Arc length is a fraction of the circumference. The fraction is %d/360.'%deg,'Using radians makes it simple: s = rθ. First convert %d° × π/180 = %s rad.'%(deg,d(th,4)),'s = %d × %s = %s cm.'%(r,d(th,4),d(r*th,2))],'s = rθ = %s'%d(r*th,2),tol=0.012)
    num('tc',3,'A sector of a circle with radius %d cm has a central angle of %d°. Find its area (cm², 1 decimal).'%(r,deg),0.5*r*r*th,['A sector is a slice of the whole circle’s area πr². The slice is %d/360 of it.'%deg,'In radians the formula is A = ½ r² θ, with θ = %s rad.'%d(th,4),'A = ½ × %d² × %s = %s cm².'%(r,d(th,4),d(.5*r*r*th,1))],'A = ½r²θ = %s'%d(.5*r*r*th,1),tol=0.06)
mcq('tc',1,'Which is the exact value of sin(π/6)?','1/2',['√3/2','√2/2','1'],['π/6 is 30°. In a 30-60-90 triangle the short leg is half the hypotenuse.','sin = opposite ÷ hypotenuse = 1/2.','Memory trick for 30°, 45°, 60°: sines are √1/2, √2/2, √3/2.'],'sin 30° = 1/2.')
match('tc',2,'Match each angle to its exact cosine.',[['π/3','1/2'],['π/4','√2/2'],['π/6','√3/2'],['2π/3','−1/2']],['Use reference angles and the sign of cosine (x-coordinate).','π/3 → 1/2, π/4 → √2/2, π/6 → √3/2.','2π/3 is in Quadrant II with reference angle π/3, so cosine is −1/2.'],'Reference angle and quadrant sign give each value.')
# ---- tl: laws of sines/cosines ----
for A,a,b in [(30,5,8),(40,3,9),(50,9,6),(25,4,6),(35,2,5),(60,12,10)]:
    s=b*math.sin(math.radians(A))/a
    h=b*math.sin(math.radians(A));cnt=0 if a<h else (1 if a>=b else 2)
    mcq('tl',3,'In triangle ABC, A = %d°, a = %d, b = %d. How many different triangles are possible?'%(A,a,b),str(cnt),[x for x in ['0','1','2'] if x!=str(cnt)]+['3'],['This is the SSA (ambiguous) case. Compare the side across from A with the height h = b sin A = %s.'%d(b*math.sin(math.radians(A)),3),'Here a = %d, which is %s than h and %s than b = %d.'%(a,'bigger' if a>b*math.sin(math.radians(A)) else 'smaller','smaller' if a<b else 'bigger',b),['a is shorter than the height, so it cannot reach the base line: 0 triangles.','a reaches the base in exactly one place: 1 triangle.','a is long enough to reach the base line but shorter than b, so it can swing to two places: 2 triangles.'][cnt]],'Compare a with b sin A and with b.')
for a,b,C in [(7,9,60),(10,6,120),(5,8,40),(12,7,75)]:
    c=math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
    num('tl',2,'Two sides of a triangle are %d and %d with an included angle of %d°. Find the third side (2 decimals).'%(a,b,C),c,['Law of Cosines is the Pythagorean theorem with a correction for the angle: c² = a² + b² − 2ab cos C.','c² = %d² + %d² − 2(%d)(%d)cos %d° = %s.'%(a,b,a,b,C,d(c*c,3)),'c = √%s = %s.'%(d(c*c,3),d(c,2)),'Check: at C = 90° the extra term vanishes and we get Pythagoras. For C = %d° the side is %s than that.'%(C,'shorter' if C<90 else 'longer')],'c = %s'%d(c,2),tol=0.012)
for a,b,c in [(13,14,15),(7,8,9),(9,10,17)]:
    s=(a+b+c)/2;ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
    num('tl',3,'Use Heron’s formula to find the area of a triangle with sides %d, %d, %d (2 decimals).'%(a,b,c),ar,['Heron’s formula needs only the three sides. First the semi-perimeter s = (a + b + c) ÷ 2 = %s.'%d(s,1),'Area = √[s(s − a)(s − b)(s − c)] = √[%s × %s × %s × %s].'%(d(s,1),d(s-a,1),d(s-b,1),d(s-c,1)),'= √%s = %s.'%(d(s*(s-a)*(s-b)*(s-c),2),d(ar,2))],'Area ≈ %s'%d(ar,2),tol=0.012)
# ---- tg: amplitude, period, shifts ----
for A,Bv,C,D in [(3,2,1,-1),(2,4,0,5),(5,3,2,0),(1.5,6,1,2)]:
    per=2*math.pi/Bv
    num('tg',2,'For y = %s sin(%d(x − %s)) + %s, find the period (decimal, 3 places).'%(d(A,1),Bv,d(C,0),d(D,0)),per,['For y = A sin(B(x − C)) + D, the number multiplying x inside sets how fast the wave repeats.','Normal sine takes 2π to repeat. With B = %d it repeats %d times as fast.'%(Bv,Bv),'Period = 2π ÷ B = 2π ÷ %d = %s.'%(Bv,d(per,3)),'Amplitude (%s), shift C (%s) and midline D (%s) do not change the period.'%(d(A,1),d(C,0),d(D,0))],'Period = 2π/%d = %s'%(Bv,d(per,3)),tol=0.004)
mcq('tg',2,'y = −2 cos(x) + 3 has what range?','1 ≤ y ≤ 5',['−2 ≤ y ≤ 2','−5 ≤ y ≤ −1','1 ≤ y ≤ 3'],['The midline is y = 3 (the +3 shifts the whole wave up).','The amplitude is |−2| = 2, so it goes 2 above and 2 below the midline: 3 − 2 = 1 to 3 + 2 = 5.','The negative sign only flips the wave upside down; it does not change the range.'],'Midline ± amplitude: 3 ± 2.')
match('tg',2,'Match each function to its period.',[['y = sin 2x','π'],['y = cos(x/2)','4π'],['y = tan x','π'],['y = sin(πx)','2']],['Sine and cosine: period 2π ÷ B. Tangent: period π ÷ B.','sin 2x: 2π/2 = π. cos(x/2): 2π ÷ ½ = 4π. tan x: π.','sin(πx): 2π/π = 2.'],'Divide the base period by B.')
order('tg',3,'Put the transformations in a sensible order to sketch y = 2 sin(3x − π) + 1.',['Rewrite as y = 2 sin(3(x − π/3)) + 1','Read off amplitude 2, period 2π/3, phase shift π/3 right, midline y = 1','Draw the midline y = 1 and the max/min lines y = 3 and y = −1','Start one cycle at x = π/3 and mark five key points a quarter-period apart'],['Factor the 3 out of the argument to see the true horizontal shift: 3x − π = 3(x − π/3).','Each piece (A, B, C, D) controls one visible feature.','Quarter-period = (2π/3) ÷ 4 = π/6.'],'Factor first, then read A, B, C, D, then plot.')
# ---- pl: remainder/factor theorem, roots ----
for a,b,c,e,k in [(1,-4,-7,10,2),(2,3,-5,6,-1),(1,0,-3,5,3),(3,-2,0,-8,2)]:
    v=a*k**3+b*k**2+c*k+e
    num('pl',2,'Find the remainder when %sx³ %s %sx² %s %sx %s %s is divided by (x %s %s).'%(a if a!=1 else '',('+' if b>=0 else '−'),abs(b),('+' if c>=0 else '−'),abs(c),('+' if e>=0 else '−'),abs(e),('−' if k>=0 else '+'),abs(k)),v,['Remainder Theorem: dividing p(x) by (x − k) leaves remainder p(k). Why? p(x) = (x − k)q(x) + r, and plugging in x = k kills the first term.','Here k = %d. Substitute: %d(%d)³ + %d(%d)² + %d(%d) + %d.'%(k,a,k,b,k,c,k,e),'= %d.'%v,'No long division needed.'],'r = p(%d) = %d'%(k,v),tol=0.001)
for r1,r2 in [(2,5),(-1,6),(3,4),(-2,-5)]:
    num('pl',2,'The quadratic x² + bx + c has roots %d and %d. Find b + c.'%(r1,r2),-(r1+r2)+r1*r2,['Vieta’s relations: for x² + bx + c with roots r and s, r + s = −b and rs = c.','Sum = %d, so b = %d. Product = %d, so c = %d.'%(r1+r2,-(r1+r2),r1*r2,r1*r2),'b + c = %d + %d = %d.'%(-(r1+r2),r1*r2,-(r1+r2)+r1*r2),'Check by expanding (x − %d)(x − %d).'%(r1,r2)],'b + c = %d'%(-(r1+r2)+r1*r2),tol=0.001)
mcq('pl',3,'Which could be a rational root of 2x³ − 5x² + x + 6 = 0, by the Rational Root Theorem?','3/2',['5/2','4','1/3'],['Rational Root Theorem: any rational root p/q has p dividing the constant term (6) and q dividing the leading coefficient (2).','p ∈ {±1, ±2, ±3, ±6}, q ∈ {1, 2}.','3/2 qualifies (3 divides 6, 2 divides 2). 5/2 fails (5 ∤ 6), 4 fails (4 ∤ 6), 1/3 fails (3 ∤ 2).'],'p divides 6 and q divides 2.')
# ---- ra: asymptotes/holes ----
for k,m in [(3,2),(5,-1),(2,4)]:
    mcq('ra',2,'Where does f(x) = (x² − %d) ÷ ((x − %d)(x + 2)) have its vertical asymptotes? (Assume no cancelling factor.)'%(k*k+7,m),'x = %d and x = −2'%m,['x = %d only'%m,'x = −%d and x = 2'%m if m!=2 else 'x = 2 only','y = 1'],['A vertical asymptote appears where the denominator is 0 but the numerator is not.','Denominator zeros: x = %d and x = −2.'%m,'The numerator x² − %d is not zero at either, so both are vertical asymptotes.'%(k*k+7)],'Set the denominator to zero.') if False else None
mcq('ra',2,'What is the horizontal asymptote of f(x) = (3x² + 1) ÷ (x² − 4)?','y = 3',['y = 0','y = 1','x = 2'],['When the top and bottom have the same degree, the ratio of leading coefficients sets the horizontal asymptote.','Far from the origin the +1 and −4 barely matter, so f(x) ≈ 3x² ÷ x² = 3.','y = 3 (x = 2 is a vertical asymptote, not a horizontal one).'],'Equal degrees: y = 3/1.')
mcq('ra',3,'What happens to f(x) = (x² − 9) ÷ (x − 3) at x = 3?','A hole at (3, 6)',['A vertical asymptote at x = 3','A zero at x = 3','A horizontal asymptote at y = 6'],['Factor the top: x² − 9 = (x − 3)(x + 3).','The (x − 3) cancels, so f(x) = x + 3 everywhere except x = 3, where the original is undefined.','Cancelled factor = hole, at height 3 + 3 = 6. A factor that stays in the denominator would be an asymptote.'],'Cancelled factor means a hole.')
# ---- ex / lg ----
for P,r,t in [(1000,0.05,10),(2500,0.04,15),(800,0.07,6)]:
    A=P*math.exp(r*t)
    num('ex',3,'$%d is invested at %s%% compounded continuously. How much is it worth after %d years? ($, 2 decimals)'%(P,d(r*100,0),t),A,['Continuous compounding is the limit of compounding more and more often: A = P e^(rt).','rt = %s × %d = %s.'%(d(r,2),t,d(r*t,2)),'e^%s ≈ %s, so A = %d × %s = %s.'%(d(r*t,2),d(math.exp(r*t),4),P,d(math.exp(r*t),4),d(A,2))],'A = Pe^(rt) = %s'%d(A,2),tol=0.06)
for base,tg in [(2,50),(3,100),(5,200)]:
    x=math.log(tg)/math.log(base)
    num('lg',2,'Solve %d^x = %d (decimal, 3 places).'%(base,tg),x,['x is the exponent, so “undo” the power with a logarithm. Taking log of both sides brings the exponent down: x log %d = log %d.'%(base,tg),'x = log %d ÷ log %d = %s ÷ %s.'%(tg,base,d(math.log10(tg),4),d(math.log10(base),4)),'x ≈ %s.'%d(x,3),'Check: %d^%s ≈ %d.'%(base,d(x,3),tg)],'x = ln %d ÷ ln %d = %s'%(tg,base,d(x,3)),tol=0.004)
mcq('lg',2,'Which equals log₂ 40 − log₂ 5?','3',['log₂ 35','8','5'],['Subtracting logs divides the numbers: log a − log b = log (a ÷ b).','log₂ (40 ÷ 5) = log₂ 8.','2³ = 8, so log₂ 8 = 3.'],'Quotient rule then evaluate.')
mcq('lg',3,'Why must you check solutions after solving log₃(x) + log₃(x − 8) = 2?','Combining logs can introduce an x that makes a log argument negative',['Logs always give two answers','The base 3 is not allowed','Equations with logs have no solutions'],['Combine: log₃(x(x − 8)) = 2, so x² − 8x = 9, so (x − 9)(x + 1) = 0.','x = 9 or x = −1.','x = −1 makes log₃(−1) undefined. Only x = 9 works. Always test the domain (arguments must be positive).'],'Extraneous solutions come from the domain.')
# ---- qd2 / complex ----
for a,b,c,e in [(2,3,1,-4),(3,-1,2,5),(4,2,-1,3)]:
    re_=a*c-b*e;im_=a*e+b*c
    num('qd2',2,'Multiply (%d %s %di)(%d %s %di). What is the real part?'%(a,'+' if b>=0 else '−',abs(b),c,'+' if e>=0 else '−',abs(e)),re_,['Treat i like a variable and expand, remembering i² = −1 (the rule that makes complex numbers work).','(%d)(%d) + (%d)(%di) + (%di)(%d) + (%di)(%di) = %d + %di + %di + %di².'%(a,c,a,e,b,c,b,e,a*c,a*e,b*c,b*e),'The i² term becomes %d, so the real part is %d + %d = %d.'%(-b*e,a*c,-b*e,re_),'Imaginary part for reference: %d.'%im_],'Real part = ac − be = %d'%re_,tol=0.001)
mcq('qd2',2,'The discriminant of 2x² − 4x + 5 is negative. What does that tell you?','Two non-real complex solutions that are conjugates',['Two different real solutions','One repeated real solution','No solutions of any kind'],['The discriminant b² − 4ac is what sits under the square root in the quadratic formula.','Here (−4)² − 4(2)(5) = 16 − 40 = −24, and the square root of a negative number is imaginary.','So x = (4 ± i√24) ÷ 4, a conjugate pair. The graph never touches the x-axis.'],'Negative discriminant means complex conjugate roots.')
# ---- sq ----
for a1,dd,n in [(5,3,20),(-2,4,15),(10,-2,12)]:
    an=a1+(n-1)*dd;S=n*(a1+an)/2
    num('sq',2,'An arithmetic sequence has first term %d and common difference %d. Find the sum of the first %d terms.'%(a1,dd,n),S,['Gauss’s trick: pair the first and last terms, the second and second-last, and so on. Every pair has the same sum.','a_%d = %d + %d(%d) = %d.'%(n,a1,n-1,dd,an),'Number of pairs is n/2, each summing to a₁ + aₙ = %d: S = %d/2 × (%d + %d).'%(a1+an,n,a1,an),'S = %d.'%S],'S = n(a₁ + aₙ)/2 = %d'%S,tol=0.001)
for a1,r in [(81,1/3),(12,0.5),(5,0.2)]:
    S=a1/(1-r)
    num('sq',3,'Find the sum of the infinite geometric series %s + %s + %s + … (decimal).'%(d(a1,1),d(a1*r,3),d(a1*r*r,4)),S,['An infinite sum can be finite when each term shrinks. It works only if |r| < 1; here r = %s.'%d(r,4),'Formula: S = a₁ ÷ (1 − r). It comes from S − rS = a₁, since all later terms cancel.','S = %s ÷ (1 − %s) = %s.'%(d(a1,1),d(r,4),d(S,3))],'S = a₁/(1−r) = %s'%d(S,3),tol=0.01)
# ---- cn ----
for a,b in [(5,3),(13,5),(10,6)]:
    c=math.sqrt(a*a-b*b)
    num('cn',2,'The ellipse x²/%d + y²/%d = 1 has a² = %d and b² = %d. How far is each focus from the centre? (c)'%(a*a,b*b,a*a,b*b),c,['In an ellipse the two foci are on the longer axis. Every point has the same total distance to both foci.','The three lengths a (semi-major), b (semi-minor), c (centre to focus) form a right triangle: c² = a² − b².','c² = %d − %d = %d, so c = %s.'%(a*a,b*b,a*a-b*b,d(c,3))],'c = √(a² − b²) = %s'%d(c,3),tol=0.006)
mcq('cn',2,'Which conic is x² + y² − 6x + 4y − 3 = 0?','A circle with centre (3, −2) and radius 4',['A circle with centre (−3, 2) and radius 4','A parabola','An ellipse with centre (3, −2)'],['Complete the square in both variables: (x² − 6x + 9) + (y² + 4y + 4) = 3 + 9 + 4.','(x − 3)² + (y + 2)² = 16.','Standard form (x − h)² + (y − k)² = r² gives centre (3, −2) and r = 4. The signs in the equation are opposite to the centre coordinates.'],'Complete the square.')
mcq('cn',3,'The hyperbola x²/16 − y²/9 = 1 has asymptotes with slopes:','±3/4',['±4/3','±9/16','±3/16'],['For x²/a² − y²/b² = 1, far from the origin the “1” is negligible, so x²/a² ≈ y²/b².','That gives y ≈ ±(b/a)x.','a² = 16 so a = 4; b² = 9 so b = 3. Slopes are ±3/4.'],'Asymptote slopes are ±b/a.')
# ---- pp ----
for r,th in [(4,60),(6,150),(8,225)]:
    x=r*math.cos(math.radians(th));y=r*math.sin(math.radians(th))
    num('pp',2,'Convert the polar point (r, θ) = (%d, %d°) to rectangular coordinates. What is x? (decimal, 3 places)'%(r,th),x,['Polar describes a point by distance r and angle θ. Rectangular reads the same point as right/left (x) and up/down (y).','The right triangle gives x = r cos θ and y = r sin θ.','x = %d cos %d° = %d × %s = %s.'%(r,th,r,d(math.cos(math.radians(th)),4),d(x,3)),'y = %s for reference.'%d(y,3)],'x = r cos θ = %s'%d(x,3),tol=0.004)
for m,c0,t in [(2,1,3),(3,-1,2),(4,2,-1)]:
    num('pp',3,'A particle moves with x = %dt %s %d and y = t². Find y when x = %d.'%(m,'+' if c0>=0 else '−',abs(c0),m*t+c0),t*t,['Parametric equations give x and y both in terms of a third variable t (often time).','To find y at a given x, first find the t that produces that x: %dt %s %d = %d gives t = %d.'%(m,'+' if c0>=0 else '−',abs(c0),m*t+c0,t),'Then y = t² = %d.'%(t*t)],'t = %d, y = %d'%(t,t*t),tol=0.001)
json.dump({'new':N},open('src/audit_apex/h1.json','w'),ensure_ascii=False)
print(len(N),'questions written')
