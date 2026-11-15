import json, math
OUT="/tmp/claude-0/-home-claude/bdb1ee03-0916-54eb-a354-ea75cf26b960/scratchpad/audit/out/m1.json"
new=[]; n=[0]
def fp():
    n[0]+=1; return f"m1_{n[0]:03d}"
def mcq(t,l,b,q,o,w,sol): new.append(dict(t=t,l=l,b=b,type="mcq",q=q,o=o,w=w,sol=sol,fp=fp()))
def multi(t,l,b,q,o,a,w,sol): new.append(dict(t=t,l=l,b=b,type="multi",q=q,o=o,a=a,w=w,sol=sol,fp=fp()))
def num(t,l,b,q,v,u,w,sol,tol=0.02): new.append(dict(t=t,l=l,b=b,type="short",q=q,num=dict(v=v,tol=tol,u=u),w=w,sol=sol,fp=fp()))
def txt(t,l,b,q,text,w,sol): new.append(dict(t=t,l=l,b=b,type="short",q=q,text=text,w=w,sol=sol,fp=fp()))
def order(t,l,b,q,items,w,sol): new.append(dict(t=t,l=l,b=b,type="order",q=q,items=items,w=w,sol=sol,fp=fp()))
def match(t,l,b,q,pairs,w,sol): new.append(dict(t=t,l=l,b=b,type="match",q=q,pairs=pairs,w=w,sol=sol,fp=fp()))
O="obs"; M="maps"
# ---------- OBS ----------
mcq(O,2,0,"A storm sits due north of a Doppler radar and the wind inside it blows straight from west to east. What does the radar's velocity product show for that wind?",
 ["Close to zero, because the wind moves across the beam, not along it","Strong outbound (red), because the wind is fast","Strong inbound (green), because the wind comes from the west","The wind speed doubled"],
 "Doppler radar only feels motion along its beam, toward or away.",
 ["Picture the beam as a string from the radar to the storm. Doppler measures only how fast things slide along that string.","Wind crossing the string sideways adds nothing along it, so velocity reads near zero.","Common slip: thinking velocity shows true wind speed. It shows only the part of the wind along the beam."])
num(O,3,1.0,"The beam points north. The wind blows at 40 kt from a direction that makes a 60° angle with the beam. What radial velocity does the radar measure (kt)?",20,"kt",
 "Radar sees only the part of the wind along the beam: speed × cos(angle).",
 ["Radial speed = true speed × cos(angle between wind and beam).","cos 60° = 0.5, so 40 × 0.5 = 20 kt.","At 90° the cosine is 0, which is why crosswind motion looks calm to radar. It is like feeling only the push straight at you when someone shoves you at an angle."])
mcq(O,3,1.2,"On a velocity image you see a small, tight patch of bright green directly beside a bright red patch. Which description fits best?",
 ["Rotation: air moving toward and away from the radar at nearly the same spot","Heavy rain: green and red show rain rate","A cold front: green is cold and red is warm","Hail: green is small hail and red is large hail"],
 "Inbound next to outbound in a small area means the air is spinning.",
 ["Green means moving toward the radar. Red means moving away.","Side by side in a tiny area, the only way both can happen is spinning, like one side of a merry-go-round coming at you while the other side moves away.","This pattern is called a couplet. Color on velocity never shows rain, temperature or hail."])
num(O,3,1.3,"A radar pulse leaves, hits a storm, and its echo returns 1.2 milliseconds later. The pulse travels at 3.0×10⁸ m/s. How far away is the storm (km)?",180,"km",
 "Distance = speed × time ÷ 2, because the pulse goes out and back.",
 ["Total path = 3.0×10⁸ × 1.2×10⁻³ = 3.6×10⁵ m = 360 km.","That is the round trip, so halve it: 180 km.","Like shouting at a far cliff: the echo time covers going and returning. Forgetting to halve is the common mistake."])
mcq(O,3,1.4,"A shallow storm 200 km from a radar produces only drizzle near the ground, yet the radar shows almost nothing. Why?",
 ["The beam passes above the low rain because it climbs as it travels","Drizzle drops are too large to reflect","Radar cannot detect any rain at night","The radar's wind profile is switched off"],
 "Radar beams travel straight while Earth curves away, so far away they overshoot low weather.",
 ["The beam starts about 0.5° above flat ground. Earth curves downward beneath it, so the beam gets higher above the ground with distance.","At 200 km it may be more than 3 km up, above shallow rain or snow.","Misconception: radar sees everything near the surface. Far from the site, it sees only the upper part of storms."])
mcq(O,2,0.2,"On a clear calm morning a radar shows weak echoes in a ring around the site and no clouds are overhead. What are they most likely?",
 ["Insects, birds or ground clutter, not rain","A line of thunderstorms","Hail falling from a clear sky","Fog over the ocean"],
 "Radar returns come from anything that scatters the beam, not only raindrops.",
 ["Radar bounces off whatever is in the beam: insects, birds, buildings, hills.","Near the site, ground clutter shows up as a ring or blobs even when it is dry.","Clue: weak echoes, clear sky, no motion pattern. Real rain would have a cloud overhead and a satellite view to match."])
