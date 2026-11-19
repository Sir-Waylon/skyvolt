#!/usr/bin/env python3
"""Honors batch 2: harder (level 2-3) Algebra 2 / Trig items with computed answers. Output src/audit_apex/h2.json."""
import json,math,random
R=random.Random(20261118);N=[];DB={1:-1.2,2:0.3,3:1.2}
def d(x,n=3):return ('%.*f'%(n,x)).rstrip('0').rstrip('.')
def num(t,l,q,v,sol,w,tol=0.006):N.append(dict(t=t,l=l,b=DB[l],type='short',q=q,num={'v':float(v),'tol':tol,'free':True},sol=sol,w=w))
def mcq(t,l,q,right,wrong,sol,w):
    o=[right]+wrong;assert len(set(o))==len(o)>=3,(q,o);N.append(dict(t=t,l=l,b=DB[l],type='mcq',q=q,o=o,sol=sol,w=w))
def multi(t,l,q,good,bad,sol,w):
    o=good+bad;N.append(dict(t=t,l=l,b=DB[l],type='multi',q=q,o=o,a=list(range(len(good))),sol=sol,w=w))
def order(t,l,q,items,sol,w):N.append(dict(t=t,l=l,b=DB[l],type='order',q=q,items=items,sol=sol,w=w))
def match(t,l,q,pairs,sol,w):N.append(dict(t=t,l=l,b=DB[l],type='match',q=q,pairs=pairs,sol=sol,w=w))
# ---- fn: transformations, composition, inverse ----
for a,b in [(2,3),(3,-1),(-2,5),(4,1)]:
    f=lambda x:a*x+b;g=lambda x:x*x-1
    for x0 in [2,-1]:
        num('fn',2,'f(x) = %dx %s %d and g(x) = x² − 1. Find f(g(%d)).'%(a,'+' if b>=0 else '−',abs(b),x0),f(g(x0)),['Composition f(g(x)) means “do g first, then feed the result into f”. Work from the inside out.','g(%d) = %d² − 1 = %d.'%(x0,x0,g(x0)),'f(%d) = %d(%d) %s %d = %d.'%(g(x0),a,g(x0),'+' if b>=0 else '−',abs(b),f(g(x0)))],'f(g(%d)) = %d'%(x0,f(g(x0))),tol=0.001)
for a,b in [(2,3),(5,-4),(3,7)]:
    num('fn',3,'The inverse of f(x) = (x − %d) ÷ %d is f⁻¹(x) = %dx + %d. What is f⁻¹(%d)?'%(b,a,a,b,2),a*2+b,['An inverse undoes the function. f subtracts %d then divides by %d, so f⁻¹ multiplies by %d then adds %d (reverse order, opposite operations).'%(b,a,a,b),'f⁻¹(2) = %d(2) + %d = %d.'%(a,b,2*a+b),'Check: f(%d) = (%d − %d) ÷ %d = 2.'%(2*a+b,2*a+b,b,a)],'f⁻¹(2) = %d'%(2*a+b),tol=0.001)
