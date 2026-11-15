import json, math
OUT="/tmp/claude-0/-home-claude/bdb1ee03-0916-54eb-a354-ea75cf26b960/scratchpad/audit/out/m3.json"
new=[]; n=[0]
def fp():
    n[0]+=1; return f"m3_{n[0]:03d}"
def mcq(t,l,b,q,o,w,sol): new.append(dict(t=t,l=l,b=b,type="mcq",q=q,o=o,w=w,sol=sol,fp=fp()))
def multi(t,l,b,q,o,a,w,sol): new.append(dict(t=t,l=l,b=b,type="multi",q=q,o=o,a=a,w=w,sol=sol,fp=fp()))
def num(t,l,b,q,v,u,w,sol,tol=0.02): new.append(dict(t=t,l=l,b=b,type="short",q=q,num=dict(v=v,tol=tol,u=u),w=w,sol=sol,fp=fp()))
def txt(t,l,b,q,text,w,sol): new.append(dict(t=t,l=l,b=b,type="short",q=q,text=text,w=w,sol=sol,fp=fp()))
def order(t,l,b,q,items,w,sol): new.append(dict(t=t,l=l,b=b,type="order",q=q,items=items,w=w,sol=sol,fp=fp()))
def match(t,l,b,q,pairs,w,sol): new.append(dict(t=t,l=l,b=b,type="match",q=q,pairs=pairs,w=w,sol=sol,fp=fp()))

# ================= DH =================
T="dh"
mcq(T,1,-1,"A hiker is confused, has hot dry skin and a body temperature of 104 °F. What is the right first move?",
 ["Call 911 and start cooling the person right away","Give salty snacks and let them nap","Wait an hour to see if sweating starts","Give a hot drink to settle the stomach"],
 "Hot, dry skin plus confusion is heat stroke, a medical emergency.",
 ["Heat stroke means the body's cooling system (sweating) has failed, like a car engine with no coolant.","Call 911 first, then move the person to shade and cool them with cold water or ice packs.","Common slip: treating it like tiredness. Waiting lets organ damage build up fast."])
num(T,1,-0.8,"Convert 40 °C to °F.",104,"°F","°F = °C × 9/5 + 32.",
 ["Multiply by 9/5: 40 × 1.8 = 72.","Add 32: 72 + 32 = 104 °F.","Memory hook: 40 °C is also the heat-stroke body temperature, 104 °F."])
mcq(T,1,-1,"Why do high-pressure ridges bring clear, hot, dry weather?",
 ["Air sinks, warms and dries, so clouds fade away","Air rises fast and builds big storm clouds","Cold air is pulled in from the north","Wind speeds are always very strong"],
 "Sinking air warms and dries, so clouds dissolve.",
 ["Picture air as a crowd being pushed down from above. Sinking air gets squeezed, so it warms and its clouds evaporate.","Rising air (low pressure) is the one that makes clouds and rain.","So a stuck ridge can give days of sun, heat and no rain."])
mcq(T,1,-0.8,"The air temperature is 32 °C and the heat index is 38 °C. Which number tells you how hot it feels to your body?",
 ["38 °C, the heat index","32 °C, the air temperature","6 °C, the difference","Neither one"],
 "The heat index adds humidity to temperature to show how it feels.",
 ["A thermometer only measures air. The heat index also counts how hard it is for sweat to evaporate.","So your body acts as if it were 38 °C.","Plan activities using the heat index, not the thermometer alone."])
match(T,2,0,"Match each type of drought to what it means.",
 [["Meteorological","Rain and snow far below normal for a long time"],["Agricultural","Soil too dry for crops to grow"],["Hydrological","Low streams, lakes, reservoirs and groundwater"],["Socioeconomic","Water shortage that hurts people and businesses"]],
 "Drought is named by what is short: rain, soil moisture, water supply or people's needs.",
 ["Think of a chain: first the rain stops (meteorological), then soil dries (agricultural), then rivers and reservoirs fall (hydrological).","Socioeconomic drought is when all of this hits towns, farms and businesses.","One dry spell can show up as all four types, at different times."])
order(T,2,0,"Order the US Drought Monitor categories from least to most severe.",
 ["D0 Abnormally dry","D1 Moderate drought","D2 Severe drought","D3 Extreme drought","D4 Exceptional drought"],
 "D0 is the mildest and D4 the worst.",
 ["The scale runs D0 to D4. A higher number means worse drought.","D0 is not yet drought; it is a warning that things are getting dry.","D4, exceptional, means widespread crop and water losses."])
mcq(T,2,0,"Which sign points to heat exhaustion rather than heat stroke?",
 ["Heavy sweating, cool clammy skin and weakness, but thinking clearly","Hot, dry, red skin","Confusion or fainting with no sweating","A seizure"],
 "Heat exhaustion: still sweating. Heat stroke: sweating stops and the brain is affected.",
 ["Heat exhaustion is a car engine running hot but still cooled by its fan. Move to a cool place, loosen clothing and sip water.","Heat stroke is the fan failing: hot dry skin and confusion. That needs 911.","Misconception: both are the same. Exhaustion can turn into stroke if ignored."])
order(T,2,0,"Order heat illnesses from mildest to most dangerous.",
 ["Heat cramps","Heat exhaustion","Heat stroke"],
 "Muscle cramps come first, then exhaustion, then life-threatening stroke.",
 ["Heat cramps are painful muscle spasms from losing water and salt.","Heat exhaustion adds heavy sweat, dizziness and weakness.","Heat stroke is the emergency: body temp 104 °F or more and the cooling system fails."])
mcq(T,2,0,"Why are city nights often hotter than nights in nearby countryside during a heat wave?",
 ["Pavement and buildings soak up heat by day and release it at night","Cities get more sunshine hours","Rural areas have thicker clouds at night","City air is always more humid"],
 "Concrete and asphalt store heat like a brick left in the sun.",
 ["A brick left in the sun stays warm long after sunset. Streets and walls do the same.","Grass and trees cool by evaporation, so rural areas lose heat faster.","This is the urban heat island, and warm nights stop people from recovering."])
