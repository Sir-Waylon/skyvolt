import json
OUT="/tmp/claude-0/-home-claude/bdb1ee03-0916-54eb-a354-ea75cf26b960/scratchpad/audit/out/m2.json"
new=[]; n=[0]
def fp():
    n[0]+=1; return f"m2_{n[0]:03d}"
def mcq(t,l,b,q,o,w,sol): new.append(dict(t=t,l=l,b=b,type="mcq",q=q,o=o,w=w,sol=sol,fp=fp()))
def multi(t,l,b,q,o,a,w,sol): new.append(dict(t=t,l=l,b=b,type="multi",q=q,o=o,a=a,w=w,sol=sol,fp=fp()))
def num(t,l,b,q,v,u,w,sol,tol=0.02): new.append(dict(t=t,l=l,b=b,type="short",q=q,num=dict(v=v,tol=tol,u=u),w=w,sol=sol,fp=fp()))
def txt(t,l,b,q,text,w,sol): new.append(dict(t=t,l=l,b=b,type="short",q=q,text=text,w=w,sol=sol,fp=fp()))
def order(t,l,b,q,items,w,sol): new.append(dict(t=t,l=l,b=b,type="order",q=q,items=items,w=w,sol=sol,fp=fp()))
def match(t,l,b,q,pairs,w,sol): new.append(dict(t=t,l=l,b=b,type="match",q=q,pairs=pairs,w=w,sol=sol,fp=fp()))

U="upper"
mcq(U,1,-0.5,"About how high above sea level is the 500 mb level?",
 ["About 5.5 km (18,000 ft)","About 1.5 km","About 3 km","About 9 km"],
 "Half the air's weight is below 500 mb, so it sits around 5.5 km up.",
 ["Pressure is the weight of the air stack above you. Climb until half the stack is below you and you are near 500 mb.","Half the atmosphere's mass lies below about 5.5 km, so 500 mb (half of ~1000 mb) is there.","Memory ladder: 850 mb ≈ 1.5 km, 700 mb ≈ 3 km, 500 mb ≈ 5.5 km, 300 mb ≈ 9 km."])
order(U,1,-0.5,"Order these upper-air levels from lowest altitude to highest.",
 ["850 mb","700 mb","500 mb","300 mb"],
 "Lower pressure means higher up.",
 ["Think of a stack of blankets: the more blankets on top of you, the higher the pressure. Fewer blankets means you are higher.","So pressure number goes down as height goes up: 850, 700, 500, 300."])
num(U,2,0,"A wind barb has one flag (pennant), two long barbs and one short barb. Using 50 kt per flag, 10 kt per long barb and 5 kt per short barb, what is the wind speed in knots?",
 75,"kt","Add the pieces: 50 + 10 + 10 + 5 = 75 kt.",
 ["A barb is like Roman numerals for wind: each mark has a fixed value you add up.","Flag = 50, long barb = 10, short barb = 5.","50 + 2×10 + 5 = 75 kt."])
mcq(U,2,0,"On a wind barb, the long staff (the line the feathers attach to) points toward the direction the wind…",
 ["Comes from","Blows toward","Is strongest","Will be tomorrow"],
 "The staff points into the wind, like a weather vane pointing at the source.",
 ["A barb is like an arrow that has been flipped: the staff points to where the wind starts.","A staff pointing west with barbs means a west wind, blowing toward the east.","Common mix-up: students read it as where the air is going."])
mcq(U,2,0,"On a 500 mb map, which feature is a trough?",
 ["A dip in the height lines, bending toward lower heights","A bulge in the height lines toward the north","A closed ring of the highest temperatures","A straight east-west line"],
 "Troughs are valleys in the wave pattern at 500 mb.",
 ["Picture a rope wiggling in the wind. The low dip is a trough and the high bump is a ridge.","Troughs bring rising air and unsettled weather ahead of them. Ridges bring sinking, warmer, drier air."])
mcq(U,3,0.9,"A 500 mb trough is moving east across Kansas. Where is the large-scale lift strongest?",
 ["Ahead of (east of) the trough axis","Behind (west of) the trough axis","Directly under a ridge axis","Only at the surface high"],
 "Air spreading apart aloft downstream of a trough pulls air upward.",
 ["Think of a crowd leaving a stadium: if the exit spreads out ahead, people from behind are pulled forward. Air aloft ahead of a trough spreads out and pulls air up from below.","That rising air cools and makes clouds and storms, so the weather turns stormy before the trough arrives.","Behind the trough, air sinks and skies clear."])
num(U,2,0,"The surface air is 30 °C and the dew point is 18 °C. Use LCL ≈ 125 m × (T − Td). A dry parcel cools 10 °C per km up to the LCL. What is the parcel's temperature at the cloud base, in °C?",
 15,"°C","LCL = 1.5 km, and the parcel cools 15 °C on the way up.",
 ["First find the cloud base: 125 × 12 = 1500 m = 1.5 km.","A rising parcel cools 10 °C per km while it is dry: 1.5 × 10 = 15 °C of cooling.","30 − 15 = 15 °C. Notice the dew point fell to about the same value: that is why the cloud forms."])
num(U,3,1.2,"Surface T = 30 °C, Td = 18 °C. A parcel rises to the cloud base (LCL = 125 m × spread, cooling 10 °C/km) and then keeps rising, cooling 6 °C per km inside cloud. What is its temperature at 4 km above the ground, in °C?",
 0,"°C","Two stages: 15 °C at 1.5 km, then 2.5 km × 6 °C = 15 °C more of cooling.",
 ["Stage 1 (dry): LCL = 125 × 12 = 1500 m. Parcel cools 1.5 × 10 = 15 °C, so it is 15 °C at 1.5 km.","Stage 2 (cloudy): condensation releases heat like a tiny heater, so the parcel cools slower: 6 °C per km. From 1.5 to 4 km is 2.5 km, so 2.5 × 6 = 15 °C.","15 − 15 = 0 °C. Common error: using 10 °C per km all the way gives −10 °C."],tol=0.05)
num(U,2,0.3,"A surface temperature is 35 °C and the dew point is 20 °C. Estimate the cloud base (LCL) height in meters using 125 m per °C of spread.",
 1875,"m","Spread = 15 °C and 15 × 125 = 1875 m.",
 ["The LCL grows with the gap between T and Td. A big gap means dry air, so the parcel must rise far before it saturates.","Spread = 35 − 20 = 15 °C.","15 × 125 = 1,875 m."])
num(U,3,1.0,"A storm chaser sees a cloud base at 2,000 m. The surface temperature is 33 °C. Using LCL = 125 m × (T − Td), what is the surface dew point in °C?",
 17,"°C","Work backward: 2000 ÷ 125 = 16 °C of spread.",
 ["The formula can run backward. Spread = LCL ÷ 125 = 2000 ÷ 125 = 16 °C.","Td = T − spread = 33 − 16 = 17 °C.","A cloud base this high means fairly dry surface air, a hint of hail or wind more than tornadoes."])
