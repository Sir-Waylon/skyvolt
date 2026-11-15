import json, math, os
OUT = os.path.dirname(os.path.abspath(__file__))
N = [0]
NEW = []

def _add(t, d):
    N[0] += 1
    d["t"] = t
    d["fp"] = "m5_%d" % N[0]
    NEW.append(d)

def mcq(t, l, b, q, ok, bad, w, sol):
    _add(t, dict(l=l, b=b, type="mcq", q=q, o=[ok] + bad, w=w, sol=sol))

def num(t, l, b, q, v, tol, u, w, sol):
    _add(t, dict(l=l, b=b, type="short", q=q, num=dict(v=v, tol=tol, u=u), w=w, sol=sol))

def txt(t, l, b, q, answers, w, sol):
    _add(t, dict(l=l, b=b, type="short", q=q, text=answers, w=w, sol=sol))

def order(t, l, b, q, items, w, sol):
    _add(t, dict(l=l, b=b, type="order", q=q, items=items, w=w, sol=sol))

def match(t, l, b, q, pairs, w, sol):
    _add(t, dict(l=l, b=b, type="match", q=q, pairs=pairs, w=w, sol=sol))

def multi(t, l, b, q, opts, a, w, sol):
    _add(t, dict(l=l, b=b, type="multi", q=q, o=opts, a=a, w=w, sol=sol))

def wc(T, V):
    return 35.74 + 0.6215 * T - 35.75 * V ** 0.16 + 0.4275 * T * V ** 0.16

# ------------------------------------------------------------------ WINTER
T = "winter"
mcq(T, 1, -0.6, "A forecast says air temperature 10°F and wind chill −5°F. What does the wind chill describe?",
    "How cold the wind makes exposed skin feel",
    ["The new air temperature once the wind arrives", "How cold a parked car's engine will get", "The temperature at which snow forms"],
    "Wind chill is a feels-like number for skin, not a new air temperature.",
    ["Wind sweeps away the thin warm layer of air next to your skin, like blowing on hot soup to cool it faster.",
     "So skin loses heat faster and feels colder than 10°F.",
     "A thermometer still reads 10°F. Cars and water bottles cannot cool below the air temperature."])
num(T, 1, -0.8, "A blizzard needs sustained winds or frequent gusts of at least how many mph?", 35, 0.01, "mph",
    "Blizzard wind is 35 mph or more.",
    ["Blizzard needs three things: wind of 35 mph or more, falling or blowing snow that cuts visibility under ¼ mile, and all of it for 3+ hours.",
     "Think of 35 as the 'speed limit' for blizzard wind."])
num(T, 1, -0.8, "Blizzard conditions must last at least how many hours?", 3, 0.01, "h",
    "A blizzard must last 3 hours or longer.",
    ["Blizzard conditions have to hold for 3 hours or more.", "A one-hour whiteout is a snow squall, not a blizzard: the storm has to 'stay on' like a long movie, not a short clip."])
mcq(T, 1, -0.8, "Cold wind blows across a big lake. Which shore gets the lake-effect snow?",
    "The downwind shore, where the wind leaves the lake",
    ["The upwind shore, where the wind arrives", "Only the shore with mountains", "Both shores equally"],
    "Lake-effect snow falls downwind of the lake.",
    ["The air picks up heat and moisture while crossing the water, like a sponge soaking up water.",
     "When it reaches land it is squeezed out as snow, so the sponge 'drips' on the downwind side."])
match(T, 1, -0.7, "Match each winter hazard to its description.",
      [["Sleet", "Ice pellets that bounce"], ["Freezing rain", "Rain that freezes on contact"], ["Snow", "Ice crystals falling as flakes"], ["Blowing snow", "Loose snow lifted by the wind"]],
      "Know the four winter precipitation and wind terms.",
      ["Sleet is frozen before it lands, like tiny pebbles.", "Freezing rain is liquid until it touches something, then it glazes it like icing on a donut.",
       "Blowing snow is old snow moved by wind, so a blizzard does not need new snow."])
txt(T, 1, -0.7, "A watch means conditions are favorable. Which alert means winter weather is happening or about to happen, so act now?",
    ["warning", "a warning", "winter storm warning", "blizzard warning"],
    "Warning means happening or about to happen.",
    ["Watch = ingredients are in the kitchen. Warning = the meal is being served.", "Act on a warning: stay off the roads."])
mcq(T, 2, 0, "Why do bridges and overpasses ice up before ordinary roads?",
    "Cold air touches them from above and below, and no ground under them stores warmth",
    ["Bridges are made of steel, which creates ice", "Bridges get more freezing rain than roads", "Salt cannot be used on bridges"],
    "Bridges lose heat from both sides.",
    ["A road sits on warm-ish ground, like a cup sitting on a heated table.",
     "A bridge is like a cup held in the air: cold air wraps it from every side.",
     "So the bridge surface cools to freezing first, and wet pavement becomes ice."])
mcq(T, 2, 0, "A snow squall warning is issued for your town. What is coming?",
    "A brief, intense burst of snow with gusty wind and sudden whiteouts",
    ["A two-day snowstorm with two feet of snow", "Ice building on power lines overnight", "Snowmelt flooding the river"],
    "Snow squalls are short but can make roads treacherous fast.",
    ["A squall is like a sudden shower in a sunny day, but made of snow and wind.", "Visibility can drop from clear to near zero in seconds, and roads may flash-freeze.",
     "Danger comes from the speed of the change, not the total snow."])
mcq(T, 2, 0, "An Alberta clipper is usually…",
    "A fast-moving low from Canada with light snow, gusty wind and colder air behind it",
    ["A slow Gulf storm that drops two feet of snow", "A lake-effect snow band", "The remains of a hurricane"],
    "Clippers move quickly, so snow totals stay modest.",
    ["Think of a speedboat: it moves quickly and makes a big wake of wind and cold air, but does not stay long in one spot.", "Little time over each town means light snow, usually a few inches."])
num(T, 2, 0, "A storm drops 1.5 inches of liquid-equivalent precipitation as snow with a 12:1 snow-to-liquid ratio. How many inches of snow fall?", 18, 0.02, "in",
    "Snow depth = liquid × ratio.",
    ["Ratio 12:1 means 12 inches of snow melt down to 1 inch of water.", "1.5 × 12 = 18 inches.",
     "Fluffy snow is like popcorn: lots of volume, little 'corn'."])