mcq(T,2,0,"Why does dry soil make a heat wave hotter?",
 ["Sunlight heats the air instead of evaporating water from wet ground","Dry soil makes more clouds","Dry soil absorbs no sunlight","Dry soil cools the air"],
 "With no water to evaporate, the Sun's energy goes into heating the air.",
 ["Compare a wet sponge with a dry one in the sun. Evaporating water uses energy and cools.","When the ground is dry, that energy heats the air instead.","This feedback is why drought and heat waves often come together."])
num(T,2,0,"A town's normal rain over three months is 60, 70 and 80 mm. It received 30, 35 and 40 mm. What percent of normal fell?",50,"%","Percent of normal = actual ÷ normal × 100.",
 ["Normal total: 60 + 70 + 80 = 210 mm. Actual: 30 + 35 + 40 = 105 mm.","105 ÷ 210 = 0.5, so 50%.","Add totals first; do not average the three percents carelessly."])
multi(T,2,0,"Select ALL good ways to avoid heat illness.",
 ["Drink water before you feel thirsty","Take breaks in shade or air conditioning","Wear light, loose clothing","Never leave a child or pet in a parked car","Do your hardest exercise at 2 pm","Drink sugary or alcoholic drinks for hydration"],[0,1,2,3],
 "Fluids, cooling breaks and light clothing protect you; midday exertion and alcohol raise risk.",
 ["Thirst shows up after you are already low on water, so drink early.","Cars heat far above the outside air within minutes.","Alcohol and sugary drinks pull water out of the body; hard exercise at the hottest hour adds heat."])
txt(T,2,0,"What is a drought called that builds fast, within a few weeks, as heat and dry weather quickly dry out the soil?",
 ["flash drought","a flash drought"],"Flash droughts intensify rapidly.",
 ["Most droughts creep in over months, like a slow leak.","A flash drought is a burst pipe: heat plus no rain dries soil in weeks.","Crops can fail before anyone sees a drought declared."])
mcq(T,3,0.8,"A ridge sits over a region and air sinks through it with no heat added or lost. What happens to the air's temperature as it sinks?",
 ["It warms, because the air is squeezed as pressure rises","It cools, because it is moving away from the Sun","It stays the same","It cools, because sinking air is always cold"],
 "Sinking air is compressed, and compression warms it.",
 ["Pump a bicycle tire fast and the pump gets hot. Compressing air heats it.","Air sinking in a ridge gets squeezed by the heavier air above, so it warms (about 10 °C per km).","That is why heat domes can bake a region even with little sunshine change."])
mcq(T,3,1.0,"Two cities both have air at 36 °C. City A has a dew point of 10 °C. City B has a dew point of 24 °C. Which is more dangerous and why?",
 ["B, because moist air slows sweat evaporation so the body cools less","A, because dry air burns skin","They are equal because air temperature is the same","A, because lower dew point means higher heat index"],
 "Higher dew point means more moisture in the air, so cooling by sweat is weaker.",
 ["Your body cools when sweat evaporates, like a wet towel drying.","In moist air the towel dries slowly, so cooling is weak.","Same temperature, but B has the higher heat index. Misconception: only temperature matters."])
num(T,3,1.0,"Heat index values assume shade. In full sunshine the heat index can be higher by up to how many °F?",15,"°F","NWS notes direct sun can add up to 15 °F.",
 ["The heat index is figured for shade and light wind.","Standing in full sun adds extra heat from sunlight, up to about 15 °F.","So a shade value of 98 °F could feel like 113 °F in the open."])
mcq(T,3,1.1,"Why is wet-bulb temperature a better heat-stress measure than ordinary air temperature?",
 ["It includes the cooling limit set by humidity and evaporation","It ignores humidity","It is always lower than dew point","It measures only sunlight"],
 "A wet-bulb thermometer shows how much evaporation can cool you.",
 ["Wrap a wet cloth on a thermometer. In dry air it cools a lot; in humid air it cools little.","That cooling is exactly what your sweat can do.","So wet-bulb blends heat and humidity into one number about body cooling."])
mcq(T,3,1.0,"Rain returns to normal for two months, but reservoirs and groundwater are still low. Which drought type is likely continuing?",
 ["Hydrological drought","Meteorological drought","No drought of any type","Heat drought"],
 "Water storage recovers slowly after rain returns.",
 ["Rain is like income; reservoirs and aquifers are savings.","After a long deficit you must refill the savings before the shortage ends.","So the rain deficit may end while the hydrological drought continues."])
mcq(T,3,1.0,"Phoenix has a typical July high near 104 °F. It hits 105 °F for a day. Is that a heat wave?",
 ["No: a heat wave needs unusual heat for the region, lasting several days","Yes, because 105 °F is above 100 °F","Yes, any day over 100 °F counts","No, heat waves happen only in humid places"],
 "A heat wave is defined relative to local normals and duration.",
 ["A 105 °F day is normal for Phoenix but would be shocking in Seattle.","Heat wave means unusually hot for that place for a period of days.","Misconception: one fixed temperature defines a heat wave."])
mcq(T,3,0.9,"Which best describes why a heat wave ends?",
 ["A trough or front arrives and the ridge weakens or moves away","The Sun gets weaker","All the humidity disappears","The ridge always lasts exactly 5 days"],
 "Heat waves end when the steering pattern changes.",
 ["A blocking ridge is a boulder in a stream. When the flow pushes it away, weather moves on.","A trough or cold front brings cooler air and storms.","Forecasters watch upper-air maps for that change."])
mcq(T,3,0.8,"While waiting for an ambulance for a heat stroke victim, which action is best?",
 ["Move to shade and cool the body with cold water or ice packs on neck, armpits and groin","Give a large amount of hot tea","Wrap them in a blanket to sweat it out","Make them run to cool off"],
 "Fast cooling is the treatment while help arrives.",
 ["The body is overheating like a stuck engine; remove the heat as fast as possible.","Ice packs on neck, armpits and groin cool blood flowing near the surface.","Do not force drinks on someone who is confused."])
mcq(T,3,1.2,"La Niña winters tend to make which part of the US drier than normal?",
 ["The southern US","The Pacific Northwest","The Great Lakes","New England"],
 "La Niña shifts the winter storm track north, leaving the south dry.",
 ["Picture the jet stream as a river of storms. In La Niña it flows farther north.","The southern states then miss many storms and run dry.","Misconception: La Niña is dry everywhere. It is wetter in parts of the north."])