mcq(U,2,0.3,"A lifted parcel is 8 °C at 3 km. The surrounding air at 3 km is 3 °C. What happens next?",
 ["The parcel is warmer, so it keeps rising","The parcel is colder, so it sinks","Nothing: temperatures do not matter","The parcel stops because it is saturated"],
 "A parcel warmer than its surroundings is lighter and keeps accelerating upward.",
 ["Think of a hot-air balloon: it rises because the air inside is warmer, hence lighter, than the air outside.","Compare the parcel to the environment at the same height. 8 °C is warmer than 3 °C, so it is buoyant.","CAPE adds up this warmth advantage over the whole climb."])
mcq(U,3,1.0,"The air around you cools 4 °C per km with height. A dry parcel you push upward cools 10 °C per km. What happens if you lift it and let go?",
 ["It becomes colder than its surroundings and sinks back (stable)","It becomes warmer than its surroundings and keeps rising","It stays at the same temperature","It turns into a cloud immediately"],
 "A parcel that cools faster than the surroundings ends up heavier than them.",
 ["Race two cars down a hill: the environment cools slowly (4 °C/km), the parcel cools fast (10 °C/km), so the parcel falls behind in temperature.","After 1 km: parcel −10 °C, environment −4 °C, so the parcel is 6 °C colder and denser.","Colder, denser air sinks. That is stable air, like a ball in a bowl."])
mcq(U,3,1.4,"The air around you cools 8 °C per km. A dry parcel cools 10 °C per km, but a saturated (cloudy) parcel only cools 6 °C per km. This layer is called…",
 ["Conditionally unstable: stable when dry, unstable once saturated","Absolutely stable","Absolutely unstable","An inversion"],
 "The environment lapse rate lies between the dry and saturated rates.",
 ["Dry parcel: cools faster (10) than the air (8), so it ends up colder and sinks. Stable.","Saturated parcel: cools slower (6) than the air (8), so it ends up warmer and rises. Unstable.","So the answer depends on a condition: whether the parcel is saturated. That is why this is the most common severe-weather setup."])
mcq(U,3,1.2,"A hot summer afternoon: the air right above a parking lot cools 11 °C per km with height. Compared with the 10 °C/km dry parcel rate, this is…",
 ["Absolutely unstable: a lifted dry parcel stays warmer than its surroundings","Absolutely stable","An inversion","Conditionally unstable only"],
 "Environment cooling faster than 10 °C/km makes any lifted parcel buoyant.",
 ["After 1 km a dry parcel is 10 °C cooler but the air is 11 °C cooler, so the parcel is 1 °C warmer than its surroundings and keeps rising.","This only happens near very hot ground and is the reason dust devils form.","Think of a hot stovetop under a pot of water: the bottom layer is too hot to stay put."])
num(U,2,0.3,"A sounding shows 16 °C at 1.5 km (850 mb) and −12 °C at 5.5 km (500 mb). What is the average lapse rate in °C per km?",
 7,"°C/km","Cooling of 28 °C over a 4 km climb is 7 °C per km.",
 ["Lapse rate = temperature drop ÷ height climbed.","Drop = 16 − (−12) = 28 °C. Careful with the negative sign.","Height = 5.5 − 1.5 = 4 km, so 28 ÷ 4 = 7 °C/km, a little steeper than the 6.5 average."])
mcq(U,2,0,"The temperatures at the surface, 1 km, and 2 km are 24 °C, 27 °C, and 20 °C. Which layer is an inversion?",
 ["Surface to 1 km","1 km to 2 km","Surface to 2 km as a whole","There is no inversion"],
 "An inversion is any layer where temperature goes UP with height.",
 ["Look at each layer separately, not the total: 24 → 27 °C is a rise, so that layer is an inversion.","1 → 2 km: 27 → 20 is a normal drop.","A thin inversion like this acts like a lid (a cap) on rising parcels."])
mcq(U,2,0.2,"What does CIN (convective inhibition) measure on a sounding?",
 ["The energy barrier a parcel must overcome to rise freely","The total rainfall expected","The amount of wind shear","The maximum hail size"],
 "CIN is the 'speed bump' energy: how strong the cap is.",
 ["Picture a ball that must be pushed over a hill before it rolls down the other side. CIN is the height of that hill, CAPE is the drop after it.","Large CIN (a strong cap) means storms need a strong trigger, like a front or dryline.","CIN is measured in J/kg, just like CAPE."])
mcq(U,3,1.0,"A morning sounding shows large CAPE and a strong cap. By afternoon the sun heats the ground 8 °C. How can this lead to explosive storms?",
 ["Heated surface parcels can break through the cap, releasing the stored CAPE all at once","Heating removes CAPE","Heating makes the air stable","Heating makes the wind shear zero"],
 "A strong cap stores energy until a warmer parcel finally pushes through.",
 ["Think of a shaken soda with a lid: pressure builds, and when the lid pops it all comes out at once.","Warmer surface parcels need less lift to reach the temperature of the air above the cap.","This 'loaded gun' setup gives few storms, but the ones that do form can be violent."])
mcq(U,3,1.0,"Forecasters call a sounding with a lot of CAPE under a strong cap a 'loaded gun.' Why?",
 ["Few storms form, but any that break the cap can be violent","Storms are certain by noon","The cap removes all moisture","It guarantees a derecho"],
 "A cap delays storms but lets energy pile up.",
 ["A cap keeps storms from starting early and using up the fuel.","When one finally breaks through at a boundary, it has loads of stored energy.","Misconception: a cap means a quiet day. It can mean a dangerous one if a trigger arrives."])
num(U,3,1.2,"The surface wind is 30 kt from the south (blowing toward the north) and the wind at 6 km is 40 kt from the west (blowing toward the east). What is the size of the wind shear vector in knots?",
 50,"kt","Shear is the vector difference, and here it forms a 3-4-5 right triangle.",
 ["Shear is the change in wind, so you subtract the vectors, not the speeds. Speeds alone (40 − 30 = 10) would hide the turning.","North 30 and east 40 are at right angles, so the difference is the hypotenuse of a right triangle: √(30² + 40²).","√(900 + 1600) = √2500 = 50 kt. Strong turning plus speed makes 50 kt of shear, supportive of supercells."])
num(U,3,1.5,"The surface wind is 20 kt blowing toward the west (an east wind). The wind at 6 km is 15 kt blowing toward the south (a north wind). What is the size of the wind shear vector in knots?",
 25,"kt","Subtract the vectors: the two arrows are at right angles, so use √(20² + 15²).",
 ["Draw the surface arrow pointing west and the 6 km arrow pointing south. The shear is the arrow from the tip of the lower one to the tip of the upper one.","Because west and south are at right angles, shear = √(20² + 15²).","√(400 + 225) = √625 = 25 kt. Adding speeds (35) is wrong: the arrows are not in line."])