order(T, 2, 0, "Put the freezing rain steps in order, from cloud to ground.",
      ["Snow forms high in the cloud", "Snow falls into a warm layer and melts to rain", "Rain falls into a shallow below-freezing layer at the ground", "Drops freeze on contact with cold surfaces"],
      "Freezing rain needs a warm layer aloft and a thin cold layer below.",
      ["Snow starts the trip, melts in the warm 'middle floor', then reaches the cold 'basement' too fast to refreeze in the air.", "The drops stay liquid (supercooled) and freeze the moment they touch a branch or wire."])
mcq(T, 2, 0, "Lake-effect snow often fades in late winter after the lake freezes over. Why?",
    "Ice cuts off the heat and moisture that the open water supplies",
    ["Ice makes the air warmer", "Frozen lakes create stronger winds", "Snow cannot fall on ice"],
    "Open water is the engine of lake-effect snow.",
    ["The lake is the stove and the water is the pot of steam. Freeze the lake and the pot has a lid on it.", "No heat and moisture transfer means no unstable air and no heavy bands."])
mcq(T, 2, 0, "Cold wind blows from the west across a long lake that runs north to south. Which shore gets lake-effect snow?",
    "The east shore", ["The west shore", "The north shore only", "The south shore only"],
    "Snow falls downwind, so for a west wind, east.",
    ["Follow the wind: it enters on the west shore and leaves on the east.", "Moisture is picked up on the way across, so snow falls where the air leaves the lake."])
num(T, 2, 0, "Hypothermia begins when core body temperature falls below about how many °F?", 95, 0.01, "°F",
    "Hypothermia starts below about 95°F (35°C).",
    ["Normal core temperature is about 98.6°F.", "Below 95°F the body cannot make heat as fast as it loses it, like a car running out of fuel on a cold day."])
mcq(T, 2, 0, "After a snowball fight in strong wind, a student's fingertips are numb, white and waxy. This is most likely…",
    "Frostbite, frozen skin and tissue", ["Hypothermia, a low core body temperature", "Heat exhaustion", "Dehydration"],
    "Frostbite is local freezing, hypothermia is the whole body cooling.",
    ["Frostbite hits the parts farthest from the 'furnace': fingers, toes, ears, nose.", "Hypothermia shows as shivering, slurred speech, confusion.", "Warm slowly and get medical help for frostbite."])
mcq(T, 2, 0, "Why can a nor'easter cause coastal flooding that lasts through several high tides?",
    "Winds from the northeast push ocean water onto the coast for many hours",
    ["The storm melts coastal glaciers", "Rain from the storm is always saltwater", "Nor'easters rotate clockwise and suck water up"],
    "Long-lasting onshore wind piles water up.",
    ["Imagine blowing across a bathtub: water piles up at the far end.", "The storm stays offshore for a day or more, so the 'blowing' goes on through multiple tides.", "Each high tide rides on top of the extra water."])
opts = [(-5, 10), (0, 5), (5, 25), (10, 40)]
vals = [wc(*o) for o in opts]
assert min(vals) == vals[0]
mcq(T, 3, 0.8, "Which has the LOWEST wind chill? Choose the (air temperature, wind speed) pair.",
    "−5°F with 10 mph", ["0°F with 5 mph", "5°F with 25 mph", "10°F with 40 mph"],
    "Wind chill depends on both temperature and wind, and temperature matters more here.",
    ["Wind chill uses 35.74 + 0.6215T − 35.75V^0.16 + 0.4275TV^0.16.", "Results: −5°F/10 mph = −22°F, 5°F/25 mph = −17°F, 10°F/40 mph = −15°F, 0°F/5 mph = −10°F.",
     "Misconception: more wind always wins. Wind helps, but a much colder start beats it, like a deep freezer with a small fan."])
mcq(T, 2, 0, "The NWS wind chill formula is only valid when…",
    "The air is at or below 50°F and wind is above 3 mph", ["The air is below 0°F only", "Snow is falling", "Wind is above 35 mph"],
    "No cold or no breeze means no wind chill.",
    ["Wind chill is about heat loss from skin, so you need cold air and moving air.", "On a calm 70°F day there is nothing to 'chill'."])
mcq(T, 2, 0, "Which snow adds more weight to a roof per inch of depth?",
    "Wet snow near 32°F", ["Dry powder at 5°F", "They weigh the same", "Powder, because it is colder"],
    "Wet snow holds much more water per inch.",
    ["Powder is mostly air, like a sponge cake. Wet snow is packed and full of water, like a soaked sponge.", "More liquid per inch means heavier roof load."])

mcq(T, 3, 1.0, "Soundings: cloud top −10°C, a 2-km layer at +4°C (1 to 3 km up), then a thin layer from the ground to 200 m at −2°C. What reaches the ground?",
    "Freezing rain", ["Sleet", "Snow", "Plain rain"],
    "A deep warm layer plus a shallow cold layer gives supercooled liquid drops.",
    ["Snow melts completely in the warm layer, becoming rain.", "The cold layer at the ground is too thin to refreeze the drops in the air.", "They stay liquid until they hit something below 0°C, then freeze: freezing rain."])
mcq(T, 3, 1.1, "Soundings: cloud top −10°C, a layer at +3°C from 1.5 to 3 km, then a deep layer at −5°C from the ground to 1.5 km. What reaches the ground?",
    "Sleet", ["Freezing rain", "Snow", "Plain rain"],
    "A deep cold layer refreezes melted drops into pellets.",
    ["Snow melts in the warm layer.", "The cold layer below is deep (1.5 km), giving drops time to refreeze, like water drops dropped into a deep freezer.", "They land as ice pellets: sleet."])
num(T, 3, 1.0, "A flat roof of 1,000 ft² carries 8 inches of snow at a 10:1 snow-to-liquid ratio. Water weighs 62.4 lb per cubic foot. About how many pounds of snow are on the roof?", 4160, 0.03, "lb",
    "Convert snow depth to water depth, then weigh the water.",
    ["Water depth = 8 ÷ 10 = 0.8 inch = 0.067 ft.", "Volume = 1,000 ft² × 0.067 ft = 66.7 ft³.", "Weight = 66.7 × 62.4 ≈ 4,160 lb, about two small cars. Light fluffy flakes add up."])
