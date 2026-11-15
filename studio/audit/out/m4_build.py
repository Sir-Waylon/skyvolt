import json, math, os
OUT = os.path.dirname(os.path.abspath(__file__))
N = [0]
def _b(t, l, b, typ, q, w, sol, **kw):
    N[0] += 1
    d = {"t": t, "l": l, "b": b, "type": typ, "q": q, "w": w, "sol": sol, "fp": "m4_%d" % N[0]}
    d.update(kw); return d
def mcq(t,l,b,q,c,wr,w,sol): return _b(t,l,b,"mcq",q,w,sol,o=[c]+wr)
def num(t,l,b,q,v,tol,u,w,sol): return _b(t,l,b,"short",q,w,sol,num={"v":v,"tol":tol,"u":u})
def txt(t,l,b,q,ans,w,sol): return _b(t,l,b,"short",q,w,sol,text=ans)
def order(t,l,b,q,items,w,sol): return _b(t,l,b,"order",q,w,sol,items=items)
def match(t,l,b,q,pairs,w,sol): return _b(t,l,b,"match",q,w,sol,pairs=pairs)
def multi(t,l,b,q,o,a,w,sol): return _b(t,l,b,"multi",q,w,sol,o=o,a=a)

def ef(mph): 
    for lim,n in [(85,"EF0"),(110,"EF1"),(135,"EF2"),(165,"EF3"),(200,"EF4")]:
        if mph<=lim: return n
    return "EF5"
def ss(mph):
    for lim,n in [(95,"1"),(110,"2"),(129,"3"),(156,"4")]:
        if mph<=lim: return n
    return "5"

