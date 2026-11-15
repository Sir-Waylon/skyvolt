import itertools, json
OUT="/tmp/claude-0/-home-claude/bdb1ee03-0916-54eb-a354-ea75cf26b960/scratchpad/audit/out/c6.json"
N=[0]
def fp():
    N[0]+=1; return "c6_%d"%N[0]
def mcq(t,l,b,q,c,wr,w,sol):
    assert len(wr)==3
    return dict(t=t,l=l,b=b,type="mcq",q=q,o=[c]+wr,w=w,sol=sol,fp=fp())
def num(t,l,b,q,v,w,sol,u="",tol=0.0):
    d=dict(t=t,l=l,b=b,type="short",q=q,num=dict(v=v,tol=tol),w=w,sol=sol,fp=fp())
    if u: d["num"]["u"]=u
    return d
def txt(t,l,b,q,ans,w,sol):
    return dict(t=t,l=l,b=b,type="short",q=q,text=ans,w=w,sol=sol,fp=fp())
def multi(t,l,b,q,o,a,w,sol):
    return dict(t=t,l=l,b=b,type="multi",q=q,o=o,a=a,w=w,sol=sol,fp=fp())
def order(t,l,b,q,items,w,sol):
    return dict(t=t,l=l,b=b,type="order",q=q,items=items,w=w,sol=sol,fp=fp())
def match(t,l,b,q,pairs,w,sol):
    return dict(t=t,l=l,b=b,type="match",q=q,pairs=pairs,w=w,sol=sol,fp=fp())
def rows(f,n): return [f(*r) for r in itertools.product([0,1],repeat=n)]
def cnt(f,n): return sum(1 for x in rows(f,n) if x)
def eq(f,g,n): return rows(f,n)==rows(g,n)
NOT=lambda x:1-x
NAND=lambda a,b:1-(a&b); NOR=lambda a,b:1-(a|b); XOR=lambda a,b:a^b; XNOR=lambda a,b:1-(a^b)
imp=lambda a,b:(1-a)|b
def valid(prem,concl,n):
    for r in itertools.product([0,1],repeat=n):
        if all(p(*r) for p in prem) and not concl(*r): return False
    return True