mcq(T,3,1.0,"The Palmer Drought Severity Index reads −3.8 in one county and +3.8 in another. What does that mean?",
 ["The first county is in severe drought and the second is unusually wet","The first is wet and the second is in drought","Both have normal moisture","Both are in drought"],
 "Negative Palmer values mean dry, positive mean wet.",
 ["Think of the index as a moisture bank balance: negative means in debt.","About −3 or lower is severe drought.","Positive values show soil moisture above normal."])
num(T,3,0.8,"A heat wave has daily highs of 95, 98, 102 and 105 °F. What is the average high in °C (nearest degree)?",38,"°C","Average first, then convert.",
 ["Average: (95 + 98 + 102 + 105) ÷ 4 = 100 °F.","Convert: (100 − 32) × 5/9 = 37.8 °C.","Round to 38 °C."],tol=0.02)
mcq(T,3,1.0,"A storm drops 3 inches of rain on a county that is in drought, and creeks flash flood. What is the best explanation?",
 ["Baked, hard soil absorbs water slowly so most of it runs off","Drought adds water to creeks","Dry soil is soft and absorbs everything","Rain in a drought is always colder"],
 "Hard dry ground sheds water like a roof.",
 ["Pour water on a dry, hard sponge or clay: it beads and runs off.","Runoff reaches creeks fast and floods them.","Drought and flood can happen in the same place."])
num(T,3,1.6,"Air starts at −5 °C at 3 km up in a ridge and sinks to the ground. Dry air warms about 10 °C per km when sinking and nothing else changes. What is its temperature at the surface in °C?",25,"°C","Compression warming is 10 °C for each km of sinking.",
 ["Distance sunk: 3 km.","Warming: 3 × 10 = 30 °C.","−5 + 30 = 25 °C. This is why sinking air in ridges bakes the surface."])
mcq(T,3,1.8,"Why do doctors worry when wet-bulb temperature reaches about 35 °C, even for a healthy person resting in shade?",
 ["Skin is near 35 °C, so heat cannot flow out and sweat cannot evaporate","Wet air is poisonous","Sweat glands run out of water at 35 °C","The body stops making heat"],
 "Cooling needs a temperature gap or evaporation; at this point both fail.",
 ["Heat flows from hot to cold. Skin at about 35 °C cannot dump heat into 35 °C air.","At 35 °C wet-bulb the air is nearly saturated, so sweat will not dry.","With both routes shut, the core temperature climbs like a locked car."])
mcq(T,3,1.3,"Which statement about a heat dome is true?",
 ["It is a strong ridge where sinking air warms, acting like a lid over the region","It is a bubble of cold air","It is a hurricane eye","It forms only over oceans"],
 "A heat dome is a persistent strong high-pressure ridge.",
 ["The ridge pushes air down and traps heat like a pot lid.","Under the lid the air is warm, dry and stagnant.","Heat dome and blocking ridge are close cousins in the same pattern."])
txt(T,2,0,"Name the type of drought when streams, lakes and reservoirs run low.",["hydrological","hydrologic","hydrological drought"],"Water supply is what is short.",
 ["Rain deficit is meteorological; dry soil is agricultural.","Low surface and groundwater supply is hydrological (hydro = water).","These can lag each other by months."])

# ================= PRECIP =================
T="precip"
num(T,1,-0.8,"How many inches of fast-moving flood water can knock an adult off their feet?",6,"in","Six inches can knock you down; about 12 can carry away a car.",
 ["Moving water pushes harder than it looks, like a strong wave at the beach.","Six inches can sweep your feet away.","Twelve inches can float and carry a car. So turn around, don't drown."])
txt(T,1,-0.8,"Hail with a diameter of about 1 inch is the size of which coin?",["quarter","a quarter"],"1 inch is quarter size, the NWS severe hail threshold.",
 ["Pea is ¼ in, penny ¾ in, quarter 1 in.","One inch or bigger counts as severe hail.","Learn the coin ladder: pea, penny, quarter, golf ball, baseball."])
order(T,2,0,"Order hail sizes from smallest to largest.",["Pea","Penny","Quarter","Golf ball","Baseball"],
 "Pea ¼ in, penny ¾ in, quarter 1 in, golf ball 1¾ in, baseball 2¾ in.",
 ["Use the numbers: ¼, ¾, 1, 1¾, 2¾ inches.","The quarter marks the severe threshold.","Bigger stones need stronger updrafts."])
mcq(T,1,-0.5,"A flash flood WATCH means…",
 ["Conditions could lead to flash flooding; be ready","Flash flooding is happening now","The river has crested","Rain has ended"],
 "Watch means be ready; warning means act now.",
 ["A watch is like ingredients on the counter: a flood could be cooked up.","A warning means the flood is happening or about to.","Misconception: watch and warning are the same."])
match(T,2,0,"Match each precipitation type to how it forms.",
 [["Rain","Warm all the way down, or warm layers melt snow"],["Snow","Cold all the way down"],["Sleet","Melted drops refreeze in a deep cold layer near the ground"],["Freezing rain","Liquid drops freeze when they touch cold surfaces"]],
 "The temperature layers a drop falls through decide its type.",
 ["Picture a drop riding an elevator through layers.","Sleet refreezes before landing; freezing rain stays liquid until it hits.","Both need a warm layer aloft."])
order(T,2,0,"Order the steps of sleet formation.",
 ["Snow falls from the cloud","Snow melts in a warm layer aloft","Drops fall into a deep cold layer near the ground","Drops refreeze into ice pellets"],
 "Sleet is snow that melts, then refreezes before reaching the ground.",
 ["It is like a snowball dipped in water and then put in the freezer.","The cold layer near the ground is deep enough to refreeze drops.","If that cold layer is shallow, you get freezing rain instead."])
mcq(T,2,0,"A cloud at −15 °C holds both supercooled droplets and ice crystals. What happens?",
 ["Ice crystals grow while droplets shrink","Droplets grow while ice shrinks","Both stay the same","Both freeze at once"],
 "Water vapor prefers to deposit on ice, so ice grows at the droplets' expense.",
 ["Ice crystals are bullies that steal moisture from nearby droplets.","Air saturated for water is extra saturated for ice, so vapor goes onto ice.","This is the Bergeron process."])