mcq(U,2,0,"The wind is from the southeast at the surface, south-southwest at 850 mb, and west at 500 mb. This turning with height is called…",
 ["Veering (clockwise)","Backing (counterclockwise)","Divergence","Subsidence"],
 "Southeast → southwest → west is a clockwise turn on a compass.",
 ["Picture the compass: SE (135°), SSW (200°), W (270°). Numbers increase, so you turn clockwise.","Clockwise turning with height is veering, which in the Northern Hemisphere favors right-moving supercells.","Backing is the opposite, and is a warning sign that the setup is less favorable."])
mcq(U,3,1.0,"On a hodograph, the curve bends clockwise with height. What type of storm motion does this favor in the Northern Hemisphere?",
 ["A right-moving supercell that deviates to the right of the mean wind","A left-moving supercell only","A storm that cannot move","A storm that rotates clockwise only at the ground"],
 "Clockwise turning favors storms that track right of the average wind.",
 ["The hodograph curve is the 'turning staircase' of the wind. A clockwise staircase pushes updraft rotation in a way that favors the right flank.","Right-movers are the long-lived tornadic supercells most chasers watch.","Misconception: the hodograph shows storm movement. It shows the wind profile that causes it."])
mcq(U,3,1.0,"Tornado forecasters care about wind shear in the lowest 1 km in particular. Why?",
 ["Spin in the lowest layer is closest to the ground, where tornadoes form","The lowest 1 km has no air","Low-level shear removes CAPE","Shear above 6 km is always zero"],
 "Low-level turning gives spin that can be stretched into a tornado near the ground.",
 ["Think of rolling a pencil between your hands near a table: the spinning air close to the ground is what gets pulled up into the storm's base.","Deep-layer shear (0–6 km) tells if a storm will be organized. Low-level shear tells if the rotation can reach the ground.","Combine with a low LCL for the best tornado setup."])
mcq(U,2,0.5,"Dry air at 700 mb on a sounding, above a moist low level, mainly raises the risk of…",
 ["Strong downdrafts and damaging winds as rain evaporates","Fog","Snow","Lower cloud bases"],
 "Rain falling into dry air evaporates, cools, and sinks fast.",
 ["Evaporation takes heat from the air, like sweat cooling your skin. The cooled air gets denser and plunges.","A deep dry layer above moist low levels is the classic downburst setup.","Dry air aloft can also help large hail."])
mcq(U,3,1.2,"Which sounding feature most directly helps large hail grow?",
 ["A strong, long updraft (large CAPE) with a low freezing level","Light winds at all heights","Warm, stable layers throughout","Saturated air near the ground only"],
 "Hail grows in strong updrafts that hold ice aloft where it is cold.",
 ["Think of a hailstone as an onion growing layer by layer; it needs to ride a strong updraft many minutes.","A lower freezing level means the stone spends less time melting on the way down.","Large CAPE means a strong updraft, enough to support heavy stones."])
num(U,2,0.3,"The surface temperature is 26 °C and temperature falls 6.5 °C per km. At about what height (in km) is the freezing level?",
 4,"km","26 ÷ 6.5 = 4 km.",
 ["The freezing level is where temperature reaches 0 °C.","Divide the drop needed by the rate: 26 ÷ 6.5 = 4.0 km.","Hail forms and falls from near this level up, so a lower freezing level helps stones reach the ground."],tol=0.03)
num(U,3,1.0,"Air with a temperature of −5 °C sinks 3 km in a dry downdraft, warming 10 °C per km (no evaporation). What is its temperature, in °C, at the ground?",
 25,"°C","Sinking air warms by compression: 3 × 10 = 30 °C of warming.",
 ["Compression warms air, like a bicycle pump heating up.","Warming = 10 °C/km × 3 km = 30 °C.","−5 + 30 = 25 °C. Chinook and Santa Ana winds work this way."])
num(U,3,1.4,"The theoretical maximum updraft speed is w = √(2 × CAPE). For a CAPE of 1,250 J/kg, what is w in m/s?",
 50,"m/s","√(2 × 1250) = √2500 = 50 m/s.",
 ["CAPE is energy per kilogram, like the energy a car has before braking. Turn all of it into motion: ½w² = CAPE.","So w = √(2 × 1250) = √2500 = 50 m/s.","Real updrafts are usually about half of this because of drag and mixing."],tol=0.02)
mcq(U,2,0.3,"A CAPE of 4,200 J/kg is best described as…",
 ["Extreme","Strong","Moderate","Marginal"],
 "Over 4,000 J/kg is extreme in this scale.",
 ["Use the ladder: under 1,000 marginal, 1,000–2,500 moderate, 2,500–4,000 strong, over 4,000 extreme.","4,200 is above the top step.","Big CAPE alone does not mean tornadoes: shear and a trigger matter too."])
mcq(U,2,0.3,"On a sounding, the temperature and dew point lines are 15 °C apart from 800 to 600 mb. What does this say about that layer?",
 ["It is dry","It is saturated and cloudy","It is an inversion","It is the jet stream"],
 "A big gap between T and Td means low humidity.",
 ["Dew point is the temperature the air would need to cool to for cloud. A wide gap means a long way to go.","Lines touching mean cloud, lines far apart mean dry air.","Dry mid-levels can strengthen downdrafts."])
mcq(U,3,1.0,"A 300 mb jet is far stronger than usual over the Plains, above a developing surface low. How does the jet help the surface low strengthen?",
 ["Air spreading apart (diverging) aloft pulls air up from below, lowering surface pressure","It pushes cold air straight down to the ground","It removes all moisture","It cools the ocean"],
 "Divergence aloft lowers pressure below.",
 ["Picture a vacuum cleaner on the top of the column: air leaving the top draws air up from the bottom.","Less air in the column means lower surface pressure, so the low deepens.","This is why strong jets, deep lows and severe outbreaks go together."])
mcq(U,2,0.2,"Why is the jet stream usually strongest in winter?",
 ["The temperature contrast between cold polar air and warm tropical air is greatest","The sun is closest to the poles","Mountains grow taller","The ocean freezes"],
 "Jet winds are driven by how sharply temperature changes from north to south.",
 ["A bigger temperature gap is like a steeper hill: the air flows faster down it.","In winter the pole is very cold while the tropics stay warm.","In spring the jet moves north and weakens, but it can still overlap warm Gulf air to make severe storms."])
mcq(U,3,1.0,"A forecaster has a sounding with CAPE of 3,000 J/kg, deep moisture, a weak cap, and 10 kt of 0–6 km shear. What is the likely storm mode?",
 ["Disorganized pulse storms that collapse quickly","Long-lived supercells","No storms at all","Hurricanes"],
 "Fuel without shear makes short-lived storms.",
 ["Without shear, rain falls straight down through the updraft and chokes it, like a person cutting off their own air supply.","Pulse storms can still produce hail and microbursts for a short time.","Supercells need shear around 40 kt or more."])
mcq(U,3,0.9,"At what height is the equilibrium level (EL) of a thunderstorm parcel found?",
 ["Where the rising parcel is no longer warmer than its surroundings, near the storm top","At the cloud base","At the ground","Where the dew point is highest"],
 "The EL marks where buoyancy ends, close to the anvil level.",
 ["A parcel rises while it is warmer than its surroundings. At the EL the temperatures match, so buoyancy ends.","Momentum carries it a bit higher: that is the overshooting top.","Spread at the tropopause makes the anvil."])