L=[]
t="logic"
# ---- logic ----
L.append(mcq(t,1,-0.8,"Which 2-input gate is the exact opposite of OR (output flips for every input row)?","NOR",["NAND","XNOR","AND"],"NOR is OR followed by an inverter.",["OR is 1 for three rows and 0 only for (0,0).","Flip every output: 0 only for three rows, 1 only for (0,0).","That is NOR. NAND flips AND, not OR."]))
L.append(mcq(t,1,-0.5,"A binary number ends in 1. Is the number odd or even?","Odd",["Even","It depends on the other bits","Only odd if it has an even number of 1s"],"The rightmost bit is worth 1; every other place value is even.",["Place values are 1, 2, 4, 8 ... Only the 1 is odd.","So the parity of the number is set by the last bit alone.","Misconception: counting 1s is parity of the bits, not of the number."]))
L.append(mcq(t,1,-0.5,"A 2-input OR gate has one input held at 1. The output is:","always 1",["equal to the other input","always 0","the inverse of the other input"],"OR with 1 gives 1 whatever the other input is.",["OR is 1 if at least one input is 1.","One input is already 1, so the output is locked at 1.","OR with 0 is the one that passes the other input."]))
L.append(mcq(t,1,-0.5,"The 2-input gate outputs for inputs (A,B) = (0,0), (0,1), (1,0), (1,1) are 1, 1, 1, 0. Which gate is it?","NAND",["NOR","XOR","OR"],"NAND is 0 only when both inputs are 1.",["List where the output is 0: only (1,1).","AND gives 0 on three rows, so the opposite gate gives 0 on one row.","That is NAND."]))
L.append(mcq(t,2,0.0,"The 2-input gate outputs for (0,0), (0,1), (1,0), (1,1) are 1, 0, 0, 1. Which gate is it?","XNOR",["XOR","NOR","AND"],"Output is 1 when the inputs are equal.",["The 1s are at (0,0) and (1,1).","Both of those have equal inputs.","That is XNOR (equality). XOR would be 0, 1, 1, 0."]))
L.append(mcq(t,2,0.2,"Even parity: a check bit is added so the total number of 1s is even. The data bits are 1011. What is the check bit?","1",["0","It cannot be found","10"],"1011 has three 1s, so a 1 makes four.",["Count the 1s in 1011: three.","Three is odd, so add a 1 to reach four (even).","The check bit equals the XOR of the data bits: 1⊕0⊕1⊕1 = 1."]))
L.append(num(t,1,-0.3,"How many of the 16 rows of a 4-input AND gate output 0?",15,"AND is 1 only when all four inputs are 1.",["2⁴ = 16 rows.","Only the row 1111 gives 1.","16 − 1 = 15 rows give 0."]))
L.append(num(t,2,0.3,"How many of the 16 rows of a 4-input XOR (1 when an odd number of inputs are 1) output 1?",8,"Odd parity is true for exactly half of the rows.",["Choose rows with one 1 (4 rows) or three 1s (4 rows).","4 + 4 = 8.","Half of 16 is 8: flipping any one input flips the output."]))
L.append(num(t,2,0.3,"A 3-input XOR gives 1 when an odd number of inputs are 1. What is its output for A = 1, B = 1, C = 1?",1,"Three 1s is an odd count, so the output is 1.",["XOR in steps: 1⊕1 = 0.","Then 0⊕1 = 1.","Odd number of 1s gives 1."]))
L.append(order(t,1,-0.7,"Put the evaluation order for  A + B·C′  from FIRST to LAST.",["NOT on C","AND of B with C′","OR with A"],"Precedence is NOT, then AND, then OR.",["NOT binds tightest.","AND comes before OR, like × before +.","OR is last."]))
L.append(match(t,2,0.3,"For a 3-input gate, match each gate to how many of its 8 rows output 1.",[["AND","1"],["OR","7"],["XOR (odd parity)","4"]],"Count rows: AND needs all 1s; OR fails only at 000; XOR is odd parity.",["AND is 1 only at 111.","OR is 0 only at 000, so 7 rows are 1.","XOR is 1 when one or three inputs are 1: 3 + 1 = 4 rows."]))
# counts
exprs=[("Y = (A ⊕ B) + B·C",lambda a,b,c:(a^b)|(b&c)),("Y = A′·(B ⊕ C)",lambda a,b,c:(1-a)&(b^c)),("Y = ((A + B)′ + C)′",lambda a,b,c:1-((1-(a|b))|c)),("Y = (A·B)′·(B + C)",lambda a,b,c:(1-(a&b))&(b|c)),("Y = NOR(AND(A,B), XOR(A,C))",lambda a,b,c:1-((a&b)|(a^c)))]
for i,(s,f) in enumerate(exprs):
    v=cnt(f,3)
    L.append(num(t,3,0.9+0.15*i,"For how many of the 8 input rows is %s equal to 1?"%s,v,"Build the 8-row table in pieces and count the 1s.",["List all 8 (A,B,C) rows.","Work out each inner part first, then combine, following NOT before AND before OR.","Count the rows with output 1: %d."%v]))