mcq(T,2,0,"A tropical cloud top never gets below freezing. How does rain form?",
 ["Droplets collide and merge (collision-coalescence)","Ice crystals grow by the Bergeron process","Snow melts into rain","Riming of graupel"],
 "Warm clouds make rain only by droplets colliding.",
 ["Big droplets fall faster, run into small ones and swallow them, like a snowball rolling downhill.","No ice means no Bergeron process.","Misconception: all rain starts as snow."])
num(T,2,0,"Fluffy snow has a 15:1 ratio. If the liquid equivalent is 2 cm, how many cm of snow fall?",30,"cm","Snow depth = liquid × ratio.",
 ["Ratio 15:1 means 15 cm of snow for each 1 cm of liquid.","2 × 15 = 30 cm.","Warm wet snow has a lower ratio, around 5:1 to 8:1."])
num(T,2,0,"A rain gauge catches 0.75 inch in 15 minutes. What is the rate in inches per hour?",3,"in/hr","Rate = amount ÷ time.",
 ["15 minutes is ¼ hour.","0.75 ÷ 0.25 = 3 in/hr.","Always convert to the unit asked before dividing."])
mcq(T,2,0,"Compared with a forest, a paved parking lot makes the flood peak…",
 ["Arrive sooner and higher","Arrive later and lower","Arrive at the same time","Disappear"],
 "Pavement sheds water quickly.",
 ["Forest soil is a sponge; pavement is a slide.","Water slides to drains and creeks within minutes.","Result: shorter lag time and a bigger peak."])
multi(T,2,0,"Select ALL conditions that raise flash flood risk.",
 ["Recent burn scar","Steep terrain","Saturated soil","Slow-moving thunderstorm","Gentle drizzle on absorbent soil","Thick forest leaf litter"],[0,1,2,3],
 "Fast runoff plus heavy rain over one place causes flash floods.",
 ["Burned ground repels water and steep slopes speed it.","Saturated soil cannot take more, like a full sponge.","Drizzle on absorbent ground or leaf litter soaks in."])
mcq(T,2,0,"Why does a 100-year flood not mean it only happens once every 100 years?",
 ["It means a 1% chance each year, and it can happen in back-to-back years","It is guaranteed once per century","It cannot happen twice","It means 100 inches of rain"],
 "Return period is an average, not a schedule.",
 ["Each year is like a fresh roll of a 100-sided die.","Rolling a 1 this year does not lower next year's chance.","Misconception: after one, we are safe for 100 years."])
mcq(T,3,1.0,"A hailstone cut open shows alternating clear and cloudy layers. What does that tell you?",
 ["It was carried through zones with different amounts of supercooled water, often lofted more than once","It froze all at once","It fell from a cold cloud","It formed from sleet"],
 "Layers record the stone's trips through the storm.",
 ["Like tree rings, layers show growth history.","Clear ice forms when lots of supercooled water freezes slowly; cloudy ice when less.","The stone rose and fell in the updraft, gaining layers."])
mcq(T,3,1.0,"Which weather map clue means a shallow below-freezing layer at the surface with warm air above?",
 ["Freezing rain","Sleet","Snow","Hail"],
 "Rain has no time to refreeze in a shallow cold layer, so it freezes on contact.",
 ["Sleet needs a deep cold layer for refreezing in the air.","Shallow cold layer: drops stay liquid, then freeze when they hit cold roads and wires.","Surface at 28 °F and rain falling is the classic ice storm setup."])
mcq(T,3,1.3,"A forecast sounding shows a warm layer at 2 km and a 1.5 km deep subfreezing layer below it. Which precipitation is most likely?",
 ["Sleet","Freezing rain","Snow","Rain"],
 "A deep cold layer lets melted drops refreeze before landing.",
 ["Snow melts at 2 km, then falls through 1.5 km of cold air.","Long exposure refreezes drops into pellets.","Misconception: freezing rain is the worst case everywhere. Layer depth decides."])
mcq(T,3,1.2,"A 40% chance of rain in a forecast means…",
 ["A 40% chance that measurable rain (at least 0.01 in) falls at any given point in the forecast area","It will rain on 40% of the day","40% of the area will get rain for sure","It will rain for 40% of the day everywhere"],
 "PoP is the chance of measurable rain at a point.",
 ["Think of rolling a 10-sided die for your backyard: 4 out of 10 times you get wet.","It is a probability, not a share of time or area.","Forecasters combine confidence and area covered."])
mcq(T,3,1.2,"Why do the biggest, most delicate snow crystals often grow near −15 °C?",
 ["The gap between vapor pressure over water and over ice is largest there, so ice grows fastest","It is warmer than 0 °C there","There are no droplets there","Wind is calm there"],
 "Ice growth by vapor deposition peaks around −12 to −18 °C.",
 ["At −15 °C the Bergeron effect is strongest; ice grabs moisture fastest.","Fast growth in humid air makes branching arms (dendrites).","Colder or warmer, crystals are plainer."])
mcq(T,2,0,"Storm A has updrafts of 15 m/s and Storm B has 35 m/s. Which can grow bigger hail?",
 ["Storm B, because strong updrafts hold heavier stones up longer","Storm A, because weak updrafts are gentler","Equal, because hail depends only on temperature","Storm A, because stones fall faster"],
 "Stones keep growing only while the updraft holds them up.",
 ["A heavier stone needs a stronger wind to float, like a bigger leaf needing a stronger gust.","Longer time in the cold supercooled zone means more riming.","Weak updrafts drop small stones early."])
num(T,3,1.3,"A storm drops 25 mm of rain evenly over 10 km². What volume of water fell, in cubic meters? (1 km² = 1,000,000 m²)",250000,"m³","Volume = area × depth, in meters.",
 ["Convert: 10 km² = 10,000,000 m²; 25 mm = 0.025 m.","10,000,000 × 0.025 = 250,000 m³.","That is about 100 Olympic pools from a modest rain."])
