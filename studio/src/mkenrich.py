#!/usr/bin/env python3
"""Adds a concept-first lead-in step to thin (very short) Apex solutions, chosen by the shape of the question.
Writes src/audit_apex/e1.json ({'fix': {id: {'sol': [...]}}}) for applyextra. Only questions whose solution is under 50 characters
and that match a rule are touched; nothing is invented about the specific numbers."""
import json,re
RULES=[
(r'plane at distance|angle of .* from the tower|polar','Idea: a polar point is a distance r and an angle θ. To get across/up distances, build a right triangle: x = r cos θ (across) and y = r sin θ (up).'),
(r'number machine','Idea: a machine applies its operations in the order given. Do each operation to the input, one at a time, in that order.'),
(r'one-to-one function with f','Idea: f and f⁻¹ undo each other. If f(a) = b, then f⁻¹(b) = a, so read the answer straight off the given fact.'),
(r'The roots of x³','Idea: Vieta’s formulas tie roots to coefficients. For x³ + bx² + cx + d, b = −(sum of roots), c = sum of pairwise products, d = −(product of roots).'),
(r'varies inversely','Idea: “varies inversely” means x · y stays constant. Use one known pair to find that constant, then use it for the new value.'),
(r'f\(x\) = \d+·\d+ˣ|view count after','Idea: in a · bˣ, a is the starting amount and b is the factor applied each step. Substitute the step count for x.'),
(r'grows by \d+% in one year, then by','Idea: a percent increase multiplies by (1 + rate). Two increases in a row multiply their factors, not add their percents.'),
(r'Solve \d+\^\(x','Idea: to solve an exponent equation, write both sides with the same base, then the exponents must match.'),
(r'half-life','Idea: half-life is the time for the amount to halve. Count how many half-lives fit in the time given; the amount is start × (½) to that power.'),
(r'What power of \d+ equals|Solve log base \d+ of x|How many times must you multiply','Idea: log_b(x) = y asks “what power of b gives x?”, which is the same statement as b^y = x. Rewrite in power form.'),
(r'Evaluate log base \d+ of','Idea: log_b(x) asks which power of b makes x. Rewrite the number as a power of the base.'),
(r'log base \d+ of \d+ plus log base','Idea: logs of the same base add when the numbers multiply: log a + log b = log(ab). Combine, then evaluate.'),
(r'log₂ \d+ ≈','Idea: log rules let you build one log from known ones: log(ab) = log a + log b and log(a/b) = log a − log b. Write the new number from the known ones.'),
(r'triples','Idea: tripling means the balance reaches 3 times the start. Solve (growth factor)^t = 3 by taking logs: t = ln 3 ÷ ln(growth factor).'),
(r'savings jar|front row has|Logs are stacked|first level has','Idea: adding the same amount each step makes an arithmetic sequence: the nth term is a₁ + (n − 1)d. Find a₁ and d first.'),
(r'rumor|chain email','Idea: multiplying by the same factor each step makes a geometric sequence: the nth term is a₁ · rⁿ⁻¹.'),
(r'opposite side is \d+ and the adjacent|right triangle has opposite side','Idea: tan θ = opposite ÷ adjacent. To find the angle from the sides, use the inverse: θ = tan⁻¹(opposite ÷ adjacent).'),
(r'pizza slice|sector','Idea: a sector is a fraction of a whole circle. The fraction is the tip angle ÷ 360°, so area = (angle ÷ 360°) × πr².'),
(r'maximum of .* and a minimum','Idea: the wave swings equally above and below its midline. Amplitude is half the distance from the maximum to the minimum, and the midline is their average.'),
(r'area of a triangle with sides .* included angle','Idea: area = ½ · a · b · sin C, where C is the angle between the two known sides. It is “half base × height” with the height found from the angle.'),
(r'magnitude of the vector','Idea: a vector’s magnitude is its length, found by Pythagoras: √(x² + y²).'),
(r'dot product','Idea: the dot product multiplies matching components and adds the results, giving a single number.'),
(r'lighthouses|distance between','Idea: distance between two points comes from Pythagoras on the change in x and the change in y: √((Δx)² + (Δy)²).'),
(r'asymptotes y = ±mx','Idea: for x²/a² − y²/b² = 1 the asymptotes are y = ±(b/a)x. a² and b² are the denominators.'),
(r'Find y when x|What is y when x','Idea: parametric equations use a third variable t. Use the given x to find t first, then substitute t into y.'),
(r'modulus \|','Idea: the modulus of a + bi is its distance from the origin on the complex plane: √(a² + b²).'),
(r'modulus of its','Idea: multiplying complex numbers multiplies their moduli, so the modulus of zⁿ is |z|ⁿ.'),
(r'angle θ is opposite','Idea: with a right triangle, pick the trig ratio that uses the two sides you know, then use its inverse to get the angle.'),
(r'included angle of','Idea: when two sides and the angle between them are known, area = ½ab sin C. (For the third side, use the Law of Cosines.)'),
(r'piecewise','Idea: a piecewise function has different rules on different intervals. Check which condition the input meets, then use only that rule.'),
(r'If f\(x\) = .*find f\(|Let f\(x\) = .* Find f\(g','Idea: f(a) means “replace every x with a”. For f(g(a)), work from the inside out: evaluate g(a), then put that result into f.'),
(r'Find the value of x³','Idea: substitute the given value for x and compute, keeping track of signs on negatives.'),
(r'vertex of y','Idea: a parabola’s axis of symmetry runs through the vertex at x = −b ÷ 2a for y = ax² + bx + c.'),
(r'roots r and s','Idea: Vieta’s formulas: for x² + bx + c, r + s = −b and rs = c. Rewrite what is asked in terms of r + s and rs.'),
(r'How many real roots','Idea: the discriminant D = b² − 4ac decides: D > 0 two real roots, D = 0 one, D < 0 none (they are complex).'),
(r'square has side|square has area','Idea: a square’s area is side × side, so side is the square root of the area.'),
(r'sin θ = \d+/\d+, find cos²θ','Idea: sin²θ + cos²θ = 1 for every angle, so cos²θ = 1 − sin²θ.'),
(r'period, in degrees|repeats every|sin\(\d*x\)','Idea: y = sin(bx) completes one cycle when bx = 360°, so period = 360° ÷ b (or 2π ÷ b in radians).'),
(r'Ferris|skate ramp','Idea: y = a·sin x + c oscillates around the midline y = c, reaching c + |a| at its highest and c − |a| at its lowest.'),
(r'y = \d+/\(x [+−] \d+\) \+','Idea: for y = a/(x − h) + k the vertical asymptote is where the denominator is zero (x = h) and the horizontal asymptote is y = k.'),
(r'Solve \d+/x','Idea: undo the division by multiplying both sides by x, then solve for x. Check that x is not 0.'),
(r'What is \d+[²³]','Idea: an exponent counts repeated multiplication: n² = n × n and n³ = n × n × n.'),
(r'nth square|th square number','Idea: square numbers are 1², 2², 3², … so the nth one is n².'),
(r'sum of the first \d+ terms of the arithmetic','Idea: pair first and last terms: every pair sums to the same amount, so S = n(a₁ + aₙ) ÷ 2.'),
(r'sum of \d+k|Evaluate the sum','Idea: Σ means “add the terms as k runs from the lower to the upper limit”. For Σk use n(n + 1) ÷ 2 and pull out constant factors.'),
(r'a₂ = .* a₅|common ratio','Idea: in a geometric sequence a₅ = a₂ · r³ (three steps from term 2 to term 5), so r³ is the ratio of the two terms.'),
(r'sin²\(A/2\)','Idea: the half-angle formula gives the sine of half an angle from the cosine of the full angle. Substitute A and compute.'),
(r'doubles in height|doubles every','Idea: doubling each step multiplies by 2 each time: amount = start × 2^(number of steps).'),
(r'grows \d+% a year|factor does the balance','Idea: a growth rate r per year multiplies the balance by (1 + r) each year, so the yearly factor is 1 + r.'),
(r'Combine like terms|combining like terms','Idea: like terms have the same variable part, so their coefficients can be added.'),
]
p=json.load(open('events/apex-math/pack.json'));fix={}
for q in p['questions']:
    s=q.get('sol') or []
    if sum(len(x) for x in s)>=50 or 'xh' in q['id']:continue
    if s and s[0].startswith('Idea:'):continue
    for rx,lead in RULES:
        if re.search(rx,q['q']):fix[q['id']]={'sol':[lead]+s};break
json.dump({'fix':fix},open('src/audit_apex/e1.json','w'),ensure_ascii=False)
print(len(fix),'solutions given a concept lead-in')