num(T, 3, 1.3, "A foot (18 inches) of snow falls from 0.9 inch of liquid-equivalent precipitation. What is the snow-to-liquid ratio? Give the first number of the ratio, ___:1.", 20, 0.02, "",
    "Ratio = snow depth ÷ liquid depth.",
    ["18 ÷ 0.9 = 20, so the ratio is 20:1.", "That is very fluffy snow, typical of cold dry air, like a pillow full of feathers.", "Typical snow is about 10:1 and wet snow is lower."])
mcq(T, 3, 1.0, "'Bomb cyclone' means a storm deepens a lot in 24 hours. The threshold is 24 mb at 60°N and smaller at lower latitudes (about 18 mb at 40°N). A storm at 40°N drops 20 mb in 24 hours. Is it a bomb?",
    "Yes, 20 mb is above the 18 mb needed at 40°N", ["No, it must be at least 24 mb everywhere", "No, bombs need winds of 74 mph", "Only if it is a hurricane"],
    "The threshold scales with latitude.",
    ["Same pressure drop means stronger storm at lower latitudes, because the Coriolis effect is weaker there.", "So the bar is lower at 40°N.", "20 mb is greater than 18 mb, so yes. Misconception: a fixed 24 mb everywhere."])
mcq(T, 3, 1.0, "Rule of thumb for lake effect: the lake surface should be at least 13°C warmer than the air at 850 mb (about 1.5 km up). The lake is 6°C, and the 850 mb air is −12°C. Is lake-effect snow likely?",
    "Yes, the difference is 18°C", ["No, the difference is only 6°C", "No, the lake must be above 15°C", "Only if the lake is frozen"],
    "Difference = lake − 850 mb air.",
    ["6 − (−12) = 18°C, above 13.", "The bigger the gap, the more unstable the air, like a pot on a hot burner versus a warm one.", "Unstable air rises fast and builds snow bands."])
num(T, 3, 1.5, "Lake water is 8°C. Using the 13°C rule, what is the warmest 850 mb air temperature (°C) that still supports lake-effect snow?", -5, 0.0, "°C",
    "850 mb air must be at most lake temperature − 13.",
    ["Need lake − air ≥ 13, so air ≤ 8 − 13 = −5°C.", "Any warmer, and the gap shrinks, so the air stays too stable. Like a hot bath: if the room is almost as warm, nothing 'steams'."])
mcq(T, 3, 1.2, "The sky is clear. Wind gusts 42 mph on loose old snow, visibility is under ⅛ mile, and this lasts 4 hours. Is this a blizzard?",
    "Yes, blowing snow counts", ["No, snow must be falling", "No, a blizzard needs 12 inches of new snow", "Only if the temperature is below 0°F"],
    "Blizzard needs wind, low visibility, and 3+ hours, not new snow.",
    ["A ground blizzard happens when wind lifts old snow like dust off a dry field.", "Wind of 35+ mph, visibility under ¼ mile, 3+ hours: all met.", "Common mistake: thinking a blizzard needs new snow."])
mcq(T, 3, 0.9, "Air temperature is 20°F and the wind chill is 5°F. A bowl of water sits outside all night. How cold can the water get?",
    "Down to 20°F, the air temperature", ["Down to 5°F, the wind chill", "Only down to 32°F", "Below 5°F because wind keeps pulling heat"],
    "Wind speeds up cooling but cannot beat the air temperature.",
    ["A fan can cool a hot bowl faster, but never below room temperature.", "Water freezes at 32°F and keeps cooling toward 20°F, the air temperature.", "Wind chill applies to warm, living skin, not to objects."])
mcq(T, 3, 1.5, "A strong low moves north along the coast. Town X is inland, 60 miles northwest of the track. Town Y is 60 miles southeast, on the ocean side. Which usually gets heavy snow?",
    "Town X, on the cold northwest side", ["Town Y, near the ocean moisture", "Both get equal snow", "Neither; the center always misses snow"],
    "Heavy snow usually falls northwest of the track; the east side gets warm ocean air.",
    ["Winds spin counterclockwise around a low.", "Northwest of the track, winds bring cold air from the north: snow.", "Southeast of the track, winds bring mild ocean air: rain or mix. Track matters more than strength."])
multi(T, 3, 1.2, "Select ALL conditions that favor lake-effect snow.",
      ["Lake water much warmer than the air", "Wind crossing many miles of open water", "Cold air mass moving over the lake", "Lake mostly covered with thick ice", "Warm air arriving from the south over land"],
      [0, 1, 2],
      "Warm water, long fetch, and cold air together build lake bands.",
      ["Fetch is the length of water the wind travels, like the distance a sponge drags across a wet table.", "Cold air over warm water becomes unstable and rises.", "Ice and warm southerly air shut the process off."])
mcq(T, 3, 1.0, "Sleet and freezing rain can both fall with the same liquid amount. Why does freezing rain usually do more damage to trees and power lines?",
    "It freezes on contact and builds a heavy ice coat", ["It is heavier, because raindrops are bigger", "Sleet melts on contact", "Freezing rain is always colder"],
    "Sleet is already frozen and bounces; freezing rain sticks and builds up.",
    ["Sleet is like pebbles hitting a wire: they bounce and pile on the ground.", "Freezing rain is like paint: it coats every side of a branch and wire.", "¼ inch of ice can bring down lines."])
mcq(T, 3, 1.6, "Hourly obs (gust mph / visibility mi), snow falling all hours: 1 pm 30/0.5, 2 pm 37/0.2, 3 pm 40/0.1, 4 pm 36/0.2, 5 pm 34/0.2, 6 pm 38/0.15, 7 pm 41/0.1. When were blizzard conditions first met for 3 straight hours?",
    "By 4 pm (2 pm to 4 pm)", ["By 7 pm", "By 5 pm", "Never; conditions never lasted 3 hours"],
    "Check each hour for 35+ mph and under ¼ mile, then count a streak of 3.",
    ["1 pm fails (30 mph, 0.5 mi). 2, 3, and 4 pm pass: that is 3 in a row.", "5 pm fails (34 mph), which breaks the streak. 6 and 7 pm pass but only 2 hours.", "Like a basketball streak, one miss resets the count."])
num(T, 3, 1.8, "A storm drops 1.8 inches of liquid-equivalent precipitation. The first 0.6 inch falls as wet snow (8:1), the remaining 1.2 inches as fluffy snow (15:1). How many inches of snow in total?", 22.8, 0.02, "in",
    "Convert each part with its own ratio, then add.",
    ["Wet part: 0.6 × 8 = 4.8 in.", "Fluffy part: 1.2 × 15 = 18 in.", "Total: 4.8 + 18 = 22.8 in. Do not use one average ratio: each period gets its own."])