multi(U,3,1.2,"Select ALL features you can read directly from a skew-T sounding.",
 ["Inversions (cap layers)","Temperature and dew point at each pressure","How far T and Td are apart (dryness)","Radar echo intensity","Rainfall totals that fell yesterday"],
 [0,1,2],
 "A sounding shows how T and Td change with height, not radar or past rain.",
 ["A sounding is a weather balloon's vertical profile of T, Td, and wind.","Inversions show as T rising with height, and dryness as a wide T–Td gap.","Radar and rainfall totals come from other tools."])
mcq(U,2,0,"Why does a long path on a hodograph mean strong shear?",
 ["Each point is the wind at a height, so a long path means the wind changes a lot with height","Long paths show strong rain","They show strong temperature","They show pressure"],
 "The farther apart the points, the bigger the wind change.",
 ["Each dot is one height's wind. Connect the dots like a path between two cities.","A short path means the winds are almost the same at all heights, little shear.","A long, curved path means lots of change in both speed and direction."])
mcq(U,3,1.0,"Which pair of 850 mb and 500 mb conditions makes the best recipe for steep mid-level cooling that supports big CAPE?",
 ["Warm, moist air at 850 mb with cold air at 500 mb","Cold air at 850 mb and warm air at 500 mb","Equal temperatures at both levels","Dry, cold air at 850 mb"],
 "Warm and moist below with cold above makes a steep lapse rate.",
 ["A steep temperature drop with height makes lifted parcels stay warmer than their surroundings.","Warm and moist at 850 supplies fuel, cold at 500 gives the buoyancy push.","Warm at 500 mb would cap the atmosphere."])
txt(U,2,0.3,"Rising dry air cools by about how many °C per kilometer?",["10","10 °C","10°C","ten"],
 "Dry air cools about 10 °C for each kilometer it rises.",
 ["As a parcel rises, pressure falls and it expands. Expanding takes energy, so it cools, like spray from a can feeling cold.","Dry rate: 10 °C/km. After condensation starts, the rate slows to roughly 6 °C/km.","Average real air: 6.5 °C/km."])
mcq(U,3,1.6,"A sounding has a surface cap at 900 mb, then a very deep dry layer, then cold air aloft. A storm forms along a dryline and rises through the cap. Which hazard is most likely from the dry layer?",
 ["Strong downdrafts and damaging outflow winds","Heavy fog","A hurricane","A blizzard"],
 "Rain falling through dry air evaporates and cools, speeding the downdraft.",
 ["Step 1: the cap breaks and the storm forms.","Step 2: precipitation falls into dry air and evaporates.","Step 3: evaporation cools the air, so it sinks fast and spreads out as damaging wind."])
mcq(U,3,1.3,"A student reads: 'LCL is low and shear is strong, so a tornado WILL happen.' What is wrong?",
 ["Favorable ingredients raise the odds but do not guarantee a tornado","Low LCLs never matter","Shear has no effect","Tornadoes only occur with a high LCL"],
 "A forecast is about probability, not certainty.",
 ["Ingredients are like the ingredients for a cake: you can have them all and still make a mess.","A trigger, storm interactions and details near the ground still decide.","A good forecast says 'the risk is higher', not 'it will happen'."])

S="setup"
match(S,1,-0.5,"Match each front to its main feature.",
 [["Cold front","Cold air pushes warm air up fast, sharp storms"],["Warm front","Warm air slides over cold air, wide steady rain"],["Stationary front","Boundary that barely moves"],["Occluded front","Cold front has caught up to a warm front"]],
 "Each front is named for which air mass is winning.",
 ["Cold front: cold air advances like a snowplow under warm air.","Warm front: warm air climbs a gentle ramp over cold air.","Stationary: neither side wins. Occluded: the faster cold front catches the slower warm front."])
mcq(S,2,0,"Which wind shift usually happens when a cold front passes in the Northern Hemisphere?",
 ["From southwesterly to northwesterly","From northwesterly to southerly","From east to south","No change"],
 "Wind turns clockwise to the northwest behind the front.",
 ["Ahead of the front, warm air flows from the south or southwest.","Behind it, cold air flows from the northwest.","Pressure also rises and dew points fall."])
mcq(S,2,0.2,"As a warm front approaches, the sequence of clouds is usually…",
 ["Cirrus, then thicker layers, then steady rain clouds","Cumulonimbus, then clear","Fog, then cirrus","Nothing changes"],
 "Warm air slides up a gentle slope, so clouds lower and thicken over many hours.",
 ["Picture a long ramp: you see the highest wisps first and then lower layers.","That's why light signs hours ahead, like halos, signal a warm front.","Cold fronts are steep, so storms come with little warning."])
mcq(S,2,0.3,"Why do cold fronts usually bring a narrow band of intense storms but warm fronts bring wide, steady rain?",
 ["Cold fronts are steeper and faster, so lift is stronger and short","Cold fronts are slower","Warm fronts have no moisture","Warm fronts push air down"],
 "Steeper slope means stronger lift in a smaller area.",
 ["A cold front acts like a steep bulldozer scoop, forcing air up quickly.","A warm front is a long gentle ramp, so lift is gentle but widespread.","Quick lift makes cumulonimbus, gentle lift makes layered clouds."])
mcq(S,3,0.8,"A cold front is 240 km away and moves toward you at 40 km/h. In about how many hours will it arrive?",
 ["6","0.17","9.6","4"],
 "Time = distance ÷ speed.",
 ["240 ÷ 40 = 6 hours.","Check the units: km ÷ km/h leaves hours.","Fronts often speed up or slow down, so treat it as an estimate."])
num(S,2,0.3,"A cold front is 240 km away and moves toward you at 40 km/h. About how many hours until it arrives?",6,"h",
 "240 ÷ 40 = 6 hours.",["Time = distance ÷ speed.","240 km ÷ 40 km/h = 6 h.","Fronts can speed up or slow down, so treat it as an estimate."])
new.pop(len(new)-2)
mcq(S,2,0,"A cold front passes. Which pairing of changes is typical?",
 ["Temperature falls, pressure rises, dew point drops","Temperature rises, pressure falls","Dew point rises, pressure falls","Temperature rises, dew point rises"],
 "Cold, dry, dense air replaces warm, moist air.",
 ["Dense cold air presses down harder, so pressure goes up.","Cold air from Canada is also drier, so the dew point falls.","Ahead of the front, pressure was falling."])
mcq(S,3,0.9,"A storm chaser wants to find lift on the Plains. Which boundary is mainly a MOISTURE boundary, not a temperature boundary?",
 ["Dryline","Cold front","Warm front","Occluded front"],
 "The dryline separates moist Gulf air from dry desert air.",
 ["Fronts are named for temperature. The dryline is named for dryness.","Dew points can fall from 65 °F to 35 °F across just a few miles.","Often the dry side is hotter, which surprises people."])