mcq(T,3,0.9,"A dry desert wash floods during clear skies overhead. Why?",
 ["Rain fell upstream and the runoff arrived down the channel","Dew formed rapidly","Hail melted overhead","The ground made water"],
 "Flash floods can be far from the rain.",
 ["Water flows downhill like cars on a highway, arriving long after rain starts.","Hard dry ground adds fast runoff.","Do not camp in washes when storms are nearby."])
mcq(T,3,0.9,"Which snow gives more depth for the same amount of liquid?",
 ["Cold, light powder at −15 °C","Wet snow near 0 °C","Both give equal depth","Sleet"],
 "Cold snow has more air in it.",
 ["Powder is like a fluffy pillow; wet snow is packed like a snowball.","Powder ratios can reach 20:1 or more, wet snow 5:1 to 8:1.","Same liquid, more depth for powder."])
mcq(T,3,1.1,"Rain falls on deep snow during a warm spell. Why is flooding likely?",
 ["Rain adds water and speeds melting, so the snowpack releases a lot at once","Snow absorbs all rain forever","Snow cools the rain","Rain freezes into the snow"],
 "Rain-on-snow combines new water and melted water.",
 ["Snowpack is a frozen reservoir. Warm rain opens the tap.","The pack can only hold so much liquid.","Add frozen ground that blocks soaking and rivers rise."])
num(T,3,1.2,"What is the chance (nearest %) of at least one 25-year flood in 25 years? Use 1 − 0.96^25.",64,"%","Chance of at least one = 1 minus chance of none.",
 ["Each year the flood misses with probability 0.96.","Missing 25 years in a row: 0.96^25 ≈ 0.36.","1 − 0.36 = 0.64, so 64%. Not 100%: a 25-year flood is not guaranteed in 25 years."],tol=0.02)
num(T,3,1.5,"A warmer climate changes a 100-year rainfall to a 50-year event. What is the chance (%) of at least one in 30 years now? Use 1 − 0.98^30.",45.5,"%","New yearly chance is 2%.",
 ["Return period 50 years: 1 ÷ 50 = 2% per year.","Miss all 30 years: 0.98^30 ≈ 0.545.","1 − 0.545 ≈ 0.455, 45.5%. Compare 26% before."],tol=0.03)
num(T,3,1.3,"An IDF curve for a 100-year storm gives 0.7 in/hr over 6 hours. What total depth falls, in inches?",4.2,"in","Depth = intensity × duration.",
 ["Rate 0.7 in/hr for 6 hours.","0.7 × 6 = 4.2 in.","Shorter bursts have higher rates but less total depth, so longer storms add up to more water."])
mcq(T,3,1.0,"Why does a 100-year storm plot higher than a 10-year storm on an IDF chart at the same duration?",
 ["Rarer storms are more intense for the same duration","Longer return periods mean longer duration","It is a plotting error","Rarer storms are weaker"],
 "Rare storms are heavier.",
 ["Each curve is one return period.","A rarer storm needs a heavier rain rate at the same duration.","Read across at one duration to compare."])
txt(T,2,0,"What does the C in IDF curve stand for? Give the full word.",["curve"],"Intensity-Duration-Frequency curve.",
 ["I is intensity, D is duration, F is frequency.","The curve shows how heavy rain gets for each length of storm.","The frequency comes from the return period."])

# ================= LIGHT =================
T="light"
mcq(T,1,-1,"Which shelter is safest during a lightning storm?",
 ["A hard-topped car with windows up","A picnic shelter","A tree","An open convertible"],
 "Only a sturdy building or a hard-topped vehicle protects you.",
 ["The metal body carries current around you.","Open shelters and trees offer no protection and make you a target.","Rule: when thunder roars, go indoors."])
mcq(T,1,-0.5,"Someone is struck by lightning. Is it safe to touch and help them?",
 ["Yes, they carry no electric charge; call 911 and give first aid","No, they stay charged for an hour","No, wait for a doctor","Yes, but only with rubber gloves"],
 "A lightning victim does not hold charge.",
 ["Lightning passes through; it does not stay like a battery.","Call 911 and begin CPR if needed.","Move them away from the storm only if safe."])
num(T,1,-0.8,"The flash-to-bang time is 10 seconds. About how many miles away is the lightning?",2,"miles","Divide seconds by 5.",
 ["Sound takes about 5 s per mile.","10 ÷ 5 = 2 miles.","Light arrives almost instantly."])
mcq(T,2,0,"Which is closest to the temperature of the air in a lightning channel?",
 ["About five times hotter than the Sun's surface","About as hot as boiling water","About as hot as a stove","About room temperature"],
 "Lightning heats air to about 30,000 K.",
 ["The Sun's surface is about 5,800 K.","Lightning's tiny channel reaches roughly 30,000 K.","That extreme heat makes thunder."])
mcq(T,2,0,"What causes thunder?",
 ["Air heated suddenly by lightning expands faster than sound, making a shock wave","Clouds bumping together","Raindrops hitting the ground","Wind in the cloud"],
 "Superheated air expands explosively.",
 ["Like a popped balloon, sudden expansion makes a bang.","The channel is the long balloon, so thunder rumbles.","No collision of clouds is involved."])
mcq(T,2,0,"Most lightning flashes stay…",
 ["Inside clouds (intracloud)","On the ground","Between clouds only","Within clear air only"],
 "Intracloud flashes outnumber cloud-to-ground flashes.",
 ["Charge centers sit in the same cloud, so a spark between them is easiest.","Roughly three of four flashes never reach the ground.","Cloud-to-ground ones get attention because they hurt people."])
mcq(T,2,0,"Where is the main positive charge in a typical thunderstorm?",
 ["High in the cloud","Low in the cloud","In the rain only","Underground only"],
 "Light positive ice crystals are carried up.",
 ["Updraft lifts small crystals up; heavy graupel stays lower.","So positive is on top and negative below.","The ground below becomes positive."])
order(T,2,0,"Order the steps of a cloud-to-ground flash.",
 ["Charge builds in the cloud","Stepped leader moves down","Streamer rises from the ground","Return stroke flashes up"],
 "The bright flash is the return stroke going up.",
 ["The leader zigzags down invisibly.","A streamer reaches up and they connect.","The big surge travels up, lighting the channel."])