num(T, 3, 2.1, "A roof is rated for 12 lb per ft². It holds 15 inches of wet snow (8:1), then rain adds 0.7 inch of liquid that the snow absorbs. One inch of water over 1 ft² weighs 5.2 lb. What is the load in lb/ft²?", 13.4, 0.03, "lb/ft²",
    "Add the snow's water equivalent and the rain, then convert to weight.",
    ["Snow water = 15 ÷ 8 = 1.875 in.", "Add rain: 1.875 + 0.7 = 2.575 in of water.", "2.575 × 5.2 ≈ 13.4 lb/ft², above 12. Rain-on-snow is like pouring water on a sponge already full: weight jumps, depth does not."])
order(T, 2, 0.3, "Put the lake-effect snow steps in order.",
      ["Cold air blows over warmer open water", "The air gains heat and moisture", "The air becomes unstable and rises into clouds", "Snow bands fall on the downwind shore"],
      "Heat and moisture make unstable air, which makes bands.",
      ["The lake warms the bottom of the air like a pot warming the bottom of a soup.", "Warm air at the bottom rises and forms clouds."])
mcq(T, 3, 1.1, "Rule of thumb: the 1000–500 mb thickness near 5,400 m separates rain from snow, and thinner means colder. A city has 5,250 m. Ignoring surface temperature, what is more likely?",
    "Snow", ["Rain, because thinner air is warmer", "Hail", "Cannot tell without wind"],
    "Thickness measures the average temperature of the air layer.",
    ["Warm air expands like a balloon, making the layer thicker. Cold air shrinks, making it thinner.", "5,250 m is below 5,400 m, so a cold layer favors snow.", "It is only a guide; the surface layer can still be warm."])
mcq(T, 3, 0.8, "Winds 36 mph, visibility 0.2 mile, falling snow, for 3.5 hours. Is this a blizzard?",
    "Yes, all three tests are met", ["No, it lasted too short a time", "No, visibility must be under ⅛ mile", "No, wind must reach 45 mph"],
    "35+ mph, under ¼ mile, 3+ hours.",
    ["Check each test: 36 ≥ 35 ✓, 0.2 < 0.25 ✓, 3.5 ≥ 3 ✓.", "Like a checklist: three ticks mean blizzard."])

# ------------------------------------------------------------------ SAFETY
T = "safety"
match(T, 1, -0.7, "Match each hazard to the right action.",
      [["Tornado", "Lowest floor, interior room"], ["Flash flood", "Move to higher ground"], ["Lightning", "Go inside a building"], ["Hurricane surge", "Evacuate when ordered"]],
      "Each hazard has a basic safe action.",
      ["Tornado: put walls between you and the wind, like hiding behind a tall fence.", "Flash flood: water flows downhill, so go up.", "Lightning: a building or hard-topped car, not a tree.", "Surge: get out of the water's path before it comes."])
mcq(T, 1, -0.5, "You hear thunder but the sky overhead is blue. Are you safe outdoors?",
    "No, lightning can strike miles from the storm", ["Yes, lightning only comes from overhead clouds", "Yes, if you are not near water", "Only safe on open ground"],
    "If you can hear thunder, you are close enough to be struck.",
    ["Lightning can travel sideways ten miles or more, like a long jump from the storm.", "Blue sky above does not mean the storm is far enough.", "Go inside at the first thunder."])
txt(T, 1, -0.5, "What is the National Weather Service slogan about flooded roads? Complete it: Turn Around, ___.", ["don't drown", "dont drown", "turn around don't drown", "turn around dont drown"],
    "Never drive through floodwater.",
    ["Water on a road hides washed-out pavement, like a trap door.", "Six inches of fast water can knock you down, and about a foot can float many cars."])
multi(T, 1, -0.4, "Select ALL items that belong in a basic emergency kit.",
      ["Water", "Flashlight and extra batteries", "First-aid kit", "Open-flame candles for light", "A gas generator running indoors"],
      [0, 1, 2], "Kits hold safe basics; flames and indoor generators are hazards.",
      ["Water, light, and first aid keep you going for a few days.", "Candles can start fires and generators make carbon monoxide: both are dangerous in a storm."])
num(T, 2, 0, "Plan 1 gallon of water per person per day. A family of 4 prepares for 3 days. How many gallons?", 12, 0.02, "gal",
    "People × days × gallons.", ["4 people × 3 days × 1 gallon = 12 gallons.", "This is drinking water; it is like packing a lunch for each day."])
num(T, 2, 0, "You see lightning and hear thunder 15 seconds later. Sound travels about 1 mile in 5 seconds. How many miles away is the strike?", 3, 0.02, "mi",
    "Divide seconds by 5.", ["15 ÷ 5 = 3 miles.", "Light arrives almost instantly, sound takes its time, like seeing a far-away hammer hit before hearing it.",
                            "3 miles is close enough to be struck: go inside."])
mcq(T, 2, 0, "Thunder was last heard at 4:10 pm. When is the earliest safe time to resume outdoor practice?",
    "4:40 pm, 30 minutes after the last thunder", ["4:15 pm, after 5 quiet minutes", "4:25 pm", "Right away if the rain stops"],
    "Wait 30 minutes after the last thunder.",
    ["The storm can leave and still strike behind it, like a bully who keeps swinging while backing off.", "Restart the 30-minute clock with each new thunder."])
mcq(T, 2, 0, "A flash flood warning is issued for your area and you are near a creek. What should you do?",
    "Move to higher ground right away", ["Wait for the creek to rise", "Drive through shallow water to get out", "Stay in the basement"],
    "Flash floods rise in minutes.",
    ["Water behaves like a slide: low spots get it first.", "Basements fill quickly.", "Do not walk or drive through floodwater."])
mcq(T, 2, 0, "A highway overpass is a safe place to shelter from a tornado.",
    "False: wind speeds up under it and debris flies through", ["True: concrete protects you", "True if you climb up high", "True only for an EF0"],
    "Overpasses are a deadly myth.",
    ["An overpass is like a wind tunnel: air squeezes through and speeds up.", "You are also exposed to flying debris.", "Instead: a sturdy building or a low ditch as a last resort."])