# eval circuits
L.append(num(t,2,0.2,"Y = NOR( AND(A,B), XOR(A,C) ). Find Y for A = 1, B = 0, C = 1.",NOR(1&0,1^1),"AND = 0 and XOR = 0, so NOR(0,0) = 1.",["AND(1,0) = 0.","XOR(1,1) = 0 (equal inputs).","NOR(0,0) = 1."]))
L.append(num(t,2,0.3,"Y = XOR( NAND(A,B), OR(B,C) ). Find Y for A = 1, B = 1, C = 0.",(1-(1&1))^(1|0),"NAND = 0, OR = 1, so XOR = 1.",["NAND(1,1) = 0.","OR(1,0) = 1.","XOR(0,1) = 1."]))
f=lambda a,b,c:(1-(a|b))&XNOR(b,c)
L.append(num(t,3,1.0,"Y = AND( NOR(A,B), XNOR(B,C) ). For how many of the 8 input rows is Y = 1?",cnt(f,3),"NOR needs A = 0, B = 0; then XNOR needs C = 0.",["NOR(A,B) = 1 only when A = 0 and B = 0.","With B = 0, XNOR(B,C) = 1 only when C = 0.","Only the row 000 works: 1 row."]))
# simplification
def chk(f,g,n=2): assert eq(f,g,n)
chk(lambda a,b:((1-a)&b)|(a&b)|((1-a)&(1-b)), lambda a,b:(1-a)|b)
L.append(mcq(t,3,1.0,"A′·B + A·B + A′·B′ simplifies to:","A′ + B",["A + B′","A′·B","A′ + B′"],"A′B + AB = B, and B + A′B′ = A′ + B (using X + X′Y = X + Y).",["A′B + AB = B(A′ + A) = B.","Now B + A′B′ = B + A′ because B + B′Z = B + Z.","Result: A′ + B. Check A = 1, B = 0: every term is 0, so Y = 0, and A′ + B = 0 too."]))
chk(lambda a,b:(a|b)&(a|(1-b)), lambda a,b:a)
L.append(mcq(t,3,1.0,"(A + B)·(A + B′) simplifies to:","A",["A + B","1","A·B"],"Expand: A + A·B′ + A·B + B·B′ = A + A(B′ + B) + 0 = A.",["Multiply out the brackets.","B·B′ = 0 and A·B + A·B′ = A.","So A + A = A. Spot check: A = 0 makes both brackets B and B′, and B·B′ = 0."]))
g=lambda a,b,c:(a&b)|((1-a)&c)|(b&c); h=lambda a,b,c:(a&b)|((1-a)&c)
assert eq(g,h,3)
L.append(mcq(t,3,1.8,"A·B + A′·C + B·C simplifies to:","A·B + A′·C",["A·B + B·C","A′·C + B·C","A·B·C"],"The B·C term is redundant (consensus): when B·C = 1, either A·B or A′·C is already 1.",["Look at B·C = 1. Then B = 1 and C = 1.","If A = 1, A·B = 1. If A = 0, A′·C = 1.","So B·C never adds a new 1 and can be removed."]))
assert eq(lambda a,b:(a^b)^b, lambda a,b:a,2)
L.append(mcq(t,3,1.0,"(A ⊕ B) ⊕ B simplifies to:","A",["B","A ⊕ B","0"],"XOR with B twice cancels: B ⊕ B = 0 and A ⊕ 0 = A.",["XOR is associative: A ⊕ (B ⊕ B).","B ⊕ B = 0 (equal inputs).","A ⊕ 0 = A."]))
assert eq(lambda a,b:1-(a^b), lambda a,b:a^(1-b),2) and not eq(lambda a,b:(1-a)^(1-b), lambda a,b:1-(a^b),2)
L.append(mcq(t,3,1.5,"XNOR(A,B) = (A ⊕ B)′ is also equal to:","A ⊕ B′",["A′ ⊕ B′","A′·B′","A′ + B′"],"Inverting one XOR input inverts the output.",["XOR with 1 inverts the other input.","Inverting one input flips the result: (A ⊕ B′) = (A ⊕ B)′.","Inverting both inputs cancels: A′ ⊕ B′ = A ⊕ B, the opposite."]))
L.append(mcq(t,2,0.4,"By De Morgan, (A·B·C)′ equals:","A′ + B′ + C′",["A′·B′·C′","A′ + B + C","A + B + C"],"Break the bar, flip the operator, complement each variable.",["Break the long bar over the AND.","AND becomes OR.","Each variable gets its own bar."]))
assert eq(lambda a,b,c:1-(a|(1-b)|c), lambda a,b,c:(1-a)&b&(1-c),3)
L.append(mcq(t,3,1.1,"By De Morgan, (A + B′ + C)′ equals:","A′·B·C′",["A′·B′·C′","A′ + B + C′","A·B′·C"],"OR becomes AND and every term is complemented, including B′ becoming B.",["Break the bar, change + to ·.","Complement each term: A′, (B′)′ = B, C′.","Do not forget B′ flips to B (double negation)."]))
# gate counts via simulation
L.append(num(t,3,1.0,"What is the minimum number of 2-input NAND gates needed to build a NOR gate?",4,"NOR = NOT(OR); OR takes 3 NAND gates and the final inverter is a 4th.",["OR from NANDs: 2 inverters + 1 NAND = 3 gates.","NOR is OR inverted.","One more NAND wired as an inverter: 3 + 1 = 4."]))
L.append(num(t,2,0.5,"What is the minimum number of 2-input NAND gates needed to build an AND gate?",2,"NAND then an inverter (a NAND with tied inputs).",["AND = NOT(NAND).","NAND is 1 gate.","Inverter is a second NAND: 2 gates."]))
L.append(num(t,3,1.0,"What is the minimum number of 2-input NOR gates needed to build an AND gate?",3,"A·B = (A′ + B′)′: invert each input with a NOR (2 gates), then NOR them (1 gate).",["NOR with tied inputs is an inverter.","Invert A and B: 2 gates.","NOR(A′,B′) = (A′ + B′)′ = A·B: 1 gate. Total 3."]))
L.append(num(t,3,1.5,"What is the minimum number of 2-input NOR gates needed to build an XNOR gate? (Use the circuit N = NOR(A,B), then NOR(A,N) and NOR(B,N), then NOR of those two.)",4,"The four-gate NOR design gives XNOR.",["N = A′B′.","NOR(A,N) = A′B and NOR(B,N) = AB′.","NOR of those = (A′B + AB′)′ = XNOR. Four gates."]))
def sim(): # verify nor xnor
    for a,b in itertools.product([0,1],repeat=2):
        n=NOR(a,b); assert NOR(NOR(a,n),NOR(b,n))==XNOR(a,b)