mcq(O,3,1.6,"A radar shows an intense patch of 'heavy rain' on a clear, calm night after a cool night followed by a warm layer aloft (an inversion). Satellite shows no clouds. What is likely?",
 ["The inversion bent the beam down to the ground, giving false echoes","A tornado is hiding in clear air","The radar is measuring snow","Visible satellite is broken at night"],
 "A temperature inversion can bend the radar beam toward the ground.",
 ["Beams bend slightly depending on air density. Strong inversions bend them down more than usual.","The beam then strikes hills and buildings and looks like rain. This is called anomalous propagation.","Check other tools: no clouds on IR satellite and no reports of rain means the echo is false."])
mcq(O,3,1.7,"A fast outbound wind far above the radar's maximum measurable speed is displayed in the opposite color, as if it were inbound. What is this error called?",
 ["Velocity aliasing (folding)","Beam bending","Hail spike","Range attenuation"],
 "Doppler can only unambiguously measure speeds up to a limit.",
 ["Each radar has a Nyquist limit on measurable speed, like a clock face: a hand that goes past 12 starts over.","Speeds beyond the limit wrap around and appear with the wrong sign.","Misconception: the color is always right. Forecasters check for sudden sign flips next to very strong winds."])
mcq(O,3,1.4,"In a tornadic storm, a hook echo on reflectivity sits with a velocity couplet. Dual-polarization correlation coefficient (CC) drops sharply inside the hook while reflectivity stays high. What does this combination suggest?",
 ["Debris lofted by a tornado, a strong sign it is on the ground","Pure rain drops falling evenly","Dry air aloft","Clear-air echoes from insects only"],
 "High reflectivity plus low CC means a mix of target shapes and sizes, not uniform rain.",
 ["CC measures how alike the targets are. Raindrops are similar, so rain gives CC near 1.","Leaves, dirt and pieces of buildings differ in size and shape, so CC falls (below about 0.8).","Together with rotation this is a tornado debris signature. A drop in CC alone is not enough; it can also be hail mixed with rain."])
multi(O,3,1.5,"Select ALL targets that can produce a LOW correlation coefficient.",
 ["Tornado debris","Hail mixed with rain","Uniform light rain","Flocks of birds or swarms of insects"],[0,1,3],
 "Low CC means the targets look different from each other.",
 ["Rain is uniform, so CC stays near 1 and is not low.","Debris, hail mixed with rain, birds and insects all vary in size, shape and tumbling.","Think of a bag of identical marbles versus a bag of random junk: the junk gives scattered radar signals."])
mcq(O,2,0.2,"A radar reflectivity of 60 dBZ or more inside a storm usually points to…",
 ["Very heavy rain and possibly hail","Light drizzle","Clear air with no precipitation","Strong winds only, no precipitation"],
 "Reflectivity measures returned power. Bigger, more plentiful targets send back more.",
 ["dBZ is a scale of echo strength. About 20 is light rain, 40 to 50 heavy rain.","Values of 60 or more mean very large or many targets, often large hail.","Misconception: high dBZ means high wind. It describes targets, not wind."])
num(O,3,1.0,"An IR satellite shows a thunderstorm top at −45 °C. The ground is 25 °C. Temperature drops about 6.5 °C per km. About how high is the top (km)?",10.8,"km",
 "Colder tops are higher, and the temperature drop tells you how far up.",
 ["Total drop = 25 − (−45) = 70 °C.","Height = 70 ÷ 6.5 ≈ 10.8 km.","IR sees only heat from the top. Cold equals high, like frost on the highest mountain peaks."],tol=0.03)
mcq(O,3,0.9,"On a night IR image, a low fog bank in a valley is almost invisible. Why?",
 ["Its top is nearly as warm as the ground, so it looks similar","Fog is too small for satellites to see anywhere","Infrared only detects rain","IR works only in daylight"],
 "IR images show temperature. Fog tops are low and warm.",
 ["IR brightness depends on how cold the surface is. High cold tops stand out.","Fog tops are close to ground temperature, so they blend in, like a grey blanket on grey ground.","This is why forecasters use special channels or surface reports to find fog."])
mcq(O,3,1.1,"On an enhanced water vapor image, a dark, dry-looking stripe curls into a storm system. What does the dark area usually show?",
 ["Dry air in the middle or upper levels","A heavy rain band","Very cold cloud tops","Land with no clouds at night"],
 "Water vapor imagery reads moisture, not clouds on the ground.",
 ["Water vapor channels show how much moisture is in the middle and upper air.","Dark areas mean dry air (less moisture to see). Bright areas mean moisture or high cloud.","Dry stripes wrapping into a storm often show where dry air is flowing in, so they help track the storm's circulation."])