mcq('fn',2,'The graph of y = f(x − 3) + 2 is the graph of y = f(x) moved:','3 right and 2 up',['3 left and 2 up','3 right and 2 down','3 left and 2 down'],['Inside the brackets, x − 3 means the input is delayed: the graph needs a larger x to give the same output, so it moves right 3.','Outside, + 2 simply lifts every output by 2.','So: right 3, up 2.'],'x − 3 inside shifts right; + 2 outside shifts up.')
mcq('fn',3,'Which transformation of f(x) is a reflection across the y-axis?','f(−x)',['−f(x)','f(x) + 1','f(2x)'],['Reflecting across the y-axis swaps left and right: the point (a, b) goes to (−a, b).','That means the input sign flips: y = f(−x).','−f(x) flips the outputs instead (a reflection across the x-axis).'],'Negate the input for a y-axis reflection.')
mcq('fn',3,'Is f(x) = x³ − x even, odd, or neither?','Odd',['Even','Neither','Both'],['Test f(−x): (−x)³ − (−x) = −x³ + x.','That equals −(x³ − x) = −f(x), the definition of an odd function.','Its graph has rotational symmetry about the origin.'],'f(−x) = −f(x) means odd.')
multi('fn',3,'Select ALL functions that are one-to-one (have an inverse function) on all real numbers.',['f(x) = 3x − 7','f(x) = x³','f(x) = 2ˣ'],['f(x) = x²','f(x) = |x|'],['A one-to-one function passes the horizontal line test: no output is repeated.','Lines with nonzero slope, x³ and 2ˣ always rise, so they pass.','x² and |x| give the same output for x and −x, so they fail on all real numbers.'],'Strictly increasing functions are one-to-one.')
# ---- qd2: vertex form, complex numbers ----
for a,h,k in [(2,3,-5),(-1,4,7),(3,-2,1),(1,5,-9)]:
    num('qd2',2,'The parabola y = %s(x %s %d)² %s %d has its vertex at (h, k). Find h + k.'%(('' if a==1 else ('−' if a==-1 else str(a))),'−' if h>=0 else '+',abs(h),'+' if k>=0 else '−',abs(k)),h+k,['Vertex form y = a(x − h)² + k shows the turning point directly: (h, k).','h is the number that makes the bracket zero. Here x %s %d = 0 gives h = %d.'%('−' if h>=0 else '+',abs(h),h),'k is the added constant, %d. h + k = %d.'%(k,h+k)],'h + k = %d'%(h+k),tol=0.001)
for a,b in [(3,4),(5,12),(8,15),(6,8)]:
    c=math.hypot(a,b);num('qd2',2,'Find the modulus |%d + %di| (decimal if needed).'%(a,b),c,['A complex number a + bi is a point (a, b) on a plane. Its modulus is its distance from the origin.','Pythagoras: √(%d² + %d²) = √%d.'%(a,b,a*a+b*b),'= %s.'%d(c,3)],'|z| = √(a² + b²) = %s'%d(c,3),tol=0.006)
mcq('qd2',3,'What is (2 + 3i)(2 − 3i)?','13',['4 − 9i²… = −5','4 + 9i','−5'][0:0] or '13',['−5','4 + 9i','4 − 9i'],['A number times its conjugate is a difference of squares: (a + bi)(a − bi) = a² − (bi)².','(bi)² = b²i² = −b², so the product is a² + b².','4 + 9 = 13. A conjugate product is always real, which is why we use it to clear i from a denominator.'],'(a+bi)(a−bi) = a² + b² = 13.') if False else None
mcq('qd2',3,'What is (2 + 3i)(2 − 3i)?','13',['−5','4 + 9i','4 − 9i'],['A number times its conjugate is a difference of squares: (a + bi)(a − bi) = a² − (bi)².','(bi)² = b²i² = −b², so the product is a² + b².','4 + 9 = 13. A conjugate product is always real, which is why we use it to clear i from a denominator.'],'(a+bi)(a−bi) = a² + b² = 13.')
mcq('qd2',3,'If x² + 6x + 13 = 0, what are the solutions?','x = −3 ± 2i',['x = 3 ± 2i','x = −3 ± 4i','x = −6 ± 2i'],['Quadratic formula: x = (−6 ± √(36 − 52)) ÷ 2 = (−6 ± √−16) ÷ 2.','√−16 = 4i, so x = (−6 ± 4i) ÷ 2 = −3 ± 2i.','Alternative: complete the square: (x + 3)² = −4, so x + 3 = ±2i.'],'x = −3 ± 2i')
# ---- pl ----
for a,b in [(2,3),(1,5),(3,-2)]:
    num('pl',3,'When p(x) = x³ + %dx² − %dx + 6 is divided by (x + 1), what is the remainder?'%(a,b+4) if False else 'When p(x) = x³ + %dx² − 7x + 6 is divided by (x + 1), what is the remainder?'%a,(-1)+a+7+6,['Remainder Theorem with x + 1 = x − (−1), so k = −1.','p(−1) = (−1)³ + %d(−1)² − 7(−1) + 6 = −1 + %d + 7 + 6.'%(a,a),'= %d.'%(a+12)],'p(−1) = %d'%(a+12),tol=0.001)