sim()
assert all(NOR(NOR(a,b),NOR(a,b))==(a|b) for a,b in itertools.product([0,1],repeat=2))
L.append(mcq(t,2,0.5,"A circuit is NAND( NAND(A,A), NAND(B,B) ). It behaves as which single gate?","OR",["AND","NOR","XOR"],"The inner NANDs are inverters, so the output is (A′·B′)′ = A + B.",["NAND(A,A) = A′ and NAND(B,B) = B′.","Outer: (A′·B′)′.","De Morgan: = A + B, an OR gate."]))
assert all(NOR(NOR(a,b),NOR(a,b))==(a|b) for a,b in itertools.product([0,1],repeat=2))
L.append(mcq(t,3,1.0,"A circuit is NOR( NOR(A,B), NOR(A,B) ). The inner gate feeds both outer inputs. It behaves as which gate?","OR",["NOR","AND","NAND"],"The outer NOR with tied inputs is an inverter, so it undoes the inner NOR.",["Tied-input NOR is a NOT.","So output = NOT(NOR(A,B)).","NOT of NOR is OR."]))
assert eq(lambda a,b:NAND(a,NAND(a,b)), lambda a,b:(1-a)|b,2)
L.append(mcq(t,3,2.0,"Y = NAND( A, NAND(A,B) ). Which expression equals Y?","A′ + B",["A·B","A + B′","A′·B"],"NAND(A,B) = A′ + B′. Then Y = (A·(A′ + B′))′ = (A·B′)′ = A′ + B.",["Inner NAND = (AB)′ = A′ + B′.","A·(A′ + B′) = A·B′.","Y = (A·B′)′ = A′ + B. It is 0 only for A = 1, B = 0."]))
# truth table to expr
L.append(mcq(t,3,0.9,"A 3-input function has Y = 1 for ABC = 001, 011, 101, 111 and Y = 0 otherwise. Y equals:","C",["A·B·C","A + B + C","A ⊕ B ⊕ C"],"Every 1 row has C = 1, and every row with C = 1 is a 1 row.",["Look at the column C in the four 1 rows: always 1.","A and B take all four combinations.","So Y ignores A and B: Y = C."]))
L.append(mcq(t,3,1.2,"A 3-input function has Y = 1 for ABC = 000, 001, 110, 111 and 0 otherwise. Y equals:","A·B + A′·B′ (XNOR of A and B)",["A ⊕ B","A·B·C","A′·B′·C′"],"C does not matter. Y = 1 exactly when A = B.",["The 1 rows pair up: 000 and 001 differ only in C.","Same for 110 and 111, so C drops out.","Left: A = B = 0 or A = B = 1, which is XNOR."]))
maj=lambda a,b,c:int(a+b+c>=2)
assert eq(maj,lambda a,b,c:(a&b)|(a&c)|(b&c),3)
L.append(mcq(t,3,1.3,"Y = 1 for ABC = 011, 101, 110, 111 (at least two inputs are 1). Which expression matches?","A·B + A·C + B·C",["A + B + C","A·B·C","A ⊕ B ⊕ C"],"Each pair of 1s makes Y = 1: AB, AC or BC.",["The rows with two or more 1s each contain a pair (AB, AC or BC).","OR the three pair terms.","A ⊕ B ⊕ C is wrong because it is 0 for 011."]))
# mux
for a_ in [1]:
    pass