mcq(T, 2, 0, "A tornado is coming. Should you open the windows to equalize the pressure?",
    "No, it wastes time and does nothing to protect the house", ["Yes, it prevents the house from exploding", "Yes, on the side facing the storm", "Only upstairs"],
    "Winds and debris do the damage, not pressure.",
    ["Damage comes from wind and flying objects.", "Open windows just let debris in. Use the time to get to shelter."])
mcq(T, 2, 0, "At school, a tornado warning is issued. Where should students shelter?",
    "An interior hallway on the lowest floor, away from the gym or large rooms", ["The gym, which is the biggest room", "Next to windows to watch", "The parking lot"],
    "Wide-roof spans collapse easily.",
    ["Wide flat roofs are like a tabletop without legs.", "Small interior rooms on the lowest floor give walls on all sides."])
mcq(T, 2, 0, "Which alert system sends a loud message to phones in a warned area, no app needed?",
    "Wireless Emergency Alerts (WEA)", ["A text from a friend", "A weather app notification", "Local TV only"],
    "WEA is from the official alert system.",
    ["It uses cell towers to 'ring everyone in the room' at the same time.", "Apps need to be installed, but WEA is built into the phone."])
num(T, 2, 0, "A portable generator should be run at least how many feet from the house, doors and windows?", 20, 0.01, "ft",
    "Run it outdoors at least 20 feet away.", ["Carbon monoxide has no smell or color and can drift in.", "20 feet is about the length of a school bus's front half; farther is safer."])
num(T, 2, 0, "A power outage begins. About how many hours does an unopened refrigerator keep food safe?", 4, 0.01, "h",
    "Fridge: about 4 hours, if the door stays shut.", ["Cold stays in like in a cooler; each time the door opens, the cold escapes.", "After 4 hours, throw out meat, milk and leftovers."])
mcq(T, 2, 0.2, "A severe thunderstorm warning is issued for a storm with hail at least ___ and wind gusts at least ___.",
    "1 inch (quarter size); 58 mph", ["½ inch; 40 mph", "1 inch; 40 mph", "2 inches; 75 mph"],
    "These are the severe criteria used by the NWS.",
    ["Quarter-size hail dents cars and 58 mph wind breaks branches.", "A storm below this is not called severe, but can still be dangerous."])
num(T, 2, 0.3, "A hurricane watch means hurricane conditions are possible within about how many hours?", 48, 0.01, "h",
    "Watch is 48 hours; warning is 36 hours.", ["Watch = 48 hours lead time, warning = 36 hours.", "Use the watch time to get ready and leave if told."])
order(T, 2, 0, "Put these tornado alerts in order, from earliest to most urgent.",
      ["SPC outlook (days ahead)", "Tornado watch", "Tornado warning", "Tornado emergency"],
      "Alerts get more urgent as the threat gets closer.",
      ["Outlook is a 'weather menu', watch is 'ingredients on the counter', warning is 'dinner's burning', emergency is 'fire in the building'."])
mcq(T, 2, 0, "A swimmer is pulled away from the beach by a rip current. What should they do?",
    "Swim parallel to shore until free, then angle back", ["Swim straight back against it", "Tread water and wait", "Swim farther out"],
    "Do not fight the current.",
    ["A rip current is like a treadmill going out: running against it tires you.", "Step off the side of the treadmill (swim parallel), then walk back."])
mcq(T, 2, 0, "At 90°F, which feels hotter?", "80% humidity", ["20% humidity", "They feel the same", "Depends only on the wind"],
    "High humidity slows sweat evaporation.",
    ["Sweat cools you only when it evaporates.", "Humid air is like a wet towel that cannot dry.", "Heat index is a feels-like number for this."])
mcq(T, 2, 0, "The county is under a tornado watch at 2 pm. At 3 pm a tornado warning is issued for your town. What changed?",
    "A tornado is occurring or imminent nearby, so act now", ["Conditions are only favorable", "The tornado watch was canceled", "The tornado has passed"],
    "A watch says 'be ready', a warning says 'act'.",
    ["Watch = favorable conditions. Warning = tornado spotted or on radar.", "Move to shelter without waiting for more information."])
mcq(T, 2, 0, "Why is leaving a child in a parked car on a mild day dangerous?",
    "The inside heats far above outdoor temperature within minutes", ["Cars cool faster than the outdoors", "Windows keep the heat out", "Only on 100°F days"],
    "Cars trap sunlight like a greenhouse.",
    ["Sunlight passes through the glass and heat cannot escape, like a greenhouse.", "Children's bodies heat up faster than adults'."])
mcq(T, 3, 1.0, "A wall of blowing dust appears ahead while you drive. What does the NWS advise?",
    "Pull off the road, turn lights off, foot off the brake", ["Keep driving fast with lights on", "Stop in the lane with brake lights on", "Park under an overpass"],
    "Pull aside, stay alive.",
    ["Cars behind you may follow your lights and crash into you.", "Off the road, lights off and foot off brake: nobody follows."])
mcq(T, 3, 1.0, "Why is a hard-topped car safer in lightning?",
    "Its metal body carries the current around you", ["Rubber tires insulate it", "Cars are not struck", "The windows are special"],
    "The metal frame protects, not the tires.",
    ["The current flows around the outside of the metal shell, like water around a boat.", "Keep windows up and avoid touching metal. Convertibles do not work."])
mcq(T, 3, 1.1, "The calm eye of a hurricane passes over your town. What comes next?",
    "The eyewall returns with strong winds from the opposite direction", ["The storm is over", "Winds stay calm", "Winds return weaker"],
    "The eye is a gap in the storm.",
    ["Think of a donut: the hole is calm but the rest is stormy.", "Winds on the back side blow the other way."])
mcq(T, 3, 1.2, "Your home is in Evacuation Zone A and the storm is forecast as a Category 1. What does the zone mean?",
    "It floods first from storm surge, so follow the order to leave", ["Category 1 winds are weak, so stay", "Zones are only for wind", "Zone A is the safest"],
    "Zones are about surge, not wind.",
    ["Evacuation zones map where water can reach, like a bathtub rim.", "Surge is the deadliest hazard, even from weaker storms."])
num(T, 3, 1.2, "A hurricane warning arrives with tropical-storm winds expected in 36 hours. You need 12 hours to travel and must be on the road at least 6 hours before the winds. What is the latest time, in hours from now, you can leave?", 18, 0.0, "h",
    "Work backward from the arrival time.",
    ["36 − 6 = 30 hours deadline to be done traveling... but you need 12 hours to travel.", "Latest departure = 36 − 6 − 12 = 18 hours from now.", "Plan with extra margin like leaving early for a flight."])