mcq('pl',3,'A polynomial of degree 5 with real coefficients has 3 real roots (counted with multiplicity). How many non-real roots does it have?','2',['0','1','3'],['The Fundamental Theorem of Algebra: a degree-5 polynomial has exactly 5 roots counting multiplicity, real and complex.','5 − 3 = 2 non-real roots.','Non-real roots of real polynomials come in conjugate pairs, so 2 is consistent (1 or 3 would not be).'],'5 − 3 = 2, in a conjugate pair.')
mcq('pl',3,'What is the end behaviour of f(x) = −2x⁴ + x³ − 5?','Falls to the left and falls to the right',['Rises to the left and rises to the right','Falls to the left and rises to the right','Rises to the left and falls to the right'],['For large |x| the highest-degree term dominates: −2x⁴.','Even degree: both ends point the same way. Negative leading coefficient: they point down.','So the graph falls on both sides.'],'Even degree, negative leading coefficient.')
multi('pl',3,'Select ALL that are factors of x³ − 6x² + 11x − 6.',['x − 1','x − 2','x − 3'],['x + 1','x − 6'],['Test candidates with the Factor Theorem: (x − k) is a factor when p(k) = 0.','p(1) = 1 − 6 + 11 − 6 = 0, p(2) = 8 − 24 + 22 − 6 = 0, p(3) = 27 − 54 + 33 − 6 = 0.','p(−1) = −24 and p(6) = 60, so those are not factors. The polynomial is (x − 1)(x − 2)(x − 3).'],'Roots 1, 2, 3.')
# ---- ra ----
for k in [3,4,5]:
    num('ra',3,'Solve 1/x + 1/(x + %d) = 1/%d for the positive solution (decimal, 3 places).'%(k,k) if False else 'Solve 6/x = x − 1 for the positive solution.',3,['Multiply both sides by x to clear the fraction: 6 = x² − x.','Rearrange: x² − x − 6 = 0, which factors as (x − 3)(x + 2) = 0.','x = 3 or x = −2. The positive solution is 3.','Check: 6/3 = 2 and 3 − 1 = 2.'],'x = 3',tol=0.001)
    break
mcq('ra',3,'After solving (x + 2)/(x − 3) = 5/(x − 3) + 1, why must you check your answer in the original equation?','x = 3 would make a denominator zero, so it may be extraneous',['Rational equations always have two answers','You must check that it is positive','The equation has no solution'],['Multiply by (x − 3): x + 2 = 5 + (x − 3), so x + 2 = x + 2.','That is true for every x, so the only possible failures are values excluded from the original: x = 3.','The solution is all real numbers except 3. Always list the excluded values first.'],'Excluded values come from the denominators.')
mcq('ra',2,'What is the domain of f(x) = (x + 1)/(x² − 4)?','All real numbers except x = 2 and x = −2',['All real numbers except x = −1','All real numbers except x = 4','All real numbers'],['A fraction is undefined when its denominator is zero.','x² − 4 = (x − 2)(x + 2) = 0 at x = 2 and x = −2.','The numerator being zero (x = −1) is fine: that just makes the value 0.'],'Exclude zeros of the denominator.')
# ---- ex / lg ----
for h,t in [(5730,11460),(8,24),(30,75)]:
    n=t/h;num('ex',2,'A sample has a half-life of %d years. What fraction remains after %d years? (decimal, 4 places)'%(h,t),0.5**n,['Half-life is the time for half the sample to decay, so each half-life multiplies the amount by ½.','Number of half-lives = %d ÷ %d = %s.'%(t,h,d(n,3)),'Fraction = (½)^%s = %s.'%(d(n,3),d(0.5**n,4))],'(½)^n = %s'%d(0.5**n,4),tol=0.004)
