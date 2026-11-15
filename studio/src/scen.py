#!/usr/bin/env python3
"""Rewrite bare symbolic stems as word problems (same numbers, same answer, same answer format).
Usage: scen.py pack.json   . Only stems that have a natural real-world version are changed."""
import json,re,sys
M='−'
def sub(pat,fn):return (re.compile(pat),fn)
def tvar(e):return e.replace('x','t')
G=[ # geometry-readiness
sub(r'^Two angles are complementary\. One measures (\d+)°\. Find the other \(degrees\)\.$',lambda m:f'A picture-frame corner is a right angle. A wooden strip splits it into two parts, and one part measures {m[1]}°. Find the other part (degrees).'),
sub(r'^Two angles form a linear pair\. One is (\d+)°\. Find the other \(degrees\)\.$',lambda m:f'A skate ramp leans against a straight, flat curb line and makes a {m[1]}° angle on one side. What angle does it make on the other side of the ramp (degrees)?'),
sub(r'^Two lines cross\. One angle is (\d+)°\. What is the angle vertical to it \(degrees\)\?$',lambda m:f'Two sidewalks cross in an X. One angle between them is {m[1]}°. What is the angle directly opposite it (degrees)?'),
sub(r'^Points A, B, C lie on a line with B between A and C\. AB = (\d+) and BC = (\d+)\. Find AC\.$',lambda m:f'A straight trail runs from camp A past a lake B to a tower C. Camp to lake is {m[1]} km and lake to tower is {m[2]} km. How far is it from camp to tower (km)?'),
sub(r'^Ray BD bisects ∠ABC, and m∠ABC = (\d+)°\. Find m∠ABD \(degrees\)\.$',lambda m:f'A laser beam splits a {m[1]}° corner of a room into two equal angles. How large is each part (degrees)?'),
sub(r'^Lines ℓ ∥ m are cut by a transversal\. One angle is (\d+)°\. Its (alternate exterior|alternate interior|corresponding) angle is how many degrees\?$',lambda m:f'Two parallel train tracks are crossed by a road. One angle the road makes with a track is {m[1]}°. Its {m[2]} angle is how many degrees?'),
sub(r'^A triangle has angles (\d+)° and (\d+)°\. Find the third angle \(degrees\)\.$',lambda m:f'A triangular sail has two corners measuring {m[1]}° and {m[2]}°. What is the third corner (degrees)?'),
sub(r'^Find the sum of the interior angles of a convex polygon with (\d+) sides \(degrees\)\.$',lambda m:f'A park is shaped like a convex polygon with {m[1]} straight sides. What is the sum of its interior angles (degrees)?'),
sub(r'^Each exterior angle of a regular polygon is (\d+)°\. How many sides does it have\?$',lambda m:f'A walkway around a regular-polygon plaza turns {m[1]}° at every corner. How many sides does the plaza have?'),
sub(r'^Find one interior angle of a regular (\d+)-gon \(degrees\)\.$',lambda m:f'A decorative tile is a regular {m[1]}-gon. Find one interior angle (degrees).'),
sub(r'^In an isosceles triangle the vertex angle is (\d+)°\. Find one base angle \(degrees\)\.$',lambda m:f'A roof truss is an isosceles triangle with a {m[1]}° peak. Find one base angle (degrees).'),
sub(r'^In an isosceles triangle a base angle is (\d+)°\. Find the vertex angle \(degrees\)\.$',lambda m:f'The front of a tent is an isosceles triangle with base angles of {m[1]}°. Find the angle at the peak (degrees).'),
sub(r'^Two sides of a triangle are (\d+) and (\d+)\. What is the (smallest|largest) WHOLE number the third side can be\?$',lambda m:f'A farmer has fence sections of {m[1]} m and {m[2]} m and will add a third whole-number section to enclose a triangular pen. What is the {m[3]} whole number of metres the third section can be?'),
sub(r'^In parallelogram ABCD, m∠A = (\d+)°\. Find m∠C \(degrees\)\.$',lambda m:f'A parallelogram-shaped picture frame has one corner of {m[1]}°. Find the opposite corner (degrees).'),
sub(r'^In parallelogram ABCD, m∠A = (\d+)°\. Find m∠B \(degrees\)\.$',lambda m:f'A parallelogram-shaped picture frame has one corner of {m[1]}°. Find the corner right next to it (degrees).'),
sub(r'^A rhombus has side (\d+)\. Find its perimeter\.$',lambda m:f'A rhombus-shaped flower bed has sides of {m[1]} m. How many metres of edging go all the way around it?'),
sub(r'^The diagonals of a rhombus are (\d+) and (\d+)\. Find its side length\.$',lambda m:f'The two diagonals of a rhombus-shaped floor tile are {m[1]} cm and {m[2]} cm. Find the side length of the tile (cm).'),
sub(r'^A rectangle has sides (\d+) and (\d+)\. How long is each diagonal\?$',lambda m:f'A rectangular tablet screen is {m[1]} in by {m[2]} in. How long is the screen’s diagonal (in)?'),
sub(r'^Find the midsegment of a trapezoid whose bases are (\d+) and (\d+)\.$',lambda m:f'A trapezoid-shaped garden has parallel sides of {m[1]} m and {m[2]} m. A path runs exactly halfway between them. How long is the path (m)?'),
sub(r'^The ratio of two lengths is (\d+) : (\d+)\. The first is (\d+)\. Find the second\.$',lambda m:f'A poster and its small copy have matching lengths in the ratio {m[1]} : {m[2]}. The poster length is {m[3]} cm. Find the copy’s matching length (cm).'),
sub(r'^△ABC ∼ △DEF with scale factor 1 : (\d+)\. AB = (\d+)\. Find DE\.$',lambda m:f'A blueprint triangle ABC is enlarged by a scale factor of 1 : {m[1]} to build a real triangular roof DEF. AB = {m[2]} units on the blueprint. Find DE.'),
sub(r'^Two similar polygons have scale factor 1 : (\d+)\. The smaller has perimeter (\d+)\. Find the larger perimeter\.$',lambda m:f'A model of a pond and the real pond are similar shapes with scale factor 1 : {m[1]}. The model’s perimeter is {m[2]} m. Find the real pond’s perimeter (m).'),
sub(r'^Two similar figures have scale factor 1 : (\d+)\. The smaller has area (\d+) cm²\. Find the larger area \(cm²\)\.$',lambda m:f'A photo and its enlargement are similar with scale factor 1 : {m[1]}. The photo has area {m[2]} cm². Find the enlargement’s area (cm²).'),
sub(r'^A right triangle has legs (\d+) and (\d+)\. Find the hypotenuse\.$',lambda m:f'A wheelchair ramp rises {m[1]} ft over a horizontal run of {m[2]} ft. How long is the ramp surface (ft)?'),
sub(r'^A right triangle has hypotenuse (\d+) and one leg (\d+)\. Find the other leg\.$',lambda m:f'A {m[1]} m ladder leans on a wall with its foot {m[2]} m from the wall. How high up the wall does it reach (m)?'),
sub(r'^A right triangle has legs (\d+) and (\d+)\. Find the hypotenuse to the nearest tenth\.$',lambda m:f'A square-cornered field has two perpendicular sides of {m[1]} m and {m[2]} m. How long is the diagonal path across it, to the nearest tenth (m)?'),
sub(r'^Find the area of a rectangle (\d+) by (\d+)\.$',lambda m:f'A rectangular rug is {m[1]} m by {m[2]} m. What is its area (m²)?'),
sub(r'^Find the area of a triangle with base (\d+) and height (\d+)\.$',lambda m:f'A triangular sail has a base of {m[1]} m and a height of {m[2]} m. Find its area (m²).'),
sub(r'^Find the area of a parallelogram with base (\d+) and height (\d+)\.$',lambda m:f'A parallelogram-shaped solar panel has a base of {m[1]} ft and a height of {m[2]} ft. Find its area (ft²).'),
sub(r'^Find the area of a trapezoid with bases (\d+) and (\d+) and height (\d+)\.$',lambda m:f'A trapezoid-shaped garden has parallel sides of {m[1]} m and {m[2]} m, and the distance between them is {m[3]} m. Find its area (m²).'),
sub(r'^Find the area of a circle with radius (\d+)\. Give the answer as a multiple of π\.$',lambda m:f'A circular pond has a radius of {m[1]} m. Find its area as a multiple of π.'),
sub(r'^Find the circumference of a circle with diameter (\d+)\. Give the answer as a multiple of π\.$',lambda m:f'A circular running track has a diameter of {m[1]} m. Find the distance once around, as a multiple of π.'),
sub(r'^Find the volume of a box (\d+) × (\d+) × (\d+)\.$',lambda m:f'A shipping box measures {m[1]} cm by {m[2]} cm by {m[3]} cm. What is its volume (cm³)?'),
sub(r'^Find the volume of a cylinder with radius (\d+) and height (\d+) \(coefficient of π\)\.$',lambda m:f'A cylindrical water tank has radius {m[1]} m and height {m[2]} m. Find its volume (coefficient of π).'),
sub(r'^Find the volume of a cone with radius (\d+) and height (\d+) \(coefficient of π\)\.$',lambda m:f'A cone-shaped paper cup has radius {m[1]} cm and height {m[2]} cm. Find its volume (coefficient of π).'),
sub(r'^Find the volume of a sphere with radius (\d+) \(coefficient of π\)\.$',lambda m:f'A spherical water balloon has radius {m[1]} cm. Find its volume (coefficient of π).'),
sub(r'^Find the distance between \((−?\d+), (−?\d+)\) and \((−?\d+), (−?\d+)\)\.$',lambda m:f'On a city map grid (one unit = one block), a library is at ({m[1]}, {m[2]}) and a café is at ({m[3]}, {m[4]}). How far apart are they in a straight line?'),
sub(r'^Find the slope through \((−?\d+), (−?\d+)\) and \((−?\d+), (−?\d+)\)\.$',lambda m:f'A hiking trail passes through map points ({m[1]}, {m[2]}) and ({m[3]}, {m[4]}). Find the trail’s slope (rise over run).'),
sub(r'^Find the slope of the line through \((−?\d+), (−?\d+)\) and \((−?\d+), (−?\d+)\)\. Fractions are fine\.$',lambda m:f'A zip line passes through the grid points ({m[1]}, {m[2]}) and ({m[3]}, {m[4]}). Find its slope. Fractions are fine.'),
sub(r'^Find the x-coordinate of the vertex of y = (.+)\.$',lambda m:('A bridge arch has height y = '+m[1]+' at horizontal position x. At which x is the arch at its '+('highest' if m[1].lstrip().startswith(M) else 'lowest')+' point (the vertex)?')),
sub(r'^∠A = \((\d+)x \+ (\d+)\)° and ∠B = \((\d+)x \+ (\d+)\)° are complementary\. Find x\.$',lambda m:f'Two roof braces meet at a right-angle corner. The angles they make are ({m[1]}x + {m[2]})° and ({m[3]}x + {m[4]})°. Find x.'),
sub(r'^△ABC ≅ △XYZ\. If AB = (\d+), how long is XY\?$',lambda m:f'Two triangular sails, ABC and XYZ, are exactly the same size and shape (congruent). Side AB is {m[1]} ft. How long is side XY (ft)?'),
sub(r'^A trapezoid has a midsegment of (\d+) and one base of (\d+)\. Find the other base\.$',lambda m:f'A trapezoid-shaped lot has a path halfway between its two parallel sides. The path is {m[1]} m long and one parallel side is {m[2]} m. How long is the other parallel side (m)?'),
sub(r'^Find the area of a (\d+)° sector of a circle with radius (\d+)\. Give the coefficient of π \(decimal ok\)\.$',lambda m:f'A pizza has radius {m[2]} in. A slice has a {m[1]}° tip. Find the slice’s area as a coefficient of π (decimal ok).'),
sub(r'^Find the length of a (\d+)° arc in a circle with radius (\d+)\. Give the coefficient of π \(decimal ok\)\.$',lambda m:f'A circular race track has radius {m[2]} m. A runner covers a {m[1]}° arc of it. Find the arc length as a coefficient of π (decimal ok).'),
sub(r'^Find the total surface area of a box (\d+) × (\d+) × (\d+)\.$',lambda m:f'A gift box is {m[1]} in by {m[2]} in by {m[3]} in. How much wrapping paper covers the whole outside (in²)?'),
sub(r'^Find the volume of a pyramid with a (\d+) × (\d+) base and height (\d+)\.$',lambda m:f'A pyramid-shaped tent has a {m[1]} ft by {m[2]} ft base and is {m[3]} ft tall. Find the volume of air inside (ft³).'),
sub(r'^Find the lateral \(side\) area of a cylinder with radius (\d+) and height (\d+) \(coefficient of π\)\.$',lambda m:f'A label wraps once around the side of a can with radius {m[1]} cm and height {m[2]} cm. Find the label’s area (coefficient of π).'),
sub(r'^A figure has area (\d+)\. A similar figure has all lengths multiplied by (\d+)\. Find the new area\.$',lambda m:f'A garden plan covers {m[1]} m². The real garden is built with every length multiplied by {m[2]}. Find the real garden’s area (m²).'),
sub(r'^A solid has volume (\d+)\. A similar solid has every length multiplied by (\d+)\. Find its volume\.$',lambda m:f'A small model of a statue has volume {m[1]} cm³. The real statue is similar, with every length {m[2]} times as large. Find the statue’s volume (cm³).'),
]
A=[ # apex-math
sub(r'^Find f′\((−?\d+)\) for f\(x\) = (.+)\.$',lambda m:f'A drone’s height after t seconds is h(t) = {tvar(m[2])} metres. How fast is the height changing at t = {m[1]} s? (Find h′({m[1]}).)'),
sub(r'^At what x does f\(x\) = (.+) have its vertex\? \(f′\(x\) = 0\)$',lambda m:f'A company’s cost for making x hundred items is C(x) = {m[1]} dollars. At what x is the cost at its turning point? (C′(x) = 0)'),
sub(r'^What is the minimum value of y = (.+)\?$',lambda m:f'A skate ramp’s height above its base line is y = {m[1]} metres at horizontal position x. What is the lowest height the ramp reaches (m)?'),
sub(r'^What is the amplitude of y = (.+)\?$',lambda m:f'A buoy’s height is y = {m[1]} metres as waves pass (x = position in the wave cycle). What is the wave amplitude (m)?'),
sub(r'^What is the maximum value of y = (.+)\?$',lambda m:f'A Ferris-wheel car’s height is y = {m[1]} metres during a ride (x = position in the turn). What is the greatest height it reaches (m)?'),
sub(r'^What is the minimum value of y = (.+·(?:sin|cos) x.*)\?$',lambda m:f'A swing’s height is y = {m[1]} metres during its motion (x = position in the swing cycle). What is the lowest height it reaches (m)?'),
sub(r'^What comes next\? (\d+), (\d+), (\d+), (\d+), \.\.\.$',lambda m:f'A savings jar holds ${m[1]}, then ${m[2]}, then ${m[3]}, then ${m[4]} at the end of four weeks, and the pattern keeps going. How many dollars will it hold next week?'),
sub(r'^An arithmetic sequence has first term (\d+) and common difference (\d+)\. What is term number (\d+)\?$',lambda m:f'A theatre’s front row has {m[1]} seats, and each row behind it has {m[2]} more seats than the row before. How many seats are in row {m[3]}?'),
sub(r'^A geometric sequence starts at (\d+) and multiplies by (\d+) each time\. What is term number (\d+)\?$',lambda m:f'On day 1 a rumor reaches {m[1]} people, and each day the number of people it reaches is {m[2]} times the day before. How many people does it reach on day {m[3]}?'),
sub(r'^Find 1 \+ 2 \+ 3 \+ … \+ (\d+)\.$',lambda m:f'Logs are stacked in rows: 1 log in the top row, 2 in the next, 3 in the next, and so on down to {m[1]} rows. How many logs are in the whole stack?'),
sub(r'^Find the sum of the first (\d+) terms of the arithmetic sequence 1, 3, 5, …$',lambda m:f'A stadium section has 1 seat in the first row, 3 in the second, 5 in the third, and so on. How many seats are in the first {m[1]} rows?'),
sub(r'^If f\(x\) = (\d+)·(\d+)ˣ, find f\((\d+)\)\.$',lambda m:f'A video’s view count after x days is f(x) = {m[1]}·{m[2]}ˣ thousand views. How many thousand views after {m[3]} days?'),
sub(r'^Solve (\d+)ˣ = (\d+)\.$',lambda m:f'A culture’s size is multiplied by {m[1]} every hour. After how many hours is it {m[2]} times its starting size?'),
sub(r'^Solve (\d+)ˣ = (\d+) using logarithms\. Give x to (\d+) decimals?\.$',lambda m:f'A bacteria colony’s size is multiplied by {m[1]} every hour. After how many hours is it {m[2]} times its starting size? Use logarithms and give the number of hours to {m[3]} decimals.'),
sub(r'^An exponential y = a·bˣ passes through \(0, (\d+)\) and \(2, (\d+)\)\. Find b\.$',lambda m:f'A town’s population was {m[1]} thousand at the start and {m[2]} thousand two years later, growing by the same factor b each year (y = a·bˣ). Find b.'),
sub(r'^Convert the polar point \((−?\d+), (\d+)°\) to rectangular coordinates\. What is y\?(.*)$',lambda m:f'A radar screen shows a plane at distance {m[1]} km from the tower, at an angle of {m[2]}° counterclockwise from due east (polar point ({m[1]}, {m[2]}°)). What is its north–south coordinate y (km)?{m[3]}'),
sub(r'^Convert the polar point \((−?\d+), (\d+)°\) to rectangular coordinates\. What is x\?(.*)$',lambda m:f'A radar screen shows a plane at distance {m[1]} km from the tower, at an angle of {m[2]}° counterclockwise from due east (polar point ({m[1]}, {m[2]}°)). What is its east–west coordinate x (km)?{m[3]}'),
sub(r'^Convert the polar point \((−?\d+), (\d+)°\) to rectangular form\. What is y\?(.*)$',lambda m:f'A radar screen shows a plane at distance {m[1]} km from the tower, at an angle of {m[2]}° counterclockwise from due east. What is its north–south coordinate y (km)?{m[3]}'),
sub(r'^Find the midpoint x-coordinate of \((−?\d+), (−?\d+)\) and \((−?\d+), (−?\d+)\)\.$',lambda m:f'Two lighthouses are at map points ({m[1]}, {m[2]}) and ({m[3]}, {m[4]}). A boat anchors at the midpoint between them. What is the x-coordinate of the boat’s spot?'),
sub(r'^Find the distance between \((−?\d+), (−?\d+)\) and \((−?\d+), (−?\d+)\)\.$',lambda m:f'A map puts the school at ({m[1]}, {m[2]}) and the park at ({m[3]}, {m[4]}), in kilometres. How far apart are they in a straight line (km)?'),
sub(r'^What is the radius of the circle \((.+)\)² \+ \((.+)\)² = (\d+)\?$',lambda m:f'A sprinkler waters the circle ({m[1]})² + ({m[2]})² = {m[3]} (units in metres). How far does the water reach from the sprinkler (m)?'),
sub(r'^A circle has equation \((.+)\)² \+ \((.+)\)² = (\d+)\. What is the x-coordinate of its center\?$',lambda m:f'On a park map, a circular pond is drawn with the equation ({m[1]})² + ({m[2]})² = {m[3]}. What is the x-coordinate of the pond’s center?'),
sub(r'^y varies inversely with x and y = (\d+) when x = (\d+)\. Find y when x = (\d+)\.$',lambda m:f'The time y (hours) a trip takes varies inversely with the speed x (mph). y = {m[1]} when x = {m[2]}. Find y when x = {m[3]}.'),
sub(r'^In an arithmetic sequence a₁ = (\d+) and d = (\d+)\. Which term number equals (\d+)\?$',lambda m:f'A parking garage’s first level has {m[1]} spaces, and each level above has {m[2]} more than the one below. Which level has {m[3]} spaces?'),
sub(r'^Find the sum of the first (\d+) terms of the geometric series starting at (\d+) with ratio (\d+)\.$',lambda m:f'A chain email reaches {m[2]} people on day 1, and each day it reaches {m[3]} times as many as the day before. How many people have been reached in total after {m[1]} days?'),
sub(r'^An arithmetic series has first term (\d+), (\d+) terms and sum (\d+)\. Find the common difference d\.$',lambda m:f'A theatre’s front row has {m[1]} seats, each row behind has d more seats than the row before, and {m[2]} rows hold {m[3]} seats in all. Find d.'),
sub(r'^Find the arc length on a circle of radius (\d+) cm cut off by a central angle of (\d+)°\. \((\d) decimals\)$',lambda m:f'A clock face has radius {m[1]} cm. The tip of the minute hand sweeps through {m[2]}°. How long is the arc it traces (cm, {m[3]} decimals)?'),
sub(r'^Find the area of a sector with radius (\d+) cm and central angle (\d+)°\. (.+)$',lambda m:f'A pizza slice is a sector with radius {m[1]} cm and a {m[2]}° tip. Find its area. {m[3]}'),
sub(r'^A ball is thrown upward: h\(t\) = (.+)\. At what time t does it reach its maximum height\?$',lambda m:f'A ball is thrown upward and its height in metres is h(t) = {m[1]}. At what time t (seconds) does it reach its maximum height?'),
]
RULES={'geometry-readiness':G,'apex-math':A}
def main(p):
    d=json.load(open(p));rules=RULES.get(d['meta']['id'].rsplit('-',1)[0],[]);n=0
    for q in d['questions']:
        if q['type']!='short':continue
        s=q['q']
        for rx,fn in rules:
            m=rx.match(s)
            if m:q['q']=fn(m);n+=1;break
    json.dump(d,open(p,'w'),ensure_ascii=False,separators=(',',':'));print('scenarized',p,n,'of',sum(1 for q in d['questions'] if q['type']=='short'))
main(sys.argv[1])