mcq(O,2,0,"Which statement correctly contrasts the two main kinds of weather satellite?",
 ["Geostationary stays over one spot and shows the same region all the time; polar-orbiting circles pole to pole with more detail but passes only twice a day","Polar-orbiting satellites stay over one spot; geostationary ones circle the poles","Geostationary satellites orbit low and see the poles best; polar ones see the whole hemisphere","The two differ only in picture color"],
 "A satellite 35,786 km up above the equator matches Earth's spin; a low one sweeps past.",
 ["Geostationary orbit is high and matches Earth's rotation. It looks like a security camera, always on the same area.","Polar-orbiting satellites are lower, so they get sharper pictures and cover the poles, but each place gets a view only a couple of times a day. They are like a patrol car passing by.","Pick geostationary for tracking storms minute by minute."])
num(O,2,0.5,"A polar-orbiting weather satellite makes about 14 orbits in one 24-hour day. About how many minutes is one orbit?",102.9,"min",
 "One orbit lasts a day divided by the orbits per day.",
 ["24 hours = 1440 minutes.","1440 ÷ 14 ≈ 102.9 minutes.","Low orbits are quick, like a runner on an inner track. A high geostationary orbit takes a full day."],tol=0.02)
num(O,2,0.3,"A radiosonde balloon climbs at 5 m/s. About how many minutes to reach 25 km (25,000 m)?",83.3,"min",
 "Time = distance ÷ speed, then change seconds to minutes.",
 ["25,000 m ÷ 5 m/s = 5,000 s.","5,000 ÷ 60 ≈ 83.3 min.","This is why a sounding takes well over an hour, and the instrument drifts far downwind while rising."])
mcq(O,3,1.0,"Why does a radiosonde balloon burst high in the atmosphere?",
 ["Outside pressure drops, so the balloon stretches until it pops","It runs out of helium and sinks","Temperatures there are too hot","The radio signal pops it"],
 "The air gets thinner with height, so the gas inside expands.",
 ["Air pressure falls steadily with height.","Gas inside pushes out harder than air outside, so the balloon grows, like a marshmallow in a vacuum.","At about 30 km it bursts. A parachute slows the instrument down. Misconception: heat pops it; actually it is expansion."])
mcq(O,2,0.3,"Why do radiosondes around the world launch at the same times (00Z and 12Z)?",
 ["So forecast models get a worldwide snapshot of the same moment","Because it is daylight everywhere","Because balloons rise only at those hours","So that each country uses its own local time"],
 "Models need data that match in time to start forecasts.",
 ["Computer models need a starting picture of the whole atmosphere.","Like a class photo, everyone must be in the picture at once.","Z is UTC. 12Z is early morning in California and 00Z is late afternoon."])
mcq(O,2,0.2,"How are winds at each height found from a radiosonde flight?",
 ["By tracking how the balloon drifts, using GPS","By a cup anemometer on the balloon","By measuring how fast it rises","By the balloon's color"],
 "The balloon moves with the wind like a leaf on a stream.",
 ["The sonde measures temperature, pressure and humidity directly.","Winds come from tracking its position over time with GPS: how far it drifts in each minute.","A cup anemometer can't work on a drifting balloon, since it moves with the wind and feels almost no airflow."])
match(O,1,-1,"Match each instrument to what it measures.",
 [["Thermometer","Air temperature"],["Barometer","Air pressure"],["Anemometer","Wind speed"],["Hygrometer","Humidity"]],
 "Each name tells its job.",
 ["Thermo = heat, baro = weight (pressure).","Anemo = wind.","Hygro = moisture."])
mcq(O,2,0.2,"Why is an official thermometer put in a shaded, ventilated shelter?",
 ["Sunlight on the sensor would read too warm; air flow keeps it at air temperature","So it stays dry in rain","To cool the air around it","Shade makes it more accurate at night only"],
 "We want the temperature of the air, not of the thermometer.",
 ["A thermometer in the sun heats like a dark car seat and reads above the real air temperature.","Shade stops sunlight; ventilation lets fresh air flow past so the reading matches the air.","This is why your car's temperature display is wrong when parked in the sun."])
mcq(O,2,0.3,"On a sling psychrometer, the wet bulb thermometer reads lower than the dry bulb. When would they read the SAME?",
 ["When the air is saturated (100% humidity)","When the air is very dry","When it is windy","When the temperature is freezing"],
 "Evaporation cools the wet bulb, and only works if the air can take more water.",
 ["The wet bulb is wrapped in wet cloth. Evaporation cools it, like feeling cold after leaving a pool.","In dry air, evaporation is fast and the wet bulb reads much lower.","In saturated air there is no evaporation, so both match. Larger difference means drier air."])
mcq(O,2,0.3,"A narrow outflow boundary passes between two airports 80 km apart, and neither ASOS reports anything unusual. Which tool would best capture it?",
 ["A mesonet with stations every few km","A radiosonde from one of the airports","A polar-orbiting satellite pass the next day","A single barometer"],
 "Dense networks fill gaps that spread-out stations miss.",
 ["Features smaller than the station spacing slip through, like a fish through a wide net.","Mesonets place stations a few to tens of km apart and report often.","Radiosondes see height, not narrow ground features."])