def winds():
    t="winds"; L=[]
    L.append(num(t,2,-0.3,"The National Weather Service calls a thunderstorm wind gust severe at what minimum speed, in mph?",58,0.02,"mph",
     "A thunderstorm wind gust of 58 mph (50 knots) or more is severe.",
     ["Severe thunderstorm criteria: wind gusts of 58 mph or more, or hail 1 inch or larger.","58 mph is about 50 knots, since 50 × 1.15 = 57.5.","Think of it as the speed where winds start breaking tree limbs and damaging roofs."]))
    L.append(num(t,1,-0.5,"A thunderstorm gust becomes severe at 50 knots. About how many mph is that? (1 kt ≈ 1.15 mph)",57.5,0.02,"mph",
     "50 × 1.15 = 57.5, which is the 58 mph severe limit.",
     ["Knots are nautical miles per hour, and a nautical mile is a bit longer than a land mile.","So multiply knots by 1.15 to get mph.","50 × 1.15 = 57.5 mph, which the NWS rounds to 58."]))
    L.append(txt(t,1,-1.0,"Sinking air inside a storm is called a…",["downdraft","down draft","downdrafts"],
     "A downdraft is air moving down; an updraft is air moving up.",
     ["Storms have two big air streams: rising air (updraft) and sinking air (downdraft).","When a downdraft hits the ground it spreads out as damaging wind."]))
    L.append(mcq(t,2,0.0,"Why does air in a thunderstorm downdraft speed toward the ground?",
     "Rain evaporating cools it and falling rain drags it, so it is denser than the air around it",
     ["Warm air always sinks fast","The Sun heats the ground and pulls it down","Wind shear pushes it down from above"],
     "Cool, rain-loaded air is heavy, so it sinks.",
     ["Evaporating rain takes heat from the air, like sweat cooling your skin, so the air gets cold and dense.","Falling raindrops also drag the air with them, like a crowd pulling you along in a stampede.","Dense air sinks quickly and then spreads out, which makes damaging winds. Misconception: warm air rises, it does not sink."]))
    L.append(mcq(t,2,0.3,"Which describes a dry microburst?",
     "A high-based storm whose rain evaporates before reaching the ground, yet its cooled air still rushes down",
     ["A downburst that only happens in winter snow","A microburst that carries a lot of heavy rain to the ground","A tornado with no funnel cloud"],
     "Dry microbursts often hit with little or no rain, so there is no warning from the rain.",
     ["In dry places, such as the western US, cloud bases are high and the air below is dry.","Rain evaporates on the way down (virga), chilling the air a lot, and that air crashes down.","Danger: no rain at the surface does not mean no wind."]))
    L.append(mcq(t,3,1.0,"Two storms have the same size. Storm A has rain falling into a thick layer of very dry air under the cloud. Storm B has humid air all the way down. Which likely has stronger downdraft winds?",
     "Storm A, because more rain evaporates and the air gets much colder and heavier",
     ["Storm B, because humid air is heavier","They are equal, since the storms are the same size","Storm B, because it keeps its rain longer"],
     "More evaporation means more cooling, and colder air sinks faster.",
     ["Evaporation is the engine of a downburst: the drier the air under the cloud, the more rain evaporates.","Think of dropping an ice cube into a glass: the more it melts, the more it cools the water. Here the cooling is done by the evaporating rain.","So a big gap between temperature and dew point below the cloud signals strong downdrafts. Humid air stops the cooling."]))
    L.append(order(t,3,1.0,"A plane flies through a microburst on takeoff. Put what the pilot experiences in order.",
     ["Headwind increases (extra lift)","Strong downdraft pushes the plane down","Wind turns to a tailwind (lift drops)"],
     "Wind blows outward from the burst, so the plane first meets a headwind, then sinking air, then a tailwind.",
     ["A microburst is like water from a tap hitting a sink: it spreads out in all directions.","Flying in, you meet the outflow coming toward you (headwind), pass the middle where air goes straight down, then meet outflow going the same way you are flying (tailwind).","Lift depends on airspeed over the wings, so the tailwind leg is when the plane loses lift."]))
    L.append(mcq(t,3,1.2,"Why is the tailwind part of a microburst the most dangerous for a plane near the runway?",
     "Airspeed over the wings drops suddenly, so lift falls while the plane is already sinking",
     ["Tailwinds make the engines stall from rain","The pilot cannot see because of the rotation","Tailwinds raise the air pressure under the wings"],
     "Less air flowing over the wings means less lift.",
     ["Wings make lift from the air rushing past them, like a hand held flat out of a car window.","In a tailwind, the air moves with the plane, so the air speed over the wings drops fast.","Combined with the downdraft, the plane may not be able to climb. That is why airports have wind shear alerts."]))
    L.append(mcq(t,3,1.5,"A Doppler velocity image shows strong inbound winds right next to strong outbound winds along the same radar beam. The inbound side is closer to the radar. This pattern means…",
     "Divergence, such as a downburst spreading out",
     ["Rotation, such as a tornado","A cold front standing still","Air flowing in one direction only"],
     "Winds spreading away from a center look like inbound on the near side and outbound on the far side.",
     ["Radar only measures motion toward or away along its beam.","Air spreading out from a downburst moves toward the radar on the near side and away on the far side: that is divergence.","Rotation is different: inbound and outbound sit side by side across the beam, not one behind the other. Misconception: any inbound-outbound pair is a tornado."]))
    L.append(mcq(t,3,1.0,"Surveyors find trees and corn lying in one direction over a wide area, with no twisting or crossing debris. Which fits this damage?",
     "Straight-line winds from a downburst or derecho",
     ["A strong tornado","A waterspout","A hailstorm"],
     "One-direction or fan-shaped damage is straight-line wind.",
     ["Tornado debris is thrown in crossing, converging patterns, like water spinning down a drain.","Downburst damage fans outward like water hitting a table, so debris points away from a center or goes the same way.","The pattern on the ground tells you the type of wind that did it."]))
    L.append(mcq(t,2,0.2,"A gust front passes your weather station. What do you most likely see?",
     "A sudden wind gust and shift, a temperature drop, and a quick pressure rise",
     ["A temperature rise and falling pressure","Wind stops and the sky clears","A slow steady wind change over many hours"],
     "The gust front is the edge of cold air, so it brings fast changes.",
     ["The outflow is a dome of cold, dense air, like cold air spilling out of an open freezer.","Dense air adds pressure, so pressure jumps, the temperature falls, and wind gusts as it arrives.","A cold front is larger and changes things over hours, not minutes."]))
    L.append(multi(t,3,0.8,"Select ALL changes you expect when a thunderstorm gust front passes.",
     ["Temperature falls","Wind speeds up and shifts direction","Pressure rises quickly","Temperature jumps up 10°F","Pressure drops quickly"],[0,1,2],
     "Cold, dense outflow cools the air, raises the pressure, and gusts.",
     ["Cold outflow = cooler air.","Dense air piles up, so pressure goes up, and air is flowing outward, so winds gust.","A temperature jump and a pressure drop are the opposite and would happen ahead of the storm, not at the gust front."]))
    L.append(mcq(t,2,0.2,"A low, wedge-shaped cloud on the front edge of a storm, over the gust front, is a…",
     "Shelf cloud",["Funnel cloud","Mammatus cloud","Anvil"],
     "Warm air lifted by cold outflow forms the shelf cloud.",
     ["The cold outflow shoves warm air up, like a plow lifting snow.","The air rises and cools, and a shelf-like cloud forms along the boundary.","It looks scary and can be mistaken for a tornado, but the rotation is not there; it signals strong gusty wind."]))
    L.append(txt(t,2,0.0,"In desert areas such as Phoenix, a wall of dust pushed along by thunderstorm outflow is called a…",["haboob","haboobs"],
     "A haboob is a dust wall lifted by a gust front.",
     ["Cold outflow rushes across dry ground and lifts the dust.","The dust makes the gust front visible as a brown wall that can be a mile high."]))
    L.append(mcq(t,2,0.3,"Santa Ana winds in Southern California are…",
     "Warm, very dry downslope winds that blow from the land toward the ocean",
     ["Moist winds from the ocean that bring rain","Winds inside a tornado","Cold winds from the Arctic Ocean"],
     "They blow out of high desert and are heated by sinking.",
     ["High pressure over the Great Basin pushes air toward the coast, down mountain slopes.","Sinking air is squeezed by higher pressure, so it warms, like a bike pump getting hot.","They are dry and gusty, and they spread wildfires."]))
    L.append(num(t,3,1.2,"Dry air at 0 °C starts at the top of a mountain and flows 2 km down a slope. It warms about 10 °C per km of descent. What is its temperature at the bottom, in °C?",20,0.03,"°C",
     "0 + 2 × 10 = 20 °C.",
     ["As air sinks to higher pressure it is squeezed and warms; no heat is added.","Warming = 10 °C per km × 2 km = 20 °C.","Start at 0 °C, so end at 20 °C. This is why chinook and Santa Ana winds feel warm and dry."]))
    L.append(mcq(t,3,0.9,"Why does a line of storms often bow outward into a bow echo?",
     "A strong rear-inflow jet drives the middle of the line forward faster than the ends",
     ["Rotation turns the whole line into a circle","The Moon pulls the line outward","Cold fronts always curve"],
     "Faster winds in the middle push that part ahead.",
     ["A rear-inflow jet is a stream of air that comes in behind the line and sinks toward the front.","Like a wind gust pushing the middle of a sail or curtain, it makes the line bulge forward.","The bow shape marks where damaging winds are strongest, usually at the apex of the bow."]))
    L.append(mcq(t,3,1.2,"Compared with tornadoes in classic supercells, tornadoes that spin up in bow echoes and squall lines are usually…",
     "Weaker, short-lived, and harder to spot on radar",
     ["Stronger and much longer lasting","Always rated EF4 or EF5","Impossible"],
     "They form fast along a line, so forecasters get little lead time.",
     ["In a line of storms, small spin-ups can form quickly along the leading edge.","They are often brief and rain-wrapped, so warnings are tricky.","Misconception: a bow echo means only straight-line winds. Tornadoes can hide in it."]))
    L.append(num(t,3,1.0,"Wind force on a building grows with the square of wind speed. Wind goes from 40 mph to 80 mph. How many times bigger is the force?",4,0.02,"times",
     "Doubling the speed makes the force 2² = 4 times bigger.",
     ["Force is proportional to speed squared.","Speed doubles, so the factor is 2 × 2 = 4.","Misconception: double the wind does not mean double the damage; it can mean four times the force."]))
    L.append(num(t,3,1.3,"Wind force grows with the square of wind speed. Gusts rise from 60 mph to 90 mph. How many times bigger is the force?",2.25,0.02,"times",
     "(90 ÷ 60)² = 1.5² = 2.25.",
     ["Find the speed ratio: 90 ÷ 60 = 1.5.","Square it, because force is proportional to speed squared: 1.5 × 1.5 = 2.25.","A 50% rise in wind speed means more than double the force."]))
    for kt,mph in [(45,51.75),(70,80.5),(90,103.5)]:
        L.append(num(t,2,0.0,"A wind gust is measured at %d knots. About how many mph is that? (1 kt ≈ 1.15 mph)"%kt,mph,0.02,"mph",
         "%d × 1.15 = %s mph."%(kt,mph),
         ["A knot is a nautical mile per hour, a bit more than a land mile per hour.","Multiply knots by 1.15 to get mph.","%d × 1.15 = %s mph."%(kt,mph)]))
    L.append(num(t,3,1.0,"A weather station reports a gust of 28 m/s. About how many mph is that? (1 m/s ≈ 2.24 mph)",62.7,0.02,"mph",
     "28 × 2.24 = 62.7 mph, above the 58 mph severe limit.",
     ["Each m/s is about 2.24 mph.","28 × 2.24 = 62.7 mph.","That is above 58 mph, so it counts as a severe thunderstorm wind."]))
    L.append(num(t,3,0.8,"A line of storms produced wind damage along a path 300 miles long in 6 hours. What was its average speed, in mph?",50,0.02,"mph",
     "Speed = distance ÷ time = 300 ÷ 6 = 50 mph.",
     ["Average speed is distance divided by time.","300 mi ÷ 6 h = 50 mph.","Long path (over 240 mi) with gusts over 58 mph is what makes a storm a derecho."]))
    L.append(num(t,2,0.3,"A gust front is 25 miles away and moving toward you at 50 mph. In how many minutes does it arrive?",30,0.03,"min",
     "25 mi ÷ 50 mph = 0.5 h = 30 min.",
     ["Time = distance ÷ speed = 25 ÷ 50 = 0.5 hour.","0.5 hour × 60 = 30 minutes.","The gust front can arrive before any rain, so there may be no warning."]))
    L.append(mcq(t,3,0.8,"Why can a gust front race out ahead of the rain?",
     "Cold, dense outflow spreads out along the ground faster than the storm itself moves",
     ["The rain is slower because it is cold","Wind is created only after rain stops","The gust front is warmer, so it moves faster"],
     "Cold outflow flows out like a spilled liquid.",
     ["Pour water on a table: it spreads out far past where you poured it.","Outflow is dense and spreads along the ground, even beyond the storm's rain.","So wind and dust may hit you minutes before the first drops."]))
    L.append(mcq(t,3,1.2,"A rear-inflow jet is…",
     "A stream of drier air entering the back of a squall line that sinks and speeds toward the front",
     ["The updraft in a tornado","A jet stream wind at 40,000 ft above a hurricane","A warm front that crosses the line"],
     "It helps push damaging winds to the surface at the bow.",
     ["Air behind the storm line flows in at mid levels and descends.","Dry air evaporates rain and cools further, so it sinks more strongly.","Picture a fan blowing from behind to push the front forward. That is why bow echoes can produce widespread wind damage."]))
    L.append(mcq(t,2,0.3,"How does a gust front differ from a cold front?",
     "A gust front is a small, short-lived edge of storm outflow; a cold front is a large air-mass boundary lasting days",
     ["They are the same thing","A gust front is warmer than the air around it","A cold front only forms over the ocean"],
     "The gust front is made by one storm, the cold front by a big weather system.",
     ["Gust front: cold air spilled out by a storm, lasting an hour or two.","Cold front: the leading edge of a big cold air mass that can stretch over states.","Both bring wind shifts and drops in temperature, so people confuse them, but their size and cause differ."]))
    L.append(mcq(t,2,-0.3,"A downburst hits the ground. Which way does the wind blow at the surface near the impact?",
     "Outward in all directions from the point it hits",
     ["In a tight circle","Straight upward","Only toward the radar"],
     "Think of a stream of water hitting a plate.",
     ["Sinking air cannot go through the ground, so it spreads sideways.","The result is a diverging pattern, like water from a tap hitting a flat sink.","A tornado, in contrast, has winds that spin around a center."]))
    L.append(mcq(t,1,-0.5,"As a severe storm approaches, what often arrives first?",
     "Gusty outflow winds from the gust front",
     ["The calm center","The heaviest rain","The hail core only"],
     "Gust fronts run ahead of the storm.",
     ["Cool outflow spreads ahead of the main storm.","That is why a dust cloud or sudden wind may hit before any rain.","Take the first gust as a signal to go inside."]))
    L.append(mcq(t,3,1.5,"On successive radar scans, a small, very high reflectivity core (heavy rain and hail) is falling from mid levels toward the ground. What might happen next?",
     "A downburst may reach the ground and cause a burst of damaging wind",
     ["A tornado will definitely form","The storm is dying and harmless","A gust front will vanish"],
     "A descending core often means a strong downdraft is about to hit the ground.",
     ["The heavy rain and hail core is the weight pulling the downdraft down.","When it sinks quickly it may reach the ground as a microburst.","Forecasters watch for this sign as a warning for damaging wind, but it does not mean a tornado."]))
    L.append(mcq(t,2,0.6,"A storm sits northwest of you. A gust front reaches you. The outflow wind most likely blows from the…",
     "Northwest",["Southeast","Southwest","East"],
     "Outflow spreads away from the storm toward you.",
     ["Cold air spreads outward from the storm in all directions.","The storm is northwest of you, so the air travels from the northwest to you.","Wind direction is the direction it comes FROM, so it is a northwest wind."]))
    L.append(mcq(t,3,1.0,"After a storm, a town has 90 mph winds for about 20 minutes across a swath 10 miles wide, with trees falling in one direction. Which term fits best?",
     "Macroburst",["Microburst","Gustnado","Waterspout"],
     "10 miles is over 4 km wide, and 20 minutes is long.",
     ["10 miles is about 16 km, which is more than 4 km, so it is a macroburst.","Microbursts are under 4 km and brief.","A gustnado is a small whirl and a waterspout is over water."]))
    L.append(mcq(t,3,1.3,"A gustnado is…",
     "A short-lived whirl along a gust front that is not connected to the storm's rotating updraft",
     ["The same as a supercell tornado","A tornado over water","A cloud shaped like a funnel high in the sky"],
     "It is a brief vortex on the ground made by the outflow, not by a mesocyclone.",
     ["Along a sharp gust front, wind differences can make little swirls near the ground, like eddies where fast water meets slow water.","They are usually weak, brief, and show up as dusty swirls.","A true tornado is linked with the base of a rotating storm cloud."]))
    L.append(mcq(t,3,1.0,"A station reports: 3:00 pm, 87 °F, wind SW 10 kt, 1010 mb. At 3:10 pm: 71 °F, wind NW 45 kt, 1014 mb. What happened?",
     "A gust front or outflow boundary passed",
     ["A warm front passed","A tornado hit the station","The sun came out"],
     "Sudden cool-down, strong wind shift, and a pressure rise within minutes.",
     ["A 16 °F drop and strong wind change in 10 minutes means very cold outflow arrived.","The pressure rise comes from the dense, cold dome of air.","A warm front would make it warmer and change slowly."]))
    L.append(match(t,2,0.2,"Match each term to its meaning.",
     [["Downburst","Sinking air that hits the ground and spreads out"],["Gust front","Leading edge of cool outflow"],["Derecho","Long-lived widespread windstorm"],["Shelf cloud","Low wedge-shaped cloud on the gust front"]],
     "Each term describes a part of the straight-line wind story.",
     ["Downburst is the cause.","Gust front is the leading edge.","Shelf cloud is what you see.","Derecho is the big event with hundreds of miles of damage."]))
    L.append(mcq(t,3,1.6,"A uniform 50 kt wind blows toward the east. A radar sits directly south of a point where the radar sees a velocity of 0 kt. Why?",
     "Radar measures only the part of the motion along its beam, and this wind is across the beam",
     ["The wind stopped at that point","Radar cannot see wind from the east","The wind is too strong to measure"],
     "Doppler sees toward or away, not sideways.",
     ["A radar beam pointing north measures motion toward or away, like a speed gun along a road.","A car driving across in front of the speed gun reads about zero.","So the east wind, crossing the beam, shows ~0 even though it is 50 kt."]))
    return L