mcq(S,3,1.0,"Two stations: A reports T 72 °F, Td 66 °F. B reports T 78 °F, Td 40 °F. A dryline lies between them. Which side is east?",
 ["A, the moist side","B, the hot side","The one with higher T","Can't tell"],
 "On the Plains the moist Gulf air is to the east of the dryline.",
 ["Compare dew points, not temperatures. A has a high dew point (moist), B has a low one (dry).","Moist Gulf air lies east of the dryline.","So A is east. Misconception: a dryline is a temperature boundary; here the dry side is actually warmer."])
mcq(S,2,0.3,"Why do storms often start along a dryline in the afternoon?",
 ["Air converges there and is forced upward, and daytime heating helps","Cold air pushes in from Canada","The dryline blocks all lift","It cools the ground"],
 "Converging air must rise, and afternoon heat adds fuel.",
 ["Two streams of air running into each other have nowhere to go but up, like cars merging into one lane.","Afternoon heating weakens the cap and lifts parcels.","Storms often pop up in a line along the boundary."])
mcq(S,3,1.2,"On the Plains, the dryline usually moves…",
 ["East during the day and back west at night","West during the day and east at night","North all day","It never moves"],
 "Daytime mixing pulls dry air eastward, and night allows moisture to return.",
 ["Sunshine stirs the air, bringing dry air from aloft down to the surface and pushing the dryline east.","After sunset, mixing stops and moist air flows back west on the low-level jet.","So chasers watch its position hour by hour."])
mcq(S,2,0.2,"Which of these is NOT a way to lift air into a storm?",
 ["Sinking air in a high-pressure center","A cold front","Mountains","Sea breeze front"],
 "Sinking air warms and dries, which suppresses storms.",
 ["Lift mechanisms push or pull air upward.","Fronts, mountains, outflow boundaries and sea breezes all do.","High pressure is the opposite: air sinks, skies stay clear."])
multi(S,3,1.0,"Select ALL that can trigger thunderstorms by lifting air.",
 ["Cold front","Dryline","Outflow boundary from an earlier storm","Sea-breeze front","Center of a strong high pressure"],
 [0,1,2,3],
 "Lift comes from converging air or terrain. Highs mean sinking air.",
 ["Fronts, drylines, outflow boundaries and sea-breeze fronts all force air to converge and rise.","An outflow boundary is a mini cold front made by a storm's cool downdraft.","A high's sinking air suppresses storms."])
mcq(S,3,1.2,"An old thunderstorm sent out a boundary of cool air. Why can it trigger new storms?",
 ["It acts like a small cold front lifting the warm air","It dries out the ground","It removes shear","It makes the cap stronger"],
 "The cool pool shoves warm air up where it meets warmer air.",
 ["The cool air is denser, so it spreads out under the warm air like a tiny cold front.","Warm moist air riding up over it can fire storms hours later.","Forecasters watch radar for thin lines called outflow boundaries."])
mcq(S,2,0.2,"What is a low-level jet?",
 ["A ribbon of fast wind a few hundred to a thousand meters up","The jet stream at 300 mb","A wind near the equator","A tornado"],
 "It carries moisture north on the Plains.",
 ["It is much lower than the high jet stream, near 850 mb.","It often blows from the south, bringing Gulf moisture.","It is strongest after midnight."])
mcq(S,3,1.4,"Why does the low-level jet often speed up after sunset?",
 ["The ground cools, so the surface layer is cut off from friction and the air above speeds up","The sun heats it","Mountains disappear","The Gulf heats the air"],
 "At night, friction no longer slows the air just above the surface layer.",
 ["By day, mixing connects the wind to the slow-moving ground, like a ball of dough sticking to a table.","At night a cool layer forms at the ground and the winds above slide freely.","This speeds up moisture transport and adds low-level shear for night tornadoes."])
mcq(S,3,1.2,"Strong vertical wind shear HELPS thunderstorms organize into supercells but HURTS most hurricanes. Why?",
 ["Shear tilts a hurricane's warm core and blows its tops away, but tilts a supercell's updraft away from its rain","Hurricanes need cold air","Supercells need calm air","Shear has the same effect on both"],
 "A hurricane needs a tall, stacked column; a supercell needs a tilted one.",
 ["Hurricane: stacked like a smokestack. Shear leans it over and mixes dry air in.","Supercell: tilting separates the updraft from the cold rain downdraft so the storm can keep going.","Contrast the two cases rather than memorizing 'shear is good/bad'."])
mcq(S,3,1.0,"Which setup is best for supercells?",
 ["Gulf moisture, steep lapse rates, and strong turning shear","Cold dry air and light wind","A stable cap over weak winds","Warm front with no instability"],
 "You need fuel (moisture, instability) and organization (shear).",
 ["Moisture and instability give fuel.","Strong, turning shear provides rotation and storm longevity.","Missing any one of these usually reduces the severe threat."])
mcq(S,2,0.4,"Which factor lets wave heights grow bigger: a longer fetch or a shorter fetch (same wind)?",
 ["Longer fetch","Shorter fetch","They are the same","Only depth matters"],
 "Wind has more distance to pass energy to the water.",
 ["Fetch is the stretch of open water the wind blows across, like how long you push a swing.","More distance and time means more energy transferred to the waves.","Wave height depends on wind speed, duration and fetch."])
multi(S,3,1.1,"Select ALL that make bigger wind waves.",
 ["Stronger wind","Longer time the wind blows","Longer fetch","Less open water","A calm morning"],
 [0,1,2],
 "Three factors build waves: wind speed, duration, and fetch.",
 ["More wind, more time, more distance means more energy.","Less open water limits fetch.","Calm air adds no energy."])
mcq(S,2,0.4,"Hurricanes need ocean water at least about…",
 ["26.5 °C (80 °F) through a deep layer","10 °C","15 °C","0 °C"],
 "Warm ocean water is the fuel.",
 ["Warm water evaporates heat and moisture into the storm like a stove under a pot.","The warmth must be deep (50 m or more), or mixing brings up cool water.","Cool wakes weaken storms that follow."])
mcq(S,3,1.2,"A hurricane moves over a deep warm eddy of Gulf water. What will probably happen?",
 ["It may intensify rapidly","It will weaken","It turns into a front","It stops rotating"],
 "Deep warm water means more fuel and little cooling from mixing.",
 ["Ocean heat content measures how deep the warmth goes.","A hurricane stirs up water from below. If that water is still warm, no cooling happens.","Over thin warm layers, stirring brings up cold water and weakens the storm."])
mcq(S,2,0.4,"Moist air flows up the windward slope of a mountain and rains there. What is the dry area on the lee side called?",
 ["Rain shadow","Fetch","Dryline","Eye"],
 "Air loses its moisture on the way up and arrives dry on the other side.",
 ["Lifting cools air so rain falls on the windward side.","The air sinks on the lee side and warms, becoming drier.","Deserts often sit in a rain shadow."])