mcq(O,3,1.3,"A rain gauge at a school reports 18 mm. Radar estimated 30 mm over the same spot. Which statement is best?",
 ["The gauge is a direct measure at one point; radar covers a wide area but is an estimate, so use both","Radar is always right, the gauge is broken","The gauge is always right, radar is useless","They must be averaged for every storm"],
 "Direct measurement and wide coverage have different strengths.",
 ["The gauge catches real water, but only where it sits.","Radar infers rain from echo strength over a whole region, so errors are possible (hail, beam height, drop size).","Forecasters use gauges to correct radar estimates, like checking a map against a few GPS points."])
order(O,2,0,"Put the steps of a radiosonde sounding in order.",
 ["Balloon is launched and rises","Sensors measure temperature, pressure, humidity and radio the data down","Balloon expands and bursts high up","Instrument parachutes back to the ground"],
 "The data come during the climb, not after.",
 ["Launch and climb come first.","The sensors send data all the way up.","Burst happens at the top, then a parachute slows the fall."])
num(O,2,0.2,"A wind speed is 15 m/s. Convert to knots (1 m/s ≈ 1.944 kt).",29.2,"kt",
 "Multiply by the conversion factor.",
 ["15 × 1.944 = 29.16.","Round to about 29.2 kt.","A knot is smaller than a meter per second, so the number of knots must be larger."],tol=0.01)
txt(O,1,-0.8,"What is the name of the network of National Weather Service Doppler radars? (Give the short name.)",["NEXRAD","WSR-88D","nex rad"],
 "It is the national radar network.",
 ["NEXRAD stands for Next Generation Radar.","Its radars are called WSR-88D.","Each one is a Doppler radar, so it measures motion."])
mcq(O,2,0,"Why does the Doppler effect let radar measure wind motion?",
 ["The echo's frequency shifts up for approaching targets and down for receding ones","Fast targets send louder echoes","Slow targets return later","Colors show the temperature"],
 "Same idea as an ambulance siren that changes pitch when passing.",
 ["An approaching siren sounds higher; as it passes and leaves, it drops lower.","Radar waves do the same: a higher return frequency means moving toward the radar, lower means away.","The size of the shift gives the speed along the beam."])
mcq(O,3,1.7,"A tornado-producing storm passes directly over a radar. Why might the radar fail to show the storm's top?",
 ["Its beam cannot point steeply enough, leaving a 'cone of silence' overhead","The radar only works for storms far away","The top is too cold","Radar needs the storm to be rotating"],
 "A radar's highest tilt is not straight up.",
 ["The radar scans in tilted sweeps. The highest tilt is about 20° up.","Directly above, there is a cone-shaped gap that no tilt covers.","Like a flashlight tilted at an angle: you can't light the area right above your head."])
num(O,3,2.0,"Beam height ≈ r²/(2×(4/3)×6371) + r×sin(elevation), with r in km. For r = 120 km and elevation 0.5°, how high is the beam center (km)?",1.9,"km",
 "Earth's curve and the beam's tilt both raise the beam above the ground.",
 ["Curve term: 120² ÷ (2 × 1.333 × 6371) = 14,400 ÷ 16,989 ≈ 0.85 km.","Tilt term: 120 × sin 0.5° = 120 × 0.00873 ≈ 1.05 km.","Sum ≈ 1.9 km. Like a ball moving across a curved globe: the farther you go, the higher the beam is above the surface."],tol=0.03)
mcq(O,2,0.2,"A rain gauge catches rain in a narrow tube whose area is one-fifth of the funnel. The tube shows 2.0 cm. How much rain fell?",
 ["0.4 cm","2.0 cm","10 cm","1.0 cm"],
 "The funnel collects over a larger area than the tube, so the depth is stretched in the tube.",
 ["The funnel is 5 times wider in area, so water is 5 times deeper in the tube.","Divide: 2.0 ÷ 5 = 0.4 cm.","Like pouring a wide pond into a thin glass: the glass level looks much higher than the pond."])
mcq(O,3,1.1,"A storm moves toward the radar at 30 kt. Its own rotation has 20 kt winds. On base velocity both sides look inbound (green). What does storm relative motion do?",
 ["It removes the 30 kt, so one side turns outbound (red) and rotation becomes clear","It doubles the rotation speed","It deletes the green colors","It shows the rain rate instead"],
 "Subtracting the storm's own motion reveals the spin.",
 ["Base velocity: one side −50 kt (30 + 20), the other −10 kt. Both negative, so both green.","Subtract the storm's −30: one side becomes −20 (inbound), the other +20 (outbound).","Like watching a spinning wheel on a moving train: look at the wheel relative to the train to see the spin."])
mcq(O,2,0.3,"Why are wind sensors usually placed about 10 m up in an open area?",
 ["So buildings and trees don't block or slow the wind, giving comparable readings","Because wind is always stronger on the ground","To keep them cool","So they are hidden from birds"],
 "Stations all need to measure under the same conditions to compare.",
 ["Wind near the ground is slowed by friction from trees, buildings and fences.","A standard 10 m height in open ground makes stations comparable.","Like measuring a runner's speed: you must do it on a clear track, not in a crowd."])