match(T,2,0,"Match each term to its meaning.",
 [["Stepped leader","Faint channel heading down"],["Streamer","Spark reaching up from the ground"],["Return stroke","Bright surge up the channel"],["Thunder","Sound of heated air expanding"]],
 "Each step has a role.",
 ["Leader goes down, streamer goes up, return stroke is the bright part.","Thunder comes after.","The flash looks like it goes down but it surges up."])
mcq(T,2,0,"Flash-to-bang counts are 20 s, then 15 s, then 10 s. What is the storm doing?",
 ["Approaching","Moving away","Staying put","Weakening"],
 "Shorter delays mean the storm is closer.",
 ["Shorter gaps mean less distance for sound.","Approaching means the risk is rising.","Longer gaps would mean moving away."])
mcq(T,2,0,"Flash-to-bang is 24 seconds. According to the 30-30 rule, what should you do?",
 ["Go indoors now","Keep playing","Wait for 40 s","Go under a tree"],
 "30 seconds or less means go inside.",
 ["24 s is about 5 miles.","Lightning can strike up to 10 miles away, so be safe.","After the last thunder, wait 30 minutes."])
mcq(T,2,0,"A lightning rod protects a building because it…",
 ["Gives lightning an easy path to the ground","Attracts and stores lightning","Repels lightning","Absorbs thunder"],
 "It guides the current harmlessly to the ground.",
 ["Like a gutter for a downpour, it carries the strike safely.","Thick wire goes into the ground.","Without it, current finds the building wiring."])
mcq(T,3,1.0,"Lightning strikes the ground in clear sky about 8 miles from the storm. What is this called?",
 ["A bolt from the blue (from the anvil)","Heat lightning","A sprite","Ball lightning"],
 "Positive lightning can leap far from the storm.",
 ["The anvil's positive charge can travel sideways far away.","Strikes can come from a clear sky next to a storm.","It is the reason for the 30-minute wait."])
mcq(T,3,1.2,"Red flashes high above a thunderstorm are called…",
 ["Sprites","Stepped leaders","Return strokes","St. Elmo's fire"],
 "Sprites are transient luminous events above storms.",
 ["They occur far above the cloud top.","They are red and brief.","Different from ordinary lightning below."])
num(T,3,1.0,"Flash-to-bang is 25 s and the storm moves straight toward you at 20 mph. About how many minutes until it is overhead?",15,"min","Distance ÷ speed.",
 ["Distance: 25 ÷ 5 = 5 miles.","Time: 5 ÷ 20 = 0.25 h = 15 min.","But you should shelter right away since 25 s is inside the 30 s rule."])
num(T,3,1.3,"Speed of sound ≈ 331 + 0.6 × T m/s (T in °C). At 30 °C you hear thunder 8 s after the flash. How many meters away is the strike?",2792,"m","Compute speed, then multiply by time.",
 ["Speed: 331 + 0.6 × 30 = 349 m/s.","Distance: 349 × 8 = 2792 m.","Warm air speeds sound slightly, but the 5 s/mile rule is still good."],tol=0.02)
num(T,3,1.6,"At 12:00 flash-to-bang is 25 s; at 12:06 it is 10 s. The storm moves straight toward you. How fast (mph)?",30,"mph","Convert delays to miles, find change over time.",
 ["12:00: 25 ÷ 5 = 5 mi. 12:06: 10 ÷ 5 = 2 mi.","Moved 3 miles in 6 min = 0.1 h.","3 ÷ 0.1 = 30 mph."])
mcq(T,3,1.0,"Why does thunder rumble instead of sounding like a single bang?",
 ["Sound from different parts of the long channel arrives at different times","Thunder echoes only in valleys","Clouds absorb part of the sound","The bang is faster than light"],
 "The channel can be miles long.",
 ["Parts nearer to you arrive first; parts farther arrive later.","Like a long line of firecrackers.","Close strikes sound sharp."])
mcq(T,3,1.0,"Why is lying flat on the ground a bad choice in a storm?",
 ["It increases contact with current spreading across the ground","The ground is positively charged","Lightning only hits standing people","It keeps you from hearing thunder"],
 "Ground current spreads out from the strike point.",
 ["Current ripples across the ground like water from a splash.","More body in contact means more current through you.","Crouch only as a last resort, minimal contact."])
mcq(T,3,1.0,"Why is a hard-topped car safe?",
 ["The metal shell carries current around you","The rubber tires insulate","The windows are glass","Cars are not charged"],
 "It is the metal body, not the tires.",
 ["Current flows on the outside of the metal.","Tires cannot insulate against millions of volts.","Keep windows up and avoid touching metal."])
mcq(T,3,1.1,"Why does lightning not start the instant charge separates in the cloud?",
 ["Air is an insulator until the electric field becomes strong enough","Charges are not strong","The ground is too far","Rain blocks it"],
 "Breakdown requires a very strong field.",
 ["Air acts like a thick rubber band that can hold stress until it snaps.","The field must grow until air breaks down.","Then the spark runs."])
mcq(T,3,1.0,"Why does the main storm cloud base turn the ground below positive?",
 ["The negative base pushes electrons away, leaving surface positive","Rain carries positive","Sun warms ground","Wind blows positive"],
 "Opposite charges attract.",
 ["Like a magnet pushes same poles away.","Electrons flee, leaving positive.","Opposite charges attract each other across the gap."])
num(T,3,1.6,"Lightning sensors use radio wave arrival times. A timing error of 2 microseconds corresponds to how many meters of location error? (radio speed 300,000,000 m/s)",600,"m","Distance = speed × time.",
 ["2 µs = 0.000002 s.","300,000,000 × 0.000002 = 600 m.","That is why sensors need extremely precise clocks."])
mcq(T,3,1.4,"Which instrument detects lightning from space?",
 ["GOES Geostationary Lightning Mapper","Rain gauge","Radiosonde","Anemometer"],
 "GLM watches flashes from geostationary orbit.",
 ["It stares at the same area from far above.","It detects optical flashes.","Ground networks use radio timing."])