mcq(S,3,1.0,"An atmospheric river hits the California coast and rises over the coastal mountains. Why does this raise flood risk?",
 ["Lifting wrings out the heavy water vapor as intense rain","The wind turns off","The air sinks","It brings dry air"],
 "Mountains force the vapor up, where it cools and condenses.",
 ["Think of squeezing a wet sponge: lift squeezes out the water.","An atmospheric river is a narrow stream of very moist air, like a firehose in the sky.","Steady supply plus lift for hours means flooding and landslides."])
mcq(S,2,0.3,"Which statement about an atmospheric river is right?",
 ["It is a long, narrow band of strong water vapor transport","It is a surface river","It is a type of tornado","It is a dry wind"],
 "It is a stream of water vapor in the sky.",
 ["It transports vapor, not liquid water.","Some reach California from near Hawaii (the 'Pineapple Express').","Landfall with mountain lift is when the heaviest rain falls."])
mcq(S,2,0.3,"A stationary front sits over one area for days with warm, moist air flowing along it. What is the main danger?",
 ["Flooding from repeated storms over the same area","Hurricanes","Dust storms","Frost"],
 "Storms keep forming and moving over the same spot.",
 ["Like train cars on a track, storms pass the same place again and again.","Totals pile up even if each storm is only moderate.","This 'training' is a flash flood setup."])
mcq(S,2,0,"A warm sector is the area…",
 ["Between the cold front and the warm front where warm moist air sits","Behind a cold front","North of a warm front","In the eye"],
 "It lies between the two fronts around a low.",
 ["In a mid-latitude cyclone the warm front is on the east, cold front on the west or southwest.","In between is the warm, moist air that fuels storms.","Severe weather is often found in the warm sector ahead of the cold front."])
mcq(S,3,0.9,"Air flows around a low pressure in the Northern Hemisphere…",
 ["Counterclockwise and inward","Clockwise and inward","Clockwise and outward","Straight in"],
 "Counterclockwise spin with inflow toward the center.",
 ["Pressure pulls air inward, and Earth's rotation turns it to the right.","The result is counterclockwise spin around lows and clockwise around highs.","Southerly winds in the east of the low bring Gulf moisture north."])
match(S,2,0.4,"Match the air mass to its source and type.",
 [["Continental polar (cP)","Cold and dry, from Canada"],["Maritime tropical (mT)","Warm and moist, from the Gulf"],["Continental tropical (cT)","Hot and dry, from deserts"],["Maritime polar (mP)","Cool and moist, from the north oceans"]],
 "Letter 1: c or m for land or sea. Letter 2: P or T for cold or warm.",
 ["c means continental (land, so dry), m means maritime (ocean, so moist).","P means polar (cold), T means tropical (warm).","So cP is cold and dry, mT is warm and moist."])
mcq(S,3,1.3,"A forecaster sees Gulf moisture, strong jet stream, steep lapse rates, a strong cap, and no front or dryline anywhere nearby. Which ingredient is most likely missing?",
 ["Lift, so storms might not start","Moisture","Instability","Shear"],
 "A cap stays closed without a trigger.",
 ["The list covers moisture, instability and shear.","Lift has no source, and a cap needs lift to break.","Result: possibly a quiet day despite scary numbers."])
mcq(S,3,1.2,"Warm air flows over cold ground ahead of a warm front. Why does it make low clouds and fog?",
 ["The air is cooled from below to its dew point","The air is heated","The air is dried","Wind speeds up"],
 "Cooling to the dew point makes cloud.",
 ["Cooling from below reduces the gap between T and Td until the air saturates.","The same idea explains why a cold drink glass 'sweats'.","Steady drizzle is common with warm fronts."])
mcq(S,2,0.4,"Before a cold front, pressure usually…",
 ["Falls, then rises after the front passes","Rises, then falls","Stays the same","Falls and keeps falling"],
 "Pressure bottoms out at the front.",
 ["Warm air ahead is light, so pressure falls.","Cold dense air arrives and pressure climbs.","A pressure trace shaped like a V marks the front."])
mcq(S,3,1.0,"A line of storms (a squall line) often forms…",
 ["Along or ahead of a fast cold front","Behind a warm front only","Over the poles","In clear air"],
 "The front gives strong lift in a line.",
 ["A cold front lifts air along its whole length, so a line of storms results.","Shear and a strong cold pool keep the line organized.","Squall lines often bring straight-line wind damage."])
mcq(S,3,1.1,"Which is the best explanation of why strong shear keeps a supercell alive?",
 ["It tilts the updraft away from the rain-cooled downdraft","It cools the updraft","It dries the air","It slows the storm"],
 "A separate updraft and downdraft don't cut each other off.",
 ["In a no-shear storm, rain falls through the updraft and kills it.","With shear, the updraft leans and the rain falls beside it.","That lets the storm last for hours."])

C="clouds"
mcq(C,3,1.2,"A spotter sees a lowered, rotating cloud base. Where is it usually found relative to the heavy rain?",
 ["In the rain-free part of the base, next to the heavy rain","In the middle of the rain core","Far from the storm","Above the anvil"],
 "A wall cloud sits where air is flowing into the updraft, not under falling rain.",
 ["Inflow air rushes toward the updraft in a rain-free area, like a straw sucking air in beside a glass of water.","Rain pours down on the other side where the downdraft is.","If the tornado gets wrapped in rain, it is hard to see."])
mcq(C,3,1.2,"A funnel does not reach the ground, but dust and debris swirl on the ground beneath it. What should it be reported as?",
 ["A tornado","A funnel cloud","Mammatus","A shelf cloud"],
 "A tornado is rotating air in contact with the ground, even without the full funnel visible.",
 ["Funnel clouds are condensation only. Look at the ground: if debris is swirling, the circulation is touching it.","The visible funnel is just where air cooled enough to make cloud.","Misconception: tornado needs a funnel to touch the ground."])
mcq(C,3,1.0,"Which statement correctly contrasts a shelf cloud and a wall cloud?",
 ["A shelf cloud is on the cool outflow edge and is not rotating, a wall cloud is under the updraft and can rotate","They are the same","A wall cloud is on the gust front","A shelf cloud is a tornado"],
 "Shelf: outflow side. Wall: inflow side.",
 ["Shelf clouds look like a long wedge at the storm's front edge and bring a cool, gusty wind.","Wall clouds are a smaller lowering beneath the updraft and may rotate.","Rotation is the key difference."])
mcq(C,3,1.1,"Ragged low clouds are quickly rising toward the base of a storm. What does this tell you?",
 ["Strong inflow is feeding the updraft","The storm is dying","Hail is melting","A front passed"],
 "Rising scud shows air flowing up into the storm.",
 ["Scud is small cloud fragments below the main base.","Watching them climb is like watching leaves sucked into a vacuum.","Fast rise plus rotation makes for a more serious sign."])