L.append(mcq(t,3,1.2,"A 4:1 mux has S1 = A, S0 = B and data inputs I0, I1, I2, I3 = 0, 1, 1, 0. The output is:","A ⊕ B",["A·B","A + B","A ⊕ B′"],"Output is 1 only for AB = 01 and 10: XOR.",["S1S0 = AB picks the input numbered AB in binary.","I1 (AB = 01) and I2 (AB = 10) are 1.","1 when A and B differ: XOR."]))
L.append(mcq(t,3,1.2,"A 4:1 mux has S1 = A, S0 = B and data inputs I0, I1, I2, I3 = 1, 0, 0, 1. The output is:","XNOR of A and B",["A ⊕ B","A·B","A′·B′"],"Output is 1 for AB = 00 and 11, the equal pairs.",["I0 (AB = 00) = 1 and I3 (AB = 11) = 1.","The other two are 0.","1 when A = B: XNOR."]))
L.append(mcq(t,3,1.0,"A 2:1 mux has select = A, I0 = B and I1 = 1. The output is:","A + B",["A·B","A ⊕ B","A′·B"],"A = 0 passes B; A = 1 outputs 1. That is OR.",["Select 0 gives I0 = B.","Select 1 gives 1.","Output is B if A = 0, 1 if A = 1: A + B."]))
L.append(mcq(t,3,1.4,"A 2:1 mux has select = A, I0 = 1 and I1 = B. The output is:","A′ + B",["A + B","A·B","A′·B"],"A = 0 gives 1; A = 1 passes B.",["Select 0 picks I0 = 1.","Select 1 picks I1 = B.","Y = 1 unless A = 1 and B = 0, which is A′ + B."]))
L.append(mcq(t,3,1.0,"To build any 3-input function with an 8:1 mux, connect A, B, C to the select lines. What goes on the 8 data inputs?","The 8 output values of the truth table (0 or 1 each)",["The inputs A, B and C repeated","Only the rows where the output is 1, one per input","Nothing; the mux calculates it"],"Each select combination picks one data input, so that input just holds the output for that row.",["8 select combinations = 8 rows.","Row k is picked by select value k.","Tie input k to 1 or 0 to match the table."]))
mx=lambda a,b,c:[0,c,1-c,0][2*a+b]
L.append(num(t,3,1.6,"A 4:1 mux has S1 = A, S0 = B and data inputs I0 = 0, I1 = C, I2 = C′, I3 = 0. For how many of the 8 rows of (A,B,C) is the output 1?",cnt(mx,3),"Only AB = 01 and AB = 10 can give 1.",["AB = 00 and 11 give 0.","AB = 01 outputs C: 1 for C = 1 (1 row).","AB = 10 outputs C′: 1 for C = 0 (1 row). Total 2."]))
# adders
L.append(mcq(t,1,-0.5,"Which gate produces the Carry output of a half adder?","AND",["XOR","OR","NAND"],"Carry is 1 only when both bits are 1.",["1 + 1 = 10 in binary.","Only 1 + 1 makes a carry.","That is AND. XOR makes the Sum."]))
L.append(mcq(t,2,0.2,"A full adder receives A = 1, B = 1, Carry-in = 1. Its outputs are:","Sum 1, Carry 1",["Sum 0, Carry 1","Sum 1, Carry 0","Sum 0, Carry 0"],"1 + 1 + 1 = 3 = binary 11.",["Add the three bits: 3.","3 in binary is 11.","Right bit is Sum = 1, left bit is Carry = 1."]))
cfa=lambda a,b,c:(a&b)|(c&(a^b))
L.append(num(t,2,0.5,"For how many of the 8 input rows is the Carry-out of a full adder equal to 1?",cnt(cfa,3),"Carry is 1 when at least two of the three inputs are 1.",["Carry means the sum is 2 or 3.","Rows with two 1s: 3. Rows with three 1s: 1.","3 + 1 = 4."]))
L.append(num(t,2,0.2,"How many full adders does an 8-bit ripple-carry adder with a carry input use?",8,"One full adder per bit position.",["Each bit adds A, B and the carry from the right.","That is a full adder.","8 bits means 8 full adders."]))
L.append(num(t,3,1.0,"A full adder is built from two half adders and one OR gate. How many XOR gates does it contain in total?",2,"Each half adder has one XOR for its Sum.",["Half adder 1: A ⊕ B.","Half adder 2: (A ⊕ B) ⊕ Cin.","Two XOR gates; the OR combines the two carries."]))
L.append(mcq(t,3,1.3,"In a ripple-carry adder, why does the top sum bit settle later than the bottom one?","The carry must pass through each stage in turn",["The top gates are slower","The top bits are larger numbers","The sum bits use a different clock"],"Each stage waits for the carry from the stage to its right.",["Stage 0 makes carry c1.","Stage 1 needs c1 before it can make c2, and so on.","The delay adds up along the chain."]))
# binary
L.append(num(t,2,0.2,"What is the largest number that fits in 8 binary bits? Give the answer in decimal.",255,"2⁸ − 1 = 255.",["8 bits give 2⁸ = 256 patterns.","They start at 0.","So the largest is 255."]))
L.append(mcq(t,2,0.3,"Adding a 0 on the right end of a binary number (for example 101 becomes 1010) does what to its value?","Doubles it",["Adds 2","Halves it","Squares it"],"Every bit moves one place to the left, so every place value doubles.",["101 = 5 and 1010 = 10.","Each bit now sits in a place worth twice as much.","Same idea as adding a 0 in decimal multiplies by 10."]))
L.append(mcq(t,3,0.9,"Deleting the rightmost bit of the binary number 101101 (leaving 10110) changes its value from 45 to:","22",["23","90","44"],"Dropping the last bit halves the number and drops any remainder: 45 ÷ 2 = 22 remainder 1.",["10110 = 16 + 4 + 2 = 22.","The right bit was the 1s place (odd remainder).","Shifting right is integer division by 2."]))
L.append(txt(t,3,1.0,"Subtract in binary: 10010 − 1011. Give the answer in binary.",["111","0111","00111"],"18 − 11 = 7 = 111.",["Convert: 10010 = 18 and 1011 = 11.","18 − 11 = 7.","7 = 4 + 2 + 1 = 111."]))
L.append(num(t,3,0.9,"How many 1 bits are in the binary form of 127?",7,"127 = 2⁷ − 1 = 1111111.",["128 = 10000000, so 127 is one less.","Subtracting 1 turns the single 1 into seven 1s.","Count: 7."]))
L.append(txt(t,2,0.4,"Add in binary: 11011 + 10101.",["110000"],"27 + 21 = 48 = 110000.",["Convert: 11011 = 27 and 10101 = 21.","Sum 48 = 32 + 16.","So 110000."]))
L.append(txt(t,3,1.1,"What is binary 11111111 + 1? Write the answer in binary.",["100000000"],"255 + 1 = 256 = 2⁸: a 1 followed by eight 0s.",["The carry ripples through all eight bits.","Each 1 + 1 = 0 carry 1.","The final carry makes a ninth bit."]))
L.append(mcq(t,2,0.2,"A signal named ENABLE′ is active-low. The device is switched ON when ENABLE′ is:","low (0)",["high (1)","floating","alternating"],"Active-low means the active state is the low voltage.",["The bar or prime says the signal is active when it is 0.","So 0 turns the device on.","1 turns it off."]))
L.append(mcq(t,2,0.5,"For inputs (A,B) = (1,0), which pair of gates both output 1?","NAND and XOR",["AND and OR","NOR and XOR","XNOR and NAND"],"NAND(1,0) = 1 and XOR(1,0) = 1.",["Test each gate at (1,0).","AND 0, OR 1, NAND 1, NOR 0, XOR 1, XNOR 0.","Only NAND and XOR are both 1."]))
L.append(mcq(t,2,0.6,"A technician says: \"A 3-input NAND gate outputs 0 only when all three inputs are 1.\" Is that right?","Yes, it is the inverse of a 3-input AND",["No, it outputs 0 when any input is 1","No, it outputs 0 only when all inputs are 0","No, it outputs 1 only when all inputs are 1"],"3-input AND is 1 only for 111; NAND flips that.",["AND is 1 only for 111.","NAND flips every output.","So NAND is 0 only for 111."]))
L.append(mcq(t,3,1.3,"A 2-input gate has output 0 at (0,0) and 1 at all other rows except (1,1) where it is 0. Which statement is true?","It is XOR, and a NAND gate cannot make it with fewer than 4 NANDs",["It is NAND","It is OR","It is XOR and needs only 2 NANDs"],"Outputs 0,1,1,0 are XOR; the standard NAND build uses 4 gates.",["Write the table: 00→0, 01→1, 10→1, 11→0.","That is XOR.","XOR from NAND needs 4 gates."]))
L.append(txt(t,2,0.6,"What is 1 + 1 in binary?",["10"],"One plus one is two, which is written 10.",["Binary has only 0 and 1.","1 + 1 = 2, but 2 is not a digit.","Write 0 and carry 1: 10."]))
L.append(txt(t,3,1.7,"A 4-bit adder adds 1111 + 1111. What 5-bit result comes out?",["11110"],"15 + 15 = 30 = 11110.",["Each number is 15.","Sum is 30 = 16 + 8 + 4 + 2.","So 11110: carry-out 1 and sum bits 1110."]))
L.append(mcq(t,3,1.9,"Y = A·B + A·C′. A student wants fewer gates. Which factored form equals Y?","A·(B + C′)",["A + B·C′","(A + B)·(A + C′)","A·B·C′"],"Factor out A: A·B + A·C′ = A·(B + C′).",["Both terms share A.","Distributive law reverses.","Check A = 0: Y = 0 and A(B + C′) = 0. (A + B)(A + C′) would be wrong because it is 1 when B = C′ = 1 and A = 0."]))
LOGIC=L

# ---------------- sym ----------------
SYM=[]
