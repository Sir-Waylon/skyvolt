import random,math,itertools
R=random.Random(2027);OUT=[]
def S(t,l,fp,q,v,u,w,tol=0.02):OUT.append({'t':t,'l':l,'fp':fp,'type':'short','q':q,'num':dict(v=v,tol=tol,**({'u':u} if u else {})),'w':w})
def uniq(fn,n,key=lambda x:x):
    seen=set();k=0
    while len(seen)<n and k<400:
        k+=1;x=fn()
        if x is None:continue
        s=key(x)
        if s in seen:continue
        seen.add(s);yield x
def g(x,s=3):return ('%.*g'%(s,x))
SUPD=str.maketrans('-0123456789','⁻⁰¹²³⁴⁵⁶⁷⁸⁹')
def sci(x):
    e=int(math.floor(math.log10(abs(x))));m=x/10**e;return '%.2f×10%s'%(m,str(e).translate(SUPD))
k=8.99e9
# static
for q1,q2,r in uniq(lambda:(R.choice([1,2,3,4,5,6,8]),R.choice([2,3,4,5,7,9]),R.choice([5,10,20,30,40,50])),22):
    F=k*q1*1e-6*q2*1e-6/(r/100)**2
    S('static',2,'cou1','Two point charges, %d µC and %d µC, are %d cm apart. Find the electric force between them in newtons.'%(q1,q2,r),F,'N','F = kq₁q₂/r². Convert µC to C and cm to m first: F = %s N.'%sci(F))
for q,F in uniq(lambda:(R.choice([1,2,3,4,5,6,8,10]),R.choice([0.02,0.05,0.12,0.4,1.5,3.0,6.0])),16,key=lambda x:x):
    S('static',2,'efld','A %d µC test charge feels a force of %g N in an electric field. Find the field strength.'%(q,F),F/(q*1e-6),'N/C','E = F/q = %g / (%d×10⁻⁶) = %s N/C.'%(F,q,sci(F/(q*1e-6))))
for I,t in uniq(lambda:(R.choice([0.2,0.5,1.5,2,3,4,6]),R.choice([10,20,30,45,60,90,120])),16):
    S('static',1,'qit','A %g A current flows for %d s. How much charge passes?'%(I,t),I*t,'C','Q = I·t = %g × %d = %g C.'%(I,t,I*t))
for d,m in uniq(lambda:(R.choice([2,3,4,5]),R.choice([2,3,4,6])),12):
    OUT.append({'t':'static','l':2,'fp':'cou-scale','type':'short','q':'Two charges attract with a force F. One charge is multiplied by %d and the distance is multiplied by %d. The new force is F times what number? (Give a decimal.)'%(m,d),'num':{'v':m/d**2,'tol':0.02},'w':'F ∝ q/r², so the factor is %d/%d² = %s.'%(m,d,g(m/d**2))})
# dcac
for f in [25,50,60,100,120,400,500,1000]:
    S('dcac',1,'per','A signal has a frequency of %d Hz. Find its period in milliseconds.'%f,1/f,'ms','T = 1/f = 1/%d s = %s ms.'%(f,g(1000/f)))
for v in [100,120,170,208,230,311,340]:
    S('dcac',2,'rms','An AC supply has a peak voltage of %d V. Find the RMS voltage.'%v,v/math.sqrt(2),'V','V_rms = V_peak/√2 = %s V.'%g(v/math.sqrt(2)))
for n,v in uniq(lambda:(R.choice([2,3,4,6,8,10]),R.choice([1.2,1.5,2.0,3.7,9.0])),14):
    S('dcac',1,'cells','%d identical %g V cells are connected in series, plus to minus. Find the total voltage.'%(n,v),n*v,'V','Series cells add: %d × %g = %g V.'%(n,v,n*v))
for f in [2,3,4,5,8,10]:
    OUT.append({'t':'dcac','l':3,'fp':'lineloss','type':'short','q':'A power line carries the same power but the voltage is raised by a factor of %d, so the current falls by %d. The heat lost in the line (I²R) becomes 1/N of the original. Find N.'%(f,f),'num':{'v':f*f,'tol':0},'w':'Loss ∝ I². Current ÷ %d means loss ÷ %d.'%(f,f*f)})
for V,P in uniq(lambda:(R.choice([120,12,24,230]),R.choice([60,100,240,600,1200,1800])),12):
    I=P/V
    S('dcac',1,'ipv','A %d W appliance runs on %d V. Find the current it draws.'%(P,V),I,'A','I = P/V = %d/%d = %s A.'%(P,V,g(I)))
# ctrl
std=[1,2,3,5,7.5,10,15,20,25,30,40,50]
for P,V in uniq(lambda:(R.choice([24,36,60,90,100,120,150,180,240]),R.choice([12,24])),16):
    I=P/V;f=[x for x in std if x>=I][0]
    OUT.append({'t':'ctrl','l':2,'fp':'fuse','type':'short','q':'A %d V DC load uses %d W. Which is the smallest standard fuse (1, 2, 3, 5, 7.5, 10, 15, 20, 25, 30, 40, 50 A) that will not blow in normal use? Answer in amps.'%(V,P),'num':{'v':f,'tol':0},'w':'I = P/V = %s A. The next rating at or above that is %g A.'%(g(I),f)})
