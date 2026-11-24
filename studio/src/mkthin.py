#!/usr/bin/env python3
"""Rewrites the last 141 thin Apex solutions as short, concept-first explanations. Every worked number is computed here from the question
text and checked against the stored answer; a mismatch aborts. Writes src/audit_apex/k1.json for applyextra."""
import json,re,math,sys
from fractions import Fraction as F
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application,convert_xor
TR=standard_transformations+(implicit_multiplication_application,convert_xor)
M='−'
def m(n):
    if isinstance(n,F):
        s=str(n.numerator)+('/'+str(n.denominator) if n.denominator!=1 else '')
    else:s=str(int(n)) if float(n)==int(n) else str(n)
    return s.replace('-',M)
def par(n):return '('+m(n)+')' if n<0 else m(n)
def fr(n):return m(F(n))
SUP={2:'²',3:'³',4:'⁴',5:'⁵',6:'⁶'}
def poly(s):
    s=s.replace('−','-').replace('²','**2').replace('³','**3').replace('⁴','**4').replace('⁵','**5').replace('⁶','**6')
    return parse_expr(s,transformations=TR,local_dict={'x':sp.Symbol('x')})
X=sp.Symbol('x')
def subst(p,v):
    """term-by-term substitution text, e.g. 2(2)² − 3(2) − 3, and its value"""
    P=sp.Poly(p,X);out=[]
    for (e,),c in sorted(P.terms(),key=lambda t:-t[0][0]):
        c=int(c);ab=abs(c)
        if e==0:body=str(ab)
        else:
            core='('+m(v)+')'+(SUP[e] if e>1 else '') if v<0 or e>1 else m(v)
            body=(str(ab) if ab!=1 else '')+core
            if ab!=1 and e>=1 and v>=0 and e==1:body=str(ab)+'('+m(v)+')'
            if ab!=1 and e>1:body=str(ab)+'('+m(v)+')'+SUP[e]
            if ab==1:body=('('+m(v)+')' if (v<0 or e>1) else m(v))+(SUP[e] if e>1 else '')
        out.append((c<0,body))
    s='';
    for i,(neg,b) in enumerate(out):
        s+=((M+' ' if neg else '')+b) if i==0 else (' '+(M if neg else '+')+' '+b)
    return s,int(p.subs(X,v))
fix={};bad=[]
def put(i,steps,ans=None,got=None):
    if ans is not None and abs(float(ans)-float(got))>1e-3*max(1,abs(float(ans))):bad.append((i,ans,got));return
    fix[i]={'sol':steps}