num(T, 3, 1.6, "A flood moves at twice the speed. The force on a person rises with the square of speed. By what factor does the force increase?", 4, 0.0, "",
    "Force ∝ speed².",
    ["Double the speed: 2² = 4 times the force.", "Like standing in a fast current: twice as fast pushes four times harder.", "That is why a little extra speed makes floods deadly."])
mcq(T, 3, 1.0, "A tornado warning is issued while you are driving and no shelter is close. What is the best option?",
    "Park, buckle up, head below the windows and cover yourself", ["Shelter under an overpass", "Outrun the tornado in a straight line", "Stay in traffic with the windows open"],
    "Use the best option when no shelter exists.",
    ["Seat belts and covering protect against debris.", "Do not shelter under an overpass.", "A low ditch is a last resort."])
mcq(T, 3, 1.0, "Which situation is most dangerous?",
    "Heat stroke: confusion and hot dry skin; call 911", ["Mild sweating after a jog", "A little thirst", "Slight tiredness"],
    "Heat stroke is a medical emergency.",
    ["Heat stroke is when the body's cooling system fails, like a radiator with no coolant.", "Heat exhaustion is milder: heavy sweating, cool clammy skin.", "Call for help and cool the person."])
mcq(T, 3, 1.0, "You are stuck in a car in a blizzard with the engine on. What should you do?",
    "Stay with the car, keep the tailpipe clear of snow and crack a window", ["Walk to find help", "Run the engine with the tailpipe buried", "Leave the engine on all the time"],
    "Snow-blocked tailpipes fill the car with carbon monoxide.",
    ["Cars are shelter and easier for rescuers to find.", "Exhaust has nowhere to go if the pipe is blocked, like a chimney with a plug.", "Run the engine briefly to save fuel."])
mcq(T, 3, 1.3, "A 'tornado emergency' differs from a tornado warning because it means…",
    "A confirmed, damaging tornado is threatening a populated area", ["It is only a watch", "A tornado is far away", "It is a hurricane alert"],
    "It is the highest tornado alert.",
    ["A warning says 'take cover'. An emergency says 'a large tornado is on the ground in a populated area'.", "It is rare and shows extreme danger."])
num(T, 3, 1.1, "Storm surge of 9 ft arrives at high tide that is 3 ft above normal sea level. How tall is the storm tide (water above normal), in feet?", 12, 0.0, "ft",
    "Storm tide = surge + astronomical tide.",
    ["9 + 3 = 12 ft.", "Surge rides on the tide like a wave on a stepladder: timing matters.", "A surge at low tide does less harm than at high tide."])
mcq(T, 3, 1.0, "A dry desert wash floods under a clear sky. How?",
    "Heavy rain fell miles upstream and rushed down", ["Flash floods only occur under rain", "The sky was lying", "Dew melted"],
    "Flash floods can arrive from far away.",
    ["Water runs through a wash like water through a gutter after rain on the roof.", "You may never see the rain."])
multi(T, 3, 1.2, "Select ALL actions that are safe during a thunderstorm.",
      ["Go inside a sturdy building", "Wait 30 minutes after the last thunder", "Stay off wired plumbing (showers, sinks)", "Stand under a tall lone tree", "Hold up a metal umbrella"],
      [0, 1, 2], "Buildings are safe; trees and metal are not.",
      ["Lightning can travel through pipes and wires.", "A lone tree is a lightning rod, and so is a metal umbrella."])

# ------------------------------------------------------------------ CASES
T = "cases"
order(T, 1, -0.6, "Put the case method steps in order.",
      ["Name the storm type", "List the clues", "Apply the scale or signature", "Check the dates (EF cutoff 1 Feb 2007)"],
      "Follow the four steps every time.",
      ["Like a detective: what kind of crime, what clues, what category, what date.", "The scale you can use depends on the date."])
match(T, 1, -0.6, "Match each event to its type.",
      [["Galveston 1900", "Hurricane and storm surge"], ["Dust Bowl", "Drought and dust storms"], ["Xenia 1974", "Violent tornado"], ["Great Flood 1993", "River flooding"], ["Blizzard of 1888", "Winter storm"]],
      "Know what kind of event each case was.",
      ["Each case has one main signature: water surge, dry dust, wind funnel, river overflow, snow."])
txt(T, 1, -0.6, "Which small, intense hurricane hit south Florida in 1992?", ["andrew", "hurricane andrew"], "Andrew, 1992.",
    ["Andrew was compact but extremely powerful, like a pocket-size drill."])
txt(T, 1, -0.5, "Hurricane Ian (2022) struck the southwest coast of which state?", ["florida", "fl"], "Ian hit southwest Florida.",
    ["Ian made landfall in Florida and caused a large surge."])
txt(T, 1, -0.5, "In which month did the great Blizzard of 1888 strike the U.S. Northeast?", ["march"], "March 1888.", ["A famous late-winter blizzard."])
txt(T, 1, -0.4, "Hurricane Melissa (2025) devastated which Caribbean island nation?", ["jamaica"], "Melissa hit Jamaica.", ["Melissa was a very intense hurricane."])
mcq(T, 2, 0.2, "Which of these storms did NOT make landfall in the mainland U.S.?",
    "Melissa (2025)", ["Katrina (2005)", "Ian (2022)", "Helene (2024)"],
    "Melissa hit Jamaica, not the U.S.",
    ["Katrina hit Louisiana/Mississippi, Ian southwest Florida, Helene Florida's Big Bend.", "Melissa hit Jamaica."])
mcq(T, 2, 0, "Hurricane Hilary (2023) is notable because…",
    "A Pacific storm brought rare tropical-storm rain to Southern California", ["It hit Florida", "It formed over land", "It was a tornado outbreak"],
    "Cool California waters usually weaken Pacific storms.",
    ["Normally Pacific storms fall apart over cool water before reaching California.", "Hilary's remnants dumped desert rain like a surprise rain on a dry yard."])
num(T, 2, 0, "An EF5 tornado, like Joplin 2011, has estimated winds above how many mph?", 200, 0.01, "mph",
    "EF5 is above 200 mph.",
    ["EF scale: EF0 65–85, EF1 86–110, EF2 111–135, EF3 136–165, EF4 166–200, EF5 >200.", "Joplin was EF5, and it hit Missouri."])
