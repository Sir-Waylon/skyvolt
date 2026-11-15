import json,sys
M={'circuit':{"Ohm's Law":'ohm','Distance is squared':'coul','Series':'sp','Parallel':'sp','AND, OR, NOT':'gate','Forward bias':'diode','Reverse bias':'diode'},
'geo':{'Angle sum in a triangle':'tri','Parallel lines and a transversal':'par','Pythagorean theorem':'pyth','Inscribed angles':'insc','Slope-intercept form':'line','Slope':'line','Perimeter and area':'scale','Similar solids':'scale','Reflection':'trn','Rotation':'trn'}}
p=json.load(open(sys.argv[1]));m=M[sys.argv[2]];n=0
for u in p['units']:
    for L in u['lessons']:
        for c in L['cards']:
            if c['h'] in m:c['lab']=m[c['h']];n+=1
json.dump(p,open(sys.argv[1],'w'),ensure_ascii=False,separators=(',',':'));print('labs',n)