mcq(C,2,0.4,"A tail cloud is…",
 ["A low band of cloud extending from the wall cloud toward the rain","The top of the anvil","A tornado","A cirrus streak"],
 "It shows inflow streaming into the wall cloud.",
 ["Think of a stream flowing into a river.","It is low and connected to the wall cloud.","It is a sign of inflow, not a tornado."])
mcq(C,2,0.2,"Why does a thunderstorm top flatten into an anvil?",
 ["The rising air hits the stable layer at the tropopause and spreads sideways","The cloud runs out of water","It hits the ground","Hail melts"],
 "Above the tropopause the air stays warmer than a lifted parcel, so it can't rise further.",
 ["Rising air stops when it is no longer warmer than its surroundings.","It spreads like water hitting a ceiling.","Winds aloft stretch it downwind."])
mcq(C,2,0.3,"An overshooting top is a dome that pokes above the anvil. What does it show?",
 ["A very strong updraft","A dying storm","A cold front","A tornado on the ground"],
 "Fast updraft momentum carries air past its equilibrium level.",
 ["A rocket coasting past the point where thrust ends.","The more it pokes up, the stronger the updraft.","Sustained overshooting tops hint at severe hail."])
mcq(C,3,1.1,"What most clearly separates a towering cumulus from a cumulonimbus?",
 ["The cumulonimbus top has turned to ice and looks fuzzy or fibrous","Its color","Its size","Rain is only on cumulus"],
 "Glaciation of the top marks a cumulonimbus.",
 ["A growing cauliflower with sharp edges is liquid droplets: towering cumulus.","Once the top turns to ice, the edges blur and an anvil can form.","Lightning is only produced once ice is present."])
order(C,2,0.3,"Put the thunderstorm life cycle in order.",
 ["Cumulus stage: updraft only","Mature stage: updraft and downdraft, heavy rain","Dissipating stage: downdraft dominates"],
 "Storms grow, peak, and then die as downdrafts take over.",
 ["Growth stage: warm air rises and builds towering cumulus.","Mature stage: rain starts and cool downdrafts form beside the updraft, with hail and lightning.","Dissipating stage: the downdraft cuts off the warm inflow and the cell fades."])
order(C,3,1.0,"Put the clouds seen as a warm front approaches in order, first to last.",
 ["Cirrus","Cirrostratus","Altostratus","Nimbostratus"],
 "Clouds thicken and lower as the front nears.",
 ["The front's gentle ramp shows its top first, so you see the highest wisps first.","Then a thin high veil (maybe a halo), then a gray midlevel sheet.","Finally dark, low rain clouds."])
match(C,1,-0.5,"Match each cloud word part to its meaning.",
 [["Cumulo-","Heap or puffy"],["Strato-","Layer or sheet"],["Nimbo- / -nimbus","Rain-bearing"],["Cirro-","High wispy ice"]],
 "Cloud names are built from simple word pieces.",
 ["Combine them: cumulo + nimbus = rain heap.","Alto means middle level.","Learning the pieces lets you decode any cloud name."])
num(C,2,0.4,"Surface temperature is 22 °F warmer than the dew point. Using about 1,000 ft of cloud base height per 4.4 °F of spread, what is the cloud base in feet?",
 5000,"ft","22 ÷ 4.4 = 5.0, so 5,000 ft.",
 ["The °F rule is 1,000 ft for each 4.4 °F of spread.","22 ÷ 4.4 = 5 thousand ft.","The same rule in °C is 125 m per °C; a big spread means high cloud bases and drier air."],tol=0.02)
num(C,2,0.2,"The temperature is 32 °C and the dew point is 20 °C. Using 125 m per °C of spread, how high (m) is the cloud base?",
 1500,"m","12 × 125 = 1500 m.",
 ["Find the spread: 32 − 20 = 12 °C.","Cloud base = 12 × 125 = 1,500 m.","The smaller the spread, the lower the base."])
mcq(C,3,1.1,"A thunderstorm has a high cloud base (about 3 km) and virga hanging underneath, with a dry surface. Which hazard is the best guess?",
 ["Dry microburst winds","Heavy flooding rain","Fog","Snow"],
 "Rain evaporating below a high base cools air that crashes down.",
 ["Virga is rain that evaporates before it hits the ground.","Evaporation cools the air, making it dense, so it plunges and spreads out.","Dry microbursts can cause damaging winds with little rain."])
mcq(C,3,1.2,"A microburst is a downburst with damaging winds spread over a distance of at most…",
 ["About 4 km (2.5 mi)","About 40 km","About 400 km","About 100 m"],
 "Microbursts are small; larger ones are macrobursts.",
 ["Microburst: ≤ 4 km. Macroburst: > 4 km.","Pilots fear microbursts because of sudden wind shifts near the ground.","Damage is straight-line, not swirling like a tornado."])
mcq(C,2,0.3,"Which cloud would you see before damaging straight-line winds arrive in a squall line?",
 ["A shelf cloud on the leading edge","A halo","Mammatus only","Cirrus"],
 "The gust front's lifting makes a shelf.",
 ["The cool outflow pushes underneath warm air and lifts it into a low wedge.","Winds hit just before the rain.","Seeking shelter before it arrives matters: damaging winds come first."])
mcq(C,2,0.3,"Are mammatus clouds a sign that a tornado is about to form?",
 ["No: they are pouches in sinking air under an anvil, and can appear with severe storms","Yes: they always come before tornadoes","Yes: they are the same as wall clouds","No: they only form in winter"],
 "Mammatus alone do not tell about tornadoes.",
 ["Mammatus are pouches formed by sinking, cooled air under the anvil.","They can show up near severe storms, but they are not rotation signs.","Look for a rotating wall cloud and funnel instead."])
mcq(C,3,1.2,"A short-lived swirl of dust appears along a storm's gust front with no rotation overhead. This is most likely…",
 ["A gustnado","A mesocyclone tornado","A hurricane","A funnel from a wall cloud"],
 "A gustnado forms from outflow shear, not the updraft's rotation.",
 ["The gust front has strong horizontal shear, like water swirling at the edge of a fast stream.","It's usually weak and short-lived, not tied to the updraft.","Misconception: all ground swirls near a storm are tornadoes from a wall cloud."])
mcq(C,2,0.4,"A cloud that is lens-shaped and stands still near a mountain is a…",
 ["Lenticular cloud","Shelf cloud","Mammatus","Funnel cloud"],
 "Lenticulars are made by air waves over mountains.",
 ["Air rises and falls over the peaks in standing waves, like ripples behind a rock in a stream.","Cloud forms at the crest, so the shape stays still while wind blows through.","They are not storm clouds, but warn of turbulence."])
mcq(C,3,1.0,"A thin cloud cap appears above a growing cumulus tower. What is it?",
 ["A pileus, showing a strong updraft pushing moist air upward","A shelf cloud","A tornado","Mammatus"],
 "Pileus forms as the tower lifts a layer above it.",
 ["Think of a pot lid sitting on top of a bubbling tower.","The rising cloud shoves the moist layer above and cools it to make a thin cap.","It signals a quick-growing tower, which may be about to turn into Cb."])