def torn():
    t="torn"; L=[]
    L.append(num(t,1,-0.3,"An EF5 tornado has winds estimated above what speed, in mph?",200,0.01,"mph","EF5 is over 200 mph.",
     ["The EF scale goes EF0 to EF5.","Each step is roughly 25 to 35 mph higher.","EF4 tops out at 200 mph, so EF5 is above 200."]))
    L.append(mcq(t,1,-0.3,"Which wind range matches EF3?","136–165 mph",["86–110 mph","111–135 mph","166–200 mph"],
     "EF3 is 136–165 mph.",["EF0: 65–85, EF1: 86–110, EF2: 111–135, EF3: 136–165, EF4: 166–200, EF5: over 200.","Remember: EF3 starts at 136."]))
    for kt in (120,150):
        mph=kt*1.15
        L.append(txt(t,3,0.9,"Radar-based estimates put a tornado's wind at %d knots. Convert to mph (1 kt ≈ 1.15 mph) and give the EF range it matches."%kt,
         [ef(mph),ef(mph).lower(),ef(mph)[-1]],
         "%d × 1.15 = %.1f mph, which is %s."%(kt,mph,ef(mph)),
         ["Step 1: knots × 1.15 = mph: %d × 1.15 = %.1f."%(kt,mph),"Step 2: look up the EF range (EF3 is 136–165, EF4 is 166–200).","%.1f mph falls in %s. Remember that real ratings come from damage, not from radar."%(mph,ef(mph))]))
    L.append(mcq(t,2,0.5,"A tornado causes mostly EF1 damage, but one well-built house is swept off its foundation (EF4 damage). The tornado is rated…",
     "EF4, the highest damage found along the path",["EF1, the most common damage","EF2, the average","EF5, because it hit a house"],
     "The rating uses the worst damage found.",
     ["Surveyors walk the whole path and note the strongest damage.","That strongest damage sets the rating for the whole tornado.","Like a test where your top score counts, one strong sign counts."]))
    L.append(mcq(t,3,1.0,"A strong tornado crosses only open farmland, with no buildings or trees. Why might it get a low rating?",
     "The EF scale rates damage to structures and trees, so little damage means a low rating",
     ["Tornadoes over farmland are always weak","Radar always gives the rating","The EF scale ignores wind speed"],
     "Ratings are based on damage, not on how strong it really was.",
     ["Surveyors use damage indicators: houses, barns, trees, and so on.","With nothing to damage, a strong tornado can leave a low or even unrated (EFU) mark.","It is like grading a test by the answers: no answers means no grade."]))
    L.append(mcq(t,3,1.2,"The old F scale has F3 as 158–206 mph, while EF3 is 136–165 mph. Why were the EF winds lowered?",
     "Engineering studies showed the old scale overestimated the wind needed to cause the damage",
     ["Tornadoes got weaker after 2007","The EF scale measures wind with new radars","The F scale used knots instead of mph"],
     "The EF scale matched wind to damage better.",
     ["The EF scale kept the same idea (damage rates tornadoes) but corrected the wind estimates.","Same damage, lower wind needed.","That is why ratings before and after 2007 are not exactly equal."]))
    L.append(mcq(t,2,0.2,"What is a funnel cloud?",
     "A rotating cone of cloud that does not reach the ground",
     ["Any tornado","A rain shaft","A cloud over the ocean only"],
     "If it touches the ground, it is a tornado.",
     ["A funnel cloud is condensation in a rotating air column hanging from the cloud.","When the circulation reaches the ground, we call it a tornado.","Like a cone that has not yet touched the table."]))
    L.append(mcq(t,3,0.8,"A rain-wrapped tornado is hard to see. Why does it matter for safety?",
     "You cannot rely on seeing a funnel, so warnings and radar matter",
     ["It is always weak","It cannot damage buildings","It only occurs at night"],
     "Rain can hide the tornado.",
     ["In heavy rain or darkness, there may be no visible funnel.","So the only reliable way to know is a warning or radar data.","Misconception: a tornado needs a visible funnel."]))
    L.append(mcq(t,1,-0.5,"Which way do most tornadoes in the Northern Hemisphere spin?","Counterclockwise (cyclonic)",["Clockwise","Straight up and down","Back and forth"],
     "Nearly all spin counterclockwise, like the mesocyclone that makes them.",
     ["Most tornadoes come from a counterclockwise-rotating storm.","A few weak ones spin the other way.","Cyclonic means the same spin as a low-pressure system."]))
    L.append(mcq(t,2,-0.3,"In a standard Doppler velocity image, red colors show winds moving…","Away from the radar",["Toward the radar","Upward","Clockwise"],
     "Green is toward and red is away.",
     ["Radar only sees motion along its beam.","Green is toward the radar and red is away.","Think: red = runs away, green = comes toward you (go)."]))
    L.append(mcq(t,3,1.4,"A tornado is due north of a radar. It spins counterclockwise as seen from above. On the velocity image, which side shows outbound (red) winds?",
     "The east (right) side",["The west (left) side","The north side","Both sides"],
     "Counterclockwise rotation sends the east side northward, away from the radar.",
     ["Picture a counterclockwise spinning wheel above you: its east edge moves north.","The radar is south, so north is away from radar: outbound.","The west edge moves south, toward the radar: inbound."]))
    L.append(mcq(t,3,1.5,"A tornado is due east of a radar, spinning counterclockwise as seen from above. Which part shows inbound winds (toward the radar)?",
     "The north side",["The south side","The east side","The west side"],
     "On the north side, counterclockwise flow goes west toward the radar.",
     ["Counterclockwise rotation: on the north edge the air moves west.","The radar is to the west, so west is toward the radar: inbound.","The south edge moves east, away: outbound."]))
    for vi,vo in [(40,60),(35,55)]:
        r=(vi+vo)/2
        L.append(num(t,3,1.0,"A velocity couplet shows inbound winds of %d kt and outbound winds of %d kt next to each other. Rotational velocity is the average of these two speeds. What is it, in kt?"%(vi,vo),r,0.02,"kt",
         "Average of %d and %d is %g kt."%(vi,vo,r),
         ["Add the two speeds: %d + %d = %d."%(vi,vo,vi+vo),"Divide by 2: %g kt."%r,"Forecasters use the rotational velocity to tell how strong the rotation is, like measuring how fast a merry-go-round turns."]))
    L.append(num(t,3,1.6,"A west-to-east wind of 60 kt is blowing. A radar beam points 60° away from the wind direction. The radar measures only the part along the beam: 60 × cos 60°. What speed does it show, in kt?",30,0.02,"kt",
     "60 × cos 60° = 60 × 0.5 = 30 kt.",
     ["Doppler radar sees only the part of the wind along the beam.","cos 60° = 0.5.","So the radar reads 30 kt even though the wind is 60 kt. If the beam were at 90°, it would read 0."]))
    L.append(mcq(t,3,1.3,"A tornado is 120 miles from the radar. Why might the radar miss its low-level rotation?",
     "The beam rises with distance and the Earth curves away, so it passes above the low rotation",
     ["Radar cannot see anything beyond 100 miles","Tornadoes cannot be seen on radar","The beam bends toward the ground"],
     "The farther away, the higher the beam is above the ground.",
     ["Think of a flashlight tilted slightly upward across a flat field.","Far away its spot is high above the ground.","So storms far from a radar may show only what is high up, missing tornadoes near the ground."]))
    L.append(mcq(t,3,1.4,"Inside a hook echo, radar shows a velocity couplet and, at the same spot, the correlation coefficient (CC) drops from 0.98 to 0.6 with high reflectivity. What does this indicate?",
     "Debris is being lofted, so a tornado is likely on the ground (tornado debris signature)",
     ["Large raindrops only","A gust front","The radar is broken"],
     "Low CC means the targets differ in shape and size, like debris.",
     ["CC compares how similar the radar targets are. Raindrops are all alike, so CC is near 1.","Mixed debris (leaves, boards, insulation) is not alike, so CC falls.","Rotation + debris = tornado confirmed by radar."]))
    L.append(mcq(t,2,0.5,"Why does correlation coefficient (CC) drop inside a debris ball?",
     "Debris has many different shapes and sizes, unlike nearly identical raindrops",
     ["Debris is colder than rain","Debris is bigger, so it reflects less","Wind speed is lower there"],
     "CC is high for similar targets and low for mixed ones.",
     ["Compare a bag of identical marbles with a bag of random junk.","Radar signals bounce back similarly from the marbles but differently from the junk.","Mixed scatterers give low CC."]))
    L.append(order(t,2,0.5,"Put the stages of a supercell tornado in order.",
     ["Rotating updraft (mesocyclone) forms","Wall cloud lowers","Funnel cloud descends","Tornado touches the ground","Tornado narrows into a rope and dissipates"],
     "A supercell's spin organizes, lowers, touches down, then fades.",
     ["First the updraft rotates (mesocyclone).","Then a wall cloud lowers, a funnel grows, and the funnel reaches the ground.","At the end, the tornado often thins into a rope shape and dies."]))
    L.append(mcq(t,2,0.3,"Who issues a tornado warning for your county?",
     "The local National Weather Service forecast office",
     ["Only the Storm Prediction Center in Oklahoma","The hurricane center","The school district"],
     "Local offices warn; the SPC issues watches.",
     ["The SPC issues the larger tornado watches.","Your local NWS office watches radar and issues warnings for specific areas.","Watch = prepare; warning = take cover now."]))
    L.append(mcq(t,2,0.3,"During a tornado warning, a highway overpass is…",
     "Not safe, because the wind can speed up under it and debris flies",
     ["The safest shelter","As safe as a basement","Safe if you climb up to the girders"],
     "Overpasses can channel wind and debris.",
     ["Wind squeezes under the bridge, like water speeding through a narrow pipe.","There is no protection from flying debris.","Better choices: a sturdy building or a ditch only as a last resort."]))
    L.append(mcq(t,2,0.2,"Should you open windows during a tornado warning to even out the pressure?",
     "No, it wastes time and does not protect the house",
     ["Yes, to stop the roof from exploding","Yes, on the side facing the storm","Yes, but only on the second floor"],
     "Damage comes from wind and debris, not from pressure.",
     ["Houses are damaged mainly by strong winds and flying debris.","Opening windows wastes precious time.","Go to a safe place right away."]))
    L.append(mcq(t,1,-0.3,"During a tornado warning, what should people in a mobile home do?",
     "Leave and go to a sturdy building",
     ["Stay inside the bathroom","Hide under the bed","Park next to the home"],
     "Mobile homes are not safe in a tornado.",
     ["Winds that are only moderate can flip or destroy a mobile home.","Get to a strong building or storm shelter before the storm arrives."]))
    L.append(num(t,2,0.5,"A tornado is 15 miles away and moving toward you at 30 mph. In how many minutes does it arrive?",30,0.03,"min",
     "15 mi ÷ 30 mph = 0.5 hour = 30 min.",
     ["Time = distance ÷ speed.","15 ÷ 30 = 0.5 hour.","0.5 hour × 60 = 30 minutes. Not much time, so move to shelter at once."]))
    L.append(num(t,2,0.3,"On radar, a hook echo moves 12 miles in 24 minutes. What is its speed, in mph?",30,0.03,"mph",
     "24 min = 0.4 h, and 12 ÷ 0.4 = 30 mph.",
     ["Convert minutes to hours: 24 ÷ 60 = 0.4 h.","Speed = distance ÷ time = 12 ÷ 0.4 = 30 mph.","Forecasters use this speed to figure out when a tornado reaches a town."]))
    L.append(mcq(t,3,1.2,"A landspout is…",
     "A weak tornado that forms from spin near the ground under a growing cloud, without a supercell",
     ["A tornado over water","Another name for a gustnado","A supercell tornado with a hook"],
     "Landspouts spin from the ground up, with no mesocyclone.",
     ["Along boundaries, air spins near the ground and a growing updraft stretches it, like an ice skater pulling in arms.","They are usually weaker than supercell tornadoes and have no mesocyclone.","They show weak or no hook echo on radar."]))
    L.append(mcq(t,2,0.3,"Why are nighttime tornadoes especially dangerous?",
     "People may be asleep or cannot see the storm, so warnings are missed",
     ["Night tornadoes are always stronger","Radar does not work at night","Tornadoes only occur at night"],
     "Visibility and sleep, not stronger winds.",
     ["At night it's hard to see the storm and people may not hear a warning.","Keep a weather radio or phone alert on.","Misconception: tornadoes are not stronger at night, just harder to see."]))
    L.append(mcq(t,3,1.5,"A radar shows a hook echo and a strong velocity couplet (55 kt) but the CC stays 0.98 everywhere. Best interpretation?",
     "Strong rotation is present; a tornado may be forming or hidden, but no debris signature is seen yet",
     ["No threat, since there is no debris","A confirmed large tornado is on the ground","The couplet is a radar error"],
     "Rotation is the warning sign even without debris.",
     ["Debris signature appears only after the tornado is on the ground and lofting debris.","Strong rotation alone is enough to issue a warning.","Missing signs do not mean safe, just less certain."]))
    L.append(mcq(t,3,1.5,"Why is it hard for radar to tell a mesocyclone from a tornado at long range?",
     "A tornado is far narrower than the radar beam, so radar sees only the broader parent rotation",
     ["Tornadoes are not rotating","Mesocyclones do not rotate","Tornadoes are too cold"],
     "The beam widens with distance.",
     ["Radar beams spread out; at long range one beam may be miles wide.","A tornado can be a few hundred yards wide, so it blends into the bigger circulation.","Think of trying to photograph a pencil from a mile away."]))
    L.append(mcq(t,2,0.6,"A tornado is one mile wide. Is it automatically EF5?",
     "No, rating depends on the damage, not the width",
     ["Yes, wide means strong","Yes, but only if it lasts an hour","It cannot be rated"],
     "A wide tornado can be weak and a narrow one violent.",
     ["EF ratings come from damage to buildings and trees.","Width, path length and duration do not set the rating.","A big weak funnel and a small violent one both exist."]))
    L.append(mcq(t,2,0.2,"A mesocyclone is…",
     "A rotating updraft a few miles wide inside a supercell",
     ["A tornado over water","A hurricane eye","A fast jet of air high above"],
     "Mesocyclones are the parent rotation that can spawn tornadoes.",
     ["A mesocyclone is the storm-sized rotating updraft.","A tornado is the much smaller, violent vortex on the ground.","Not every mesocyclone makes a tornado."]))
    L.append(match(t,2,0.5,"Match each radar signature with its meaning.",
     [["Hook echo","Rain and debris wrapped around a mesocyclone"],["Velocity couplet","Tight rotation"],["Low CC in the hook","Debris lofted into the air"],["Bow echo","Straight-line wind"]],
     "Each shape or color shows one thing.",
     ["Reflectivity shows precipitation shapes.","Velocity shows rotation.","CC shows how similar the targets are.","Bow echoes show a line of wind damage."]))
    L.append(multi(t,3,0.8,"Select ALL signs that suggest a tornado is likely on radar.",
     ["Velocity couplet","Hook echo","Low CC inside the hook","A thin line of weak echo far ahead of the storm","Uniform inbound winds across the storm"],[0,1,2],
     "Rotation, hook shape, and debris signals point to tornadoes.",
     ["Couplet = rotation.","Hook = rain wrapping the mesocyclone.","Low CC = debris.","A thin line ahead is a gust front; uniform inbound wind has no rotation."]))
    L.append(txt(t,2,0.5,"A tornado's damage suggests a 3-second gust of 135 mph. What is its EF rating?",["EF2","ef2","2"],
     "111–135 mph is EF2.",
     ["EF2 range is 111 to 135 mph.","135 is the top of EF2.","One mph more (136) would be EF3."]))
    return L

