# -*- coding: utf-8 -*-
from wid_h import *
W={}
W['fn']={
'Input and output':calc('A function is a machine: put a number in, one number comes out.',[P('x','Input x',-5,10,1,3)],[O('Output','2*x+1',25,'',0)],eq='Rule: output = 2 × input + 1',note='Put in <b>{x}</b>, the machine gives <b>{=2*x+1|0}</b>. The same input always gives the same output.',pre=('If the rule is "double it, then add 1", what comes out when 3 goes in?',['6','7','8'],1,'2 × 3 = 6, then 6 + 1 = 7.'),take='A function gives exactly one output for each input.'),
'Function notation':calc('f(x) is just a name for the output.',[P('x','x',-4,6,1,2)],[O('f(x)','x^2-3',30,'',0)],eq='f(x) = x² − 3',note='f({x}) means: replace every x with <b>{x}</b>. So f({x}) = {x}² − 3 = <b>{=x^2-3|0}</b>.',take='f(2) is read "f of 2". It does not mean f times 2.'),
'Tables, graphs and the vertical line test':plot('A graph is a picture of every input-output pair. Slide a and watch the picture.',['a*x'],[P('a','Slope a',-3,3,.5,1)],x=(-5,5),y=(-6,6),out='Each x has one y: y = {a}·x. Every vertical line crosses this graph once.',take='Vertical line test: if any vertical line hits a graph twice, it is not a function.'),
'Domain and range':plot('Domain = inputs allowed. Range = outputs you get. Slide c to shift the square-root curve.',['sqrt(x-c)'],[P('c','Start c',-3,4,1,1)],x=(-4,10),y=(-1,6),out='sqrt(x − {c}) only works when x ≥ <b>{c}</b>. The outputs are 0 and up.',pre=('Can you take the square root of −4 and get a real number?',['Yes','No'],1,'No real number times itself is negative, so inputs below the start are not allowed.'),take='Domain: allowed x-values. Range: possible y-values.'),
'Composing functions':calc('Feed one machine into another: f(g(x)).',[P('x','x',-3,6,1,2)],[O('g(x) = x + 2','x+2',10,'',0),O('f(g(x)) = 3·g(x)','3*(x+2)',30,'',0)],eq='g first (add 2), then f (multiply by 3)',note='{x} → g → <b>{=x+2|0}</b> → f → <b>{=3*(x+2)|0}</b>',take='Work from the inside out: do g first, then f.'),
'Inverse functions':plot('An inverse undoes the function. Its graph is the mirror image across the line y = x.',['x','a*x+1','(x-1)/a'],[P('a','Multiplier a',1,4,1,2)],x=(-4,6),y=(-4,6),out='f(x) = {a}x + 1 and its inverse (x − 1)/{a} are mirror images across the diagonal.',take='f⁻¹ swaps inputs and outputs. It is not 1/f.'),
'Transformations':plot('Move and stretch the parabola y = a(x − h)² + k.',['a*(x-h)^2+k','x^2'],[P('h','Right/left h',-4,4,1,2),P('k','Up/down k',-4,4,1,1),P('a','Stretch a',-2,3,.5,1)],x=(-6,6),y=(-5,8),out='Vertex at (<b>{h}</b>, <b>{k}</b>). Gold = original y = x².',pre=('Which way does y = (x − 2)² move y = x²?',['Left 2','Right 2','Up 2'],1,'The graph shifts the opposite way from the sign inside the bracket: right 2.'),take='(x − h) moves right by h. + k moves up by k. a stretches or flips.'),
'Even and odd functions':plot('Even functions are mirror images across the y-axis. Odd ones spin 180° about the origin.',['x^n'],[P('n','Power n',1,6,1,2)],x=(-3,3),y=(-6,6),out='x^{n}: n is <b>{n}</b>. Even n gives a mirror graph. Odd n gives a spin.',take='Even: f(−x) = f(x). Odd: f(−x) = −f(x).'),
}
W['qd2']={
'Squares and square roots':calc('A square root asks: what number times itself gives this?',[P('s','Side length',1,12,1,5)],[O('Area = s²','s^2',150,'',0)],eq='s × s = area',note='A square with side <b>{s}</b> has area <b>{=s^2|0}</b>. Going backwards: √{=s^2|0} = {s}.',take='Square root undoes squaring.'),
'Solving by factoring':plot('The roots are where the curve crosses the x-axis. y = (x − p)(x − q).',['(x-p)*(x-q)'],[P('p','Root p',-5,5,1,-2),P('q','Root q',-5,5,1,3)],x=(-7,7),y=(-8,12),out='Crosses the axis at x = <b>{p}</b> and x = <b>{q}</b>.',take='Zero-product rule: if (x − p)(x − q) = 0, then x = p or x = q.'),
'Vertex form':plot('Vertex form shows the turning point right away.',['a*(x-h)^2+k'],[P('a','a',-3,3,.5,1),P('h','h',-4,4,1,1),P('k','k',-5,5,1,-2)],x=(-6,6),y=(-8,8),out='The vertex is (<b>{h}</b>, <b>{k}</b>). Positive a opens up, negative a opens down.',pts=[dict(x='h',y='k',l='vertex')]),
'The quadratic formula':plot('Change a, b, c and see where the parabola meets the x-axis.',['a*x^2+b*x+c'],[P('a','a',-3,3,.5,1),P('b','b',-6,6,1,0),P('c','c',-8,8,1,-4)],x=(-6,6),y=(-10,10),out='b² − 4ac = <b>{=b^2-4*a*c}</b>. Roots: x = (−b ± √(b² − 4ac)) / 2a.'),
'The discriminant':plot('The discriminant b² − 4ac tells how many times the curve touches the x-axis.',['x^2+b*x+c'],[P('b','b',-6,6,1,0),P('c','c',-8,8,1,1)],x=(-6,6),y=(-8,10),out='Discriminant = <b>{=b^2-4*c}</b>. Positive: 2 crossings. Zero: touches once. Negative: none.',pre=('If a parabola floats above the x-axis, how many real roots does it have?',['0','1','2'],0,'It never touches the axis, so no real roots.')),
}
W['pl']={
'Powers and terms':calc('A polynomial is a sum of terms like a·xⁿ.',[P('x','x',-3,4,1,2)],[O('x³','x^3',70,'',0),O('x²','x^2',16,'',0),O('x','x',4,'',0)],eq='Bigger powers grow much faster',note='At x = {x}: x = {x}, x² = {=x^2|0}, x³ = {=x^3|0}.'),
'Evaluating and the remainder theorem':plot('Dividing by (x − a) leaves the remainder p(a).',['x^3-2*x^2-x+2'],[P('a','Test value a',-3,4,1,2)],x=(-3,4),y=(-8,10),out='p({a}) = <b>{=a^3-2*a^2-a+2|0}</b>. That is the remainder when you divide by (x − {a}).',pts=[dict(x='a',y='a^3-2*a^2-a+2',l='p(a)')]),
'The factor theorem':plot('If p(a) = 0, then (x − a) is a factor. Slide a until the point lands on the axis.',['x^3-2*x^2-x+2'],[P('a','Test value a',-3,4,1,0)],x=(-3,4),y=(-8,10),out='p({a}) = <b>{=a^3-2*a^2-a+2|0}</b>. Zero means (x − {a}) divides it exactly.',pts=[dict(x='a',y='a^3-2*a^2-a+2',l='p(a)')]),
'End behavior':plot('Far left and far right, only the highest power matters.',['a*x^n'],[P('a','Leading coefficient',-2,2,1,1),P('n','Degree n',1,5,1,3)],x=(-3,3),y=(-10,10),out='Degree <b>{n}</b>, coefficient <b>{a}</b>.',take='Even degree: both ends go the same way. Odd degree: ends go opposite ways.'),
}
W['ra']={
'Fractions are division':calc('A fraction is a division. Watch what happens as the bottom gets small.',[P('d','Bottom number',1,20,1,10)],[O('1 ÷ bottom','1/d',1,'',3)],note='1 ÷ <b>{d}</b> = <b>{=1/d|3}</b>. A smaller bottom makes a bigger answer.'),
'Vertical asymptotes and holes':plot('Dividing by something near 0 blows up. Slide a to move the asymptote.',['1/(x-a)'],[P('a','Zero of the bottom a',-3,3,1,1)],x=(-5,5),y=(-6,6),out='The bottom is zero at x = <b>{a}</b>, so the graph shoots off there.',vl=[dict(x='a')],take='A vertical asymptote sits where the denominator is 0 and the numerator is not.'),
'Horizontal asymptotes':plot('Far from zero, y = (x + 1)/(x − 1) settles near 1.',['(x+1)/(x-1)','1'],[],x=(-10,10),y=(-4,6),out='As x gets huge, y gets close to <b>1</b>.'),
'Direct and inverse variation':plot('Direct: y = kx grows together. Inverse: y = k/x trades off.',['k*x','k/x'],[P('k','k',1,5,1,2)],x=(0.2,6),y=(0,10),out='Blue: y = {k}x. Gold: y = {k}/x.'),
}
W['ex']={
'Doubling and tripling':calc('Doubling over and over becomes huge very fast.',[P('n','Number of doublings',0,12,1,5)],[O('Amount','2^n',4096,'',0)],eq='Start at 1 and double n times',note='After <b>{n}</b> doublings you have <b>{=2^n|0}</b>.',pre=('A coin doubles in value 10 times starting at 1 cent. About how much?',['10 cents','$1','About $10'],2,'2¹⁰ = 1024 cents ≈ $10.24. Doubling is fast.')),
'Exponential functions':plot('y = a·bˣ. Change the growth factor b.',['a*b^x'],[P('a','Start a',1,4,1,1),P('b','Growth factor b',0.3,2.5,.1,2)],x=(-3,5),y=(0,20),out='b = <b>{b}</b>. Above 1 the curve grows; below 1 it shrinks.',take='b > 1 is growth. 0 < b < 1 is decay.'),
'Percent growth and decay':calc('A 5% rise multiplies by 1.05 each time.',[P('r','Percent per year',-20,30,1,5),P('t','Years',0,30,1,10)],[O('Value of 100','100*(1+r/100)^t',500,'',1)],eq='value = start × (1 + r/100)ᵗ',note='100 grows to <b>{=100*(1+r/100)^t|1}</b> after {t} years at {r}%.'),
'Half-life':plot('After each half-life, half is left.',['100*0.5^(x/h)'],[P('h','Half-life',1,10,1,4)],x=(0,30),y=(0,100),out='Half-life = <b>{h}</b>. After {h} steps there is 50%; after {=2*h|0}, 25%.',xl='time',yl='% left'),
}
W['lg']={
'What a logarithm asks':calc('A log asks: what power do I need?',[P('b','Base',2,10,1,2),P('n','Power',0,8,1,3)],[O('bⁿ','b^n',1000,'',0)],eq='log_b(answer) = n',note='{b}^{n} = <b>{=b^n|0}</b>, so log base {b} of {=b^n|0} is <b>{n}</b>.',pre=('What power of 2 gives 8?',['2','3','4'],1,'2 × 2 × 2 = 8, so the power is 3.')),
'Product and quotient rules':calc('Logs turn multiplying into adding.',[P('a','log of A',0,5,1,2),P('b','log of B',0,5,1,3)],[O('log(A×B)','a+b',10,'',0)],note='If A = 10^{a} and B = 10^{b}, then A×B = 10^{=a+b|0}. Multiply → add the exponents.'),
}
W['sq']={
'Patterns and sequences':calc('A sequence is a list that follows a rule.',[P('n','Which term',1,12,1,5)],[O('Term n','3*n+2',40,'',0)],eq='Rule: 3n + 2',note='Term <b>{n}</b> is <b>{=3*n+2|0}</b>.'),
'Arithmetic sequences':calc('Each term adds the same amount d.',[P('a','Start',0,10,1,2),P('d','Add d',-3,6,1,3),P('n','Term n',1,12,1,6)],[O('Term n','a+(n-1)*d',70,'',0)],eq='aₙ = a + (n − 1)d',note='Term {n} = {a} + ({n} − 1)×{d} = <b>{=a+(n-1)*d|0}</b>.'),
'Geometric sequences':calc('Each term multiplies by the same ratio r.',[P('a','Start',1,5,1,2),P('r','Ratio r',1,4,1,2),P('n','Term n',1,8,1,5)],[O('Term n','a*r^(n-1)',600,'',0)],eq='aₙ = a·rⁿ⁻¹',note='Term {n} = {a} × {r}^({n}−1) = <b>{=a*r^(n-1)|0}</b>.'),
}
W['tc']={
'Sine, cosine and tangent':simple('tri','Slide the angle and the size. Watch the ratios.',take='sin = opp/hyp, cos = adj/hyp, tan = opp/adj. The ratios depend only on the angle.'),
'Radians':calc('A radian is an angle measured by arc length.',[P('d','Degrees',0,360,15,90)],[O('Radians','d*pi/180',6.3,'',3)],eq='radians = degrees × π/180',note='<b>{d}°</b> = <b>{=d*pi/180|3}</b> radians. A half turn (180°) is π ≈ 3.14.'),
'The unit circle':simple('circle','Drag the angle around the circle. Read sin and cos from the point.',pre=('At 90°, the point is straight up. What is cos 90°?',['0','1','−1'],0,'The point is (0, 1): x = cos = 0, y = sin = 1.'),take='On the unit circle, the point is (cos θ, sin θ).'),
'Special angles':simple('circle','Set the angle to 30°, 45°, 60°. Notice the values.',a0=45,take='sin 30° = 1/2, sin 45° = √2/2 ≈ 0.707, sin 60° = √3/2 ≈ 0.866.'),
'Reference angles and signs':simple('circle','Move through the four quadrants. When are sin and cos negative?',a0=150,pre=('In quadrant II (90°–180°), which is negative?',['sin','cos','both'],1,'x is negative there, so cos is negative while sin stays positive.')),
}
W['tg']={
'The sine graph':plot('Trace the unit circle height as the angle grows.',['sind(x)'],[],x=(0,360),y=(-1.5,1.5),out='One full wave every 360°.',xl='degrees',yl='sin'),
'Amplitude':plot('Amplitude is how tall the wave is from the middle.',['A*sind(x)'],[P('A','Amplitude A',0.5,4,.5,1)],x=(0,360),y=(-4,4),out='Amplitude = <b>{A}</b>: the wave goes up to {A} and down to −{A}.',xl='degrees'),
'Period':plot('Period is how long one full wave takes.',['sind(b*x)'],[P('b','Speed b',1,4,1,1)],x=(0,360),y=(-1.5,1.5),out='Period = 360 ÷ {b} = <b>{=360/b|0}°</b>.',xl='degrees',take='Period = 360° ÷ b (or 2π ÷ b in radians).'),
'Phase shift':plot('Phase shift slides the wave left or right.',['sind(x-c)','sind(x)'],[P('c','Shift right c',-90,180,15,45,'°')],x=(0,360),y=(-1.5,1.5),out='Blue is shifted right by <b>{c}°</b>. Gold is the original.',xl='degrees'),
'Vertical shift (midline)':plot('Vertical shift moves the middle line up or down.',['2*sind(x)+k'],[P('k','Midline k',-2,3,1,1)],x=(0,360),y=(-5,5),out='Middle line at y = <b>{k}</b>.',xl='degrees'),
'Cosine and tangent graphs':plot('Cosine is sine shifted. Tangent has asymptotes.',['cosd(x)','sind(x)'],[],x=(0,360),y=(-1.5,1.5),out='Cosine (blue) is sine (gold) shifted 90° left.',xl='degrees'),
'Modeling with sinusoids':plot('A Ferris wheel height is a wave: height = r·sin + middle.',['8+7*sind(360*x/T)'],[P('T','Minutes per turn',2,10,1,6)],x=(0,20),y=(0,16),out='One turn every <b>{T}</b> minutes. Height swings from 1 m to 15 m.',xl='minutes',yl='height'),
}
W['ti']={'Same value, different look':calc('Two different-looking expressions can always agree. Test it.',[P('a','Angle',0,360,10,40,'°')],[O('sin² + cos²','sind(a)^2+cosd(a)^2',1.2,'',3)],note='sin²({a}°) + cos²({a}°) = <b>{=sind(a)^2+cosd(a)^2|3}</b> for every angle.'),
'The Pythagorean identity':simple('circle','The point sits on a circle of radius 1, so x² + y² = 1.',a0=40,take='cos²θ + sin²θ = 1.')}
W['id']={'Double angles':calc('sin 2θ and 2 sin θ cos θ are the same.',[P('a','θ',0,90,5,30,'°')],[O('sin 2θ','sind(2*a)',1,'',3),O('2 sinθ cosθ','2*sind(a)*cosd(a)',1,'',3)],note='Both equal <b>{=sind(2*a)|3}</b>.'),
'Sum and difference':calc('Check sin(A + B) = sinA cosB + cosA sinB.',[P('a','A',0,90,5,30,'°'),P('b','B',0,90,5,45,'°')],[O('sin(A+B)','sind(a+b)',1,'',3),O('Right side','sind(a)*cosd(b)+cosd(a)*sind(b)',1,'',3)],note='Left and right match: <b>{=sind(a+b)|3}</b>.')}
W['iv']={'Trig takes an angle, inverse takes a ratio':calc('Inverse sine turns a ratio back into an angle.',[P('r','Ratio (opp ÷ hyp)',0,1,.05,.5)],[O('sin⁻¹(ratio) in °','asind(r)',90,'°',1)],note='sin⁻¹({r}) = <b>{=asind(r)|1}°</b>.',pre=('sin 30° = 0.5. So what is sin⁻¹(0.5)?',['30°','60°','0.5°'],0,'The inverse gives the angle back: 30°.'))}
W['tl']={'Law of Sines':calc('In every triangle, side ÷ sin(opposite angle) is the same.',[P('A','Angle A',20,100,5,40,'°'),P('B','Angle B',20,100,5,60,'°'),P('a','Side a',3,12,1,6)],[O('Side b','a*sind(B)/sind(A)',20,'',2)],eq='a / sin A = b / sin B',note='b = {a} × sin({B}°) ÷ sin({A}°) = <b>{=a*sind(B)/sind(A)|2}</b>.')}
W['cn']={'Circles':plot('A circle is every point at the same distance r from the center.',['sqrt(r^2-x^2)','-sqrt(r^2-x^2)'],[P('r','Radius r',1,5,1,3)],x=(-6,6),y=(-6,6),out='x² + y² = <b>{=r^2|0}</b>.'),
'Parabolas':plot('A parabola opens toward its focus.',['x^2/(4*p)'],[P('p','Focus distance p',.5,3,.5,1)],x=(-6,6),y=(-1,8),out='y = x²/(4·{p}). The focus is {p} above the vertex.')}
W['pp']={'Two ways to name a point':calc('(r, θ): how far and which direction.',[P('r','Distance r',0,6,1,4),P('t','Angle θ',0,360,15,60,'°')],[O('x = r cos θ','r*cosd(t)',6,'',2),O('y = r sin θ','r*sind(t)',6,'',2)],note='Polar (<b>{r}</b>, <b>{t}°</b>) = rectangular (<b>{=r*cosd(t)|2}</b>, <b>{=r*sind(t)|2}</b>).')}
W['lm']={'Getting closer and closer':plot('A limit asks what y does as x creeps toward a number.',['(x^2-1)/(x-1)'],[],x=(-1,3),y=(0,4),out='As x gets near 1, y gets near <b>2</b>, even though x = 1 is not allowed.',pts=[dict(x='1',y='2',l='hole')]),}
W['dv']={'Slope of a curve':plot('The derivative is the slope of the tangent line.',['x^2','2*a*x-a^2'],[P('a','Point a',-3,3,.5,1)],x=(-4,4),y=(-3,10),out='At x = <b>{a}</b>, the slope of x² is <b>{=2*a|1}</b>.',pts=[dict(x='a',y='a^2')]),
'Power rule':calc('Power rule: the derivative of xⁿ is n·xⁿ⁻¹.',[P('n','Power n',1,6,1,3),P('x','x',-2,3,1,2)],[O('Slope at x','n*x^(n-1)',100,'',1)],note='d/dx x^{n} = {n}x^({n}−1). At x = {x} that is <b>{=n*x^(n-1)|1}</b>.')}
W['da']={'Critical points':plot('The curve flattens at maximum and minimum points.',['x^3-3*x'],[P('a','Point a',-2.5,2.5,.5,0)],x=(-3,3),y=(-5,5),out='Slope at x = {a}: <b>{=3*a^2-3|1}</b>. It is 0 at x = ±1.',pts=[dict(x='a',y='a^3-3*a')])}
W['in']={'Riemann sums':calc('Add thin rectangles to find the area under y = x².',[P('n','Rectangles',1,50,1,5)],[O('Estimate (0 to 3)','sum_',9,'',2)],note='')}
del W['in']
WID=W