mcq(C,3,1.2,"Why does a funnel cloud become visible?",
 ["Low pressure inside the vortex cools the air until water vapor condenses","Dust fills it","Hail forms in it","The wind slows"],
 "Air is cooled by expansion where pressure is lowest.",
 ["Inside the whirl, pressure is lower, and expanding air cools like spray from a can.","Cooled below the dew point, vapor condenses to droplets and you see a funnel.","So a tornado can exist even if the funnel part is thin or missing."])
multi(C,3,1.1,"Select ALL that are signs of possible rotation near the base of a storm.",
 ["A wall cloud that appears to rotate","A funnel cloud","Debris swirling on the ground under the base","Mammatus under the anvil","A smooth shelf cloud moving ahead of the storm"],
 [0,1,2],
 "Rotation clues are at the base, not the anvil or outflow front.",
 ["Wall clouds, funnel clouds and swirling debris all show spinning air.","Mammatus are anvil-pouches and shelf clouds mark outflow.","Treat any rotation as dangerous and report it."])
num(C,3,1.0,"A gust front with a shelf cloud is moving toward you at 45 mph. The leading edge is 9 miles away. How many minutes until it arrives?",
 12,"min","9 ÷ 45 = 0.2 h = 12 min.",
 ["Time = distance ÷ speed = 9 ÷ 45 = 0.2 hours.","Convert to minutes: 0.2 × 60 = 12.","Common error: leaving the answer in hours."],tol=0.03)
mcq(C,3,1.0,"A spotter reports: sharp low wedge, no rotation, sudden cool wind at the ground before rain. Which cloud and hazard?",
 ["Shelf cloud with a gust front","Wall cloud with a tornado","Funnel cloud","Mammatus"],
 "Cool outflow arriving first, with no rotation, points to a gust front.",
 ["Gust fronts reach you first, with cool, gusty wind.","Wall clouds sit in the inflow area and tend to rotate.","Straight-line wind is the hazard."])
mcq(C,2,0.3,"A waterspout is…",
 ["A tornado-like vortex over water","A cloud of fog","A rain shaft","A shelf cloud on a lake"],
 "A rotating column of air over water.",
 ["Like a tornado but over a lake or ocean.","Some are weak fair-weather types, some from storms.","Treat them as hazards to boats."])
mcq(C,2,0.4,"Which cloud height group do altocumulus and altostratus belong to?",
 ["Middle level","Low level","High level","Ground level"],
 "Alto- means middle.",
 ["Alto is the middle floor of the sky.","High clouds start with cirro-.","Low ones are strato- and cumulus."])
mcq(C,3,1.5,"A cumulonimbus is called a cloud that spans all heights. How does that fit the family of cloud levels?",
 ["It has a low base but its top reaches the high levels","It is only low","It is only high","It has no levels"],
 "The base can be near 1 km while the top reaches around 12 km.",
 ["Cb is a tall tower, like a skyscraper.","Its base sits low and its top can be at the tropopause.","That's why it is classed as a vertical-development cloud."])
mcq(C,2,0.3,"A halo around the Moon usually comes from…",
 ["Cirrostratus ice crystals","Cumulonimbus","Fog","Mammatus"],
 "Ice crystals in high thin cloud bend light into a ring.",
 ["The ring is made when light passes through tiny hexagonal ice crystals, like a prism.","Cirrostratus often leads a warm front.","Rain may follow within about a day."])
mcq(C,2,0.3,"Which cloud type produces most thunderstorm hail, lightning and heavy rain?",
 ["Cumulonimbus","Cirrus","Stratus","Altocumulus"],
 "Cb has a deep updraft with ice and water.",
 ["Strong updrafts lift water into the cold zone where it freezes.","Collisions of ice and water make charge and lightning.","Cirrus is just ice and does not produce storms."])
mcq(C,3,1.6,"A spotter says 'there's a tornado, but I can't see a funnel; it's wrapped in rain.' Why is a rain-wrapped tornado especially dangerous?",
 ["It is hidden from view, so people may not see it coming","It is weaker","It is only a gust front","It is not on the ground"],
 "Rain curtains hide the vortex.",
 ["Rain hides the tornado like fog hides a road sign.","Warnings and radar become more important than eyesight.","A low-hanging cloud base can add to the problem."])

import sys
sys.path.insert(0,'.')
fix={
 "upper-005":{"l":2,"b":0.2},
 "upper-008":{"l":2,"b":0.3},
 "upper-010":{"l":2,"b":0.2,"q":"On a sounding the temperature drops very quickly with height (steeper than 6.5 °C per km). The layer is more…","text":None},
 "upper-013":{"l":2,"b":0.3},
 "upper-037":{"l":2,"b":0.4},
 "setup-015":{"l":2,"b":0.3},
 "setup-026":{"text":["west to east","from west to east"]},
 "clouds-006":{"q":"You see a ragged, lowered cloud base rotating in the rain-free part of a storm's base, right beside the heaviest rain. What best describes your concern?"},
 "clouds-005":{"w":"Mammatus are pouches of sinking air under the anvil. They are not a tornado sign by themselves."},
 "clouds-041":{"w":"Mammatus form where cooled, sinking air bulges below the anvil. They can occur with severe storms but do not signal a tornado."},
 "clouds-055":{"q":"Put these cloud types in order from the lowest base height to the highest.","items":["Stratus (low)","Altocumulus (middle)","Cirrus (high)"],"w":"Stratus is low, altocumulus middle, cirrus high."},
}
fix["upper-010"].pop("text")
fix["upper-010"].update({"w":"Fast cooling with height lets lifted parcels stay warmer than their surroundings."})
fix["upper-010"]["q"]="A sounding shows temperature dropping very fast with height. The layer is most…"
fix["upper-010"].pop("o",None); fix["upper-010"]["q"]="A sounding shows temperature dropping very fast with height. The layer is most likely…"; fix["upper-010"]["text"]=["unstable","unstable air"]
fix["upper-010"].pop("text",None)
d=dict(fix=fix,
 **{"del":["upper-034","upper-036","upper-041","upper-051","upper-006","upper-055","setup-016","setup-017","setup-020","setup-025","clouds-007","clouds-038","clouds-040","clouds-042","clouds-047","clouds-051","clouds-054"]},
 del_family=["cb1","lr1"],new=new,
 report="Fixed/re-leveled 11, deleted 17 dups/weak items plus families cb1 (taught 400 ft per degF, inconsistent with 125 m/degC rule, about 1.75x too high) and lr1 (trivial multiplication). Fixed clouds-006 (wall cloud is in the rain-free base, not under the heaviest rain), mammatus 'weakening' claims (not reliable), ambiguous order item. Added %d new (upper/setup/clouds). Doubts: study note says mammatus 'often a storm weakening', which is shaky; upper-001 and setup-034 untouched."%len(new))
json.dump(d,open(OUT,"w"),ensure_ascii=False,indent=1)
from collections import Counter
print(len(new),Counter((x['t'],x['l']) for x in new))
