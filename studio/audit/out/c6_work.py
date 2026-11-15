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
S=[]
t="sym"
P=lambda *a:None
S.append(mcq(t,2,0.2,"What is the contrapositive of P → Q?","~Q → ~P",["Q → P","~P → ~Q","~(P → Q)"],"The contrapositive swaps and negates both parts, and it always has the same truth value as the original.",["Converse: Q → P (swap only).","Inverse: ~P → ~Q (negate only).","Contrapositive: swap AND negate = ~Q → ~P."]))
S.append(mcq(t,1,-0.3,"Statement: \"If the switch is closed, the lamp lights.\" What is its converse?","If the lamp lights, the switch is closed.",["If the switch is open, the lamp is off.","If the lamp is off, the switch is open.","The switch is closed and the lamp lights."]))
S.append(mcq(t,2,0.3,"Statement: \"If the switch is closed, the lamp lights.\" What is its inverse?","If the switch is open, the lamp does not light.",["If the lamp lights, the switch is closed.","If the lamp is off, the switch is open.","The switch is open or the lamp lights."]))
assert eq(lambda p,q:imp(p,q),lambda p,q:(1-p)|q,2)
S.append(mcq(t,3,1.0,"Which statement is logically equivalent to P → Q?","~P ∨ Q",["P ∨ ~Q","~P ∧ Q","Q → P"],"P → Q fails only when P is true and Q is false, and ~P ∨ Q fails in exactly that row.",["P → Q is false only for P = T, Q = F.","~P ∨ Q is false only when ~P is F and Q is F, i.e. P = T, Q = F.","The tables match."]))
assert eq(lambda p,q:1-imp(p,q),lambda p,q:p&(1-q),2)
S.append(mcq(t,3,1.2,"Which statement is the negation of P → Q?","P ∧ ~Q",["~P → ~Q","P → ~Q","~P ∧ Q"],"The only way an if-then fails is when the if-part is true and the then-part is false.",["Ask when P → Q is false: P true, Q false.","Write that as P ∧ ~Q.","Misconception: the negation of an if-then is NOT another if-then."]))
assert eq(lambda p,q:1-(p&(1-q)),lambda p,q:(1-p)|q,2)
S.append(mcq(t,3,1.4,"By De Morgan and double negation, ~(P ∧ ~Q) is equivalent to:","~P ∨ Q",["~P ∧ Q","P ∨ ~Q","~P ∨ ~Q"],"Flip ∧ to ∨ and negate each part: ~P ∨ ~~Q = ~P ∨ Q.",["Break the bar over the AND.","Negate P and negate ~Q.","~~Q = Q, so ~P ∨ Q (which is P → Q)."]))
S.append(mcq(t,2,0.4,"Which pair of related statements ALWAYS have the same truth value?","An if-then and its contrapositive",["An if-then and its converse","An if-then and its inverse","An if-then and its negation"],"The contrapositive is equivalent; the converse and inverse are not.",["Test with \"If it is a square, it is a rectangle.\"","The converse (every rectangle is a square) is false.","The contrapositive (not a rectangle, so not a square) is true."]))
S.append(mcq(t,3,1.5,"Which pair of statements are logically equivalent to each other?","The converse and the inverse of the same if-then",["An if-then and its converse","An if-then and its inverse","An if-then and its negation"],"Converse is Q → P; inverse is ~P → ~Q. These are contrapositives of each other.",["Take the contrapositive of Q → P: ~P → ~Q.","That is exactly the inverse.","So they always match each other, but not the original."]))
S.append(mcq(t,2,0.0,"When P is false, the statement P → Q is:","true (whatever Q is)",["false","true only if Q is true","unknown"],"An if-then is broken only when P is true and Q is false.",["The rule says nothing when P does not happen.","So it cannot be broken.","This is called vacuously true."]))
S.append(num(t,2,0.3,"In how many of the 4 rows of a truth table is (P → Q) ∧ (Q → P) true?",2,"That is P ↔ Q: true when P and Q match.",["Rows (T,T) and (F,F) have P = Q.","Rows (T,F) and (F,T) break one direction.","2 rows."]))
f=lambda p,q,r:imp(imp(p,q),r)
S.append(num(t,3,1.2,"In how many of the 8 rows of a truth table for P, Q, R is (P → Q) → R true?",cnt(f,3),"Work out P → Q first, then the outer if-then.",["R true: always makes the outer if-then true (4 rows).","R false: need (P → Q) false, i.e. P = T, Q = F (1 row).","4 + 1 = 5."]))
f=lambda p,q,r:imp(p,imp(q,r))
S.append(num(t,3,1.3,"In how many of the 8 rows is P → (Q → R) true?",cnt(f,3),"It is false only when P is T, Q is T and R is F.",["The outer if-then fails only if P is T and Q → R is F.","Q → R is F only for Q = T, R = F.","1 failing row, so 8 − 1 = 7."]))
S.append(txt(t,1,-0.5,"A statement that is true in every row of its truth table, like P ∨ ~P, is called a ______.",["tautology"],"A tautology is always true.",["Check P true: P ∨ ~P is true.","Check P false: ~P is true, so still true.","Always true means tautology."]))
S.append(txt(t,2,0.2,"A statement that is false in every row of its truth table, like P ∧ ~P, is called a ______.",["contradiction"],"A contradiction is always false.",["P and ~P cannot both be true.","So P ∧ ~P is false in every row.","That is a contradiction."]))
S.append(mcq(t,2,0.4,"Given P → Q is true and Q is true. What can you conclude about P?","Nothing; P may be true or false",["P is true","P is false","P → Q must be false"],"A true Q is consistent with P true or false: affirming the consequent is invalid.",["With Q true, P → Q is true whatever P is.","So P can be T or F.","No conclusion follows."]))
S.append(mcq(t,2,0.4,"Premises: P → Q and ~P. Which conclusion follows validly?","None of the usual conclusions (~Q is not forced)",["~Q","Q","P"],"Denying the antecedent proves nothing about Q.",["Try P = F, Q = T: both premises true.","Then ~Q is false, so ~Q is not forced.","Q is also not forced (Q = F works)."]))
S.append(mcq(t,3,1.0,"Which is the correct translation of \"The relay clicks only if the switch is closed\"? (R = relay clicks, S = switch closed)","R → S",["S → R","R ↔ S","R ∧ S"],"\"Only if\" points to the necessary condition: the click needs the closed switch.",["If the relay clicks, the switch must have been closed.","So R is the \"if\" part: R → S.","Misconception: \"only if\" does not mean S → R."]))
S.append(mcq(t,3,1.1,"Translate: \"The lamp is lit if the switch is closed.\" (L = lamp lit, S = switch closed)","S → L",["L → S","L ∧ S","S ∨ L"],"A plain \"if\" introduces the condition: closed switch is sufficient for a lit lamp.",["\"X if Y\" means Y → X.","Y is the closed switch.","So S → L."]))
S.append(mcq(t,2,0.3,"Translate \"P and Q are not both true.\"","~(P ∧ Q)",["~P ∧ ~Q","~P ∨ ~Q ∨ P","P ∨ Q"],"\"Not both\" negates the whole AND.",["Put the bar over the entire P ∧ Q.","Neither P nor Q would be ~P ∧ ~Q (both false), which is stronger.","~(P ∧ Q) = ~P ∨ ~Q by De Morgan."]))
S.append(mcq(t,2,0.2,"Let D = battery is dead, S = switch is open, L = lamp is off. \"If the battery is dead or the switch is open, then the lamp is off.\"","(D ∨ S) → L",["D ∨ (S → L)","(D → S) ∨ L","D ∨ S ∨ L"],"The \"if\" part contains the OR group.",["The comma after \"open\" marks the end of the if-part.","The if-part is D ∨ S.","So (D ∨ S) → L."]))
S.append(mcq(t,3,1.3,"Let D = battery is dead, S = switch is open, L = lamp is off. \"The lamp is off only if the battery is dead or the switch is open.\"","L → (D ∨ S)",["(D ∨ S) → L","L ↔ (D ∨ S)","L ∧ (D ∨ S)"],"\"Only if\" puts the lamp-off on the if side.",["Lamp off needs a cause: D or S.","So L implies D ∨ S.","(D ∨ S) → L is the converse."]))
S.append(mcq(t,2,0.4,"Let L = lamp is on, S = switch is closed, B = battery is charged. \"The lamp is on if and only if the switch is closed and the battery is charged.\"","L ↔ (S ∧ B)",["L → (S ∧ B)","(L ↔ S) ∧ B","L ∨ (S ∧ B)"],"\"If and only if\" is ↔; the group S ∧ B sits on the right.",["\"If and only if\" is the double arrow.","Both conditions (S and B) are grouped.","So L ↔ (S ∧ B)."]))
S.append(mcq(t,1,-0.5,"Two switches are wired in series with a lamp. In logic, the lamp is on when:","A ∧ B (both closed)",["A ∨ B","A → B","~A ∧ ~B"],"Series switches must all be closed for current to flow, like AND.",["Current goes through A and then B.","Either one open stops it.","So both must be closed: A ∧ B."]))
S.append(mcq(t,1,-0.5,"Two switches are wired in parallel with a lamp. In logic, the lamp is on when:","A ∨ B (at least one closed)",["A ∧ B","A → B","~(A ∨ B)"],"Parallel switches give two paths; one closed path is enough.",["Current can take either branch.","One closed switch is enough.","That is OR."]))
S.append(mcq(t,2,0.5,"Switch A is in series with a parallel pair of switches B and C. The lamp is on when:","A ∧ (B ∨ C)",["(A ∧ B) ∨ C","A ∨ (B ∧ C)","(A ∨ B) ∧ C"],"The parallel pair works like OR, and the series link with A works like AND.",["B and C in parallel: B ∨ C.","That block is in series with A: AND.","A ∧ (B ∨ C)."]))
S.append(mcq(t,2,0.7,"Switches A and B in series form one branch. A switch C forms a second branch in parallel with it. The lamp is on when:","(A ∧ B) ∨ C",["A ∧ (B ∨ C)","A ∨ B ∨ C","(A ∨ B) ∧ C"],"Each branch is a way for current to flow: either A and B both closed, or C closed.",["Branch 1 works if A ∧ B.","Branch 2 works if C.","Parallel branches: OR of the two."]))
S.append(mcq(t,3,1.0,"Proof lines: 1. A → B (P)  2. B → C (P)  3. A (P)  4. B (MP 1,3)  5. C (?). The reason for line 5 is:","MP, lines 2 and 4",["HS, lines 1 and 2","MP, lines 1 and 3","MT, lines 2 and 4"],"Line 5 uses B → C and B, which is modus ponens.",["Need an if-then and its antecedent.","Line 2 is B → C and line 4 gives B.","That is MP. HS would give A → C, not C."]))
S.append(mcq(t,3,1.0,"Proof lines: 1. P ∨ Q (P)  2. ~P (P)  3. Q (DS 1,2)  4. Q → R (P)  5. R (?). The reason for line 5 is:","MP, lines 3 and 4",["DS, lines 1 and 4","MT, lines 3 and 4","HS, lines 3 and 4"],"Q is true (line 3) and Q → R, so R by modus ponens.",["Look for an if-then with a true antecedent.","Line 4 is Q → R and line 3 is Q.","That is MP."]))
S.append(mcq(t,3,1.6,"Proof lines: 1. ~A ∨ B (P)  2. A (P)  3. ~~A (DN 2)  4. B (?). The reason for line 4 is:","DS, lines 1 and 3",["DS, lines 1 and 2","MP, lines 1 and 2","MT, lines 1 and 3"],"Disjunctive syllogism needs the NEGATION of one side of the OR. The negation of ~A is ~~A (line 3).",["Line 1 is ~A ∨ B.","To use DS we must deny ~A, which means having ~~A.","Line 3 does that, so B follows by DS from 1 and 3."]))
assert not valid([lambda p,q:p|q, lambda p,q:p],lambda p,q:1-q,2)
S.append(mcq(t,3,1.3,"P ∨ Q, P ∴ ~Q. Is this argument valid?","Invalid: both P and Q can be true",["Valid by disjunctive syllogism","Valid by modus ponens","Valid by modus tollens"],"The OR here is inclusive, so P true does not make Q false.",["Try P = T, Q = T.","Both premises are true.","The conclusion ~Q is false, so the argument fails."]))
assert valid([lambda p,q:1-(p&q), lambda p,q:p],lambda p,q:1-q,2)
S.append(mcq(t,3,1.6,"~(P ∧ Q), P ∴ ~Q. Is this argument valid?","Valid",["Invalid: Q could be true","Invalid: needs P ∨ Q","Valid only if Q is false already"],"~(P ∧ Q) is ~P ∨ ~Q by De Morgan; with P true, ~P is false, so ~Q.",["De Morgan: ~P ∨ ~Q.","P is true, so ~P is false.","Disjunctive syllogism leaves ~Q."]))
assert valid([lambda p,q,r:imp(p,q), lambda p,q,r:imp(1-p,r)],lambda p,q,r:q|r,3)
S.append(mcq(t,3,2.0,"P → Q and ~P → R. Does Q ∨ R follow?","Yes; either P or ~P is true, so Q or R",["No; P might be false","No; the premises share no letter","Only if Q and R are both true"],"Constructive dilemma with P ∨ ~P (a tautology) as the third premise.",["P ∨ ~P is always true.","If P, then Q. If ~P, then R.","So Q ∨ R in every case."]))
assert valid([lambda p,q,r:imp(p,imp(q,r)), lambda p,q,r:p, lambda p,q,r:q],lambda p,q,r:r,3)
S.append(mcq(t,3,1.4,"Premises: P → (Q → R), P, Q. Which conclusion follows?","R",["Q → R only, not R","~R","P → R"],"MP on P gives Q → R; MP again with Q gives R.",["P → (Q → R) and P give Q → R (MP).","Q → R and Q give R (MP).","Two modus ponens steps."]))
assert not valid([lambda p,q,r:imp(p&q,r), lambda p,q,r:p],lambda p,q,r:r,3)
S.append(mcq(t,3,1.5,"(P ∧ Q) → R and P. Is R a valid conclusion?","No; Q is not known to be true",["Yes, by modus ponens","Yes, by conjunctive elimination","Yes, by modus tollens"],"The if-part needs P AND Q. Knowing only P is not enough.",["MP needs the whole antecedent P ∧ Q.","Try P = T, Q = F, R = F.","Premises true, conclusion false: invalid."]))
assert not valid([lambda p,q,r:imp(p,q),lambda p,q,r:imp(r,q),lambda p,q,r:q],lambda p,q,r:p|r,3)
S.append(mcq(t,3,1.8,"P → Q, R → Q, Q ∴ P ∨ R. Is this valid?","Invalid (affirming the consequent)",["Valid (constructive dilemma)","Valid (modus ponens)","Valid (hypothetical syllogism)"],"Q can be true for a third reason, with P and R both false.",["Constructive dilemma needs P ∨ R as a premise, not Q.","Try P = F, R = F, Q = T.","All premises true, conclusion false."]))
assert valid([lambda p,q,r:imp(p,q),lambda p,q,r:imp(p,r)],lambda p,q,r:imp(p,q&r),3)
S.append(mcq(t,3,1.8,"P → Q and P → R. Which conclusion follows?","P → (Q ∧ R)",["(Q ∧ R) → P","P → (Q ∨ R) only","Q ↔ R"],"If P is true, both Q and R must be true.",["Assume P.","Then Q by the first premise and R by the second.","So P → (Q ∧ R). The converse does not follow."]))
S.append(mcq(t,3,1.0,"Premises: A → B and B → C. Which extra premise lets you conclude C?","A",["~A","C → A","~C"],"HS gives A → C; then A and modus ponens give C.",["Chain: A → C.","Need A to be true to reach C.","~C would instead lead to ~A by modus tollens."]))
S.append(mcq(t,3,2.0,"From A → C, B → C and A ∨ B you get C ∨ C. Which identity lets you write just C?","P ∨ P = P (tautology)",["Double negation","De Morgan","Commutation"],"Repeating the same statement in an OR adds nothing.",["Constructive dilemma gives C ∨ C.","C or C is true exactly when C is.","This is the tautology rule P ∨ P = P."]))
for (txtq,fn,tv) in [("(A → B) ∨ C",lambda a,b,c:imp(a,b)|c,(1,0,1)),("~(A ∧ B) → C",lambda a,b,c:imp(1-(a&b),c),(1,1,0)),("(A ∨ B) → (A ∧ B)",lambda a,b,c:imp(a|b,a&b),(1,0,0)),("~(A → B) ∨ ~C",lambda a,b,c:(1-imp(a,b))|(1-c),(0,1,1))]:
    pass