mcq(T,3,1.3,"Why does graupel become negatively charged while ice crystals become positive?",
 ["Collisions transfer charge, and the heavier graupel falls while crystals rise","Rain gives it","Sunlight causes it","Air friction with fog"],
 "Charge transfers in collisions then sorting by weight.",
 ["Collisions pass tiny charges, like rubbing a balloon.","Updrafts carry light crystals up, graupel falls.","The result is a separated charge."])
mcq(T,2,0,"Why wait 30 minutes after the last thunder?",
 ["Lightning can still strike from the storm's trailing area","Thunder echoes for 30 min","Rain lasts 30 min","The cloud grows"],
 "A storm's back edge can still strike.",
 ["Strikes can still occur after the rain ends.","Waiting protects you.","Do not rush out."])

# ================= TSTORM =================
T="tstorm"
mcq(T,1,-0.8,"A SEVERE THUNDERSTORM WARNING means…",
 ["A severe storm is happening or about to, take cover","A severe storm could form later today","Only lightning is likely","The storm has ended"],
 "Warning means act now.",
 ["Watch: conditions favorable. Warning: severe storm detected.","Warnings come from radar or spotters.","Go to shelter."])
num(T,1,-0.5,"What is the minimum wind speed, in mph, for a thunderstorm to be called severe?",58,"mph","NWS severe wind is 58 mph.",
 ["58 mph equals 50 knots.","Other criteria: hail 1 inch, or a tornado.","Any one makes it severe."])
num(T,2,0,"A storm 36 miles away moves toward you at 48 mph. In how many minutes does it arrive?",45,"min","Time = distance ÷ speed.",
 ["36 ÷ 48 = 0.75 h.","0.75 × 60 = 45 min.","Convert hours to minutes."])
num(T,2,0,"Convert 58 mph to knots (1 kt = 1.15 mph), nearest knot.",50,"kt","Divide by 1.15.",
 ["58 ÷ 1.15 = 50.4.","About 50 kt.","Knots are used by radar and aviation."],tol=0.03)
order(T,1,-0.5,"Order the thunderstorm life cycle.",["Cumulus","Mature","Dissipating"],
 "Updraft only, then both, then downdraft only.",
 ["Cumulus is building.","Mature is the worst weather.","Dissipating has downdraft."])
multi(T,2,0,"Select ALL that make a storm severe by NWS criteria.",
 ["Hail 1 inch or larger","Wind gusts 58 mph or more","A tornado","Hail 0.75 inch","Wind gusts of 40 mph","Frequent lightning only"],[0,1,2],
 "Hail, wind or tornado.",
 ["Penny hail is below threshold.","40 mph is below 58.","Lightning alone does not count."])
match(T,2,0,"Match each storm type to its trait.",
 [["Single-cell","Short-lived, one cell"],["Multicell","Cluster in different stages"],["Supercell","Rotating updraft"],["MCC","Large round long-lived cluster"]],
 "Each type has a defining trait.",
 ["Single cell rains out.","Multicells renew.","Supercells rotate."])
mcq(T,2,0,"Why does a single-cell pulse storm die in about an hour?",
 ["Its own rain-cooled downdraft cuts off the updraft","The Sun sets","The ocean cools it","It runs out of dust"],
 "It rains out its own fuel.",
 ["Falling rain drags air down.","Downdraft falls into the updraft.","Cuts off warm air."])
mcq(T,2,0,"How does a gust front help a multicell storm renew?",
 ["Cool outflow lifts warm moist air to form new cells","It stops the storm","It adds hail","It rotates"],
 "Outflow acts like a plow.",
 ["A plow pushes snow up.","Warm air lifted into new storms.","Cells form along the outflow."])
mcq(T,2,0,"Why does the top of a thunderstorm spread out into an anvil?",
 ["The updraft hits a stable layer at the tropopause and spreads sideways","Wind blows only there","It is made of ice only","The Sun pulls it"],
 "Air can't rise further.",
 ["Like water hitting a ceiling.","The tropopause is stable.","Anvil points downwind."])
mcq(T,2,0,"What is a derecho?",
 ["A widespread, long-lived windstorm with straight-line damaging winds","A large tornado","A big hailstorm","A hurricane remnant"],
 "Straight-line winds over a long path.",
 ["It comes from a fast-moving line of storms.","Damage in a swath hundreds of miles.","Not a tornado."])
mcq(T,3,1.0,"Trees in a field all lie pointing the same direction. Which is more likely?",
 ["Straight-line wind (downburst)","A tornado","Hail","A waterspout"],
 "Tornado damage converges or twists.",
 ["Straight-line wind pushes everything one way.","Tornado debris is crossed.","Survey patterns tell storm type."])
mcq(T,3,1.2,"A strong cap over a warm moist area breaks at 5 pm. What can follow?",
 ["Explosive storm development","No storms","Gentle rain","Fog only"],
 "A capped atmosphere builds energy.",
 ["Like a pressure cooker lid.","When the lid breaks, air bursts up.","Storms then explode."])
mcq(T,3,1.2,"Two storms have equal updrafts. One has a freezing level at 2 km, the other at 4.5 km. Which gives larger hail at the surface?",
 ["The 2 km freezing level, since less melting before landing","The 4.5 km level","Equal","Neither"],
 "Hail melts in warm air.",
 ["Less warm fall distance means less melting.","More depth for stones to grow cold.","Lower freezing level favors larger stones."])
mcq(T,3,1.5,"A bounded weak echo region on radar shows…",
 ["A strong updraft carrying rain aloft so none falls there","A tornado debris","A hail core","A cold front"],
 "A BWER marks strong updraft.",
 ["Updraft holds precipitation up.","Leaves a hole in the echo.","Seen in supercells."])
mcq(T,3,1.0,"A hook echo on radar suggests…",
 ["Rotation in the storm; tornado possible","Hail only","Heavy fog","Calm winds"],
 "Hook shape wraps around rotation.",
 ["Rain wraps around rotating updraft.","Mesocyclone indicator.","Not proof of a tornado."])
mcq(T,3,1.4,"Mean winds blow from the west. Which direction does a right-moving supercell tend to travel in the Northern Hemisphere?",
 ["East-southeast, to the right of the mean wind","West-northwest","Due north","Exactly with the mean wind"],
 "Supercells deviate right.",
 ["Rotation creates a push to the right.","Multicells follow the mean wind.","Supercells veer."])