def hurr():
    t="hurr"; L=[]
    L.append(num(t,2,0.3,"A hurricane warning means hurricane conditions are expected within about how many hours?",36,0.01,"h",
     "Warning: within 36 hours.",
     ["A hurricane watch means conditions are possible within 48 hours.","A warning means they are expected within 36 hours.","Watch = get ready; warning = finish preparations."]))
    L.append(num(t,2,0.3,"A hurricane watch means hurricane conditions are possible within about how many hours?",48,0.01,"h",
     "Watch: within 48 hours.",
     ["The watch comes first, with more time.","48 hours for a watch, 36 for a warning.","Use the time to get supplies and leave if told to."]))
    L.append(num(t,2,0.3,"A hurricane's sustained winds are 100 mph. About how many knots is that? (1 kt ≈ 1.15 mph)",87,0.02,"kt",
     "100 ÷ 1.15 ≈ 87 kt.",
     ["To go from mph to knots, divide by 1.15.","100 ÷ 1.15 = 87.0.","The NHC reports in knots and mph."]))
    L.append(mcq(t,2,0.2,"In the US, a hurricane's sustained wind is the average over…","One minute",["3 seconds","One hour","One day"],
     "Sustained = 1-minute average; gust = a few seconds.",
     ["A gust is a brief burst, usually a few seconds.","Sustained winds smooth these out over one minute.","Category is based on sustained winds, so gusts are higher."]))
    L.append(txt(t,2,0.5,"A hurricane has sustained winds of 156 mph. What Saffir-Simpson category is it? (Cat 4 is 130–156, Cat 5 is 157+)",["4","cat 4","category 4"],
     "156 mph is the top of Cat 4.",
     ["Cat 4 goes up to 156.","Cat 5 starts at 157.","Boundaries matter in competition: one mph can change the category."]))
    for kt in (70,100,120):
        mph=kt*1.15; c=ss(mph)
        L.append(txt(t,3,0.9,"A hurricane has sustained winds of %d kt. Convert to mph (1 kt ≈ 1.15 mph) and give the Saffir–Simpson category (1: 74–95, 2: 96–110, 3: 111–129, 4: 130–156, 5: 157+)."%kt,
         [c,"cat "+c,"category "+c],
         "%d × 1.15 = %.1f mph, so category %s."%(kt,mph,c),
         ["Step 1: kt × 1.15 = %.1f mph."%mph,"Step 2: match to the mph ranges.","%.1f mph is in category %s."%(mph,c)]))
    L.append(mcq(t,3,0.8,"Why can a Category 1 hurricane still cause a deadly disaster?",
     "The category only rates wind; storm surge and heavy rain flooding can be huge",
     ["Category 1 storms are really Category 3 storms","The category includes surge","Weak storms have no wind"],
     "The scale rates wind only.",
     ["Saffir–Simpson ranks only the sustained wind.","Surge and rainfall flooding depend on size, speed and coast shape.","A slow, wet, weak storm can be deadlier than a fast, strong one."]))
    L.append(mcq(t,2,0.5,"What is the main energy source of a hurricane?",
     "Heat released when water vapor from warm ocean condenses",
     ["Heat from the Earth's core","Cold fronts","The Moon's pull"],
     "Condensation releases latent heat.",
     ["Warm ocean water evaporates into vapor.","When vapor condenses into cloud, it releases heat, which makes air rise faster and drops pressure.","Think of it as an engine fueled by the warm ocean."]))
    L.append(mcq(t,3,1.3,"A hurricane stalls over the same water for two days and weakens. Which process helps explain this?",
     "Its winds stir up cold water from below, cooling the surface",
     ["The ocean gets warmer from the storm","The Moon shifts the tide","Salt content rises"],
     "Mixing brings cold water up.",
     ["Winds churn the ocean like a spoon stirring a mug of hot cocoa with cold milk at the bottom.","Cooler water means less heat and moisture for the storm.","Fast-moving storms leave less time for this."]))
    L.append(mcq(t,2,0.8,"Why do tropical storms rarely form within about 5° latitude of the equator?",
     "The Coriolis effect is too weak to start the spin",
     ["Too cold","The ocean is too cool","Too much shear from mountains"],
     "No Coriolis, no rotation.",
     ["Earth's rotation bends moving air, and this effect nearly vanishes at the equator.","Without it, air flows straight into a low and fills it.","Hurricanes need that bending to spin up."]))
    for sp,mv in [(100,15),(120,20)]:
        L.append(num(t,3,1.0 if sp==100 else 1.8,"A Northern Hemisphere hurricane has sustained winds of %d mph and moves forward at %d mph. Roughly, how strong are the winds on its right side? (Add the forward speed.)"%(sp,mv),sp+mv,0.02,"mph",
         "%d + %d = %d mph."%(sp,mv,sp+mv),
         ["On the right side, the storm's forward motion adds to its spin.","On the left side it subtracts: %d − %d = %d."%(sp,mv,sp-mv),"So the right-front side usually has the strongest winds and surge."]))
    L.append(mcq(t,3,1.2,"A hurricane moves north and makes landfall on a Gulf coast that faces south. Which place likely gets the biggest surge?",
     "A town 30 miles east of the center (right side)",
     ["A town 30 miles west of the center","A town far inland","The center only"],
     "East is the right side, where winds blow water onshore.",
     ["Counterclockwise winds on the east side blow from the south, pushing water onto the coast.","Add the storm's forward speed, and winds on the right side are stronger.","The west side has winds blowing offshore."]))
    L.append(num(t,2,0.5,"Storm surge is 12 ft and it arrives at a time when the astronomical tide is 3 ft above normal. What is the storm tide, in ft?",15,0.02,"ft",
     "12 + 3 = 15 ft.",
     ["Storm tide = storm surge + normal tide.","12 + 3 = 15 ft.","That is why landfall at high tide is worse."]))
    L.append(mcq(t,3,0.8,"What is the difference between storm surge and storm tide?",
     "Storm tide is surge plus the normal tide",
     ["They are the same","Surge is rain; tide is wind","Surge only occurs in winter"],
     "Total water level = surge + tide.",
     ["Storm surge is the extra water the storm pushes up.","The tide is the normal rise and fall of the sea.","Storm tide is the total water level you see, so timing with the tide matters."]))
    L.append(mcq(t,3,1.0,"The cone of uncertainty on a hurricane forecast map shows…",
     "The probable path of the storm's center, not the size of the storm or its impacts",
     ["The area of the hurricane's winds","Where flooding will happen","The area of the eye"],
     "The cone is about the track of the center.",
     ["The cone covers the area where the center is expected to pass about two-thirds of the time.","Dangerous winds and surge can extend far outside the cone.","Misconception: being outside the cone does not mean you are safe."]))
    L.append(mcq(t,3,1.2,"Why are hurricane intensity forecasts usually less accurate than track forecasts?",
     "Small-scale changes inside the storm, such as eyewall changes and shear, are hard to predict",
     ["Tracks are measured by hand","Intensity is not important","Forecast models cannot see the ocean"],
     "Track is set by big flow patterns; intensity depends on small details.",
     ["Steering winds are large and easier to forecast.","Internal changes like eyewall replacement are small.","Like predicting where a leaf goes in a river versus how fast it spins."]))
    L.append(mcq(t,3,1.5,"During an eyewall replacement cycle, a hurricane…",
     "Builds an outer eyewall; the inner one weakens, so winds dip and then the larger eye re-strengthens",
     ["Loses its eye forever","Turns into a tornado","Moves faster"],
     "An outer ring replaces the inner ring.",
     ["A new ring of storms forms outside the original eyewall.","It chokes off the inner one, so the wind drops for a while.","Then the new eyewall contracts and the storm may strengthen again, with a larger eye."]))
    L.append(mcq(t,3,1.0,"The NHC defines rapid intensification as an increase in sustained winds of at least…",
     "30 knots in 24 hours",["10 knots in 24 hours","30 knots in a week","30 knots in 1 hour"],
     "30 kt (35 mph) in 24 h.",
     ["It is a fast jump in one day.","30 kt is about 35 mph.","These storms are hard to forecast and dangerous."]))
    L.append(mcq(t,2,0.5,"Many Atlantic hurricanes begin as…",
     "African easterly waves moving off the coast of Africa",
     ["Cold fronts from Canada","Dust devils","Waterspouts"],
     "Waves in the winds seed the storms.",
     ["These are ripples in the wind pattern over Africa.","They cross the warm Atlantic, where they can grow into tropical storms.","They are one of the seeds for the Cape Verde storms."]))
    L.append(mcq(t,3,1.2,"The Saharan Air Layer is…",
     "A dry, dusty air mass from Africa that can weaken Atlantic tropical storms",
     ["A warm, humid air mass that helps storms grow","A jet stream over Africa","A tornado outbreak"],
     "Dry air weakens storms.",
     ["Dry air makes clouds evaporate and downdrafts chill the storm.","Dusty air is also stable, which prevents rising air.","It is like throwing a dry towel on a campfire."]))
    L.append(mcq(t,2,0.3,"Why do hurricanes rarely reach California?",
     "The ocean off California is too cold and storms turn away",
     ["Mountains block them","California is too far north from the equator, so there is no rain","California has no wind"],
     "Cold water cuts off the heat source.",
     ["The California Current brings cool water from the north.","Hurricanes need about 26.5 °C or warmer.","So storms that approach fade away."]))
    L.append(mcq(t,1,-0.5,"Northern Hemisphere hurricanes spin…","Counterclockwise",["Clockwise","Straight up","Randomly"],
     "In the north they spin counterclockwise; in the south, clockwise.",
     ["The Coriolis effect turns inflowing air.","North of the equator that turn is to the right, so storms spin counterclockwise.","Southern Hemisphere storms spin clockwise."]))
    L.append(match(t,2,0.2,"Match each region to the name used for its tropical cyclones.",
     [["Atlantic Ocean","Hurricane"],["Northwest Pacific","Typhoon"],["Indian Ocean","Cyclone"],["Northeast Pacific (east of the dateline)","Hurricane"]],
     "Same storm, different names.",
     ["Hurricane: Atlantic and eastern Pacific.","Typhoon: northwestern Pacific.","Cyclone: Indian Ocean and South Pacific."]))
    L.append(mcq(t,3,1.3,"After moving north, a hurricane gets fronts and gains energy from temperature contrasts. It is now…",
     "Extratropical (post-tropical)",["Tropical","A tornado","A mid-level wave"],
     "Its fuel is no longer ocean heat.",
     ["A hurricane has a warm core and no fronts.","Moving north, it meets cold air and fronts.","It becomes a cold-core storm, still dangerous with wind and rain."]))
    L.append(mcq(t,2,0.0,"When does a tropical cyclone get a name?","When it reaches tropical storm strength",
     ["When it forms as a disturbance","When it hits land","When it becomes a Category 3"],
     "Names begin at 39 mph.",
     ["A depression has a number.","At 39 mph it gets a name from the list.","Names of very deadly storms are retired."]))
    L.append(order(t,2,-0.3,"Order these from the weakest to the strongest.",
     ["Tropical depression","Tropical storm","Category 1 hurricane","Category 3 hurricane","Category 5 hurricane"],
     "Strengthening ladder.",
     ["Depression: under 39 mph.","Tropical storm: 39–73 mph.","Hurricane: 74+ mph; Cat 3 starts at 111 and Cat 5 at 157."]))
    L.append(num(t,2,0.3,"A hurricane is 320 miles away moving toward you at 10 mph. In how many hours does it arrive?",32,0.03,"h",
     "320 ÷ 10 = 32 h.",
     ["Time = distance ÷ speed.","320 ÷ 10 = 32 hours.","That is less than 36 hours, so you would already be in the warning window."]))
    L.append(mcq(t,2,0.8,"Why does a slow-moving hurricane often cause more flooding rain?",
     "It sits over one place longer and drops more rain there",
     ["It has more wind","It makes less rain","Slow storms are weaker"],
     "More time over the same place means more rain.",
     ["Picture a hose: if you hold it still, the spot gets soaked; if you walk, each spot gets less.","Speed matters as much as strength for rain totals.","Example: Harvey (2017) stalled over Texas."]))
    L.append(mcq(t,3,1.0,"In a hurricane, tornadoes most often form in the…",
     "Outer rain bands in the right-front quadrant",["Eye","Left-rear quadrant","Open ocean only"],
     "Right-front quadrant is the favorite spot.",
     ["Extra wind shear is greatest there.","Spiral bands over land spin up small rotations.","Tornadoes in hurricanes are usually weak."]))
    L.append(mcq(t,2,0.5,"A dropsonde, dropped from a hurricane hunter aircraft, measures…",
     "Pressure, temperature, humidity, and wind as it falls",
     ["Only ocean depth","Only rainfall","The eye's color"],
     "It is a weather instrument on a parachute.",
     ["Hurricane hunters fly into the storm.","They drop instruments that radio data back.","This helps forecasters know the true strength."]))
    L.append(mcq(t,3,0.8,"Why does a lower central pressure usually mean stronger winds?",
     "A bigger pressure difference over a short distance drives faster winds",
     ["Low pressure heats the air","Low pressure makes the ocean colder","Low pressure removes friction"],
     "Wind blows from high to low pressure; steeper difference means faster wind.",
     ["Picture a ball rolling down a hill: steeper hill, faster ball.","Pressure difference is the hill for air.","So a very low center pressure with high pressure outside means a steep drop and strong wind."]))
    L.append(mcq(t,3,0.8,"Forecasters expect La Niña this summer. The Atlantic hurricane season is more likely to be…",
     "More active, because wind shear is lower",
     ["Less active, because wind shear is higher","Unchanged","Active only in the Pacific"],
     "La Niña reduces shear in the Atlantic.",
     ["El Niño raises shear over the Atlantic and suppresses storms.","La Niña does the reverse.","Low shear lets storms grow tall and organized."]))
    L.append(mcq(t,2,0.8,"Why is the eye of a hurricane clear?",
     "Air sinks in the eye, warming and drying it so clouds evaporate",
     ["Air rises quickly","It is above the cloud layer","The Sun burns off clouds"],
     "Sinking air dries out.",
     ["Air in the eye sinks, like air pressed by a pump.","Sinking air warms and its clouds evaporate.","The eyewall has the rising air and the storm."]))
    L.append(mcq(t,3,1.2,"Atlantic hurricanes usually move west, then curve north and east. What mostly causes the curve?",
     "Steering winds around the subtropical high, then westerlies",
     ["The Moon","Ocean tides","The eye"],
     "Large wind patterns steer.",
     ["Winds flow clockwise around the Bermuda high, west in the tropics and north at its edge.","Farther north, westerlies carry storms east.","Like a leaf in a river bend."]))
    return L