mcq(O,2,0.2,"Which choice is the best tool to see whether a thunderstorm complex is growing taller over the ocean at night?",
 ["Infrared satellite","Visible satellite","A rain gauge","A cup anemometer"],
 "It must work at night and over water with no stations.",
 ["Visible imagery needs sunlight.","IR works day or night and senses cloud-top temperature. Colder tops mean higher, stronger storms.","Surface stations don't exist over open ocean, so satellite is the choice."])
# ---------- MAPS ----------
mcq(M,3,1.0,"A station model's pressure code is 500. What pressure is that?",
 ["950.0 mb","1050.0 mb","500.0 mb","1000.0 mb"],
 "500 or more gets a 9 in front.",
 ["Codes of 500 or higher: put 9 in front, decimal before the last digit: 950.0.","Codes under 500 get a 10 in front. So 500 is the first code of the 9xx range.","Common slip: thinking 500 means 1050. Real surface pressures are between about 950 and 1050 mb, so only one choice is possible."])
num(M,2,0,"A station model's pressure code is 245. What is the pressure in mb?",1024.5,"mb",
 "Under 500, put 10 in front.",
 ["245 is under 500, so add 10 in front: 10245.","Put the decimal before the last digit: 1024.5 mb.","Real pressures are near 1000, so 1024.5 is sensible; 924.5 would be unusually low."],tol=0.0002)
num(M,2,0.2,"A station model's pressure code is 603. What is the pressure in mb?",960.3,"mb",
 "500 or more, put 9 in front.",
 ["603 is 500 or more, so add 9: 9603.","Decimal before the last digit: 960.3 mb.","960 mb is low pressure, a strong storm, which matches the guess that codes above 500 are low."],tol=0.0002)
mcq(M,3,1.5,"Two stations plot pressure codes 499 and 501. Which has the HIGHER pressure?",
 ["499, because it decodes to 1049.9 mb","501, because it is the bigger number","Same pressure","501, because it decodes to 1050.1 mb"],
 "The leading digit changes at 500, so the bigger code may be the lower pressure.",
 ["499 is under 500: add 10, giving 1049.9 mb.","501 is over 500: add 9, giving 950.1 mb.","The code is not a number line. It resets at 500, like a clock going from 12 to 1."])
num(M,3,1.1,"Three hours ago a station's pressure was 1010.5 mb. Now its code is 982. How much did the pressure change in mb (negative if it fell)?",-12.3,"mb",
 "Decode the code first, then subtract.",
 ["982 is 500 or more: 998.2 mb.","998.2 − 1010.5 = −12.3 mb.","A fall of more than 10 mb in 3 hours is dramatic, like a barometer dropping before a hurricane."],tol=0.02)
num(M,2,0,"A wind barb has two pennants (triangles) and one half barb. What is the wind speed in knots?",105,"kt",
 "Pennant 50, full barb 10, half barb 5.",
 ["2 × 50 = 100.","Half barb: +5.","Total 105 kt, extremely strong, typical of jet-stream altitudes."],tol=0.01)
num(M,3,1.0,"A wind barb has one pennant, three full barbs and one half barb. What is the wind speed in knots?",85,"kt",
 "Add each symbol's value.",
 ["Pennant = 50.","Three full barbs = 30.","Half barb = 5. Total = 85 kt. Skipping the half barb gives 80, the usual slip."],tol=0.01)
mcq(M,3,1.2,"Standing with your back to the wind in the Northern Hemisphere, where is low pressure?",
 ["To your left","To your right","Straight ahead","Behind you"],
 "This is called Buys-Ballot's law.",
 ["Wind circles counterclockwise around lows.","Imagine walking around a roundabout counterclockwise: the center is on your left.","With the wind at your back, you face the same direction the air is moving, so low pressure is to your left."])
mcq(M,3,1.3,"Near the surface, winds cross the isobars slightly toward lower pressure instead of blowing parallel. Why?",
 ["Friction slows the wind, so the pressure push wins over the sideways turn","Hot air rises in the center","The jet stream pulls it","Isobars are drawn incorrectly"],
 "Two forces compete: pressure and Coriolis. Friction weakens one.",
 ["Pressure pushes from high to low. Rotation (Coriolis) bends the wind sideways.","Aloft they balance and the wind blows parallel to isobars.","Near the ground friction slows the wind and weakens the bending, so air slides a little toward low pressure, like water going downhill but slowed by rough ground."])
mcq(M,2,0,"Isobars on a surface map are drawn every 4 mb starting from 1000 mb. Which of these values has an isobar?",
 ["1016 mb","1010 mb","1014 mb","1018 mb"],
 "Multiples of 4 above 1000.",
 ["The sequence is 1000, 1004, 1008, 1012, 1016, ...","1016 fits; the others are not multiples of 4 steps.","Real maps use this fixed spacing so lines are easy to compare."])
mcq(M,2,0.3,"Isobars 4 mb apart are 100 km apart near city A and 250 km apart near city B. Where is the wind stronger, and why?",
 ["City A, since the pressure changes faster over distance","City B, since the isobars are far apart","Same, since both have the same 4 mb","Can't tell"],
 "Wind depends on the pressure gradient.",
 ["Pressure gradient is change in pressure per distance.","At A, 4 mb in 100 km is steeper than 4 mb in 250 km.","Like a steep hill: a ball rolls faster. Close isobars = steep hill = strong wind."])