cases=[("(A → B) ∨ C",lambda a,b,c:imp(a,b)|c,(1,0,1),2,0.4),("~(A ∧ B) → C",lambda a,b,c:imp(1-(a&b),c),(1,1,0),2,0.6),("(A ∨ B) → (A ∧ B)",lambda a,b,c:imp(a|b,a&b),(1,0,0),3,0.9),("~(A → B) ∨ ~C",lambda a,b,c:(1-imp(a,b))|(1-c),(0,1,1),3,1.1)]
for s,fn,v,l,b in cases:
    r=fn(*v)
    S.append(num(t,l,b,"Let A = %s, B = %s, C = %s (1 = true, 0 = false). Find the value of %s. Give 1 or 0."%(*v,s),r,"Evaluate the inside parts first, then the connectives in order.",["Substitute the values.","Work out each smaller piece.","Combine to get %d."%r]))
order_=order(t,3,1.2,"Put the proof of ~Q from the premises ~(P ∨ Q) in order.",["~(P ∨ Q)  (premise)","~P ∧ ~Q  (De Morgan)","~Q  (conjunctive elimination)"],"Break the bar with De Morgan, then pull out the part you need.",["Start with the premise.","De Morgan turns ~(P ∨ Q) into ~P ∧ ~Q.","Conjunctive elimination keeps ~Q."])
S.append(order_)
S.append(order(t,3,1.2,"Put these proof lines in order to prove R from P → Q, Q → R and P.",["P → Q (premise)","Q → R (premise)","P → R (HS)","P (premise)","R (MP)"],"Chain the conditionals first, then apply modus ponens with P.",["Premises first.","HS joins P → Q and Q → R into P → R.","MP with P gives R."]))
S.append(match(t,2,0.2,"Match each rule to its pattern.",[["Conjunctive elimination","P ∧ Q ∴ P"],["Conjunctive addition","P, Q ∴ P ∧ Q"],["Disjunctive addition","P ∴ P ∨ Q"],["Double negation","~~P ∴ P"]],"Know each short pattern by sight.",["Elimination takes a part out of an AND.","Addition builds a bigger AND or OR.","Double negation removes two tildes."]))
S.append(multi(t,2,0.5,"Select ALL argument forms that are VALID.",["P → Q, P ∴ Q","P → Q, ~Q ∴ ~P","P → Q, Q ∴ P","P → Q, ~P ∴ ~Q"],[0,1],"Only modus ponens and modus tollens are valid here.",["MP and MT always work.","Affirming the consequent (third) fails when P is false and Q is true.","Denying the antecedent (fourth) fails in the same row."]))
imp_ok=[lambda p,q:imp(1-q,1-p),lambda p,q:(1-p)|q,lambda p,q:1-(p&(1-q))]
assert all(eq(f,lambda p,q:imp(p,q),2) for f in imp_ok)
assert not eq(lambda p,q:imp(q,p),lambda p,q:imp(p,q),2) and not eq(lambda p,q:imp(1-p,1-q),lambda p,q:imp(p,q),2)
S.append(multi(t,3,1.5,"Select ALL statements equivalent to P → Q.",["~Q → ~P","~P ∨ Q","~(P ∧ ~Q)","Q → P","~P → ~Q"],[0,1,2],"The contrapositive, the OR form and the negated-failure form all match P → Q. The converse and inverse do not.",["Each true option is false only in the row P = T, Q = F.","Q → P is false in the row P = F, Q = T.","~P → ~Q (inverse) is also false in that row."]))
taut=[lambda p,q:p|(1-p),lambda p,q:imp(p&q,p),lambda p,q:imp(p,p|q)]
assert all(all(rows(f,2)) for f in taut)
assert not all(rows(lambda p,q:imp(p,p&q),2)) and not all(rows(lambda p,q:imp(imp(p,q),imp(q,p)),2))
S.append(multi(t,3,1.8,"Select ALL statements that are tautologies (always true).",["P ∨ ~P","(P ∧ Q) → P","P → (P ∨ Q)","P → (P ∧ Q)","(P → Q) → (Q → P)"],[0,1,2],"Test the last two with P = T, Q = F: both come out false.",["The first three can never fail.","P → (P ∧ Q) fails at P = T, Q = F.","(P → Q) → (Q → P) fails at P = F, Q = T (P → Q true, Q → P false)."]))
S.append(mcq(t,3,1.8,"One row of the truth table shows that BOTH affirming the consequent and denying the antecedent are invalid. It is:","P false, Q true",["P true, Q false","P true, Q true","P false, Q false"],"With P false and Q true, P → Q is true, ~P is true and Q is true, yet P and ~Q are both false.",["Affirming: P → Q, Q ∴ P. Premises true, P false.","Denying: P → Q, ~P ∴ ~Q. Premises true, ~Q false.","Both break in the row P = F, Q = T."]))
S.append(mcq(t,2,0.4,"Premises: P ↔ Q and ~P. Which conclusion follows?","~Q",["Q","P","Q → P is false"],"P ↔ Q includes Q → P; with ~P, modus tollens gives ~Q.",["P ↔ Q means (P → Q) ∧ (Q → P).","Use Q → P and ~P.","Modus tollens: ~Q."]))
S.append(mcq(t,2,0.2,"\"If the circuit is shorted, the fuse blows. The fuse blew. So the circuit was shorted.\" This argument is:","invalid (affirming the consequent)",["valid (modus ponens)","valid (modus tollens)","invalid (denying the antecedent)"],"A fuse can blow for another reason, such as an overload.",["Form: S → F, F ∴ S.","That reverses modus ponens.","Another cause of F is enough to break it."]))
S.append(mcq(t,2,0.3,"\"If the switch is closed, the lamp lights. The lamp does not light. So the switch is open.\" This argument is:","valid (modus tollens)",["invalid (affirming the consequent)","invalid (denying the antecedent)","valid (modus ponens)"],"Closed switch would force a lit lamp, so an unlit lamp means the switch is not closed.",["Form: S → L, ~L ∴ ~S.","That is modus tollens.","\"Open\" means not closed."]))
assert valid([lambda a,b,c:imp(a,b),lambda a,b,c:1-b,lambda a,b,c:a|c],lambda a,b,c:c,3)
S.append(mcq(t,3,1.3,"Premises: A → B, ~B, A ∨ C. Which conclusion follows?","C",["A","B","~C"],"MT with the first two gives ~A; then DS on A ∨ C leaves C.",["A → B and ~B give ~A (modus tollens).","A ∨ C and ~A give C (disjunctive syllogism).","Two steps."]))
assert valid([lambda p,q,r:imp(p,q),lambda p,q,r:imp(q,r),lambda p,q,r:1-r],lambda p,q,r:1-p,3)
S.append(mcq(t,3,1.3,"Premises: P → Q, Q → R, ~R. Which conclusion follows?","~P",["P","Q","~Q ∧ P"],"MT with Q → R and ~R gives ~Q; MT again with P → Q gives ~P.",["~R and Q → R give ~Q.","~Q and P → Q give ~P.","Or chain HS first: P → R, then MT."]))
assert valid([lambda p,q,r:imp(p&q,r),lambda p,q,r:p,lambda p,q,r:q],lambda p,q,r:r,3)
S.append(mcq(t,3,1.0,"Premises: (P ∧ Q) → R, P, Q. To reach R you need these steps in order:","Conjunctive addition (P ∧ Q), then modus ponens",["Modus ponens, then conjunctive elimination","Disjunctive syllogism, then modus ponens","Modus tollens, then double negation"],"The antecedent is P ∧ Q, so build it from P and Q first.",["MP needs the full antecedent.","Conjunctive addition makes P ∧ Q.","Then MP with (P ∧ Q) → R."]))
assert valid([lambda p,q,r:p|q,lambda p,q,r:(1-p)|r],lambda p,q,r:q|r,3)
S.append(mcq(t,3,2.2,"P ∨ Q and ~P ∨ R. Which conclusion follows?","Q ∨ R",["Q ∧ R","P ∨ R","~Q ∨ ~R"],"If P is true, ~P is false so R is true; if P is false, Q is true. Either way Q ∨ R.",["Case P true: second premise gives R.","Case P false: first premise gives Q.","In both cases Q ∨ R. (This is the resolution rule.)"]))
S.append(txt(t,2,0.3,"Name the rule: P → Q, R → S, P ∨ R ∴ Q ∨ S.",["constructive dilemma","cd"],"If P or R holds, one of their results must hold.",["Two if-thens and an OR of their antecedents.","Conclusion is the OR of the consequents.","That is constructive dilemma."]))
S.append(mcq(t,1,-0.5,"In \"If the capacitor is charged, the LED fades,\" the antecedent is:","the capacitor is charged",["the LED fades","the capacitor is charged and the LED fades","if"],"The antecedent is the \"if\" part.",["Antecedent comes first and follows \"if\".","The consequent is what follows \"then\".","Here: capacitor charged."]))
S.append(mcq(t,3,1.0,"\"The lamp is lit only if the switch is closed.\" Which situation would make this statement FALSE?","Lamp lit, switch open",["Lamp off, switch closed","Lamp off, switch open","Lamp lit, switch closed"],"The statement forbids a lit lamp with an open switch.",["Write it as L → S.","False only when L is true and S is false.","Lamp off with a closed switch is allowed."]))
S.append(mcq(t,2,0.2,"\"If the switch is closed, the lamp is lit.\" Which situation shows this statement is FALSE?","Switch closed, lamp off",["Switch open, lamp lit","Switch open, lamp off","Switch closed, lamp lit"],"A true if-part with a false then-part breaks the promise.",["The promise is: closed switch means lit lamp.","Only a closed switch with an unlit lamp breaks it.","An open switch does not test the promise."]))
S.append(num(t,1,-0.4,"In how many of the 4 rows of a truth table is P → Q true?",3,"It is false only for P = T, Q = F.",["Four rows for two letters.","One row is false.","3 rows true."]))
S.append(mcq(t,3,1.7,"A student says: \"P ∨ Q and ~P ∴ Q is valid, so P ∨ Q and Q ∴ ~P must be valid too.\" What is wrong?","The OR is inclusive, so Q true does not rule out P",["Nothing, both are valid","Disjunctive syllogism needs three premises","~P is not a legal conclusion in any proof"],"DS denies one side to get the other. Affirming one side proves nothing about the other.",["Try P = T, Q = T.","Premises P ∨ Q and Q are true.","~P is false, so the argument fails."]))
SYM=S