for b,x in [(2,32),(3,81),(5,125),(10,1000)]:
    pass
mcq('lg',3,'Which expression equals log₅ 12 using the change-of-base formula?','ln 12 ÷ ln 5',['ln 5 ÷ ln 12','ln 12 − ln 5','ln 12 × ln 5'],['Change of base: log_b(x) = ln x ÷ ln b. It lets a calculator with only ln or log compute any base.','The new base cancels: log₅ 12 = (ln 12) ÷ (ln 5).','Check by raising: 5^(ln12/ln5) = e^(ln 12) = 12.'],'log_b x = ln x ÷ ln b.')
num('lg',3,'Solve log₂(x + 3) + log₂(x − 3) = 4 for x.',5,['Combine: log₂((x + 3)(x − 3)) = 4, so x² − 9 = 2⁴ = 16.','x² = 25, so x = 5 or x = −5.','Domain: x − 3 > 0 means x > 3, so x = −5 is extraneous. Answer 5.','Check: log₂8 + log₂2 = 3 + 1 = 4.'],'x = 5',tol=0.001)
mcq('ex',3,'A population grows 8% each year. Which function gives P after t years from 500?','P = 500(1.08)ᵗ',['P = 500 + 0.08t','P = 500(0.08)ᵗ','P = 500(8)ᵗ'],['Each year multiplies by 1 + 0.08 = 1.08 (keep 100% and add 8%).','After t years you have multiplied t times: 500 × 1.08 × 1.08 × …','Linear growth would add a fixed amount; exponential growth multiplies.'],'Growth factor 1.08.')
# ---- sq ----
for a1,r,n in [(3,2,8),(5,3,6),(2,-2,7)]:
    S=a1*(r**n-1)/(r-1);num('sq',3,'Find the sum of the first %d terms of the geometric sequence starting %d, %d, %d, …'%(n,a1,a1*r,a1*r*r),S,['A geometric sum has a neat trick: S − rS leaves only the first and last terms.','S = a₁(rⁿ − 1) ÷ (r − 1) with a₁ = %d, r = %d, n = %d.'%(a1,r,n),'= %d(%d − 1) ÷ %d = %d.'%(a1,r**n,r-1,S)],'S = %d'%S,tol=0.001)
mcq('sq',2,'A sequence is defined by a₁ = 4, aₙ = 3aₙ₋₁ − 2. What is a₃?','28',['10','14','22'],['A recursive rule builds each term from the previous one.','a₂ = 3(4) − 2 = 10.','a₃ = 3(10) − 2 = 28.'],'a₂ = 10, a₃ = 28.')
num('sq',3,'Evaluate the sum of (3k − 2) for k = 1 to 20.',3*210-40,['Split the sum: Σ(3k − 2) = 3Σk − 2Σ1.','Σk from 1 to 20 = 20·21/2 = 210, and Σ1 = 20.','3(210) − 2(20) = 630 − 40 = 590.'],'Sum = 590',tol=0.001)
# ---- tc / tg ----
mcq('tc',2,'What is the exact value of tan(5π/4)?','1',['−1','√2/2','0'],['5π/4 is 225°, in Quadrant III, with reference angle π/4.','sin and cos are both −√2/2, so their ratio is positive.','tan = sin ÷ cos = 1.'],'The two negatives cancel.')
mcq('tc',3,'Which angle is coterminal with −π/3?','5π/3',['2π/3','4π/3','π/3'],['Coterminal angles differ by a full turn (2π).','−π/3 + 2π = 5π/3.','They end at the same point on the unit circle.'],'Add 2π.')
for deg in [120,210,300]:
    rad=math.radians(deg);num('tc',2,'Convert %d° to radians (decimal, 3 places).'%deg,rad,['A full turn is 360° = 2π radians, so 180° = π radians.','Multiply degrees by π/180: %d × π/180.'%deg,'= %s radians.'%d(rad,3)],'%d° = %s rad'%(deg,d(rad,3)),tol=0.004)