for br,P in uniq(lambda:(R.choice([15,20]),R.choice([40,60,75,100,150,200])),12):
    OUT.append({'t':'ctrl','l':2,'fp':'brk','type':'short','q':'How many %d W bulbs on a 120 V line can run together before a %d A breaker trips? (Largest whole number that does not exceed the limit.)'%(P,br),'num':{'v':int(120*br/P),'tol':0},'w':'Capacity = 120 × %d = %d W. %d/%d = %s, so %d bulbs.'%(br,120*br,120*br,P,g(120*br/P),int(120*br/P))})
# kirchhoff
def kir():
    I1,I2=R.choice([1,2,3,4,5]),R.choice([1,2,3,4,5]);I3=I1+I2
    R1,R2,R3=R.choice([1,2,3,4]),R.choice([1,2,3,4]),R.choice([1,2,3,5])
    return I1,I2,I3,R1,R2,R3
for I1,I2,I3,R1,R2,R3 in uniq(kir,12,key=lambda x:x[3:]+x[:2]):
    E1=I1*R1+I3*R3;E2=I2*R2+I3*R3
    S('kirch',3,'k2loop','Two batteries share a middle branch. Left: E₁ = %d V with R₁ = %d Ω. Right: E₂ = %d V with R₂ = %d Ω. The shared branch has R₃ = %d Ω. Find the current in R₃.'%(E1,R1,E2,R2,R3),I3,'A','Let I₃ = I₁ + I₂. KVL left: %d = %dI₁ + %dI₃. KVL right: %d = %dI₂ + %dI₃. Solving gives I₃ = %d A.'%(E1,R1,R3,E2,R2,R3,I3))
for a,b,c in uniq(lambda:(R.choice([2.0,3.5,4.2,5.0,6.5,8.0]),R.choice([1.0,1.5,2.5,3.0,4.0]),R.choice([0.5,1.2,2.0,2.5,3.2])),14):
    S('kirch',1,'kcl','At a junction, %g A and %g A flow in. One wire carries %g A out. Find the current in the remaining wire that leaves the junction.'%(a,b,c),a+b-c,'A','KCL: in = out. %g + %g = %g + I, so I = %s A.'%(a,b,c,g(a+b-c)),tol=0.02) if a+b>c else None
for E,x,y in uniq(lambda:(R.choice([9,12,15,20,24,30]),R.choice([2,3,4,5,6]),R.choice([1,2,3,4,5])),14):
    if x+y<E:S('kirch',1,'kvl','A %d V battery drives a series loop with three resistors. Two of them drop %d V and %d V. Find the voltage across the third.'%(E,x,y),E-x-y,'V','KVL: %d = %d + %d + V₃, so V₃ = %d V.'%(E,x,y,E-x-y))
# diode
std5=[100,120,150,180,220,270,330,390,470,560,680,820,1000]
for Vs,Vf,I in uniq(lambda:(R.choice([5,9,12,3.3]),R.choice([1.8,2.0,2.1,3.0,3.2]),R.choice([5,10,15,20])),16):
    if Vs-Vf<=0.5:continue
    r=(Vs-Vf)/(I/1000)
    if r>1000:continue
    f=[x for x in std5 if x>=r][0]
    OUT.append({'t':'diode','l':3,'fp':'ledstd','type':'short','q':'An LED with a %g V forward drop must carry no more than %d mA from a %g V supply. Which is the smallest safe standard resistor (%s Ω)? Answer in ohms.'%(Vf,I,Vs,', '.join(map(str,std5))),'num':{'v':f,'tol':0,'u':'Ω'},'w':'R = (%g − %g)/%g A = %s Ω. Round UP to %d Ω so the current stays under the limit.'%(Vs,Vf,I/1000,g(r),f)})
for Vs,n,R_ in uniq(lambda:(R.choice([3.0,5.0,9.0,12.0]),R.choice([1,2,3]),R.choice([47,100,220,330,470,1000])),12):
    I=(Vs-0.7*n)/R_
    if I<=0.001:continue
    S('diode',2,'sidiode','A %g V supply is connected through %d silicon diode%s in series (0.7 V drop each, forward biased) and a %d Ω resistor. Find the current in milliamps.'%(Vs,n,'' if n==1 else 's',R_),I*1000,'mA','Diode drops add: %g V. I = (%g − %g)/%d = %s mA.'%(0.7*n,Vs,0.7*n,R_,g(I*1000)))
# logic/binary
for a,b in uniq(lambda:(R.randint(5,60),R.randint(5,60)),16):
    OUT.append({'t':'logic','l':2,'fp':'binadd','type':'short','q':'Add in binary: %s + %s. Give the result in binary.'%(bin(a)[2:],bin(b)[2:]),'text':[bin(a+b)[2:]],'w':'%d + %d = %d = %s in binary.'%(a,b,a+b,bin(a+b)[2:])})