def build():
    N[0]=0
    out={}
    for f in (winds,torn,hurr):
        out[f.__name__]=f()
    return out

if __name__=="__main__":
    B=build()
    new=[q for k in ("winds","torn","hurr") for q in B[k]]
    for k in B:
        l3=sum(1 for q in B[k] if q["l"]==3); print(k,len(B[k]),"l3:",l3)
    for q in new:
        if q["type"]=="mcq":
            assert len(q["o"])==4 and len(set(q["o"]))==4,q["q"]
        assert q["w"] and len(q["sol"])>=2
    fix={
     "winds-023":{"q":"The NWS defines a derecho as wind damage along a path of more than how many miles (with gusts of at least 58 mph along most of it)?","w":"NWS: damage swath of more than 240 miles with gusts of at least 58 mph.","sol":["A derecho is a long-lived, widespread windstorm from a fast-moving line of storms.","Its damage path is over 240 miles (about 400 km) with gusts 58 mph or more.","A single microburst is tiny by comparison: under 4 km wide."]},
     "hurr-035":{"w":"Surge is one of the deadliest hurricane hazards, along with flooding rain.","sol":["Surge is water pushed ashore by the wind, like a bathtub wave sloshing over the edge.","Historically it has caused a large share of hurricane deaths.","Inland rain flooding is also very deadly."]},
     "winds-005":{"l":3,"b":0.8},
    }
    d=["winds-024","winds-025","winds-026","winds-028","torn-024","torn-025","torn-030","torn-033","torn-034","torn-038","hurr-032","hurr-033","hurr-039","hurr-048","winds-020","winds-021","winds-022","torn-026","hurr-037","hurr-044","hurr-007b"]
    d=[x for x in d if x!="hurr-007b"]
    rep=("m4: winds/torn/hurr. Added %d new (winds %d, torn %d, hurr %d), ~%d%% level 3. Deleted kt1 family (tol 1.01 was effectively unbounded; replaced with 3 numeric conversions) and %d duplicate/trivial items (torn-025 had no figure). Fixed winds-023 wording (NWS derecho: >240 mi, gusts >=58 mph), hurr-035 overclaim. Doubts: none major; derecho definitions vary by source."
      %(len(new),len(B["winds"]),len(B["torn"]),len(B["hurr"]),round(100*sum(q["l"]==3 for q in new)/len(new)),len(d)))
    json.dump({"fix":fix,"del":d,"del_family":["kt1"],"new":new,"report":rep},open(os.path.join(OUT,"m4.json"),"w"),ensure_ascii=False,indent=1)
    print("ok",len(new))