mcq('tg',3,'Which equation has amplitude 3, period π and midline y = −1?','y = 3 sin(2x) − 1',['y = 3 sin(x/2) − 1','y = 2 sin(3x) − 1','y = 3 sin(2x) + 1'],['Amplitude is the number in front: 3.','Period = 2π ÷ B = π means B = 2.','Midline is the constant added: −1. So y = 3 sin 2x − 1.'],'A = 3, B = 2, D = −1.')
multi('tg',3,'Select ALL statements true for y = cos x.',['It is an even function','Its period is 2π','Its maximum value is 1'],['It passes through the origin','Its period is π'],['cos(−x) = cos x, so it is even and symmetric about the y-axis.','One full cycle is 2π and the output stays between −1 and 1.','cos 0 = 1, so the graph starts at the top, not at the origin.'],'Even, period 2π, max 1.')
# ---- ti / id ----
order('ti',3,'Put these steps in order to prove (1 − cos²x)/sin x = sin x.',['Start with the left side: (1 − cos²x) ÷ sin x','Use sin²x + cos²x = 1 to replace 1 − cos²x with sin²x','Simplify sin²x ÷ sin x to sin x','Conclude the left side equals the right side'],['Prove identities by transforming one side only, until it matches the other.','The Pythagorean identity rearranged gives 1 − cos²x = sin²x.','Cancelling one factor of sin x finishes the proof (for sin x ≠ 0).'],'Work on one side only.')
num('id',3,'Use the half-angle formula to find sin 15° (decimal, 4 places).',math.sin(math.radians(15)),['Half-angle: sin(θ/2) = √[(1 − cos θ) ÷ 2] for θ in the right quadrant. Here 15° = 30° ÷ 2.','cos 30° = √3/2 ≈ 0.8660.','sin 15° = √[(1 − 0.8660) ÷ 2] = √0.0670 ≈ 0.2588.'],'sin 15° ≈ 0.2588',tol=0.004)
for t in [60,120]:
    num('id',2,'Find sin 2θ for θ = %d° (decimal, 3 places).'%t,math.sin(math.radians(2*t)),['Double the angle first: 2θ = %d°.'%(2*t),'sin %d° = %s.'%(2*t,d(math.sin(math.radians(2*t)),3)),'Or use sin 2θ = 2 sin θ cos θ = 2(%s)(%s).'%(d(math.sin(math.radians(t)),3),d(math.cos(math.radians(t)),3))],'sin 2θ = %s'%d(math.sin(math.radians(2*t)),3),tol=0.004)
mcq('id',3,'Which equals cos²x − sin²x?','cos 2x',['sin 2x','1','2 cos x'],['This is one of the double-angle forms of cosine.','cos 2x = cos²x − sin²x = 2cos²x − 1 = 1 − 2sin²x.','It comes from cos(x + x) = cos x cos x − sin x sin x.'],'cos 2x = cos²x − sin²x.')
# ---- iv ----
mcq('iv',2,'What is arctan(1) in degrees?','45°',['30°','60°','90°'],['arctan asks which angle has tangent 1.','tan 45° = opposite ÷ adjacent = 1 (equal legs).','arctan returns angles between −90° and 90°, so 45° is the answer.'],'tan 45° = 1.')
mcq('iv',3,'What is the range of y = arccos x?','0 ≤ y ≤ π',['−π/2 ≤ y ≤ π/2','0 ≤ y ≤ 2π','−π ≤ y ≤ π'],['Cosine is not one-to-one over a full turn, so its inverse uses a restricted piece.','The piece 0 to π covers every cosine value from 1 down to −1 exactly once.','arcsin uses −π/2 to π/2 for the same reason applied to sine.'],'Arccos outputs live in [0, π].')
for x in [0.6,0.8,-0.5]:
    num('iv',2,'Evaluate arcsin(%s) in degrees (decimal, 1 place).'%d(x,1),math.degrees(math.asin(x)),['arcsin gives the angle between −90° and 90° whose sine is the input.','Calculator in degree mode: sin⁻¹(%s).'%d(x,1),'= %s°.'%d(math.degrees(math.asin(x)),1),'Check: sin %s° = %s.'%(d(math.degrees(math.asin(x)),1),d(x,1))],'arcsin(%s) ≈ %s°'%(d(x,1),d(math.degrees(math.asin(x)),1)),tol=0.06)