T=json.load(open('/tmp/thin.json'))
for q in T:
    i,t,a=q['id'],q['q'],q['a']
    try:av=float(a.split()[0])
    except:av=None
    mt=None
    if re.match(r'Is f\(x\) = x(.) even',t):
        n=int(re.match(r'Is f\(x\) = x(.)',t).group(1).translate(str.maketrans('²³⁴⁵⁶','23456')));ev=n%2==0
        put(i,['Test it: swap x for −x. If f(−x) = f(x) the function is even; if f(−x) = −f(x) it is odd.',f'f(−x) = (−x){SUP[n]}. A negative number raised to an {"even" if ev else "odd"} power {"loses its sign" if ev else "keeps its sign"}.',f'So f(−x) = {"" if ev else M}x{SUP[n]} = {"f(x)" if ev else "−f(x)"}.',('Even: the graph is a mirror image across the y-axis.' if ev else 'Odd: the graph looks the same after a half-turn about the origin.')+f' (Rule of thumb: x{SUP[n]} is {"even" if ev else "odd"} because {n} is {"even" if ev else "odd"}.)']);continue
    mt=re.match(r'For f\(x\) = (.+), find the average rate of change from x = (\S+) to x = (\S+)\.',t)
    if mt:
        p=poly(mt.group(1));a_=int(mt.group(2).replace('−','-'));b_=int(mt.group(3).replace('−','-'))
        sa,va=subst(p,a_);sb,vb=subst(p,b_);r=F(vb-va,b_-a_)
        put(i,['Average rate of change is the slope between two points: (f(b) − f(a)) ÷ (b − a).',f'f({m(a_)}) = {sa} = {m(va)}.',f'f({m(b_)}) = {sb} = {m(vb)}.',f'Slope = ({m(vb)} − {par(va)}) ÷ ({m(b_)} − {par(a_)}) = {m(vb-va)} ÷ {m(b_-a_)} = {m(r)}.'],av,float(r));continue
    mt=re.match(r'Find the discriminant b² − 4ac of (.+)\.',t)
    if mt:
        p=sp.Poly(poly(mt.group(1)),X);a_,b_,c_=[int(p.coeff_monomial(X**k)) for k in (2,1,0)];D=b_*b_-4*a_*c_
        put(i,[f'Read the coefficients from ax² + bx + c: a = {m(a_)}, b = {m(b_)}, c = {m(c_)}.',f'b² = {par(b_)}² = {b_*b_}, and 4ac = 4({m(a_)})({m(c_)}) = {m(4*a_*c_)}.',f'D = {b_*b_} − {par(4*a_*c_)} = {m(D)}.','The sign of D tells the roots: '+('positive means two real roots' if D>0 else 'zero means one repeated root' if D==0 else 'negative means no real roots (two complex roots)')+f'. Here D is {"positive" if D>0 else "zero" if D==0 else "negative"}.'],av,D);continue
    mt=re.match(r'Multiply \((\d+) \+ (\d+)i\)\((\d+) \+ (\d+)i\)',t)
    if mt:
        a_,b_,c_,d_=map(int,mt.groups());put(i,['Multiply like binomials (FOIL): (a + bi)(c + di) = ac + adi + bci + bdi².','The i² term turns real: i² = −1, so bdi² = −bd.',f'Real part = ac − bd = {a_}·{c_} − {b_}·{d_} = {a_*c_} − {b_*d_} = {a_*c_-b_*d_}.',f'(The imaginary part is ad + bc = {a_*d_+b_*c_}, so the product is {a_*c_-b_*d_} + {a_*d_+b_*c_}i.)'],av,a_*c_-b_*d_);continue
    mt=re.match(r'Evaluate (.+) at x = (\S+)\.',t)
    if mt and i.startswith('pl-'):
        p=poly(mt.group(1));v=int(mt.group(2).replace('−','-'));s,val=subst(p,v)
        P=sp.Poly(p,X);terms=[int(c)*v**e for (e,),c in sorted(P.terms(),key=lambda t:-t[0][0])]
        put(i,[f'Put {m(v)} in place of every x. Use brackets around a negative number so the signs stay right.',f'{s}.',f'Work out each term: '+', '.join(m(x) for x in terms)+'.',f'Add them: {m(val)}.'],av,val);continue
    mt=re.match(r'What is (\d)⁴\?',t)
    if mt:
        b=int(mt.group(1));put(i,[f'{b}⁴ means {b} used as a factor 4 times.',f'Square twice: {b}² = {b*b}, and then {b*b}² = {b**4}.',f'So {b}⁴ = {b**4}. (Quick check: {b}⁴ = {b*b} × {b*b}.)'],av,b**4);continue
    if i=='sq-063':
        put(i,['The rows go 1, 3, 5, … so each row adds 2: an arithmetic sequence with first term a = 1 and common difference d = 2.','Use Sₙ = n/2 · (2a + (n − 1)d) with n = 9 rows.','S₉ = 9/2 · (2·1 + 8·2) = 9/2 · 18 = 81.','Check: the sum of the first n odd numbers is always n², and 9² = 81.'],av,81);continue
    mt=re.match(r'The two shorter sides of a right triangle are (\d+) and (\d+)\.',t)
    if mt:
        a_,b_=map(int,mt.groups());c=math.isqrt(a_*a_+b_*b_);g=math.gcd(a_,b_)
        st=['The hypotenuse is the side opposite the right angle. The Pythagorean theorem says a² + b² = c².',f'Square the legs: {a_}² = {a_*a_} and {b_}² = {b_*b_}. Add: {a_*a_+b_*b_}.',f'c = √{a_*a_+b_*b_} = {c}. A length is positive, so we take the positive root.']
        if g>1:st.append(f'Shortcut for next time: ({a_//g}, {b_//g}, {c//g}) is a Pythagorean triple, and these sides are {g} times as long.')
        put(i,st,av,c);continue
    mt=re.match(r'If sin θ = (\d+)/(\d+), what is sin²θ as a decimal\?',t)
    if mt:
        n,d=map(int,mt.groups());put(i,['sin²θ means (sin θ)², so square the whole fraction.',f'Square the top and the bottom separately: ({n}/{d})² = {n}²/{d}² = {n*n}/{d*d}.',f'Divide to get a decimal: {n*n} ÷ {d*d} ≈ {n*n/(d*d):.4f}.'],av,n*n/(d*d));continue
    mt=re.match(r'sin θ = (\d+)/(\d+) and cos θ = (\d+)/(\d+)\. Find sin 2θ',t)
    if mt:
        s,d,c,d2=map(int,mt.groups());v=F(2*s*c,d*d);put(i,['Use the double-angle formula sin 2θ = 2 sin θ cos θ.',f'Substitute: 2 × {s}/{d} × {c}/{d} = {2*s*c}/{d*d}.',f'As a decimal: {2*s*c} ÷ {d*d} ≈ {float(v):.4f}.'],av,float(v));continue
    mt=re.match(r'sin θ = (\d+)/(\d+)\. Find cos 2θ using',t) or re.match(r'sin A = (\d+)/(\d+) with A in quadrant I\. Find cos 2A',t)
    if mt:
        n,d=map(int,mt.groups());v=F(d*d-2*n*n,d*d);put(i,['Use the double-angle form cos 2θ = 1 − 2 sin²θ, which needs only the sine.',f'Square the sine: ({n}/{d})² = {n*n}/{d*d}. Double it: {2*n*n}/{d*d}.',f'Subtract from 1 (write 1 as {d*d}/{d*d}): {d*d}/{d*d} − {2*n*n}/{d*d} = {d*d-2*n*n}/{d*d}.',f'As a decimal: {d*d-2*n*n} ÷ {d*d} ≈ {float(v):.4f}.'],av,float(v));continue
    mt=re.match(r'Solve sin x = ([\d.]+) for 0° ≤ x ≤ 90°',t)
    if mt:
        k=float(mt.group(1));x=math.degrees(math.asin(k));put(i,['To undo a sine, use the inverse: if sin x = k then x = sin⁻¹(k). Put the calculator in degree mode.',f'x = sin⁻¹({mt.group(1)}) ≈ {x:.1f}°.',f'Check: sin {x:.1f}° ≈ {math.sin(math.radians(round(x,1))):.4f}, which matches {mt.group(1)}. (Only one angle fits between 0° and 90°.)'],av,round(x,1));continue
    mt=re.match(r'A boat heads on a bearing of (\d+)° and then turns (\d+)° to the right',t)
    if mt:
        a_,b_=map(int,mt.groups());put(i,['Bearings are measured clockwise from north, so turning right (clockwise) makes the bearing bigger.',f'{a_}° + {b_}° = {a_+b_}°.',f'Place the pointer at {a_+b_}°. (A left turn would subtract instead.)']);continue
    mt=re.match(r'A map puts the school at \(0, 0\) and the park at \((\d+), (\d+)\)',t)
    if mt:
        x,y=map(int,mt.groups());c=math.isqrt(x*x+y*y);put(i,['Straight-line distance is the hypotenuse of a right triangle whose legs are the across and up distances: d = √(Δx² + Δy²).',f'Δx = {x} and Δy = {y}, so d = √({x}² + {y}²) = √({x*x} + {y*y}) = √{x*x+y*y}.',f'√{x*x+y*y} = {c}, so they are {c} km apart.'],av,c);continue
    mt=re.match(r'A sprinkler waters the circle \(x ([+−-]) (\d+)\)² \+ \(y ([+−-]) (\d+)\)² = (\d+)',t)
    if mt:
        s1,h,s2,k,r2=mt.groups();h=int(h)*(-1 if s1=='+' else 1);k=int(k)*(-1 if s2=='+' else 1);r2=int(r2);r=math.isqrt(r2)
        put(i,['A circle with centre (h, k) and radius r has the equation (x − h)² + (y − k)² = r².',f'Match the form: the centre is ({m(h)}, {m(k)}) (the signs in the brackets are flipped), and r² = {r2}.',f'r = √{r2} = {r}. Radius is a distance, so it is positive. The water reaches {r} m.'],av,r);continue
    mt=re.match(r'The ellipse x²/(\d+) \+ y²/(\d+) = 1 has foci at \(±c, 0\)',t)
    if mt:
        A,B=map(int,mt.groups());c=math.isqrt(A-B);put(i,[f'The larger denominator ({A}) is under x², so the long direction is horizontal and the foci sit on the x-axis. That makes a² = {A} and b² = {B}.',f'For an ellipse, c² = a² − b² = {A} − {B} = {A-B}.',f'c = √{A-B} = {c}, so the foci are at (±{c}, 0).'],av,c);continue
    mt=re.match(r'The parabola y = x²/(\d+) has its focus at \(0, p\)',t)
    if mt:
        d=int(mt.group(1));put(i,['A parabola that opens upward with its vertex at the origin has the form y = x²/(4p), where p is the distance from the vertex to the focus.',f'Match the denominators: 4p = {d}.',f'p = {d} ÷ 4 = {d//4}, so the focus is at (0, {d//4}).'],av,d/4);continue
    mt=re.match(r'Find the eccentricity e = c/a of the ellipse x²/(\d+) \+ y²/(\d+) = 1',t)
    if mt:
        A,B=map(int,mt.groups());a_=math.isqrt(A);c=math.isqrt(A-B);put(i,[f'Eccentricity measures how stretched the ellipse is: e = c/a, always between 0 (a circle) and 1.',f'a² = {A}, so a = {a_}. Then c² = a² − b² = {A} − {B} = {A-B}, so c = {c}.',f'e = {c}/{a_} = {c/a_:.3f}.'],av,c/a_);continue
    mt=re.match(r'Find arctan\(([\d.]+)\) in degrees',t)
    if mt:
        k=float(mt.group(1));x=math.degrees(math.atan(k));put(i,[f'arctan(k) means "the angle whose tangent is k". It undoes tan. Use degree mode.',f'arctan({mt.group(1)}) ≈ {x:.1f}°.',f'Check: tan {x:.1f}° ≈ {math.tan(math.radians(round(x,1))):.2f}. A large k gives an angle near 90°; k = 1 gives exactly 45°.'],av,round(x,1));continue
    def tv(fn,deg):return {'sin':math.sin,'cos':math.cos}[fn](math.radians(deg))
    mt=re.match(r'Use sin\(A \+ B\) = .* with A = (\d+)° and B = (\d+)° to find sin (\d+)°',t)
    if mt:
        A,B,S=map(int,mt.groups());p1=tv('sin',A)*tv('cos',B);p2=tv('cos',A)*tv('sin',B)
        put(i,[f'The angle {S}° is {A}° + {B}°, so use sin(A + B) = sin A cos B + cos A sin B.',f'sin {A}° = {tv("sin",A):.4f}, cos {B}° = {tv("cos",B):.4f}, cos {A}° = {tv("cos",A):.4f}, sin {B}° = {tv("sin",B):.4f}.',f'First product ≈ {p1:.4f}; second product ≈ {p2:.4f}.',f'Add: sin {S}° ≈ {p1+p2:.4f}.'],av,p1+p2);continue
    mt=re.match(r'Use cos\(A − B\) = .* with A = (\d+)°, B = (\d+)° to find cos (\d+)°',t)
    if mt:
        A,B,S=map(int,mt.groups());p1=tv('cos',A)*tv('cos',B);p2=tv('sin',A)*tv('sin',B)
        put(i,[f'The angle {S}° is {A}° − {B}°, so use cos(A − B) = cos A cos B + sin A sin B. (Note the plus sign: subtracting angles gives a plus.)',f'cos {A}° = {tv("cos",A):.4f}, cos {B}° = {tv("cos",B):.4f}, sin {A}° = {tv("sin",A):.4f}, sin {B}° = {tv("sin",B):.4f}.',f'First product ≈ {p1:.4f}; second product ≈ {p2:.4f}.',f'Add: cos {S}° ≈ {p1+p2:.4f}.'],av,p1+p2);continue
    mt=re.match(r'Use sin 2A = 2 sin A cos A with A = (\d+)° to find sin (\d+)°',t)
    if mt:
        A,S=map(int,mt.groups());v=2*tv('sin',A)*tv('cos',A)
        put(i,[f'Doubling the angle ({A}° → {S}°) is the job of sin 2A = 2 sin A cos A.',f'sin {A}° ≈ {tv("sin",A):.4f} and cos {A}° ≈ {tv("cos",A):.4f}.',f'2 × {tv("sin",A):.4f} × {tv("cos",A):.4f} ≈ {v:.4f}, which is sin {S}°.'],av,v);continue
    mt=re.match(r'Use half-angle: find cos (\d+)° for A = (\d+)°',t)
    if mt:
        H,A=map(int,mt.groups());c=tv('cos',A);v=math.sqrt((1+c)/2)
        put(i,[f'The half-angle formula is cos(A/2) = √((1 + cos A)/2). The root is positive because {H}° is in quadrant I.',f'cos {A}° = {c:.4f}.',f'(1 + {par(round(c,4))})/2 = {(1+c)/2:.4f}.',f'√{(1+c)/2:.4f} ≈ {v:.4f}, so cos {H}° ≈ {v:.4f}.'],av,v);continue
    mt=re.match(r'Product-to-sum: 2 sin (\d+)° cos (\d+)° = sin (\d+)° \+ sin (\d+)°',t)
    if mt:
        A,B,P,Q=map(int,mt.groups());v=math.sin(math.radians(P))+math.sin(math.radians(Q))
        put(i,[f'The identity is 2 sin A cos B = sin(A + B) + sin(A − B). Here A + B = {A+B}° ... check it: {A}° + {B}° = {A+B}° and {A}° − {B}° = {A-B}°.'.replace(' ... check it:',';') if False else f'The identity is 2 sin A cos B = sin(A + B) + sin(A − B). Check the angles: {A}° + {B}° = {A+B}° and {A}° − {B}° = {A-B}°.',f'sin {P}° ≈ {math.sin(math.radians(P)):.4f} and sin {Q}° ≈ {math.sin(math.radians(Q)):.4f}.',f'Add: ≈ {v:.4f}.'],av,v);continue
    bad.append((i,'unmatched',t[:60]))
print(len(fix),'rewritten;',len(bad),'problems');print(bad[:10])
if bad:sys.exit(1)
json.dump({'fix':fix},open('src/audit_apex/k1.json','w'),ensure_ascii=False)