for n in uniq(lambda:R.randint(20,250),14):
    OUT.append({'t':'logic','l':2,'fp':'dec2bin','type':'short','q':'Convert decimal %d to binary.'%n,'text':[bin(n)[2:]],'w':'%d = %s in binary.'%(n,bin(n)[2:])})
for n in uniq(lambda:R.randint(30,255),10):
    OUT.append({'t':'logic','l':2,'fp':'bits','type':'short','q':'What is the smallest number of bits needed to write the decimal number %d?'%n,'num':{'v':n.bit_length(),'tol':0},'w':'2^%d = %d ≤ %d < 2^%d, so %d bits.'%(n.bit_length()-1,2**(n.bit_length()-1),n,n.bit_length(),n.bit_length())})
exprs=[('A + B·C',lambda A,B,C:A|(B&C)),("A·B + C′",lambda A,B,C:(A&B)|(1-C)),("(A + B)·C",lambda A,B,C:(A|B)&C),("A ⊕ B ⊕ C",lambda A,B,C:A^B^C),("A·B′ + B·C′",lambda A,B,C:(A&(1-B))|(B&(1-C))),("(A·B)′ + C",lambda A,B,C:(1-(A&B))|C),("A′·B′·C′ + A·B·C",lambda A,B,C:((1-A)&(1-B)&(1-C))|(A&B&C)),("(A + B′)·(B + C′)",lambda A,B,C:(A|(1-B))&(B|(1-C)))]
for s,f in exprs:
    n=sum(f(*x) for x in itertools.product([0,1],repeat=3))
    OUT.append({'t':'logic','l':3,'fp':'tt-count','type':'short','q':'For how many of the 8 input combinations of A, B, C is Y = %s equal to 1?'%s,'num':{'v':n,'tol':0},'w':'Check each of the 8 rows: %d rows give Y = 1.'%n})
for n in [2,3,4,5,6,7,8]:
    OUT.append({'t':'logic','l':1,'fp':'mux','type':'short','q':'How many select lines does a %d:1 multiplexer need? (Round up to a whole number.)'%(2**n if n<=5 else 2**n),'num':{'v':n,'tol':0},'w':'2^%d = %d inputs, so %d select lines.'%(n,2**n,n)})
# virpe/hands
for Vk,Rk,Vx in uniq(lambda:(R.choice([1.0,2.0,3.0,4.5]),R.choice([100,220,330,470,1000,2200]),R.choice([2.0,3.0,4.0,6.0,7.5])),14):
    S('hands',3,'mystery','Mystery resistor: a known %d Ω resistor is in series with Rx. A voltmeter reads %g V across the known resistor and %g V across Rx. Find Rx.'%(Rk,Vk,Vx),Rk*Vx/Vk,'Ω','Same series current: Rx = %d × %g/%g = %s Ω.'%(Rk,Vx,Vk,g(Rk*Vx/Vk)))
for Wh,P,eta in uniq(lambda:(R.choice([9.25,11.55,15.4,18.5,27.0]),R.choice([5,10,12,18,20,45]),R.choice([1.0,0.8,0.9])),14):
    t=Wh/(P*eta)
    S('hands',3,'usb','A %g Wh battery is charged from a %d W charger that is %d%% efficient. How many hours does a full charge take?'%(Wh,P,round(eta*100)),t*3600,'h','t = Wh ÷ (P × efficiency) = %g ÷ (%d × %g) = %s h.'%(Wh,P,eta,g(t)))
# magnetism/capacitance (adjacent)
for Np,Ns,V in uniq(lambda:(R.choice([100,200,400,500,1000]),R.choice([25,50,100,250,600]),R.choice([12,24,120,240])),12):
    S('mag',2,'xfmr','An ideal transformer has %d primary turns and %d secondary turns. The primary is connected to %d V AC. Find the secondary voltage.'%(Np,Ns,V),V*Ns/Np,'V','Vs = Vp × Ns/Np = %d × %d/%d = %s V.'%(V,Ns,Np,g(V*Ns/Np)))
for C,V in uniq(lambda:(R.choice([10,22,47,100,220,470]),R.choice([3,5,9,12,16])),14):
    S('cap',3,'cap-e','A %d µF capacitor is charged to %d V. Find the energy stored in millijoules.'%(C,V),0.5*C*1e-6*V*V,'mJ','E = ½CV² = 0.5 × %d×10⁻⁶ × %d² = %s mJ.'%(C,V,g(0.5*C*V*V/1000)))
for a,b in uniq(lambda:(R.choice([1,2,3,4,6,10,12]),R.choice([2,3,4,6,12,20])),10):
    S('cap',2,'cap-s','Capacitors of %d µF and %d µF are connected in series. Find the equivalent capacitance in microfarads.'%(a,b),a*b/(a+b)*1e-6,'µF','1/C = 1/%d + 1/%d, so C = %s µF.'%(a,b,g(a*b/(a+b))))
if __name__=='__main__':
    import collections;print(len(OUT),collections.Counter(q['t'] for q in OUT))