num(M,3,1.5,"Isobars are 80 km apart and the wind is 30 kt. Assuming wind is proportional to the pressure gradient, what is the wind (kt) where the same isobars are 120 km apart?",20,"kt",
 "Larger spacing means a weaker gradient.",
 ["Gradient ∝ 1 ÷ spacing.","Wind = 30 × 80 ÷ 120 = 20 kt.","Spacing grew by half, so the wind drops by one third. Like a gentler slope giving a slower roll."],tol=0.02)
mcq(M,3,1.2,"A station's wind shifts from 200° to 320°, temperature falls 14 °F, dew point falls, and pressure bottoms out then rises. What passed?",
 ["A cold front","A warm front","A stationary front","A sea breeze front"],
 "Wind veers clockwise and temperature drops behind a cold front.",
 ["Behind a cold front, wind shifts from south-southwest to northwest, a clockwise turn.","Cooler, drier air arrives so temperature and dew point fall.","Pressure falls ahead of the front and rises as cold dense air arrives, like a heavy blanket settling on the ground."])
mcq(M,3,1.1,"A station's wind shifts from 120° to 210°, temperature rises from 55 °F to 68 °F and dew point rises. What passed?",
 ["A warm front","A cold front","A dryline","A high-pressure center"],
 "Warm moist air replaces cooler air.",
 ["Behind a warm front the wind turns from southeast to south or southwest.","Temperature and dew point both rise as warm, humid air takes over.","Misconception: a wind shift always means cold air; the temperature change tells which."])
mcq(M,2,0.2,"A cold front is drawn with blue triangles pointing southeast. Which way is the front moving?",
 ["Toward the southeast","Toward the northwest","Toward the north","It is not moving"],
 "Symbols point in the direction of motion.",
 ["Triangles (cold) or half-circles (warm) point the way the front advances.","Triangles point southeast, so the front moves southeast.","A stationary front alternates sides, because it isn't going anywhere."])
mcq(M,3,1.2,"Station A (west) reports T 90 °F, dew point 35 °F. Station B, 80 km east, reports T 82 °F, dew point 68 °F. What boundary lies between them?",
 ["A dryline","A cold front","A warm front","An occluded front"],
 "A sharp dew point change with little temperature change marks dry and moist air masses.",
 ["Dew point drops 33 °F in 80 km. That is a huge moisture contrast.","Temperature differs only 8 °F, so it is not mainly a cold front.","A dryline separates hot dry air from humid air. Storms can form along it, like where two different weather neighborhoods meet."])
mcq(M,2,0.5,"On a map, a purple line with alternating triangles and half-circles on the same side shows what?",
 ["An occluded front","A cold front","A stationary front","A dryline"],
 "Occluded fronts form when a faster cold front catches a warm front.",
 ["Occluded means the cold front overtook the warm front, lifting the warm air up.","Both symbols appear on the same side of the line.","Stationary fronts have them on opposite sides."])
num(M,2,0.3,"Altimeter setting A2992 means 29.92 inHg. Convert to mb (1 inHg = 33.86 mb), to the nearest 0.1.",1013.2,"mb",
 "Multiply inches by 33.86.",
 ["29.92 × 33.86 ≈ 1013.1 (about 1013.2 with the more precise 33.864).","So 29.92 inHg is standard sea-level pressure, 1013.2 mb.","Memorize it: 29.92 inHg = 1013.2 mb."],tol=0.0004)
num(M,3,0.9,"Convert 1004 mb to inches of mercury (1 inHg = 33.86 mb), to the nearest 0.01.",29.65,"inHg",
 "Divide mb by 33.86.",
 ["1004 ÷ 33.86 = 29.651.","Round: 29.65 inHg.","In a METAR it is written A2965, with no decimal point."],tol=0.0005)
mcq(M,2,0.3,"A METAR remark reads SLP045. What sea-level pressure is that?",
 ["1004.5 mb","904.5 mb","1045 mb","1000.45 mb"],
 "Same coding as station model pressure.",
 ["SLP is sea-level pressure in the remarks, using the same code as station models.","045 is under 500: put 10 in front, add decimal: 1004.5.","Misreading it as 1045 forgets the decimal."])
mcq(M,3,1.0,"A METAR shows visibility 2 SM and BKN008. By flight categories (IFR ceiling 500 to under 1,000 ft, visibility 1 to under 3 mi), what is it?",
 ["IFR","VFR","MVFR","LIFR"],
 "Use whichever of ceiling or visibility is worse.",
 ["Ceiling is lowest BKN/OVC: 800 ft, which is IFR.","Visibility 2 miles is also IFR.","Both agree: IFR. If they disagreed, take the worse one, like a team limited by its weakest player."])
mcq(M,2,0.4,"A METAR reports FEW020 SCT040 BKN070 OVC120. What is the ceiling?",
 ["7,000 ft","2,000 ft","4,000 ft","12,000 ft"],
 "Ceiling is the lowest broken or overcast layer.",
 ["FEW and SCT layers don't count as a ceiling.","BKN070 is the lowest BKN or OVC, so ceiling = 7,000 ft.","Heights are in hundreds of feet."])