mcq(T, 2, 0, "The 1974 Xenia tornado was rated on which scale?",
    "The original Fujita (F) scale", ["The Enhanced Fujita (EF) scale", "The Saffir-Simpson scale", "The Richter scale"],
    "EF only began 1 Feb 2007.",
    ["Before Feb 1, 2007, tornadoes got an F rating.", "Check the date before choosing the scale."])
mcq(T, 2, 0, "Why did plowing the prairie worsen the Dust Bowl?",
    "Plowed soil lost the grass roots that held it in place", ["Plowing made it rain less", "Plowing made the wind stronger", "Soil is always heavy"],
    "Drought plus bare soil blew away.",
    ["Prairie grass roots are like rebar in concrete.", "Remove them and dry soil lifts into dust storms."])
mcq(T, 2, 0, "Why was the Galveston 1900 hurricane so deadly?",
    "A big surge covered a low island with little warning", ["It was a tornado", "It was a blizzard", "It was a drought"],
    "Galveston was only a few feet above sea level.",
    ["A low, flat island is like a plate: any water spills over everything.", "In 1900 there was little warning and no seawall yet."])
mcq(T, 2, 0, "Hurricane Andrew (1992) is remembered as…",
    "A small but extremely intense storm that crossed a populated area", ["A huge slow storm with little wind", "A tornado outbreak", "A Pacific storm"],
    "Size is different from intensity.",
    ["Andrew was compact but its eyewall crossed south Florida.", "A small saw cuts deeper than a big paintbrush."])
multi(T, 2, 0, "Select ALL hazards of the 1993 Storm of the Century.",
      ["Blizzard conditions", "Tornadoes", "Storm surge", "Volcanic ash", "A drought"],
      [0, 1, 2], "It combined winter weather, severe storms and surge.",
      ["One huge system had hazards from the Gulf to Canada.", "No volcano or drought was involved."])
mcq(T, 2, 0, "Both April 1974 and April 2011 had record tornado outbreaks. How were the tornadoes rated?",
    "1974 with the F scale, 2011 with the EF scale", ["Both with EF", "Both with F", "Neither was rated"],
    "EF replaced F on 1 Feb 2007.",
    ["The scale depends on the date.", "Same name, different measuring stick."])
num(T, 2, 0, "The Tri-State Tornado (1925) traveled 219 miles in about 3.5 hours. What was its average speed in mph?", 62.6, 0.03, "mph",
    "Speed = distance ÷ time.",
    ["219 ÷ 3.5 ≈ 62.6 mph.", "That is very fast for a tornado, like a car on a highway."])
num(T, 2, 0.3, "Ida made landfall in Louisiana on Aug 29, 2021 and flooded New York on Sep 1. How many days later?", 3, 0.0, "days",
    "Count days across the month change.",
    ["Aug 29 → Aug 30 → Aug 31 → Sep 1: 3 days.", "Even remnants can bring huge rain far from the coast."])
num(T, 2, 0.3, "Black Sunday, the famous Dust Bowl dust storm, happened in what year?", 1935, 0.0, "",
    "Black Sunday was April 14, 1935.", ["It was a huge wall of dust across the Plains.", "It happened during the 1930s Dust Bowl."])
mcq(T, 3, 1.3, "Storm A: Category 4, small, hits a thinly populated coast. Storm B: Category 1 but huge and slow, hits a bay. Which likely produces the greater surge?",
    "Storm B, because size and duration drive surge", ["Storm A, because wind speed alone determines surge", "Both the same", "Neither makes surge"],
    "Surge depends on size, speed, and shape of the coast, not just category.",
    ["Think of a big fan blowing across a bathtub for a long time: it piles up more water than a small strong one.", "Sandy had a large surge as a post-tropical storm."])
mcq(T, 3, 1.0, "Ida's remnants flooded the Northeast with winds well below hurricane strength. What is the lesson?",
    "Weak winds do not mean weak rain, remnants can flood", ["Remnants are harmless", "Wind speed is all that matters", "Floods only happen at the coast"],
    "Tropical moisture stays after the winds drop.",
    ["A storm is like a wet sponge that is squeezed over cities.", "Category tells wind, not rain."])
mcq(T, 3, 1.3, "Ian (2022) came ashore on Florida's southwest coast heading north-northeast. Why was the surge worst south of the eye?",
    "Winds blew onshore there, and the storm's forward motion added to them", ["Winds blew offshore there", "The eye pushes the water down", "Surge only happens north of the eye"],
    "Surge peaks to the right of the landfall point.",
    ["Winds spin counterclockwise, so south of a north-moving eye they blow onshore.", "The right side adds the storm's speed to its wind."])
mcq(T, 3, 1.2, "Helene (2024) killed many people far inland in the Appalachians. What made the flooding so extreme?",
    "Heavy tropical rain lifted by mountains onto already wet ground", ["Storm surge in the mountains", "Hail", "Tornadoes only"],
    "Mountains squeeze rain out of moist air.",
    ["Mountains force air upward, like squeezing a wet towel.", "Rain on saturated ground runs off quickly."])
mcq(T, 3, 1.0, "Erin (2025) rapidly intensified. NHC calls it rapid intensification when winds rise at least 35 mph in 24 hours. A storm goes from 75 to 115 mph in 24 hours. Is it rapid intensification, and is it a major hurricane?",
    "Yes to both: +40 mph, and 115 mph is Category 3", ["Yes, but 115 mph is only Category 2", "No, it needs a 60 mph rise", "No, and Category 3 starts at 130 mph"],
    "Category 3 is 111–129 mph, and the rise is above 35 mph.",
    ["115 − 75 = 40 mph, more than 35.", "Major hurricanes are Category 3 or higher (111+ mph).", "Rapid intensification leaves little time to prepare."])
mcq(T, 3, 1.4, "The Great Flood of 1993 lasted for months. What best explains it?",
    "Repeated heavy storms over soaked ground kept rivers high", ["One giant storm", "A hurricane", "Snowmelt only"],
    "Saturated soil sheds rain, so rivers stay high.",
    ["Soil is a sponge: when full, extra rain runs off.", "Storms kept coming back over the same basins."])
order(T, 3, 1.2, "Put these events in order, earliest first.",
      ["Hurricane Andrew", "Storm of the Century", "Great Flood of 1993", "Hurricane Katrina"],
      "Andrew Aug 1992, Storm of the Century Mar 1993, Great Flood summer 1993, Katrina 2005.",
      ["Andrew (Aug 1992) → Storm of the Century (March 1993) → Great Flood (summer 1993) → Katrina (Aug 2005).", "Hint: winter storm before summer floods in the same year."])