# ---- tl ----
for A,B,a in [(40,65,8),(35,80,12),(50,60,10)]:
    b=a*math.sin(math.radians(B))/math.sin(math.radians(A));num('tl',2,'In triangle ABC, A = %d°, B = %d° and side a = %d. Find side b (2 decimals).'%(A,B,a),b,['Law of Sines: each side divided by the sine of its opposite angle is the same: a ÷ sin A = b ÷ sin B.','b = a sin B ÷ sin A = %d × sin %d° ÷ sin %d°.'%(a,B,A),'= %s.'%d(b,2)],'b = %s'%d(b,2),tol=0.012)
mcq('tl',3,'Which law do you use first when given two sides and the angle between them (SAS)?','Law of Cosines',['Law of Sines','Pythagorean theorem','Law of Tangents is required'],['Law of Sines needs a side and its opposite angle as a known pair. SAS has no such pair yet.','Law of Cosines uses exactly two sides and the included angle to find the third side.','After that, the Law of Sines is easy for the remaining angles.'],'SAS starts with Law of Cosines.')
# ---- cn ----
for h,k,r in [(2,-3,5),(-4,1,3),(0,6,7)]:
    num('cn',2,'A circle has equation (x %s %d)² + (y %s %d)² = %d. What is its radius?'%('−' if h>=0 else '+',abs(h),'−' if k>=0 else '+',abs(k),r*r),r,['Standard form: (x − h)² + (y − k)² = r². The right-hand side is r squared, not r.','Take the square root of %d.'%(r*r),'r = %d.'%r],'r = %d'%r,tol=0.001)
mcq('cn',3,'A parabola has focus (0, 3) and directrix y = −3. What is its equation?','x² = 12y',['y² = 12x','x² = 6y','x² = 3y'],['Every point on a parabola is equally far from the focus and the directrix.','The vertex is halfway between them: (0, 0), with p = 3 (distance vertex to focus).','Opening up with p = 3: x² = 4py = 12y.'],'x² = 4py with p = 3.')
mcq('cn',3,'Which conic has the equation 9x² + 4y² = 36?','An ellipse',['A hyperbola','A parabola','A circle'],['Divide by 36: x²/4 + y²/9 = 1.','Both squared terms are positive with different denominators, so it is an ellipse.','If the denominators were equal it would be a circle; with a minus sign it would be a hyperbola.'],'Positive terms, different denominators: ellipse.')
# ---- pp ----
for x,y in [(3,4),(5,12),(-6,8)]:
    r=math.hypot(x,y);num('pp',2,'Convert the rectangular point (%d, %d) to polar form. What is r?'%(x,y),r,['Polar r is the straight-line distance from the origin: r = √(x² + y²).','r = √(%d² + %d²) = √%d.'%(x,y,x*x+y*y),'r = %s.'%d(r,3)],'r = %s'%d(r,3),tol=0.006)
mcq('pp',3,'Which parametric equations trace the unit circle once as t goes from 0 to 2π?','x = cos t, y = sin t',['x = t, y = t²','x = cos 2t, y = sin t','x = 2 cos t, y = 2 sin t'],['A point on the unit circle satisfies x² + y² = 1.','cos²t + sin²t = 1, so (cos t, sin t) is always on the circle and sweeps once as t covers 2π.','2 cos t and 2 sin t gives a circle of radius 2; cos 2t with sin t is not a circle.'],'Pythagorean identity.')
json.dump({'new':N},open('src/audit_apex/h2.json','w'),ensure_ascii=False)
print(len(N),'questions written')