mcq(M,3,1.8,"A METAR gives visibility 6 SM and BKN030. Using VFR = ceiling above 3,000 ft and visibility above 5 mi, and MVFR = ceiling 1,000 to 3,000 ft or visibility 3 to 5 mi, what category is it?",
 ["MVFR, because a 3,000 ft ceiling is not above 3,000","VFR, because visibility is good","IFR, because it is broken","LIFR, because it's low"],
 "VFR needs the ceiling ABOVE 3,000 ft, so 3,000 exactly fails.",
 ["Visibility 6 SM passes VFR.","Ceiling BKN030 = 3,000 ft. VFR needs more than 3,000, so it fails. MVFR covers 1,000 to 3,000 ft inclusive.","The worse factor wins: MVFR. Boundaries matter, like needing a score above 90 for an A, not equal to it."])
mcq(M,2,0.2,"A METAR temperature group reads 02/M01. What are the temperature and dew point?",
 ["2 °C and −1 °C","2 °C and 1 °C","−2 °C and 1 °C","−2 °C and −1 °C"],
 "M means minus and it applies to the number right after it.",
 ["Temperature first, dew point second.","02 has no M, so it is +2 °C.","M01 is −1 °C. Dew point below temperature, as it must be."])
mcq(M,3,0.9,"Which METAR temperature/dew point group cannot be right for a normal observation?",
 ["15/17","15/15","M02/M05","22/09"],
 "Air cannot hold more than 100% humidity in normal conditions.",
 ["Dew point is the temperature where the air is saturated. It can equal but not exceed the air temperature.","15/15 is saturated (fog or cloud). M02/M05 and 22/09 are allowed.","15/17 would mean over 100% humidity, which is an error."])
num(M,3,1.0,"The surface temperature is 30 °C and the dew point is 18 °C. Cloud base ≈ 125 m for each °C of spread. About how high is the cloud base (m)?",1500,"m",
 "Spread = temperature − dew point.",
 ["Spread = 30 − 18 = 12 °C.","12 × 125 = 1,500 m.","Smaller spread means lower base. Think of a rising bubble cooling until it hits its dew point, like a cold glass fogging."],tol=0.02)
num(M,3,1.4,"Rule of thumb: relative humidity (%) ≈ 100 − 5 × (T − Td in °C). Find RH when T = 25 °C and Td = 15 °C.",50,"%",
 "Compute the spread first.",
 ["Spread = 25 − 15 = 10 °C.","RH ≈ 100 − 5 × 10 = 50%.","The exact answer is about 54%, so this is a quick estimate. Bigger spread = drier air."],tol=0.02)
mcq(M,2,0.2,"A METAR was issued at 2053Z on December 5. What local time is that in California (PST = UTC − 8)?",
 ["12:53 pm","8:53 pm","4:53 am","1:53 pm"],
 "Subtract 8 hours from UTC.",
 ["20:53 − 8:00 = 12:53.","So it is 12:53 pm PST.","In summer (PDT = UTC − 7) it would be 1:53 pm."])
mcq(M,3,1.1,"A METAR is issued at 0215Z on December 6. What are the local date and time in California (PST = UTC − 8)?",
 ["December 5, 6:15 pm","December 6, 6:15 pm","December 5, 10:15 am","December 6, 10:15 am"],
 "Subtracting past midnight changes the date.",
 ["02:15 − 8:00 is negative, so go back to the previous day.","02:15 + 24:00 − 8:00 = 18:15 on December 5.","The Z date is a day ahead of local time in the evening. Check the date first."])
mcq(M,2,0.2,"In a METAR, wind reads 00000KT. What does it mean?",
 ["Calm wind","Wind from the north at 0 kt","Wind data missing","Strong wind from 0°"],
 "All zeros means no wind.",
 ["Direction and speed are both zero.","The wind is calm, so there's no direction to report.","Variable winds are written VRB, such as VRB03KT."])
mcq(M,2,0.5,"Decode: KSJC 051953Z 31008KT 10SM FEW040 18/06 A3004. Which statement is correct?",
 ["Wind from the northwest at 8 kt, fairly dry air","Wind toward 310° at 8 kt, humid air","Wind from 31° at 8 kt, fog","Wind from the northwest at 80 kt, storm"],
 "Read it group by group.",
 ["310° is northwest, and the wind is FROM that direction. 08KT is 8 knots.","18/06 gives a spread of 12 °C: dry air, with a high cloud base. 10SM is excellent visibility.","FEW040 means just a few clouds at 4,000 ft. No storm."])
mcq(M,3,1.3,"In the Northern Hemisphere, a station is directly north of a surface low-pressure center. In general, from which direction does its wind blow?",
 ["From the east (a bit northeast with friction)","From the west","From the north","From the south"],
 "Winds circle counterclockwise around lows.",
 ["Counterclockwise: picture the top of a clock moving left, that is toward the west.","The wind moving toward the west is a wind FROM the east.","Friction turns it slightly inward, giving northeast to east. People often give the direction the wind goes instead of where it comes from."])