num(T,3,1.6,"Using max updraft speed ≈ √(2 × CAPE), what is the theoretical updraft (m/s) for CAPE of 1800 J/kg?",60,"m/s","Plug into the formula.",
 ["2 × 1800 = 3600.","√3600 = 60 m/s.","Real updrafts are weaker."])
num(T,3,1.2,"A storm is 60 miles away at 3:00 and 40 miles away at 3:30, same track. How many minutes after 3:30 does it arrive?",60,"min","Speed from change in distance.",
 ["20 miles in 30 min = 40 mph.","40 ÷ 40 = 1 h.","60 minutes."])
num(T,3,1.2,"Wind force on a wall scales with wind speed squared. If gusts go from 30 mph to 60 mph, by what factor does force grow?",4,"×","Square the ratio.",
 ["Ratio 2.","2² = 4.","Small speed rises produce big damage."])
mcq(T,3,1.5,"A dry microburst forms under a high-based cloud. Why does the air sink fast?",
 ["Rain evaporates in dry air, cooling it so it becomes dense and sinks","Warm air rises","Hail falls","Cold front"],
 "Evaporation cools.",
 ["Evaporation takes heat.","Cold air is heavy.","It crashes down."])
mcq(T,3,1.2,"A dome above the anvil, called an overshooting top, shows…",
 ["A very strong updraft pushing into the stable layer","A weak storm","A tornado","Dissipation"],
 "Strong updraft overshoots.",
 ["Like a geyser.","Severe signal.","Short lived."])
mcq(T,3,1.0,"Storms repeatedly move over the same area. Why does this cause flash flooding?",
 ["Repeated heavy rain over one place adds up, like train cars on one track","Rain gets lighter","Soil dries","Wind speeds drop"],
 "Training of cells.",
 ["Like train cars.","Rain adds up.","Flash flood risk."])
mcq(T,3,1.0,"Along a dry line, which air masses meet?",
 ["Moist air and dry air","Warm and cold","Two moist","Two dry"],
 "Dry line is a moisture boundary.",
 ["Southern Plains.","Storms form on it.","Lift occurs."])
mcq(T,3,1.8,"A forecast has high CAPE, strong deep-layer shear, and a cap holding until 5 pm. Best statement?",
 ["If the cap breaks, supercells with large hail and tornado risk are likely","Only light showers","No storms","Fog"],
 "Fuel + shear + trigger.",
 ["High CAPE is fuel.","Shear organizes.","Cap breaking triggers."])
num(T,3,1.8,"Convert a theoretical 70 m/s updraft to mph (1 m/s = 2.237 mph), nearest mph.",157,"mph","Multiply by 2.237.",
 ["70 × 2.237 = 156.6.","About 157 mph.","Real updrafts are weaker."],tol=0.02)
mcq(T,3,1.0,"Why does wind shear help storms last?",
 ["It tilts the updraft so rain falls away and does not choke it","It adds moisture","It cools","It stops rotation"],
 "Tilt separates updraft and downdraft.",
 ["Like leaning a chimney.","Rain falls beside.","Storm lives longer."])

# checks
assert math.sqrt(2*1800)==60 and abs(70*2.237-156.6)<.1
assert round(1-0.96**25,2)==0.64 and round(1-0.98**30,3)==0.455 and 349*8==2792
assert 3/0.1==30 and round(58/1.15)==50

fix={
"dh-031":{"q":"The emergency condition when the body's cooling system fails, sweating stops and skin turns hot and dry is heat…","text":["stroke","heat stroke"],"w":"Heat stroke is an emergency: call 911.","sol":["In heat stroke the body's sweat cooling fails.","Core temperature climbs past 104 °F and the brain is affected.","Heat exhaustion is milder: heavy sweating and weakness."]},
"dh-005":{"o":["Dry, hardened ground absorbs water slowly","Dry soil adds extra water","Clouds hold less rain after a drought","Rain on dry ground always evaporates"],"w":"Baked soil sheds water like a roof, so runoff floods creeks.","sol":["Dry clay is hard, like a dry sponge that repels water.","Water cannot soak in fast, so it runs off.","Drought and flooding can happen in the same place."]},
"dh-036":{"q":"What is the main reason a drought raises wildfire risk?","text":["dry plants","dry vegetation","dry fuel","dry"],"w":"Dry plants are easy fuel; a spark spreads fast."},
"dh-030":{"l":1,"b":-1},
"precip-013":{"l":1,"b":-0.5},
"precip-011":{"l":2,"b":0.2},
"precip-012":{"l":2,"b":0.3},
"precip-025":{"q":"Sleet is…","o":["Ice pellets formed when melted snow refreezes before landing","Rain that freezes on contact","Hail from a thunderstorm","Fog that freezes"],"w":"Sleet is refrozen snowmelt falling as ice pellets."},
"precip-026":{"o":["Coats surfaces with ice","Is heavier than snow","Falls silently","Gives no warning"]},
"tstorm-009":{"l":2,"b":0.3},
"tstorm-043":{"l":2,"b":0.3},
"tstorm-050":{"text":["downburst","microburst"],"q":"A strong rush of sinking air that spreads out at the ground and can cause straight-line wind damage is called a…"},
"light-051":{"w":"Most cloud-to-ground strikes carry negative charge down."},
}
dele=["dh-024","dh-026","dh-028","light-059","tstorm-041","tstorm-044","tstorm-046","tstorm-048","precip-024","precip-031","light-052"]
d=dict(fix=fix,**{"del":dele},del_family=["cf1","cf2","th1","th2","mo1"],new=new,
 report="")
d["report"]=f"Fixed {len(fix)}, deleted {len(dele)} singles + 5 families (cf1,cf2 temp conversions; th1,th2 lightning timing; mo1 storm arrival; replaced by varied items), added {len(new)} (dh/precip/light/tstorm). Remaining doubt: simplified rule-of-thumb items (CAPE updraft, right-moving supercell)."
json.dump(d,open(OUT,"w"),ensure_ascii=False,indent=1)
import collections
print(len(new),collections.Counter((q['t'],q['l']) for q in new))