num(T, 3, 1.2, "The April 3–4, 1974 Super Outbreak produced how many tornadoes?", 148, 0.02, "",
    "The 1974 Super Outbreak had 148 tornadoes.", ["It was in 13 states in about 24 hours.", "Xenia, Ohio was one of the F5 tornadoes."])
mcq(T, 3, 1.0, "A tornado hit on March 12, 2006. Which scale was used to rate it?",
    "The Fujita (F) scale", ["EF scale", "Saffir-Simpson scale", "Beaufort scale"],
    "EF cutoff is 1 Feb 2007.",
    ["The date is before Feb 1, 2007, so F scale.", "Always check the date."])
mcq(T, 3, 1.3, "Which tornado was NOT part of the April 25–28, 2011 Southeast outbreak?",
    "Joplin, Missouri (EF5)", ["Hackleburg–Phil Campbell, Alabama (EF5)", "Smithville, Mississippi (EF5)", "Tuscaloosa, Alabama (EF4)"],
    "Joplin was May 22, 2011.",
    ["Joplin happened about a month later, in Missouri.", "The Southeast outbreak was April 25–28."])
mcq(T, 3, 1.2, "Clues: October; landfall in New Jersey; labeled post-tropical; tropical-storm winds across about 1,000 miles; surge flooding New York. Which event?",
    "Sandy 2012", ["Katrina 2005", "Andrew 1992", "Ida 2021"],
    "Size and surge, not category, define Sandy.",
    ["Sandy merged with a front and was huge.", "Katrina was Gulf Coast; Andrew was small; Ida was in Aug/Sep."])
mcq(T, 3, 1.0, "Katrina (2005) reached Category 5 over the Gulf, but at its Louisiana landfall it was a…",
    "Category 3", ["Category 5", "Category 1", "Tropical storm"],
    "It weakened before landfall but kept a huge surge.",
    ["Katrina weakened to Category 3 at landfall, but its huge size kept the surge enormous.", "Size, not just category, determined the surge."])
mcq(T, 3, 1.1, "A case packet: Texas coast, September 1900, low island, thousands dead. Which event?",
    "Galveston 1900", ["Andrew 1992", "Hilary 2023", "Dust Bowl"],
    "Galveston is the deadliest U.S. natural disaster.",
    ["The clues point to a surge on a low barrier island in Texas.", "No other listed event fits the date or place."])

# ------------------------------------------------------------------ assemble
FIX = {
    "winter-006": {"l": 2, "b": 0, "w": "About ¼ inch of ice can bring down power lines.",
                   "sol": ["Ice weighs a lot: ¼ inch coating every wire adds many pounds.", "Wind then pushes on the iced wire like a sail.", "Freezing rain, not sleet, builds this coating."]},
    "winter-071": {"o": ["Hazardous winter weather is possible in the next day or two; get ready", "It is happening right now; act", "The storm just ended", "Only flurries are expected"], "l": 2, "b": -0.2,
                   "w": "Watch = favorable conditions; warning = happening or about to.",
                   "sol": ["A watch means the ingredients are in the kitchen: prepare.", "A warning means the meal is served: act now."]},
    "winter-072": {"w": "Freezing rain freezes on contact and coats everything.",
                   "sol": ["Sleet bounces like tiny pebbles.", "Freezing rain sticks like glaze on a donut.", "Glaze builds up on lines, so freezing rain is the line-breaker."]},
    "safety-012": {"q": "Historically, which hurricane hazard has caused the largest share of U.S. hurricane deaths?", "type": "mcq",
                   "o": ["Storm surge", "Wind", "Tornadoes", "Hail"], "l": 2, "b": 0.2,
                   "w": "Water, especially storm surge, has been the leading killer.",
                   "sol": ["Surge pushes the ocean onto land like a tide with a shove.", "Fresh water flooding from rain is also deadly inland.", "Wind causes fewer deaths than water."]},
    "safety-013": {"l": 2, "b": 0.2},
    "safety-028": {"q": "A family plans 4 liters of water per person per day for 3 days. There are 5 people. How many liters total?",
                   "sol": ["4 L × 5 people × 3 days.", "4 × 5 = 20 L per day.", "20 × 3 = 60 L total."]},
    "cases-008": {"o": ["Was very large and drove surge into NY/NJ", "Was a Category 5 hurricane at landfall", "Formed over the Pacific Ocean", "Was a small tornado-like storm"],
                  "w": "Size and surge mattered more than category.",
                  "sol": ["Sandy's wind field was about 1,000 miles wide.", "A big storm pushes lots of water, like a big paddle in a bathtub.", "It was post-tropical at landfall, not a Cat 5."]},
    "cases-011": {"l": 1, "b": -0.4},
    "cases-012": {"q": "A case packet shows early 1900s deaths in the thousands, a huge surge, and a Texas island city. Which event does this best match?"},
    "cases-013": {"w": "Joplin killed about 160 people and was rated EF5."},
    "cases-025": {"l": 1, "b": -0.6},
}
DEL = ["winter-069", "winter-070", "winter-077", "winter-078",
       "safety-014", "safety-015", "safety-017", "safety-019", "safety-022", "safety-025",
       "cases-014", "cases-015", "cases-022"]
DEL_FAMILY = ["bl1"]

def build():
    return {"fix": FIX, "del": DEL, "del_family": DEL_FAMILY, "new": NEW,
            "report": "m5 Meteorology B winter/safety/cases. Verified wc1 wind chills (ok, kept). Deleted: dup, trivial or wrong items (e.g. lightning crouch, 4 L/person ambiguity) and the bl1 family (all-No template, replaced). Fixed 12 existing; added %d new, about half level 3. Remaining doubts: Hurricane watch 48h/warning 36h and 13°C lake-effect rule are standard NWS/NHC figures; Joplin deaths 158-161." % len(NEW)}

if __name__ == "__main__":
    d = build()
    for q in d["new"]:
        assert q["t"] in ("winter", "safety", "cases")
        if q["type"] == "mcq":
            assert len(q["o"]) == 4 and len(set(q["o"])) == 4
    json.dump(d, open(os.path.join(OUT, "m5.json"), "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    print(len(d["new"]), Counter((q["t"], q["l"]) for q in d["new"]))