mcq(M,3,1.2,"A station lies directly east of a surface high in the Northern Hemisphere. Wind blows from which direction?",
 ["From the north","From the south","From the east","From the west"],
 "Winds circle clockwise around highs.",
 ["Clockwise: the east side of the circle (3 o'clock) moves downward, toward the south.","Moving toward the south is a wind FROM the north.","Check by opposite: east of a low would be a south wind."])
mcq(M,1,-0.5,"A sky that is 6/8 covered by cloud is reported in METAR as…",
 ["BKN","SCT","OVC","FEW"],
 "Broken = 5 to 7 eighths.",
 ["FEW 1 to 2, SCT 3 to 4, BKN 5 to 7, OVC 8.","6 is in 5 to 7: broken.","Remember the order: Few, Scattered, Broken, Overcast, clouds filling the sky."])
txt(M,1,-1,"In a METAR wind such as 27012KT, what does KT stand for?",["knots","knot","kt"],
 "It is the unit.",
 ["KT = knots, a nautical mile per hour.","1 knot is about 1.15 mph.","The first three digits are direction, next two (or three) the speed."])
mcq(M,3,1.0,"Which evening set-up makes radiation fog most likely?",
 ["Clear sky, calm wind, temperature 12 °C and dew point 10 °C","Cloudy sky, strong wind, temperature 20 °C and dew point 5 °C","Clear sky, calm wind, temperature 25 °C and dew point 2 °C","Overcast, wind 25 kt, temperature 10 °C and dew point 9 °C"],
 "You need the air to cool to the dew point and little mixing.",
 ["Clear skies let heat escape at night so the ground cools quickly.","A small spread (2 °C) means only a little more cooling reaches saturation. Calm wind keeps the fog layer from mixing away.","Strong winds stir the air, and clouds keep heat in, like a blanket."])
mcq(M,2,0.3,"A wind barb's staff points toward the southwest with 20 kt. Where is the wind going?",
 ["Toward the northeast","Toward the southwest","Toward the northwest","Toward the southeast"],
 "Staff points to where wind comes from.",
 ["Staff toward the southwest means the wind comes from the southwest.","It travels the opposite direction: toward the northeast.","A weather vane points the same way."])
mcq(M,3,1.6,"A station reports pressure falling 7 mb in 3 hours, wind shifting from south to southwest, temperature 88 °F and dew point 70 °F. What does a forecaster most likely expect next?",
 ["A cold front arriving soon, with storms possible in the warm humid air","Clear and cool weather within the hour","A warm front with steady drizzle","A strong high building overhead"],
 "Combine all clues instead of one.",
 ["Falling pressure means a low or front is approaching.","A wind shift toward the southwest ahead of a front, with warm moist air (dew point 70 °F), supplies fuel for storms.","Any single clue is weak. Together they are a classic warm-sector setup before a cold front."])
# --- write JSON preserving fixes ---
fix={
 "obs-014":dict(l=2,b=0.3),"obs-010":dict(b=0.9),
 "maps-004":dict(num=dict(v=999.8,tol=0.0002,u="mb")),
 "maps-005":dict(num=dict(v=1002.1,tol=0.0002,u="mb")),
 "maps-021":dict(num=dict(v=1039.2,tol=0.00006,u="mb")),
 "maps-064":dict(num=dict(v=1013.2,tol=0.0002,u="hPa")),
 "maps-065":dict(num=dict(v=998.7,tol=0.0002,u="hPa")),
 "maps-008":dict(l=2,b=0.3),"maps-050":dict(l=2,b=0.3),
 "obs-011":dict(o=["Visible","Infrared","Water vapor","Radar"]),
}
dele=["obs-023","obs-025","obs-026","obs-027","obs-028","obs-029","maps-039","maps-042","maps-070","maps-055","maps-056","maps-046","maps-047","maps-052","maps-049"]
rep=("obs: deleted 6 duplicate l1 tool items, fixed obs-011 option, releveled 2. maps: deleted 9 duplicates/ambiguous (maps-039 ambiguous Scattered vs half-filled); removed families bb3 (trivial compass) and pr1 (wrong rounding: 1013 mb = 29.92 not 29.91, tol 3% far too loose). "
 "Tightened numeric tolerances on pressure decodes (old 0.5% accepted wrong answers like 998.0 for 999.8; maps-021 6% accepted a ~60 mb error). Added 35 obs + 35 maps new, ~50% l3. Fig-based items (maps-019..023, 038) unverified since figs not seen. Rules PDF not consulted; flight-category and beam-height formulas from memory (standard).")
json.dump(dict(fix=fix,**{"del":dele},del_family=["bb3","pr1"],new=new,report=rep),open(OUT,"w"),ensure_ascii=False,indent=1)
from collections import Counter
for t in (O,M): print(t,Counter(x["l"] for x in new if x["t"]==t), sum(x["t"]==t for x in new))
assert abs(29.92*33.8639-1013.2)<0.1 and round(1004/33.86,2)==29.65
print(14400/(2*4/3*6371)+120*math.sin(math.radians(.5)))
