# -*- coding: utf-8 -*-
"""
Created on Thu May 30 07:59:17 2019

@author: Devlin
"""

import dungeon_toolkit as kit

###############################################################################
## Rules ######################################################################
###############################################################################
stats_explanation = """
You build your own character, starting with assigning stats. There are 5 stats 
in this game : Strength, Dexterity, Constitution, Intelligence, and Charisma.

    Strength is how strong you are. Duh. It affects your damage and how many 
    items you can carry in your bag
    
    Dexterity is how nimble you are. It affects how often your attacks hit
    their target and how often you get hit.
    
    Constitution is how tough you are. It affects your max health.
    
    Intelligence is how smart you are. It affects how fast you level up, and
    how well you can read or interpret certain bits of writing. For the Wizard
    and Sorcerer, intelligence affects the accuracy of your spells.
    
    Charisma is a measure of willpower. It determines your own magical resistence 
    to enemy spells, your ability to persuade people to help you, and for the 
    Wizard and Sorcerer, the power and effect magnitude of spells. 
    
There are challenges based on these stats around the game. Assign wisely.
When starting, the game rolls 4 sets of numbers for you, and you pick one. You
can then assign any number from the set to any stat, allowing you semi-direct
control over your starting stats. When you level up you can assign 2 points 
in any way you wish to your stats."""

races_explanation = """
There are 5 races you can play as: Human, Gnome, Orc, Elf, and Tiefling.
These races affect your stats and, except for humans, have a language their 
culture speaks. Humans get to pick one language to learn, including two 
languages inaccessible by any other race. Languages are used to decipher 
certain texts throughout the game."""

races_flavor = {"Human": "The dominant race of the Kingdom of Galenia, Humans are hardworking, industrious, and stubborn. They have a penchant for making money and a talent for surviving where they shouldn't. Above all humans are blessed with ambition, driving them to greater success than many say they deserve.",
                "Orc": "Orcs were, ages ago, invaders of a different sort. Fleeing conflict in their ancestral homelands, they settled in Galenia as refugees. While they can be violent and aggressive, they are also loyal, family driven, and fearless.",
                "Gnome": "nimble and charming, Gnomes live in the treetops of Galenia's many forests. Inhabitants since the ancient times, they are deeply spiritual, but also very crafty. Gnomes famously secured their independence in a game of cards that was later revealed to be rigged.",
                "Elf": "Descendants of an ancient human race, blessed by the gods with long life and enduring grace, Elves are the proud northerners who usually separate themselves from the affairs of men. Elves are blessed more so by mystique; people seek their services due to their mysterious nature and magical reputation.",
                "Tiefling": "The bastard offspring of Elves and Devils, Tieflings were cast out from Elven society long ago. Today they are a rare sight outside of Galenian slums and secret societies. Known for their shocking appearance and devious natures, Tieflings usually seek the company of kin above strangers."}

classes_explanation = """
There are 5 classes you can pick, set up to work well with any build. They each 
have a preferred type of weapon that gives them a damage bonus and a combat skill 
that sets them apart."""

classes_flavor = {'Warrior': "The Warrior gets a combat bonus with any weapon he wields, unlike the other three classes. He also gets a second wind health bonus when he kills an enemy. For a Warrior, focus on Strength.",
                  'Spy':  "The Spy gets a combat bonus from using Daggers. He gets a bonus to his accuracy and evasion in combat and if his accuracy ever exceeds 100%, the excess becomes a chance to land a critical hit, the damage of which is based on your character's level. He can only land crits when wielding his daggers though, so consider that before trading in for a more powerful weapon! For the Spy, Dexterity is key to maximizing your critical hits.",
                  'Brute': "The Brute gets a combat bonus from using bludgeons. These are the only weapon type that carry a chance to stun their foes. They pair well with the Brutes ability, Brutal Swings, where he attacks every foe in the encounter on his turn instead of having to focus on one, like the other classes. He only gets to Brutal Swing when his health drops below a certain level (depending on the level of the character) and he's wielding a bludgeon. For the Brute, Constitution is essential for maximizing the effectiveness of Brutal Swings.",
                  'Wizard': "The Wizard can learn two spells at a time but can't wield weapons. The Wizard's spells have a splash effect where it's effect rolls over and hits the next foe for a smaller effect. The size of the splash effect depends on your accuracy with the main attack, this makes Intelligence very important for Wizards.",
                  'Sorcerer': "The Sorcerer can only learn 1 spell at any time but gets to also wield a weapon, taking a preferred damage bonus from staffs. The sorcerer also gets a chance to shrug off damage that is below twice his charisma modifier. This chance is higher at higher character levels. Keeping a high Charisma is will help the sorcerer take advantage of this skill."}

prologue = """
***Check your characters stats by typing 'stats' at the consider screen
***Check, use, and drop items in your bag by typing 'bag' at the consider screen
***In conversation, type 'goodbye' to exit and return to the game

You have awoken upon a large altar in a stone room. You don't remember 
how you got here but you feel uncomfortable, and you don't wish to stay any longer
than you have to. As you regain consciousness you hear a door slam and feel a strange
sensation come over your body, as though you are falling gently into a very cold space.
"""

###############################################################################\
## Doors #######################################################################]
###############################################################################/
door_desc = ['glittery and red, with an ornate handle and a large jewel in the center', 
             'sparkly and shiny metal, with a polish that reflects the room back at you', 
             'flaking yellow paint and splintering from old age', 
             'painted green with a small barred window in the middle', 
             'red and tall, as though built for a very tall skinny man', 
             'blue and round, as though repurposed from an old barrel', 
             'elegant and gold, with intricate leafing and patterns', 
             'silver and reflective, so that you can see your own face in it', 
             'pewter and tarnishing, any appearance of wealth or fashion is well faded', 
             'a simple wood door, like one seen taverns everywhere',
             'cheap and ill fitted',
             'a cloth hanging, that somehow forms a perfect seal',
             'a barrier of solid energy that hums gently',
             'a barrier of fire and smoke that crackles and pops at random intervals',
             'a wall of ice that gives no feeling of cold to the room',
             'a fog hanging in the air, obstructing all sight and sound of the room beyond it',
             'a door large enough only for a mouse',
             'a great stone slab, wind-worn and covered in moss'
             ]

door_trans = ['You turn the handle, the jewel glows, and you appear on the other side of the door',
              'You turn the handle and notice the reflection of the room is unchanged as the door swings open',
              'You turn the handle and the door creaks open',
              'You turn the handle and step through the door',
              'You grab the door handle and heave the surprisingly heavy door open',
              'You push the door open and step through it',
              'You turn he handle gently to avoid damaging the delicate leafing',
              'You watch your reflection walk away from you in the door and take the hint to step forward and pass through the door and into the reflection',
              'The door jams at first but eventually swings open on rusted hinges',
              'You step through the door',
              'You push on the door and it falls off it\'s hinges, allowing you to step through',
              'You push it aside and walk into the next room',
              'You walk up to the barrier and put your hand through it - it seems to allow you to pass unharmed',
              'As you approach the fire a small hole opens up just large enough for you to pass through',
              'You touch the wall and it begins to melt until there is enough space you to pass',
              'You step into the fog and feel lost for only a moment before you emerge in the next room',
              'As you approach this tiny door you see it start to grow - it\'s not until you reach it that you see it is you who have shrunk! As soon as you emerge on the other side you return to your regular size',
              'The slab rumles and retracts into the earth at your approach'
              ]

door_barred = ["You turn the handle but the door doesn't budge no matter how hard you push",
               "You find it impossible to even turn the handle",
               "You find the door surprisingly sturdy and immovable",
               "The door doesn't budge as you push on it",
               "You find the door impossibly heavy and immovable",
               "You go to open the door but the handle disappears as you reach towards it",
               "The handle retracts into the door when you try to turn it. The door remains unmoved",
               "You turn the handle and your reflection wags his finger at you",
               "The door seems to be jammed and refuses to open",
               "The door catches fire as you turn the handle, causing you to jump back. As you walk away the door returns to normal",
               "You walk towards the door but you never seem to get any closer to it",
               "The cloth seems harder the steel and totally immovable",
               "The barrier holds firm and refuses to let you pass",
               "You approach the flames but don't see a safe way through",
               "You touch the wall and feel an immense sense of cold that causes you to retract your hand immediately",
               "You step into the fog and wander for a moment before stepping out into the same room",
               "As you approach the door it seems to get smaller. There's no way you can get through it",
               "The slab remains unmoved and refuses to let you past"
               ]

door_unlock = ['You insert the key into the handle and the jewel glows in acceptance',
                'You insert the key and the door reflection seems to brighten',
                'You insert the key and turn',
                'You insert the key and turn',
                'You insert the key and door unlocks',
                'You insert the key and the door spins before you hear the click of it unlocking',
                'You insert the key and the gold leafing moves around as though blowing in the wind',
                'You insert the key and your reflection smiles at you',
                'You insert the key and turn',
                'You insert the key and turn',
                'You insert the key and turn',
                'You can\'t seem to find a keyhole but when you hold the key up, the cloth blows as if in a breeze and the key disappears into the wind',
                'You hold the key up and it turns into a ball of energy and zooms towards the door. The energy-key merges with the barrier, which glows in acceptance',
                'You bring the key to the fire and a key hole forms in the smoke. You insert the key and turn. They key turns to smoke and floats away',
                'You bring the key to the wall and a key hole appears. You insert the key and turn. The key melts and the cold disappears from the air',
                'You hold the key up to the fog and a wind blows. The fog seems to move in place and the key disappears from your hand',
                'You hold the key up and it flies out of your hand and into the tiny keyhole, shrinking as it zips through the air',
                'The key flies from your hand and smashes into the wall, breaking into a thousand pieces!'
                ]

door_short = ['The Glittery Door',
              'The Sparkly Door',
              'The Old Yellow Door',
              'The Green Door',
              'The Red Door',
              'The Blue Door',
              'The Gold Door',
              'The Silver Door', 
              'The Pewter Door', 
              'The Wood Door',
              'The Cheap Door',
              'The Cloth Hanging',
              'The Energy Barrier',
              'The Fiery Gate',
              'The Wall of Ice',
              'The Foggy Pass',
              'The Small Door',
              'The Stone Slab'
              ]

door_statue = kit.Door("A small hatch appears on the ground", 
                       "You lift the hatch and descend into the next room", 
                       '', 
                       '', 
                       "the Small Hatch", 
                       rooma = 'temple', 
                       roomb = 'lab')

door_underwater = kit.Door("You notice a tunnel under the water", 
                           "You swim through the tunnel", 
                           '', 
                           '', 
                           "the Underwater Tunnel", 
                           rooma = 'fountains', 
                           roomb = 'uwater')

door_broken_wall = kit.Door("There's a hole in the rubble big enough to pass through",
                            "You move carefully through the gap so as to not disturb the rubble",
                            '',
                            '',
                            "the Hole in the wall",
                            rooma = 'mess',
                            roomb = 'armory')

door_wall_hole = kit.Door("A small but ornately carved hole in the wall",
                          "You crawl through the hole",
                          '',
                          '',
                          "the Small Hole",
                          rooma = '',
                          roomb = 'shrine')

door_bookshelf = kit.Door("An ornate bookshelf, swung open on hinges revealing a stone archway behind it",
                          "You walk through the archway",
                          '',
                          '',
                          'the Bookshelf',
                          rooma = 'library',
                          roomb = 'sanctum')

door_end = kit.Door("a cobblestone path leading away from the compound",
                    "You begin walking down the path",
                    '', 
                    '', 
                    "The cobblestone path",
                    rooma = 'garden',
                    roomb = 'exxit')

door_holder = kit.Door('', '', '', '', 'placeholder', rooma = 'altar room', roomb = 'portal')

door_option = 'Pass through {}'

###############################################################################\
## Rituals ###############################################***CONTAINS PLOT***###)
###############################################################################/
ritual_names = ['RITUAL OF THE SKY',
                'RITUAL OF ANDROMEDA',
                'RITUAL OF LIGHTNING',
                'RITUAL OF FEAR',
                'RITUAL OF THE MOUNTAIN',
                'RITUAL OF PERSEPHONE'
                ]

ritual_vials = ["a sweet-smelling nectar",
                "red paint made from berries that grow near your childhood home",
                "blue paint made from the flowers that grow on your family's graves",
                "yellow paint made from the shells from the beach your mother lives on",
                "cool water",
                "a silvery substance that seems to float as much as flow"
                ]

ritual_dishes = ["the petals of a pink flower",
                 "pebbles of various sizes",
                 "the petals of a blue, exotic-looking flower",
                 "small smooth pebbles",
                 "small speckled pebbles",
                 "small gears and levers and wires"
                 ]

ritual_bowls = ["coarse black sand",
                "powdered bone",
                "a tangle of light blue string",
                "a dense yellow slime",
                "a neon-green liquid giving off smoke",
                "a clear liquid that gives off a foul odor"
                ]

ritual_order = [[0,1,2],
                [2,0,1],
                [0,2,1],
                [2,1,0],
                [1,0,2],
                [1,2,0]]

all_rituals = [kit.Ritual(ritual_names[i], 
                          ritual_vials[i], 
                          ritual_dishes[i], 
                          ritual_bowls[i], 
                          ritual_order[i]) for i in range(len(ritual_vials))]

game_rituals = {'John': all_rituals[0],
                'Ulldar': all_rituals[4],
                'Urumbrior': all_rituals[2],
                'Lyestra': all_rituals[5],
                'Jaggard': all_rituals[1],
                'Halenhadra': all_rituals[3]}

###############################################################################\
## Potions #####################################################################)
###############################################################################/
potion_str = "dense and viscous red liquid"
potion_dex = "bubbly and energetic green liquid"
potion_con = "steaming yellow liquid"
potion_int = "sweet smelling blue liquid"
potion_cha = "bitter smelling sludge that reminds you of thick mud"
potion_mhealth = "purple liquid that seems to sparkle when the light hits it just right"
potion_health = "violet liquid with flecks of blue and red still floating in it"
potion_gold = "liquid that looks like liquid gold"
poison_str = "red liquid that turns crimson when you shake it"
poison_dex = "green liquid that foams when you uncork it"
poison_con = "yellow liquid that seems more a dense sludge than anything edible"
poison_cha = "salty smelling liquid that reminds you of seawater"
poison_int = "blue liquid that smells like strawberries"
poison_mhealth = "bright orange liquid that never stops moving"
poison_health = "brown liquid that looks sticky"
poison_gold = "liquid that looks like liquid gold"

potion_names = ['Potion of Strength', 'Potion of Dexterity', 'Potion of Constitution', 'Potion of Intelligence',
                'Potion of Charisma', 'Potion of Max Health', 'Potion of Health', 'Potion of Gold',
                'Strength Poison', 'Dexterity Poison', 'Constitution Poison', 'Intelligence Poison',
                'Charisma Poison', 'Max Health Poison', 'Pure Poison', 'Poverty Poison']

potion_flavors = [potion_str, potion_dex, potion_con, potion_int, potion_cha, potion_mhealth, potion_health, potion_gold,
                  poison_str, poison_dex, poison_con, poison_int, poison_cha, poison_mhealth, poison_health, poison_gold]

potion_stats = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Charisma', 'Max Health', 'Health', 'Gold',
                'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Charisma', 'Max Health', 'Health', 'Gold']

potion_lower = [1, 1, 1, 1, 1, 5, 10, 10, -3, -3, -3, -3, -3, -40, -50, -100]

potion_upper = [4, 4, 4, 4, 4, 40, 100, 100, 0, 0, 0, 0, 0, -5, -10, -10]

potion_masks = ['Mysterious', 'Suspicious', 'Suspect', 'Strange', 'Weird', 'Unusual', 'Odd', 
                'Bizarre', 'Curious', 'Peculiar', 'Wacky', 'Uncomfortable', 'Slippery']

###############################################################################\
## Food Flavor ################################################################<
###############################################################################/
food_names = ['Turkey Leg', 'Cheese', 'Sandwich', 'Ale', 'Apple', 'Pear', 'Whole Ham',
              'Pie', 'Grapes', 'Wine', 'Roast Turkey', 'Pork Roast', 'Mashed Potatoes',
              'Orange', 'Caramelized Onions', 'French Onion Soup', 'Crackers', 
              'Asparagus', 'Cheesecake', 'Cookies']

food_flavor = ["a delicious looking turkey leg",  
               "a small part of a cheese wheel",
               "half of a smoked turkey sandwich",
               "delicious ale, home brewed",
               "a fresh apple, complete with worm",
               "a ripe pear, which smells fantastic",
               "an entire ham, which somehow fits in your bag",
               "your favorite pie, fresh from the oven (at some point) and delicious",
               "fresh and juicy grapes",
               "aged wine whose smell relaxes you more than is appropriate for the situation",
               "a whole roasted turkey, spiced, salted, and slow cooked",
               "a salted pork roast, juicy and delicious",
               "salty and creamy mashed potatoes",
               "a juicy and fresh orange",
               "cooked real slow over low heat in lots of butter to bring out the natural sugars of the onions",
               "served in a bread bowl with a thick layer of melted mozzarella over top",
               "crunchy and crumbly and salty, would pair well with cheese and wine",
               "asparagus is nasty even in my fantasy dungeon",
               "delicious cheesecake that melts in your mouth",
               "fresh, hot, gooey chocolate chip cookies"
               ]

###############################################################################\ \
## Equipment Flavor ##############################################################
###############################################################################/ /
equipment_gloves = "Skillfully crafted black leather gloves"
equipment_amulet = "An amulet with a beautiful opal set in the center"
equipment_beads = "A bracelet of bright blue glass beads"
equipment_bracers = "Steel bracers that clamp firmly around your wrists"
equipment_ring = "A gold ring that emboldens your confidence and willpower"
equipment_boots = "A pair of very fine leather boots"
equipment_satchel = "A canvas bag that can go over your shoulder and carry your shit"
equipment_shield = "An Iron Circle of impenetrability"
equipment_belt = "A belt of finely tanned leather with a simple gold buckle"
equipment_sash = "A fur sash that hangs over your chest"
equipment_bones = "A simple crown made of various bones, teeth, and claws"
equipment_light = "A simple crown that glows light a fire"
equipment_iron = "A simple iron crown, mildly rusted and poorly wrought"
equipment_green = "A crown of vines, branches, leaves, and flowers"
equipment_gauntlet = "A gauntlet of fur and steel that whispers to you while you wear it"
equipment_fire = "A wreath of fire that sits elegantly, yet firmly, upon your head"
equipment_pendant = "A brilliant red jewel that glows with what looks like a fire within"
equipment_mask = "A red mask that bears a frightening expression" 
equipment_helm = "A helmet of wrought iron that makes any wearer a fearsome warrior"
equipment_orb = "A crystal orb that empowers the mind of spirit of the holder"
equipment_tome = "A holy book, blessed by the original 6 gods of Firellia"

###############################################################################
## Weapon Flavor ##############################################################
###############################################################################
flavor_fists = 'nyeeeeeeehah'
flavor_shortsword = 'You slash with your shortsword with deadly effect'
flavor_mace = 'You throw all your weight behind your barbaric swings'
flavor_dagger = 'You lunge forward and stab the dagger into your foe'
flavor_staff = 'You bring your staff crashing down upon your enemies\' head'
flavor_knuckles = 'You pummel your foe into a bloody pulp'
flavor_cutlass = 'You make a long slash across your foe\'s chest, evoking a howl of pain!'
flavor_hammer = 'You bring your war hammer crashing down upon your foe\'s head with a mighty swing!'
flavor_longsword = 'Your longsword slices through skin like a knife through butter'
flavor_broadsword = 'The weight of your broadsword cracks bone as it comes down on your foe'
flavor_club = 'Your club comes down on your foe\'s head with a mighty THWACK'
flavor_dread = 'Your dagger finds it\'s mark, causing a shriek of pain from its victim'
flavor_ornate = 'The staff courses with energy as it comes down on your foes'

encounter_intro = "You've been ambushed! Prepare to fight!"
encounter_victory = "You breathe a sigh of relief as you emerge victorious"
encounter_cont = "You enter the room and your old foes are still there waiting for you!"

###############################################################################
## RNG Walls ##################################################################
###############################################################################
wall_ornaments = ["a mural of a handsome man in heavy armor, gazing off into the sunset. Birds are flying all around him and there is a ring of birds flying around the sun",
                  "a stone engraving of a large hooded figure. It is worn and weathered and you think you can see where it used to be painted",
                  "the remains of a grand mural, you can't make out much detail but it appears to depict a large flood or a similar disaster",
                  "a great deal of empty wooden shelves, covered in cobwebs and dust",
                  "a star chart, intricately painted, that doesn't show any constellations you recognize",
                  "a rough brick wall, with plaster falling off to reveal granite blocks underneath"
                  ]

###############################################################################
## RNG Statues ################################################################
###############################################################################
statues = ["This statue is of a strange looking beast. The heavily armored body of a man with the head of a dog. Hs fangs are beared and his sword is out and pointed at the room. On his breastplate is a symbol: a large dead tree.",
           "This statue is of a conletely cloaked figure. His only visible feature is the tips of his fingers extending out of his sleeves. You think you can make out a face inside the hood but you can't be sure.",
           "This statue is of a lion standing over a man. The lions teeth are beared ad the man has a look of sheer terror in his face. He is unarmed and defenseless. On the lions back sit three small birds.",
           "This statue is an old man wearing elegant robes and holding a large staff. He has a look of absolute confidence on his face and his staff is topped with an actual jewel.",
           "This statue is of an orc wearing nothing but a loincloth and looking particularly fierce and barbaric. He stands in an agressive pose over a pile of bones, with exagerated tusks and claws.",
           "This statue is of an orc wearing elegant robes with the insignia of a great eye on the chest. He has a confident, intelligent look about him. One hand is raised, conjuring a fireball, the other holds a scroll by his side.",
           "This statue is of a group of gnomes working together to hold up a mechanical contraption. They look excited and energetic and their device is bulky with lots of gears and wires and tubing.",
           "This statue is of a single gnome wearing a cloak with the hood down. He holds a dagger in one hand and has a very angry expression on his face. The ground he stands on is marked with an insignia: A strange geometric design that looks as though its moving.",
           "This statue is of a tall elf, wearing heavy armor and wielding a great club. He looks stubbornly proud and haughty, with his chin pointed up and his mouth curled into a half scowl.",
           "This statue is of a great angel, with 4 pairs of wings and 2 pairs of arms. He holds one hand a small scepter and in another a long scroll. The statue is ballanced on the toes of one foot.",
           "This statue is of a skeleton standing limply, skull pointed down, as though it was suspended by marrionette strings. It holds another skeletons arm in its hand and is missing several ribs.",
           "This statue is of a tree, with few leaves and fewer blossoms. There are some small birds in the branches and one large owl sitting near the trunk. You think the owls eyes are amber because they seem to glow orange.",
           "This statue is of a woman, not particularly beautiful, but definitely deadly. She wears chainmail and wields a spiked mace as though it weighs nothing. The look in her eye is unmistakable - rage."
           ]

statue_john = "This statue is a tall man in armor, he's holding a large sword and looking down at his feet. He's wearing a sash over his chest and a scarf around his neck. At his feet is a symbol: a sun with a bird at the center."
statue_halenhadra = "This statue is of a hideously deformed woman whose lower body has assumed the form of a giant spider. Her upper body is naked and quite beuatiful but its impossible to ignore the 8 long legs and the sharp stinger emerging from her abdomen."
statue_ulldar = "This statue is of a short man, wearing a wooden helmet. He has attached antlers to it and carved primitive eye-holes, giving it an eerie, discomforting look. He's oherwise dressed head to toe in furs and standing very innocently."
statue_jaggard = "This statue depicts a robed skeleton, missing his lower jar, but still standing strong. His arms are entirely hidden by long sleves and he appears to be hovering slighly above the ground. Most disconcerting are the empty eye sockets that still seem to stare right through you"
statue_urumbrior = "This statue is of a Half-Dragon, tall and proud. Wearing heavy armor and weilding an enormous battle-axe, he gazes over your head and looks invincible. But there's something menacing in his stance - something evil and aggressive that you can just barely detect..."
statue_lyestra = "This statue is of an old an wrinkled woman, her hands outstreched, either to hug you or choke you. He skin barely hangs to her bones and her robe barely covers her flesh, she seems to be very poorly put together, just hanging onto life."

###############################################################################
## RNG Faces ##################################################################
###############################################################################
fountain_faces = ["one that is making a face like a monkey with water coming out of his nose",
                  "one that is a clown face, with make-up and hair done up",
                  "one that has abnormally large eyes, with spots were jewels used to be in the pupils",
                  "one that has large ears with droopy earlobes and water coming out of its eyes",
                  "one that is shaped like a bird head, with water comeing out of the beak",
                  "one that is spitting water out of each of its three mouths",
                  "one that has strange shape carved into its cheeks",
                  "one that is upside down, with eyes wide opne",
                  "one that is almost rectangular, with strange lines on it's chin",
                  "one that has tusks like an orc, ears like and elf, and eyes like a gnome",
                  "one that has feathers coming out of his head instead of hair",
                  "one that has no lips, just rows of teeth",
                  "one that has a wide open mouth, as if it's gasping"
                  ]

###########################################################################################\
## GAME LORE ###############################################################################\
#############################################################################################\  
## Lore is constant amongst all games. It describes the world around the dungeon           ##/
## The in game plot is variable, but what is here is always the same.                     ##/
###########################################################################################/
provinces_coastal = """The Provinces of Galenia - The Coastal Province: The Kingdom of Galenia has 6 major provinces. The Coastal Province is the major powerhouse of the Kingdom, being the ancient home of King Galen and the location of the Capital City. The coastal region benefits from rich farmland in the Ishmarani River Delta and commerce brought by river traffic. Historically, oversea shipping was near impossible because of the 3 great leviathans that lurked off the coast, and though these beasts haven't been sighted in over a century, people are still reluctant to take to the sea. But this hasnt stopped the region from flourishing. Between the cities of Ronsinland and Drarden the region has a thriving economy and a rapidly growing population. Ronsinland is a major river port and past piate base, full of bad smells, foul personalities, and rich merchants. Drarden is a wealth city full of noblemen, built on the road to the forest province, and home to several notable organizations. Several small cities and towns dot the landscape, roads and bridges are well maintained, and Galenian gaurd are common sights (though crime thives regardless). None of this comapres to the capital city, however; The city of Galenia is elegant, magnificent, and robust. There is a shop for everything, a tavern for everyone, and people from everywhere. Many churches and guilds have their headquarters in Galenia and the royal court is numerous and quite wealthy. The taxes of living in the capital are higher but there is quite literally nothing you cannot do in Galenia. The Coastal Region is truly the jewel in the crown of the kingdom. 
"""

provinces_plains = """The Provinces of Galenia - The Great Plains Province: The Kingdom of Galenia has 6 major provinces. The Great Plains province is the true bread-basket of the kingdom and was the first to get conquered dring the unification. The plains are safe and boring, though lacking in commerce and economic opportunity. Devoid of great cities, the plains is instead home to hundreds of small towns and communities where people ake care of each other and tradition is very important. While people can be a little old fashioned, they are accepting to all people and have hospitality to spare. Travelers are always welcome in the Great Plains, if for not other reason than there aren't that many. Not to say that the PLains aren't without intruigue. The great pit is an enormous and myserious hole in the ground that is said to house the bastard son of the God of Light, Theofen. And the Lich King Jaggard had his headquarters at the far northern edge of the province, near the Dwarven kingdom of Kalash. But for the most part, the people of the great plains live simple lives and are devoted citizen of the kingdom.
"""

provinces_forest = """The Provinces of Galenia - The Forest Province: The Kingdom of Galenia has 6 major provinces. The Forest Province to the south of the coastal region is dominated by the Ardani Forest. The forest is ancient and a pilgrimage site to many who worship the traditional gods. There is only one road through the woods and there a few minor cities established along it. The most famous is Constantieren, the tree-top city. Originally built by Gnomes, the city became a popular rest site for travelers until it eventually became absorbed into the kingdom. Today, there are few Gnomes left in the city and few places left of the original Gnomish Architecture. The city is especially important considering the magic of the forest. While not strictly proven, several local legends tell of the forest having a very close relationship to the feywilds. Many local townspeople claim to have accidentally stumbled into the feywilds while walking the woods, and many travelers have gone missing after wandering off road, but this is far from the evidence the mages guild reqires to lanunch an official royal investiagtion. Regardless, the Forest Province is an enchaning and unique part of the kingdom. 
"""

provinces_halea = """The Provinces of Galenia - The Halean Province: The Kingdom of Galenia has 6 major provinces. The Halean Province is the second most populated province due to Halea, the city on the lake. Lake Silva is the larget lake in the kingdom and Halea is built on an island in the center. The lake is home to a city of merpeople; between that and the road to the neighboring kingdom of Lewanir, the City has become a trade hub. At some point the city become too large for the island so city engineers started to build out over the water. The poor parts of town are built upon simple wood stilts, but the richer parts are built on stone outcroppings. The mer-market is one of a kind, it has special booths for mer-people to sell their crafts and is a major tourist destination. The central tower is the other landmark; it was constructed before unification to house the city's mage's guild. After unification, it became a chapter of the Galenian Mage's Guild but due to the resources collected, the tower has remained a hub of magical research and learning. Outside of the city, the province is home to several small fishing settlements on the edge of the lake (the tower of Halea is visible from all of them) and even more trading posts along the Lewanir Road. The border is well protected but easy to cross due to healhy relations between the two kingdoms. The Halean Province is an economic and cultural powerhouse in the kingdom.
"""

provinces_gavenhall = """The Provinces of Galenia - The Gavenhall Province: The Kingdom of Galenia has 6 major provinces. The province of Gavenhall is named after it's major city, which was a strong and respected independant kingdom before unificaton. Founded by the druid Gaven, it was based on he druid beliefs of respect for nature and ballance between man and wilds. While Gaven could be a bit extreme, the city he founded became a cultural hub, home to several churches and artistic guilds. After Gaven passed disapeared, the city was ruled by Denoran Galvear, who established the legendary Knights of Gavenhall. The Knights of Gavenhall have extremely high entry requirements and are elite gaurdians of the cities cultural history. When King Galen moved on the city, the Knights held off an enemy force 12 times larger than them for over two weeks before the seige was broken. It was a costly victory for King Galen and he respected the effort. Gavenhall has the most independence of any city in the kingdom because of it. Outside of The city, the province is notable for the continuation of the Ishmarani River and the swamps of Malashar (the site of the famous seige and pyrhic victory against the Knights of Gavenhall). There are small fishing communities in the swamps, rumors of a cave that leads to the underworld, and a surprising amount of giant spiders in the wilderness, but overall, the major destination is Gavenhall. 
"""

provinces_mountains = """The Provinces of Galenia - The Mountain Province: The Kingdom of Galenia has 6 major provinces. The Mountain Province is the northernmost province and the most unusual. It is home to The Scar - the site of the famous battle between King Gaven and Urumbrakil, the kingdom of Kalash - the mighty dwarves who function as the bankers and investors of he kingdoms of Firellia, and Mount Horatio, the only active volcano on the continent. The city of Lansaria is built into the mountainside and is a popular site with religious pilgrims, paladins, clerics, and acolytes. The mountain it's built on, Mount Diasmar, is the source of the Lansing River, and is famous for being the highest peak in the kingdom. While the climb is grueling, the peak is a holy site and and the destination of many pilgrimages. Illenstar, Galenian god of the sky, is said to come to those who reach the peak, though in order to get there one must make it past storm giansts, dragons, chimeras, and other dangerous beasts. The Kalashite Dwarves are the hardiest and most independent people in existence but without the alliance between them and he royal family, the Galenian economy would be DOA. Urumbrakill is the most famous story of the kingdom, so we will not waste time discussing that. Really, the Mountain Province is the important diversity that allows the kingdom to function. It also acts as the nothernmost border to the kingdom, with the elven city of Istellian on the other side of the mountains. 
"""

kalahite_dwarves = """The Kalashite Dwarves are a proud and noble kingdom. Living deep inside Mount Kalash, they became extremely wealthy through mining and used that wealth to establish world-class banking and investing services. But these are no finance-nerds. When the Lich King, Jagard, threatened to devour the (the independent) city of Hadrensville to give his followers imortality, it was the Kalashite Dwarves who stopped him. They laid seige to his fortess in the mountains and when the fortress broke, they chased him into the forest. The Kalashite King, King Egard, lost his only son in the battle of Malashar Forest, but the Lich King's reign of terror was over. Since then, the Kalashite King has been democratically elected, and all the kingdoms of Firellia have had a great fear of Necromancy. The Kalashite Dwarves have the respect and admiration of the the kingdoms of Firellia, to the point where King Galen did not conquer them duirng unification. Focusing on mining and using their tremendous wealth to finance the world around them, the kingdom today is wealthy, strong, and necessary to the world. Kalash City is often said to be the safest city in the world and the Kalash King is the most respected and powerful person in the land.
"""

urumbrakill = """The great battle between King Galen and Urumbrakill is the most famous story in Galenian History. Urumbakill, the great black dragon of the north, terrorized and decimated the cities of the north for ages before he met his end in the battle of the Scar. His followers, deluded as they were, believed that they were protecting themselves and their families by serving. In reality, they were probably in more danger tha most due to having more contact with the scourge of the mountains. The Kalashite dwarves purposely buit Kalash City behind monstorous defenses to keep Urumbrakill out and the Elves of Istellian worked powerfull magic to keep him away (there are rumors of more sinister defenses of Istellien but nothing has been proven). When King Galen unified the indpendent human provinces, his unification campaign climaxed with the battle of the Scar, where his troos fought Urumbrakill's forces in the forests at the base of the mountains. Urumbrakills fires scorched the land so intensely that the trees could not grow back, forming a permanent black scar on the land, hence the name. Before the fight, King Galen worked to gain divine blessings from all 6 Gods of Firellian tradition, so when he encountered Urumbrakil, he had the magic and strength to match him in combat. After hours of grueling combat, King Galen summoned a bolt of lighting that struck the great beast from the sky, after which the Divine King removed his head and ended his reign of terror. 
"""

istellian = """The trade hub of the Elven kingdom, Istellian is the least traditional of all Elven cities but also the wealthiest and most populous. Istellian is the most neopolitan of all cities in Firellia; you can find Gnomes, Orcs, Humans, Dwarves, and all varieties of Elves in the city. Elves are technically a minority in the city compared to human merchants but the city is under the rule of the Elf Lord Faiellen, and Elven culture can be found in surprising places. The city is home to 4 ancient and respected Elven families; the Faiellens, the Solirias, the Ellarias, and the Irithyls. the Faiellens have been highly respected politicians for generations; a member of this family is frequently chosen by the Elven King of Winds to be lord of the city. The Solirias are renowned masons and architects. The designers and builders of Istellian castle, Ria'lew castle, and the walls of Ololewin, they have the respect, admiration, and appreciation of many. The Ellarias are merchants and traders, clever with finances and ambitious in all things. They have been advisers to the King of Winds for generations. Lastly, but no less important, the Irithyls are an ancient magical family known for their ruthlessness and trickery. Well respected by elven high society, they are often asked to do things that few others would want to. High in the mountains above the city is the headquarters of Istels Ruby, a mysterious organization founded by the 4 families. Adventurers, warriors, and mages can be seen coming and going, but all remain very tight lipped about what actually goes on there. 
"""

sholan = """The mighty god Sholan is the Firellian God of the Sea. He created the seas as a home for his children, Kraken, Sunderfoe, and Leviathan. He can be summoned through a decent sacrifice or by a ritual that involves killing one of his children but summoning Sholan is unadvisable. He is violent and merciless, treating all with a fairness and equality that the poor and downtrodden find appealing but the gifted and powerful find frustrating. He has a great respect for power but the sea is uncoquerable and the tides cannot be tamed or overpowered. He will take great pride in meeting a powerful adventurer but will kill them just the same. Sholan is worshiped by the Church of the Sea in Drarden.
"""

illenstar = """The ellusive god Illenstar is the Fireliian God of the Sky. It is said that Illenstar drpaed the heavens over the land at the beginnig of existence, that a flap of his wings creates a breeze felt on the surface, and that the sun rises and sets when he roars. Illenstar flies high above the clouds and uses his true-sight to see everything that happens in the mortal world. He is a fierce warrior and many dragons carry scars from encounters with him. Despite the rarity of his sightings, he is an incredibly social being and incredible simple to reach. All you have to do is climb to the top of Mount Diasmar and shout out to him. Easier said than done, many pilgrims try to reach the summit and die trying. Illenstar values freedom, bravery, and loyalty and will respect visitors who demonstrate the same values. Illestar is worshiped by the Church of the Sky.
"""

nirani = """Nirani is the many-armed Firellian God of Passion and Art. The Story of Nirani's Court is legendary - Ages ago, the God Nirani had a court that was open to anyone. Artists and Craftsmen could come and demonstrate their tallents to the people of the court and recieve boons from the God himself. It was a place of creativity and debate and soul. One day, a great warrior, blessed in skill with a blade but lacking in imagination, heard of Nirani's court and became enraged at what he saw as the wasting of power. He visited the court and demanded a boon from the God. When Nirani refused, the warrior challenged him to a duel, which he lost. Infuriated with his defeat, the warrior turned on the court and slaughtered many innocent people before Nirani could stop him. Devastated at the loss of life, Nirani sealed the doors to his court and created 18 spirits of worldly experience to spread his philosophy. It is said that only with the blessing of all 18 spirits can one unlock the gate to Nirani's Court, but no one even knows where the gate is. This hasn't stopped adventurers from seeking it, but there as been no word of any substantial success. Nirani is worshiped by the Church of the Flame.
"""

theofen = """Theofen is the elephantine Firellian God of Light. It is said that he first carved a spot out of the darkness for Firerllia. He lives in a castle made out of clouds and sends mesages though thunder and lightning to his chosen followers. Theofen believes in absolute morality, justice, and independence. He is very helpful to powerful people who share these values, otherwise, getting his help is very difficult. Theofen is worshiped by the Church of Light.
"""

bastard = """Probably Theofen's most famous legend is the legend of his bastard, Garrofen. Generations ago, Theofen was in love with the Queen of Galenia. He disguised himself as a man and, over several months, seduced the Queen. Their offspring was Garrofen. In his youth Garrofen looked like a young boy, but as he grew his monstorous form became more evident. When he reached adulthood he ate his mother and the King banished him. It took the enitre Galenian Faesae Gaurd to subdue him, but the they managed to drop him into Klimsfield Pit in the Great Plains Province. There, the Mages Guild layered enchantments to trap him there. Today, the pit is heavily guarded but no one really knows what's in there. There are rumors that the stories of Theofens Bastard are simply a coverup for more sinister things - secrets of the king. Necromancy, portals to hell, political prisoners, and other things. Very few will every know the truth.  
"""

daltos = """The legendary god Daltos is the Firellian God of the Earth. A very passive being, it is said Daltos sleeps somewhere on the earth in the form of a great mountain and has not woken for centuries. He has instead appointed 4 Gaurdian to protect the natural world and wakes only at their request. Powerful beings in their own right, his gaurdians are equally legendary and a frequent subject of traveler stories and tall tales. The Wispy Wolf is an enormous wolf who lives hidden in a continuous dense fog that follows him around. He wanders the mountains, protecting the land from miners and other dangers. The Gnarled Giant lives disguised as a tree, only moving when another tree call to him. The only Guardian who can speak to plants, he protects against deforestation and polution by merhants guilds and other factions. Though slow-moving, he is the oldest and most dangerous Guardian. The Barkskin King is a horrible disfigred man with skin like tree-bark. It is said he can walk in one tree and out another, and in doing so can move through a entire forest in a day. He protects against deforestation and frequently collaborates with the Gnarled Giant. The Shambling Swamp is a being composed entirely of vines who protects the swamps from pollution and overfishing. It is said he can split himself into multiple parts and be in many places at once. Daltos is worshiped by the Church of the Storm, both of whom stress humility, practicality, creative destruction, and bowing to the inevitable.
"""

barkskin = """The Barkskin King was an ancient King who once did battle with another of Daltos' Guardians. As King, he oversaw a grand expansion of his city requiring a vast amount of timber from a nearby forest. When his citizens cut down large swaths of trees, the Great Root Serpent was enraged and began attacking lumber camps. The King set out personally to stop him and eventually encountered him in a great battle. When he slayed the Guardian, Daltos awoke with a rage and cursed him, turning his skin to bark. The ruined king fled and found refuge in the forest, and there came to find happiness. Until the new king sought to finish the cities expansion and resumed loggin. They threatened the happiness he had found among nature so he, nonviolently, drove them off, saving the forest he had once condemned. Daltos saw this and made him a Guardian. 
"""

aaramesh = """The most fearsome Orc who ever lived, Aaramesh claimed his Godhood at the tip of a sword. As an Orc General, he led a campaign against all of Firellia with the express goal of angering the Gods. He committed atrocity after atrocity, displaying a strength and cunning to rival any who ever lived. His plan worked and when the 5 came to confront him, the battle lasted days. Eventually, Aaramesh wounded Sholan and held his great sword to his throat. That is when he made his famous demand "Make me a God or I'll make him a Mortal". The Gods, forced to acquiesce, told him that he would become a God only if his army was allowed to be destroyed. Aaramesh agreed without hesitation but secretly kept his 10 top lieutenants alive, to carry out his will in the shadows. And thus a god was made. Sholan is said to still walk with a limp.
"""

ulldar = """A man or a myth? Ulldar Kang is as mysterious a figure as was ever spoke of. The legends say that was once a Knight of Gavenhall, pre-unification, before becoming a powerful Druid. He grew in power and influence in the city until his power rivaled that of the King. The King, being aware of the danger posed by this man, worked in the shadows to drive him from the city, killing his sister and framing him for necromancy. It worked and Ulldar fled to the forest. From there he becomes even more msyterious with stories popping up about him sproadically, some more credible than others. If these stories are to be believed, he has lived much longer than the average Druid and has adoped some strange and unusual druidic practices. More likely, he is long dead and these are travelers stories, designed to impress at the local tavern or keep people from leaveing the roads. 
"""

halenhadra = """Ages ago, a Dark Elf woman named Halendra fled her underground community becase she refused to participate in an attack against a rival village. In a tale as old as time, she was in love with a man from that village and pregnant with his child. When her father renounced her and her death was assured, she did what no Dark Elf has ever done before and started a community on the surface. Not just any community, the town of Halendra became famous as a pacificst community and attracted many peace loving people of every race. But peace is ellusive in the world of men. The great Necromancer and future Lich King, Jagard, was rising in power and attracting followers with promises of eternal life. He had already delivered to his top generals and many believed he would become a new God, the God of Death. But Jagard felt threatened by Halendra's peaceful community. The idea of a town of people who neither feared death nor fought to prevent it undermined his base philosophy. In an attempt to destroy Halendra's legacy, Jagard began wooing her daughter, Halenhadra, with promises of power and influence. Raised in the pacifist bubble of the community, she was easily seduced and joined his side as his favorite trophy. Jagard transformed her into a monstrous being, half-woman, half-spider, and gave her a magic to rival any in the mages guild. Halendra was devastated and died soon after. But her community persists, a testament to the notion that people will stand up for peace. As for Halenhadra, she was not present at Jagards downfall, and rumors circulate that she still exists somehwere but no one knows her true fate.
"""

jagard = """The most famous threat to Firellia in recent history, Jagard was anything but unexpected. Born to a wealthy family, he displayed an innate magical talent from youth. His parents gave him every advantage, every opportunity to excel. And excel he did, at 20 years old he was the youngest member of the mages council and a respected advisor to the king. Then tragedy struck when the King's young wife fell deathly ill. The King instructed the Mages Council to do anything necessary to save her. Most of the Council interpreted that as "anything necessary but dark magic", only Jagard researched those magics that are forbidden above all else. When he brought his findings to the council, they flew into a rage and barred him from aiding the Queen. The Council proceeded with their own methods, and, regrettably, the Queen died a month later. Jagard was furious. He was convinced he could have saved the Queen and his return to the council made that fact known. It didn't help that the King, full of grief, agreed that the wunderkind could have helped. The King only grew closer to Jagard in the following months and Jagard thrived in the King's inner circle. From there his descent into madness was clear and direct. He gained a reputation as the Sage who would fight Death. The physical changes were slower and took more time. It wasn't until the next king that his physique began to show signs of the unnatural transormation he was undergoing. His skin paled, his body shriveled, his eyes darkened, and most everyone tried their best to ignore it. He was still very popular, and no one wanted to confront the monster they had allowed to grow in their midst. If only they knew what would happen next...
"""

egard = """The most famous of all the dwarven kings is King Egard, slayer of Jagard and last hereditary monarch of the Kalashite Dwarves. Noble, brave, and virtuous are words that are often used to describe him; his rule was defined by an increase in Kalashite Pride. As a young King he championed infrastrcture improvements and grand construction projects. He contructed Giant's Stride Bridge between two nearby mountain peaks, an incredible feat of engineering and an icon of Dwarven mountain dominance. His other achitectural claim to fame is the indomitable Griffons Call Fortress. A mighty structure that stands atop a small mountain overlooking the main path, Griffons Call is the first thing visitors see when traveling through Dwarven Land. It was also the site of the encounter that propelled Egard into legend. When the Lich King Jagard sent his armies to Mount Kalash, it was at Griffons Call where the dwarves made their stand. For 5 weeks the Necromancer and his followers laid seige to the fort; dwarven morale was low, supplies short, and tensions high. Egard knew something mst be done, so he slipped out in the night and didn't return for 4 days. When he came back, he was followed by a small army of giants. He had marched them across Giants Stride Bridge (hence the name) surprising the Lich King and terrifying his armies. Sensing his moment, Egards son broke out of the fortress with several legions of dwarven soldiers and killed many of Jagards men. Egard and his army pursued Jagard and his fleeing forces to their own fortress, and defeated the lich king in a decisive battle. Egard personally smashed in the Lich King's head and earned his place in the pantheon of great heroes
"""

istels_ruby = """Hey Reysca, \n          I got something something I gotta talk to you about. A week ago, I got a letter from the Solirias inviting me to their weird compound in the mountains. I didn't really want to go but how do you refuse an invitation from the Solirias? So I make my way up there and... it's not a compound. It's a fortress. An old one. Basically in ruins. But there are soldiers, mercernaries!, standing guard, fully stocked armories, and battallions who just seem to be there. So I show the guards at the gate my invitation and they let me in and show me to a dining hall and inside is Liran Solirias, along with Ducan Faiellen, Vallian Ellarias, and Oenel Irithyl! I wasn't expecting that and I definitely wasn't expecting what came next. You Mother! She's head researcher there and I think she might be into something a little dangerous. Besides the army sitting outside the doors, she kept asking me what I knew about Solars. I told her what I knew, that Solars are an ancient race of winged men who possesed immense strength and power. But she seemed to already know what I was telling her... she wanted to know how to control one. Reysca, no one has seen a Solar for centuries, and that's a good thing. They had rigid codes of honor and jusice and would massacre entire towns for their perceived sins. Trying to control it... it's signing your death warrant. Even if you manage to do it for a while, eventually it will wake up. And it will kill you. Anyways, I thought you should know.  \n     -Niada
"""

swords_of_ithel = """Gerald! \n          I got us in! It's unbelievable! I was in Halea at a bar and I'm telling the story of when we took down that hydra in the coastal caverns, the one that soldiers kept trying to kill by cutting the head off so it had like 75 heads by the time we got to it, and sitting at the table behind me was Darian Eritreor! He heard the whole thing and invited us to join the Swords! US! In the SWORDS OF ITHEL! We would belong to the same guild as Faeris Traygar, who killed two medusas (according to Darian they were lovers) while blindfolded AND deafened, and Erian Decain, who cleared the Windsong Crypt of undead singlehandedly (Darian said one of Jagards lieutenants was down there!)! We need 200 gold pieces as an entry fee and there's a test phase where we're on tryout but c'mon we're a shoe in. Hurry up and get here, and bring 200 gold pieces. I used all my money to buy Darian drinks. Whoops. HURRY! \n     -Boch
"""

church_of_sea = """The traditional church of the coastal province, the Church of the Sea is about the unknown, constant change, chaos, and mortality. Sholan is the head of the pantheon, and a physical manifestation of those ideals. Impossible to read or understand, with a violent temper to match his merciless willpower, he almost never appears in the same form twice. He is identifiable in most depictions by his piercing red eyes and limp leg. The church of the sea is headed in Ronsinland, in the Chapel of the Breaking Wave. The Chapel of the Breaking Wave is build into an old shipwreck on the coast. 
"""

church_of_flame = """Founded and practiced primarily in Gavenhall is the Church of the Flame. While most people expect that the home of the famous Knights of Gavenhall would have a more militaristsic, disciplined faith, it is actually quite the opposite. Locals view religion as the other side of the coin, where battle and work is for discipline, religion is for passion and whimsy. The Church of the Flame is all about passion, art, energy, honesty, joy, and celebration. Church is less like a more traditional service and more like an exhibition of tallent and acomplishment. You will find many people gathered in a room, standing, showing others what they made, what they can do, and what they are learning. In fact, all Church of the Flame leaders are professional artists of some kind. As a result, the most fearsome city in the Kingdom is also the most thriving artistic community. The head of the church's pantheon is Nirani, god of fire and passion, and creator of the 18 great spirits of passion who give drive and inspiration to all of us. Church meetings are modeled after his famous court, but discussion of the past is not common. This church is not interested in what was, but what is.
"""

church_of_sky = """High up in the mountains in the city of Lansaria, there exists a peculiar faith. The Church of the Sky is unlike almost any other because it doesn't exist. Or should we say that no churches dedicated to it exist. It exists only as an idea, spread by word of mouth, with no written texts, official organization, or ceremony. The faith worships Illenstar, the half tiger, half eagle God of the Sky, and it teaches freedom, community, and simplicity above all else. Worship is done through action, not through words; helping your neighbor, doing your job well, and avoiding extravagence are noble and religious acts. Illenstar is said to be always flying above the clouds yet able to see everything on the gound. Being closer to the clouds than most, the people of Lansaria take this more literally than most, and strive to make sure their every action is in line with the church's ideals. 
"""

church_of_light = """In the flatland of the Great Plains Province, people worship what they have in abundance: Light. Here the skys are always blue and the sun is always shining. Farmers by trade, the sun is an important part of their life and their faith reflects this. The head of the Pantheon is Theofen, God of Light, whose concrete sense of morality and goodness inspire the same in his devoted followers. Church meetings usually happen at noon, and traditional church architecture includes stained glass in the roof so the midday sun refracts and fills the room with color. Great Plains communities are small, so religious devotion counts for a lot. Church leaders are often well respected and live for free at the expese of the community.
"""

church_of_battle = """While not a traditional Galenian faith, the Church of Battle is a human variation of the traditional Orc faith. After the Orc Crisis several hundred years ago, many Orcish tribes remained in the Halean Province and set up in small camps away from Galenian Settlements. But the lure of trade with Halea and of demand for Orc mercenaries led to more cultural mixing than was anicipated. The Church of Battle was one of many outcomes of that mixing. Preaching strength, acceptance of who you are, and living for the betterment of your people, the Church's pantheon is headed by Aaramesh, the famous general turned God. His place at the head of the Church provokes fierce discssion about the nature of good, evil, violence, and sacrifice. Do the ends justify the means? Does might make right? By ascending to godhood, Aaramesh gave a voice to his people that were previously viewed as litle better than monsters, unworthy of civilized society. But he had to sacrifice a great number of his people to get there, and the war her waged in the process only intensified anti-orc prejudice. These issues are at the core of the Church of Battle, which says not that battle is great, but asks why it is necessary.
"""

church_of_storm = """The evolution of the traditional Gnomish faith, the Church of the Storm is all about bowing to natures will. While the Church of the Sea emphasizes that nature must destroy in order to create, the Church of the Storm argues that nature's goal is irrelevant. We are a part of nature, therefore we have only to submit to the current that nature dictates. Besides a decided fatalistic streak, the Church stresses the balance of the natural world and the importance of maintaining that ballance. In an ironic twist, while the Church of the Sea believes that people are incapable of affecting the ballance, the Church of the Storm preaches the inherent fragility of the balance. Daltos is the head of the Pantheon and his passivity serves as the example. Allow nature to thrive around you and only act when the balance is threatened.
"""

elven_kingdom = """Above the Kalash Mountains exists a very different kingdom from Galenia. The Kingdom of Lanaria is the great elven empire of our age. In the capital of Windong, King Faiellen is the latest ruler in a dynasty that streches back centuries. His kingdom contains 4 mighty elven cities, the most powerful and respected Mages Guild in Firellia, and over 6 million people. Elves ar neither prodigious breeders or ambitious expansionists, these acomplishments are the result of the longest strech of uninterupted peace in history. While Galenia was fighting Orcs, Necromancers, Dragons, and rival Kingdoms, Lanaria has been at rest. And in that time of rest, they have built, grown, created, and developed. Elven cities are the cleanest, wealthiest, healthiest cities in the world and the people thrive because of it. Not to say that elves don't seek excitement, elven mercernaries are frequent hires by foreign governments and many elves travel abroad for at least a small period of their life. This doesn't change that Lanaria is as perfect a place as will ever be created.
"""
#
#gnomish_society = """
#"""
#
#orc_nomads = """
#"""
#
#galenia = """
#"""
#
#windsong = """
#"""
#
#rialew = """
#"""
#
#ramalara = """
#"""
#
#cult_of_john = """
#"""
#
#yolchunara = """
#"""
#
#high_order = """
#"""
#
#keyonins_hand = """
#"""
#
#ghara = """
#"""
#
#unification = """
#"""
#
#orc_crisis = """
#"""
#
#council_of_kings = """
#"""
#
#galen_is_racist = """
#"""
#
#jagard_alive = """
#"""
#
#garrofen_escaped = """
#"""

lore = [provinces_coastal, provinces_plains, provinces_mountains, provinces_gavenhall, provinces_halea,
        provinces_forest, kalahite_dwarves, urumbrakill, istellian, sholan, illenstar, nirani,
        daltos, theofen, aaramesh, bastard, barkskin, ulldar, halenhadra, jagard, egard, istels_ruby,
        swords_of_ithel, church_of_sea, church_of_flame, church_of_light, church_of_sky,
        church_of_battle, church_of_storm, elven_kingdom]

## Currently 21 lore objecs in game
## Currently 30 lore objects written

###############################################################################
## Shrines Flavor #############################################################
###############################################################################
shrine_desc = {'Illenstar': "Your firt impression of this room is that you've gone crazy. Somehow you have left the indoors and are standing on top of a mountain. There are small mountain trees around you, and a light dusting of snow on the ground. You whip around to check for your way back and see the small hole you emerged from in a medium sized boulder. Relieved, but still suspicious, you take a closer look at your surroundings. You are standing on a large-enough outcropping from a mountain with no path up or down - there is no safe way out except for back through the hole. In the center of everything, shaded by three medium sized crooked trees is a small wood box on top of a wooden table. Next to the box is 3 large white feathers, stained with red. It seems to be some sort of shrine.",
               'Sholan': "The room is dark and damp, and you vaguely think you can hear water sloshing and waves crashing in the distance. The walls are all stone, smooth and worn down. The only source of light in the room comes from it's center, where a pool of water glows red. Looking closer, you see a stone statue of a woman sunk in the water. It is cracked and broken in places, but she is still quite beautiful. Around her neck is the source of the light, a lage red jewel glowing like a fire. Looking around the room, there is nothing else, this must be some kind of shrine.",
               'Theofen': "The room is large and grand, marble floors and large columns in each corner. Except that the columns have nothing to support, there is no roof. In its place is a thick layer of cloud, giving off a muted midday light. All four walls are marked by an enourmous, round, stained glass window. The light entering these windows throws colored spots on the floors - mysteriously, it appears as though the light comes equally through all of them, though that can't be possible. At the center of the room is block of marble, upon which is a candle and a bronze elephant. This must be some kind of shrine.",
               'Aaramesh': "The room is small, with low ceilings and wooden construction. There are 4 wooden posts holding up a thatched roof, they have torches attached to them to give light to the room. On the edge of the room are two lions, pacing in opposite directions. They see you and snarl but make no move to break from their patterns, they continue to loop arond the room, eyes fixed on you. In the center of the room is an enormous bloody sword, stabbed into the earth. The blood is still dripping, forming a small puddle in the dirt. This is the strangest shrine you've ever seen.",
               'Nirani': "You emerge onto a rocky platfrom in a very hot area. You look around and ... yeah, you're in a volcano. There's lava on three sides of you and a steep wall behind you that leads to the rim. The whole place smells terrible and the sound of the bubling lava is far from comforting. But the more look, the more amazing it becomes. Carved into the cliffside, high above you, are 18 statues of different humanoid being. Some of them have wings, other masks, but all look dignified, almost holy. On the platform with you is a statue carved from wood, depicting a 6 armed man in a mask, wearing a half-robe and a sword. Hs arms are held up around him as though he wants to show them off to impress you. This is obviously a shrine to him",
               'Daltos': "You emerge in a thicket of branches and leaves. After a minute of struggling to get past them, you emerge in a small clearing, surrounded by even denser brush. Above you the midnight sky is clear and the full moon shines down on you. In the center of the clearing is a large moss-covered boulder. You are tansfixed by how silent it is, as though nature itself is asleep so as to create the most perfetly peaceful moment in history. This is some kind of simple shrine, and a beautiful one at that."}

shrine_prayer = {'Illenstar': """You hear a roar like a tiger and then a voice echo throughout the mountains. \n\n"MORTAL! YOU HAVE COME TO A MOST SACRED PLACE. I KNOW NOT YOUR INTENTIONS BUT I CANNOT DOUBT YOUR BRAVERY. FOR THIS I MAKE YOU AN OFFER: SHOW ME PROOF OF YOUR HUMILITY AND I WILL HELP YOU." The voice fades away, it's source never revealing itself.""",
                 'Sholan': """The roar of the waves gets louder, and you start to hear a bell toll in the distance. You start to feel a little on edge, then a cold voice pierces the moment. \n\n"Mooortaaaaal. You have come to the bottom of the sea to see me? I think not. Methinks you know not where you are, nor with whom you are speaking. No matter, you are insignificant compared to me ... Oh, you doubt me? Allow me to show you how little you actually control. Make me a scarifice, and I will show you true power..." """,
                 'Theofen': """You hear nothing but as you kneel, the light begins to change. The scattered, difracted rays from the stained glass begin moving around the room until they come to rest in a large open spot in the floor. Together, they make the image of a patchwork, multicolored elephant. More shocking is when it begins to speak... \n\n"Hmmm you're new. I admit, it has been a while since I was visited. Maybe a familiar face was a bit too much to hope for. But you'll do. You seem a righteous person. Hmmm, yes. I like you. In fact, I'll help you. Give me a sacrifice so that I can give you my aid. I've missed people." """,
                 'Aaramesh': """The lions stop snarling as a voice, deep and rough, reverberates through the room. \n\n"YOU. YOU HAVE COME TO THE RIGHT PLACE. YOU ARE A KILLER. I, TOO, AM A KILLER. IT IS WHAT MOST REFUSE TO SEE, DEATH IS NECESSARY. THEY LIVE IN WORLDS OF IDEALS WHILE WE MAKE THOSE WORLDS POSSIBLE. YES, YOU HAVE KILLED MANY. AND YOU WILL KILL MORE. AND I WILL HELP YOU. FOR GODS, OUR MAGIC RUNS ON BLOOD. GOLD WILL DO, BLOOD IS BETTER. FOR ALL GODS, EVEN THOSE WHO PRETEND NOT TO NOTICE." """,
                 'Nirani': """The lava starts bubbling faster and the smell gets worse. You hear a voice, coming from nowhere, but clear as day. They could be standing right next to you. \n\n"Curious. I have not had a visitor here in some time. You look like a fighter. Fighters are a curious group; They are assumed to be uncreative and are required to possess a certain amount of stoicism, and yet they must always be passionate. Passion drives men to die for a cause, or to kill for one. It is the same thing that drives men to create life and to create art. Amazing, isn't it? Passion is our greatest power. I see passion in you. I like that. Let me help you. Make me a tribute, show me your passion, and I will show you mine" """,
                 'Daltos': """The wind starts blowing and the trees start shaking and the very earth seems to speak to you. \n\n"MmmmmmmmmMortal... You have enterrrrred a holy place. I wake forrrrrr few. I know what you wish frrrrrom me. My aid. My Powerrrr. I must dissapoint. I am no killerrrrrr. But I willllll give you one blessing. Pay me trrrrribute so that I can return to my rest" """}

###############################################################################\
## The Altar ##################################################################|>
###############################################################################/
altar_desc = """There are two doors on either side of the room, one door is {}, the other is {}. Your altar is in the center of a room, elevated above the floor by a series of stone steps. On the wall behind you is {}. The wall in front you contains {}. You can see some vials set up at your feet, filled with strange things, possibly whoever took you here was preparing some kind of ritual before having to leave. {}
"""

altar_weapon = """At your feet there is a {} that you should probably pick up.
"""

altar_altar = """The altar is cut from stone and about 3 feet high. Its a simple stone with a flat surface, it looks out of place in the finely crafted chamber, as though a stone from the forest was placed here by a giant.
"""

altar_roof = """The roof has a big hole cut into it, so that natural light shines through. It is too high up for you to get up to, but you can see the clouds floating through the sky and birds fly in and out of the chamber. On a ledge near the top, you can see the silver glinting of a key...
"""

altar_vials = """You count 3 small vials, each contains {}. There are two medium sized dishes, one holding {} and the other having {}. It very perplexing, you can't seem to understand what its all for
"""

altar_stupid = """You don't really understand what you're looking at, just looks like a bunch of random junk.
"""

altar_ritual = """The Altar Room looks the same as before, with its high valutled ceiling and elegant stone columns, except now, lying on the altar is the body of {}, {}...
"""

altar_evil = {'John': "The room grows dark and in the domes skylight, you can see a crackling purple electricity start to appear. It grows louder and stronger before a hole in the very fabric of the universe rips open! Darkness stares back at you... except the darkness has eyes... it can see you. There's something there but you can't really make it out, a great lumbering thing whose presence is heavier than all the stones in the earth. Eyes begin to open up in the void, not ust here but all around you. Great, yellow, peircing eyes who stare directly through you. They see you mind, your soul, your body, and every atom of your existence... The great truth is finally revealed.",
              'Jaggard': "",
              'Lyestra': "",
              'Halenhadra': "",
              'Urumbrior': "",
              'Ulldar': ""}

###############################################################################
## The Temple #################################################################
###############################################################################
temple_desc = """This room is a grand temple full of columns and statues. One the wall behind you are 3 doors, including the one you just came from. One door is {}. Another is {}. The third and last is {}. The wall above the doors behind you you is {} but the wall across from you is a grand mosaic depicting an old man standing between bit gnarled trees. The sun is rising behind him and there are animals in the background looking at him with...respect? On either side of the room are statues depicting different figures. Two of them really stand out to you, for whatever reason. The floor and columns are covered in writing, some of which is so old it's barely legible. But what stands out to you most, what makes you most uncomfortable, is that is a slight murmur in the air. A muffled shispering that you can barely make out.
"""

temple_challenge = """You notice grooves in the floor and think you can push this statue aside
"""

temple_fresco = ["You approach the mosaic to investigate it closer.", "As you get nearer, the murmur in the room grows louder, though any precise words or sounds are indistingishable from the noise.",  "You make it up to the wall and the whispers sound like steam venting from a boiler, they are so noisy you can barely focus", "You reach out to touch the mosaic", "The murmurs stop", "For a moment the room is silent", "Then in your ear, a whisper", '"the password"'
                 ]

temple_accept = """The old man in the mosaic suddenly comes alive. He looks down at you and smiles before tapping a particularly large knot on the tree nearest to him. He resumes his self-assured pose as a small hole opens in the wall, at the base of the tree.
"""

temple_fail = """The word "WRONG" bellows through the room and the whispers resume...
"""

temple_hatch = """You push the statue aside and reveal a small hatch in the floor
"""

temple_columns = """HAIL TO THE HEROS OF OUR AGE. HAIL TO THE SACRIFICES THAT MAKE THEM KINGS AMONG MEN. FOR BEHOLD THE WORD IS {} AND THAT WORD SHALL BE THE SHIBOLETH OF OUR AGE. GODS HAVE COME AND GONE, BUT MEN REMAIN. HEROS REMAIN. LIFE REMAINS. LET THE GODS RECIEVE THEIR DUES BUT FORGET NOT THAT WE EXIST OF OR OWN ACCORD, OF OUR OWN VOLITION, OF OUR OWN DESIGNS. WE DESIGN OUR OWN DESTINY! WE LOOK INTO THE ABYSS OF THE WORLD AND CARVE OUT OUR PLACE IN IT. WE SURVIVE, WE THRIVE, WE EXPAND AND DEVELOPE AND CREATE DUE ONLY TO OUR OWN WILLPOWER! GODS NO LONGER CREATE MEN, MEN CREATE MEN. AND THUS MAN IS UNDENIABLY SUPPERIOR.
"""

temple_floor = """BEHOLD THE GRANDEUR OF THE WORLD! ALL THINGS ARE BEAUTIFUL AND ALL THINGS ARE WORTHY OF LOVE. THE MOST NOBLE PURSUIT IN THIS WORLD TO LEARN AND TO LOVE EVERYTHING. IT IS THE DESTINY OF MAN TO UNCOVER ALL THE SECRETS OF THE UNIVERSE AND THOUGH THIS REQUIRED GREAT SACRIFICE THIS IS HOW WE WILL REMAIN. THE WORLD CHANGES AROUND US AND YET WE REMAIN BECAUSE WE STAY AHEAD, BECAUSE WE DON'T ALLOW THE ABYSS TO SWALLOW US UP. WE THRIVE BECAUSE WE HAVE THE WILLPOWER TO THRIVE, NOT BECAUSE WE ARE NATURALLY GIFTED. WE ARE SUPERIOR BECAUSE WE HAVE THE WILLPOWER TO BE SUPERIOR, NOT BECAUSE NATURE MAKES IT SO. NO MATTER WHAT HAPPENS, WE REMAIN.
"""

temple_passphrases = ["DESTINY", "SACRIFICE", "REMAIN", "SUPERIOR", "THRIVE", "ABYSS", "WILLPOWER"]

###############################################################################
## The Fountain ###############################################################
###############################################################################
fountain_desc = """This room is dominated by a grand fountain. One wall is taken up entirely by water spouts that spit water into a pool on the floor. The spouts are shaped like various faces, some raining water from their eyes, others from the mouth, still others by the nose or ears. The pool extends into the center of the room where a magnificent silver fountain spits water in 360 degrees. The fountain is entrancing, almost hypnotic. You find that the longer you stare at it, the harder it is to look away. There are also 3 doors in the room, one on each non-fountain wall. The first is {}. The next one is {}. Finally, there is {}.
"""

fountain_inv = """You step forward to observe the fountain and feel youself getting sucked in. You stare and can't look away. You find yourself approaching the fountain, stepping forward and forward and closer and closer without any willpower with which to stop yourself. You feel your boots getting wet and hear the sloshing of the water as you wade deeper. Water starts dripping down your face and trickling down your back. You feel it getting deeper...no that's impossible, it's a small fountain in a medium sized room...but there's water up to your waist. You're still walking and now water is up to your neck. Is that a tunnel under the water? Suddenly you feel something grasp your neck and lift you out of the water. You hit the floor, wet, dazed, and confused. When you regain your senses, you are alone with no sign of your savior...
"""

fountain_faces_inv = """You step forward to observe the faces on the wall. There are too many to note but you can see {} and {}. There is also one that {}. Some of them seem to be speaking. They aren't moving but you can hear them all the same. 
"""

fountain_infernal = """Kay'leth sees another one, yes she does. Maybe it will last longer than the last. She always likes to drown them slowly, she likes to watch them struggle, she likes to pull them under herself and watch the bubbles stop. She hates that she must save them but the mean mages told her she must. She will have fun with this one I think.... Yesss... she will...
"""

fountain_murmur = """the monsters are here the people are gone the monsters are here the people are gone the monsters are here the people are gone the monsters are here the people are gone the monsters are here the people are gone the monsters are here the people are gone the monsters are here the people are gone the monsters are here the people are gone 
"""

fountain_glowing = """You approach the glowing face and feel an inexplicable surge of knowlege
"""

fountain_whisper = """You walk in the direction of the whispers, trying to locate the source. You can hear them getting louder, clearer, until you hear clearly in your head...          \n\n"who are you"
"""

fountain_base = {"Who are you?": 2,
                 "None of your business": 3,
                 "This can't be real": 4}

fountain_qs = {"What is this place?": 23,
               "How do I leave?": 24,
               "I still want to know what you are": 25,
               "Whats with the fountain?": 26}

fountain_convo_you = {1: fountain_base,
                      2: {"What do you mean, you don't remmber?": 5,
                          "We?": 6,
                          "Why do you wanna know so bad?": 7},
                      3: {"That's awfully arrogant of you": 8,
                          "I'm trying to escape": 9,
                          "\"Our\" Business?": 6},
                      4: fountain_base,
                      5: {"How long?": 10,
                          "Why are you here?": 11},
                      6: {"How many?": 12,
                          "No I don't see...": 13},
                      7: {"I don't know if I can trust you": 14,
                          "Because I don't like you": 15,
                          "Because I can barely remember myself...": 16},
                      8: fountain_base, 
                      9: {"Because I was kidnapped!": 17,
                          "Because I want to go home!": 17,
                          "Because this place is full of things trying to kill me!": 17},
                      10: {"You must know a lot about this place then": 18,
                           "Your memory seems to be shit": 18,
                           "What can you remember?": 18},
                      11: {"I give up": 15},
                      12: {"You mean to say that all these faces are you?": 19,
                           "Everywhere...in this room? Or...?": 20},
                      13: {"You mean to say that all these faces are you?": 19},
                      14: fountain_base,
                      15: fountain_base,
                      16: {"Many?": 21,
                           "Fuck, you're vague": 15,
                           "Where would I lose myself?": 22},
                      17: {"Well at least out there I could see the sky": 15},
                      18: fountain_qs,
                      19: {"Doomed to lose it?": 25},
                      20: {"The Unity?": 25},
                      21: fountain_base,
                      22: {"Like what?": 27},
                      23: fountain_qs,
                      24: fountain_qs,
                      25: fountain_qs,
                      26: fountain_qs,
                      27: {"Nearby?! Where?": 28,
                           "That's batshit": 15},
                      28: {"Thanks!": 15},
                      'denial': fountain_base}

fountain_convo_face = {1: "who are you",
                       2: "we don't remember. who are you?",
                       3: "all things are our business",
                       4: "it is",
                       5: "we haves been here a very long time",
                       6: "there are many of us, you see",
                       7: "why do you want to hide it so bad?",
                       8: "but it is without question",
                       9: "why escape?",
                       10: "longer than we can remember",
                       11: "we don't remember. why are you?",
                       12: "we are EVERYWHERE",
                       13: "look around you. the room is full of us",
                       14: "trust is the luxury of fools",
                       15: "...",
                       16: "yes, it can be easy to lose oneself here... many have done it before you",
                       17: "you may find that out there is no different",
                       18: "we know some things, other things have been forgotten. what do you need to know?",
                       19: "yes. we are spirits passed, trapped for our knowledge, yet doomed to lose it",
                       20: "trapped here we are, imprisoned in stone for eternity and losing our selves for the unity",
                       21: "you are not the first to wander these halls without directon",
                       22: "there are many things here that could steal you away from yourself",
                       23: "a place of learning, a place of trial, a place of error...",
                       24: "one of these doors leads to the anterchamber, from there you can leave",
                       25: "we are collected spirits brought here and preserved so that our knowlege will last for eons. but by preserving us in this way, our identities are converging into a unified soul and our individual memories are dissapearing",
                       26: "that is kay'leth. a demon princess with a fondness for water, trapped inadvertently in a fountain. ignore her if you can",
                       27: "there are many sacred places here. small domains of beings above us all. one is even nearby",
                       28: "we can't tell you. but we will speak to kay'leth. she will lower the water to help you pass",
                       'denial': '...'}

###############################################################################
## Underwater #################################################################
###############################################################################
underwater_desc = """You emerge from the tunnel in a small cavern. There is a table with some food and mysterious liquids on it, along with some playing cards and a small pile of gold coins. There is a small mace leaning on a leg of the table. In the corner is a glinting obect, a twinkle in the darkness. The cave itself is cold and damp, lit only by a jar of magical fire placed out of reach on a rocky outcroping. You can see a small, ornately carved hole in the wall to your left. Its just big enough to crawl through.
"""

underwater_ring = """You kneel down to get a closer look and find a gold rind lying on the ground. It seems a little cliche but you don't want to question free loot.
"""

###############################################################################
## The Tower >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   CONTAINS PLOT   ##
###############################################################################
tower_entry = """You pass through the {} and into a tall winding staircase, it seems to go on forver. You climb and climb and climb and emerge in a room at the top of a tower.
"""

tower_desc_base = """The tower room contains a large window with a telescope sticking out of it. There is a desk underneath of it covered in parchment and quills, what looks like furrious note-taking. Hanging from the roof is the skeleton of an enormous snake and in the corner is an {}. There is a couch and a coffee table on the far wall, on the coffee table is a vile of some liquid, a silver key, and, mercifully, some food.
"""

tower_desc_bird = """The tower room contains an enormous birdcage, inside which is the largest bird you've ever seen. There is a desk next to it covered in parchment and quills, what looks like furrious note-taking. Hanging from the roof is a model of you assume is the solar system but you don't recognize the planets. In the corner is a {}. There is a couch and a coffee table on the far wall, on the coffee table is a vile of some liquid, a silver key, and, mercifully, some food.
"""

tower_desc_machine = """The tower room contains a huge machine with lots of gears and levers. There is a desk next of it covered in parchment and quills, what looks like furrious note-taking. The entire roof is gone and from the looks of it, it was removed haphazardly. In the corner is a {}. There is a couch and a coffee table on the far wall, on the coffee table is a vile of some liquid, a silver key, and, mercifully, some food..
"""

tower_telescope = """You approach the telescope and appeciate, more than anything, it's size. It's easily 3 times as large as you and must be very heavy because it is supported by a stand and a series of cables. It's daylight, so looking through it seems pointless but you do it anyways. You put your eye up to the eyepeice and it is as though all the light on the planet disapears. You can see stars, galaxies, nebulae, and everything. Most significantly, you see a series of planets that are almost in a straight line. As you stare into a space one star become especially clear. Very clear... almost as though it is right in front of you. And with a 'clink' it falls to the ground at your feet, a small glowing rock.
"""

tower_bird = """You apprach the bird with caution, it looks at you with interest but when you get too close, it shrieks and starts flapping it's wings at you. But the adventuring spirit runs deep in you, so you approach it closer, hand extended to show your peaceful intentions. It stops its squawking and resumes looking at you with intense curiosity. You reach for the door, but there is none, how is that possible? But the bird noticed, and seems to trust you. One feather drops from it's wing and it looks at you appreciatively.
"""

tower_machine = """You apprach the machine and curiosity strikes you, so you begin to pull levers. As soon as you pull the first one, the machine whirs to life and smoke starts pouring out of it smoke stacks. Suddenly the weather starts changing. Clouds get darker and being to gather, thunder sounds in the distance. Rain begins to fall and you begin to regret ever pulling the lever. The wind is cold and howling when the lightning first strikes. Off in the distance, though you can see the flash and the arcing plasma. The next time is much closer. Finally, after a minute or two, lightning strikes an extended rod coming off the machine. The gears start working faster, but smoke stops coming off the stacks. The weather changes again, reverting to normal. The machine works harder and you realize you're already dry. Suddenly, a glass sphere rolls out of the machine. Looking at it, it seems to have lightning at its core...
"""

tower_scroll_notes_telescope = """This is it! The planets are in alignment. I need to perform the ritual today! I can't wait another 600 years. Too many lost friends, too many sacrfices. Besides, who's to say I'll live another 600 years? The priests promised me eternal youth but they're clueless. I could die tomorrow for all they know. The ritual. As soon as possible. It must be done. Now I only need to find a sacrifice... 
"""

tower_scroll_notes_bird = """Legend says that the Jupiter Eagle flys throughout the multiverse, opening gates with a flap of its wings. It's doubtfull that it's been where we want to go, almost nothing has been where we want to go, but any kind of portal magic is worth investigating... About the Jupiter Eagle, let me describe him. Wingspan: 24 meters, talons: .5 meter, jaw strength: enough to crush my steel chest in one go. I had to rig a magical cage for it, he's a dangerous animal.
"""

tower_scroll_notes_machine = """IT'S WORKING! Finally, I can produce elemental lightning on demand. After years of trying to time natural storms to harness the power, I can now create it whenever I desire. This is true magic. Now, if I peform the ritual, I will be able to force those people to obey me. I will control the skies and the eath! God it feels good to be king! Or at least it will. Now to find a sacrifice...
"""

tower_builds = {
                'John': [tower_desc_bird, 'large bird', tower_bird, tower_scroll_notes_bird, 'Jupiter Eagle Feather'], 
                'Ulldar': [tower_desc_base, 'telescope', tower_telescope, tower_scroll_notes_telescope, 'Fallen Star'], 
                'Urumbrior': [tower_desc_machine, 'machine', tower_machine, tower_scroll_notes_machine, 'Sphere of lightning'], #Rewrite
                'Lyestra': [tower_desc_base, 'telescope', tower_telescope, tower_scroll_notes_telescope, 'Fallen Star'],
                'Jaggard': [tower_desc_base, 'telescope', tower_telescope, tower_scroll_notes_telescope, 'Fallen Star'],
                'Halenhadra': [tower_desc_base, 'telescope', tower_telescope, tower_scroll_notes_telescope, 'Fallen Star']
                }

tower_table = """The table is covered in notes written in various languages. The ones you can decifer are few in number but great in interest. You see one scroll describing some kind of ritual, another is some sort of diary entry. There are two spell scrolls nearby, a wizard could learn from them.
"""

tower_scroll_ritual = """{}: First, add {} to represent the sacrifices of the gods, then add {} to represent the penetence of the soul, last add {} as a sign of everlasting devotion to the gods.
"""

tower_scroll_diary = """Dear Diary, my new boss is evil. I found out today. His work in this room was evil and my helping him was evil by accessory. Or by proxy. I don't really understand either of those two words. Regardless, his plan is now in motion, we have succeeded here and he is going to perform the ritual tonight. It's too late to stop him, so I'm just gonna let him. Why not? I'm already sorta evil for helping him so I may as well lean into it. Besides he's the best boss I've ever had. He pays overtime and gives 45 minute breaks. What. A. Dude.
"""

###############################################################################
## The Lab ####################################################################
###############################################################################
lab_desc = """This room is some kind of laboratory. There are vials and beakers and tubing spread out on multiple tables, along with notes and various ingredients. You can see 4 finished potions on a table and on the floor under a table is a heavy looking book.
"""

lab_experiment_scroll = """POTION OF IMMACULATE WEALTH: First we need to add {} to show respect for our almighty ancestors. Next we add {} out of admiration for the earth. I learned the hard way to avoid adding {} here because it ruins the whole thing. What we should add is {}. The next ingredient is {} and immediately after we add {}. This produces the ideal effect!"
"""

lab_run_experiment = """You approach the complicated looking apparatus and take note of all the ingredients available. There is an already bubling solution sitting in the base of the contraption. It seems to only need a few more ingredients.
"""

###############################################################################
## The Catacombs ############################################################## 
###############################################################################
catacombs_desc = """This room is some kind of cemetary, full of coffins and dust and cobwebs. The tombs in the walls are denoted by plaques but the coffins on the floor are anonymous and exposed. In the center of the room are 4 ornately carved stone sarcophagi, with a firepit between them. There are 3 doors here, one is {}, another is {}, and the last one is {}.
"""

catacombs_opened = """The lid is already opened. You searched this one already.
"""

catacombs_coffin1 = """You push off the stone lid to reveal a dusty skeleton. Lucky you, he was burried with his coin purse. Seeing as he won't be needing it, you collect 75 gold pieces!
"""

catacombs_coffin2 = """...a skeleton jumps out to attack you!
"""

catacombs_coffin3 = """The stone lid slides off revealing a skeleton entombed in his heavy armor, still holding onto his {}. It looks like it's still useable.
"""

catacombs_coffin4 = """You heave the stone lid off the sarcophogus and a find a skeleton dressed in decaying, yet still obviously elegant, wizard robes. His staff is decayed beyond all use but there is a spell scroll that a wizard could use.
"""

catacombs_ghoul_encounter = """You hear an eerie cackle permeate the room and suddenly two pale Ghouls materialize before you! You are under attack!
"""

catacombs_ghoul_victory = """The ghouls emit a terrifying death rattle as they fade out of existence forever. As if to signify your victory, the firepit crackles to life. 
"""

catacombs_bonfire = """You apprach the lit bonfire and feel an indescribable sense of warmth throughout your entire body. You know...somehow...that if you throw 100 gold peices into the fire something good will happen...how strange...
"""

###############################################################################
## The Pantry #################################################################
###############################################################################
pantry_desc = """This is a small room full of shelves of food. In one corner are several barrels, full of what is probably ale. Resting on top of a barrel is a {}. There is an interesting looking bracelet on a shelf in the back, among some cheese and grapes. On a shelf near the floor is a moldy old book. The wall.. is strange... you could swear you hear it whispering for just a split second after you walked in. There are two doors here, one is {}, the other {}.
"""

pantry_pass = """The wall opens its mouth real wide to become a small hole, just big enough to crwl throgh.
"""

pantry_wall = """You open your mouth to speak...then stop. You were about to talk to a wall. That's fucking insane.
"""

pantry_wall2 = """You screw up your courage, telling yourself that you're not crazy but you just have to try this, because ... maybe ... whatever! You're gonna do this. You walk up to the wall and before you can say anything a great mouth opens up in the bricks and says to you...                                         \n\n"Oh Great What do you want?" 
"""

pantry_wall_encounter = """I'm gonna come down on you like a brick wall!
"""

pantry_you_base = {"Ehhh, What the hell are you?": 2,
                   "Woah you talk!": 3,
                   "Where am I?": 4}

pantry_you_qs = {"Why are you here, in this room?": 14,
                 "Have you seen anything strange?": 15,
                 "How do I leave this place?": 16}

pantry_convo_you = {1: pantry_you_base,
                    2: {"But, like, you can talk...": 3,
                        "Most walls don't talk to me": 5,
                        "How did you get like this?": 6},
                    3: {"Well, it's just never happened to me before": 7,
                        "Do you have a brain somewhere in there?": 8,
                        "How did you get like this?": 6},
                    4: {"Your view? It's a dark room full of food": 9,
                        "But you don't even have eyes!": 10,
                        "If you help me I'll leave": 11},
                    5: pantry_you_base,
                    6: {"No seriously, how is this possible?": 12,
                        "All right then, keep your secrets": 13},
                    7: pantry_you_base,
                    8: pantry_you_base,
                    9: pantry_you_base,
                    10: pantry_you_base,
                    11: pantry_you_qs,
                    12: pantry_you_base,
                    13: pantry_you_base,
                    14: {"My gods?": 17,
                         "Oh. Can you let me in?": 18,
                         "Seems like a lot of effort to make you just to protect a shrine": 19},
                    15: pantry_you_qs,
                    16: {"Why are you here, in this room?": 14,
                         "Have you seen anything strange?": 15,
                         "How do I leave this place?": 16,
                         "The Fountain of Kay'Leth?": 20},
                    17: pantry_you_qs,
                    18: {"Well, ok, I guess": 21,
                         "What if i just smash you and go in anyways?": 22,
                         "CMON! Help me. Please?": 23},
                    19: pantry_you_qs,
                    20: pantry_you_qs,
                    21: pantry_you_qs,
                    22: {"Why are you here, in this room?": 14,
                         "Have you seen anything strange?": 15,
                         "How do I leave this place?": 16,
                         "Yeah I think I can...": 24},
                    23: {"Pleeeeeaaaasseee": 25},
              'denial': pantry_you_base}

pantry_convo_wall = {1: "Oh great, what do you want?",
                     2: """I'm a wall genius, what do I look like, a window?""",
                     3: """Yeah so do you, what of it?""",
                     4: """Blocking my view, that's where you are""",
                     5: """Well most walls are smarter than I am, then""",
                     6: """I dunno, how did you get so ugly?""",
                     7: """Oh I get to be your first, how wonderful. If I had eyes I'd roll them.""",
                     8: """I try to avoid asking existential questions""",
                     9: """Which you're ruining, so bye""",
                     10: """Hey! I don't come to your room and start insulting you!""",
                     11: """Deal, whaddaya want?""",
                     12: """My father was an I-beam and my mother was a roof, they're very proud""",
                     13: """Yeah, I was going to anyways, thanks""",
                     14: """I protect a shrine to one of your gods""",
                     15: """Well, I don't technically "see" anything, but a couple nights ago, there was a lot of foot traffic through here. I think they were preparing for a feast. It was annoying.""",
                     16: """There's a couple ways out but they all lead through the antechamber. It's next to the Fountain of Kay'leth""",
                     17: """Well, somebody's gods""",
                     18: """That would make me a pretty sorry excuse for a wall, wouldn't it?""",
                     19: """Trust me, asshole, I'm worth it.""",
                     20: """Yeah, some demon that they accidentally turned into a fountain. Pretty sure they were trying to turn her into a teapot but they fucked up and ran with it. Yeah, she like to enchant people and drown them in the water, but they told her that if she kpet doing that, they'd finish what they started. So now she just mostly drowns people, then saves them for kicks. Nice girl, we talk sometimes.""",
                     21: """Yeah, that's right. You done yet?""",
                     22: """You really think you can take me?""",
                     23: """Hmmmmmmm... No.""",
                     24: pantry_wall_encounter,
                     25: """FINE! WHATEVER! JUST LEAVE ME ALONE!""",
                     'denial': "Gods I hate you, please leave"}

###############################################################################
## The Kennel  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   CONTAINS PLOT   ##
###############################################################################
kennel_desc = """This room is notable for the 2 large cages the take up most of the floor. Both are empty except for bones and scraps of paper, though some scraps do have legible writing on them. One has a small hole in the side of it, just big enough for a Gnome to crawl through. There are barred gates in the walls, cages that you can't see into, though they seem to be in use. There is straw on the ground, covering dirt floors or maybe covering stone floors that are covered by dirt. Either way there's a lot of dirt. There are 3 levers on the far wall, they are unlabled and could do anything. Hung from the ceiling far above you is a simple iron-wrought chandelier that provides warm light to the room and has a slight twinkle in its center. The room has 3 doors. One is {}, another is {}, and the last one is {}.
"""

kennel_pulled = """You already pulled this lever, pulling it again does nothing.
"""

kennel_lever1 = """You pull the lever and nothing happens. After a few seconds you hear gears start turning in the walls. Loud clicking and clacking and clanging fills the room and the gate to one of the cages lifts open. You stare at the now-open gate with apprehension as you hear growling come from the dark. 
"""

kennel_wolves = """Slowly, 4 wolves emerge from the cage, teeth bared, yellow eyes fixed on you...
"""

kennel_wolf_victory = """You kill the last wolf and take a deep breath of relief.
"""

kennel_lever2 = """You pull the lever and nothing happens. After a few seconds you hear gears start turning in the walls. Loud clicking and clacking and clanging fills the room and the gate to one of the cages lifts open. You stare at the now-open gate with mild terror as you hear a roar echo from the dark. 
"""

kennel_drake = """Slowly, a Drake, 8 feet long with teeth like razors and scales like iron, emerges from the cage. He snorts a plume of fire and fixes his gaze on you. Brace for attack!
"""

kennel_drake_victory = """You stand over the slain drake, the smoldering hay crackles in the background. 
"""

kennel_lever3 = """You pull the lever and hear a high pitched whirring come from the wall. You hear a rumbling sound and part of the wall to your left slides away revealing 3 vials.
"""

kennel_lever4 = """You pull the lever and hear the rumbling of moving pistons and stones. Behind you, a part of the wall rolls away revealing a small pile of gold.
"""

kennel_lever5 = """You pull the lever and hear the sound of turning gears and machinery. A deafening 'CLICK' echoes from the door to your left.
"""

kennel_lever6 = """You pull the lever and hear the sound of gears turning and stones moving.
"""

kennel_dex_dodge = """You hear a 'THWIP' and arrows come shooting out of the walls! Luckily you manage to dodge out of the way just in time. Those looked painful.
"""

kennel_dex_fail = """You hear a 'THWIP' and arrows come shooting out of the walls! You try to dodge but you're just not fast enough. One sticks in your leg, and it really hurts.
"""

kennel_lever7 = """You pull the lever and hear the sounds of heavy gears and machinery moving. The cage to your right suddenly opens. You look at the open gate for a moment but can't hear anything, and nothing seems to be coming out, so you move closer to investigate. Inside you see a massive skeleton sprawled out on the ground. Upon closer inspection you see that it's actually two skeletons, one still large drake skeleton and one that you assume must've been a wizard - his broken staff and singed robes are now obvious. In the wizards boney hand is a spell scroll that a wizard could learn from.
"""

kennel_plot_scroll = {'John': """THE PARABLE OF THE HORSE - "3 sheep, 2 dogs, and a cat go for a walk. After 1 mile, they meet {} sparrow{}, who show{} them the best trees to sleep under. They resume walking, they make it 3 miles when they meet {} rabbit{} who show{} them the best fields to run through. They, again, resume walking. They walk 2 more miles before they meet {} otter{} who show{} them the best rivers to swim in. The sun begins to set and the animals return home. Their friend, the horse, says to them 'You did not travel far, my friends, how sad for the world is full of wonders'. To which one of the dogs replies, 'But my friend, it is not the distance that matters, but the friendships made along the way'"  - By John of Ardshiama""",
                      'Jaggard': """THE PARABLE OF THE HORSE - "3 sheep, 2 dogs, and a cat go for a walk. After 1 mile, they meet {} sparrow{}, who show{} them the best trees to sleep under. They resume walking, they make it 3 miles when they meet {} rabbit{} who show{} them the best fields to run through. They, again, resume walking. They walk 2 more miles before they meet {} otter{} who show{} them the best rivers to swim in. The sun begins to set and the animals return home. Their friend, the horse, says to them 'You did not travel far, my friends, how sad for the world is full of wonders'. To which one of the dogs replies, 'But my friend, it is not the distance that matters, but the friendships made along the way'"  - By """,
                      'Halenhadra': """THE PARABLE OF THE HORSE - "3 sheep, 2 dogs, and a cat go for a walk. After 1 mile, they meet {} sparrow{}, who show{} them the best trees to sleep under. They resume walking, they make it 3 miles when they meet {} rabbit{} who show{} them the best fields to run through. They, again, resume walking. They walk 2 more miles before they meet {} otter{} who show{} them the best rivers to swim in. The sun begins to set and the animals return home. Their friend, the horse, says to them 'You did not travel far, my friends, how sad for the world is full of wonders'. To which one of the dogs replies, 'But my friend, it is not the distance that matters, but the friendships made along the way'"  - By""",
                      'Ulldar': """THE PARABLE OF THE HORSE - "3 sheep, 2 dogs, and a cat go for a walk. After 1 mile, they meet {} sparrow{}, who show{} them the best trees to sleep under. They resume walking, they make it 3 miles when they meet {} rabbit{} who show{} them the best fields to run through. They, again, resume walking. They walk 2 more miles before they meet {} otter{} who show{} them the best rivers to swim in. The sun begins to set and the animals return home. Their friend, the horse, says to them 'You did not travel far, my friends, how sad for the world is full of wonders'. To which one of the dogs replies, 'But my friend, it is not the distance that matters, but the friendships made along the way'"  - By""",
                      'Lyestra': """THE PARABLE OF THE HORSE - "3 sheep, 2 dogs, and a cat go for a walk. After 1 mile, they meet {} sparrow{}, who show{} them the best trees to sleep under. They resume walking, they make it 3 miles when they meet {} rabbit{} who show{} them the best fields to run through. They, again, resume walking. They walk 2 more miles before they meet {} otter{} who show{} them the best rivers to swim in. The sun begins to set and the animals return home. Their friend, the horse, says to them 'You did not travel far, my friends, how sad for the world is full of wonders'. To which one of the dogs replies, 'But my friend, it is not the distance that matters, but the friendships made along the way'"  - By""",
                      'Urumbrior': """THE PARABLE OF THE HORSE - "3 sheep, 2 dogs, and a cat go for a walk. After 1 mile, they meet {} sparrow{}, who show{} them the best trees to sleep under. They resume walking, they make it 3 miles when they meet {} rabbit{} who show{} them the best fields to run through. They, again, resume walking. They walk 2 more miles before they meet {} otter{} who show{} them the best rivers to swim in. The sun begins to set and the animals return home. Their friend, the horse, says to them 'You did not travel far, my friends, how sad for the world is full of wonders'. To which one of the dogs replies, 'But my friend, it is not the distance that matters, but the friendships made along the way'"  - By"""
                      }

kennel_cage_challenge = """You approach the cage and see a small hole in the side of it. It looks as though something broke it's way out. You might be able to fit through there...
"""

kennel_size_win = """You manage to squeez through and you find a modest pile of gold. What an odd place to keep it, but oh well, it's yours now.
"""

kennel_size_lose = """Nope. You don't fit. Oh well
"""

kennel_chandelier = """After you pull the lever you hear a deep thud and the sound of moving chains coming from above you. You look up and see the chandelier descending from the roof. It stops (a loud CLUNK comes from the wall) about a foot off the ground and you can see a vial at the center.
"""

###############################################################################
## The Barracks  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   CONTAINS PLOT   ##
###############################################################################
barracks_desc = """This room is full of beds and with one small table in the center. On the table is a candle, burned down to the wick, two small vials, and a note. The beds are all bunks and immaculately made, two of the beds have books tucked under the pillows, looks like people were reading in bed. There is a nice looking belt strewn on the floor, some people are just messy. There are two doors in the room, one is {} and the other one is {}. In one corner is a small table set up with a board game. The rooms feels simultaneously comfortable and discomforting; you both want to stay for a while and leave as soon as possible.  
"""

barracks_plot_note = {'John': """Ser John came through this morning and roused the alarm. Apparently some of the high priests fucked up and a bunch of goddamn monsters got into the compound. We took care of it but still, it feels like a close call. I can't shake the feeling that this could have been worse. We didn't lose anyone, but Patrick got pretty beat up by a Skeleton. Damn thing didn't even have a weapon, he just used one of his arms as a club. Real fucked up shit.""",
                      'Jaggard':  """Ser John came through this morning and roused the alarm. Apparently some of the high priests fucked up and a bunch of goddamn monsters got into the compound. We took care of it but still, it feels like a close call. I can't shake the feeling that this could have been worse. We didn't lose anyone, but Patrick got pretty beat up by a Skeleton. Damn thing didn't even have a weapon, he just used one of his arms as a club. Real fucked up shit.""",
                      'Halenhadra':  """Ser John came through this morning and roused the alarm. Apparently some of the high priests fucked up and a bunch of goddamn monsters got into the compound. We took care of it but still, it feels like a close call. I can't shake the feeling that this could have been worse. We didn't lose anyone, but Patrick got pretty beat up by a Skeleton. Damn thing didn't even have a weapon, he just used one of his arms as a club. Real fucked up shit.""",
                      'Ulldar': """Ser John came through this morning and roused the alarm. Apparently some of the high priests fucked up and a bunch of goddamn monsters got into the compound. We took care of it but still, it feels like a close call. I can't shake the feeling that this could have been worse. We didn't lose anyone, but Patrick got pretty beat up by a Skeleton. Damn thing didn't even have a weapon, he just used one of his arms as a club. Real fucked up shit.""",
                      'Lyestra':  """Ser John came through this morning and roused the alarm. Apparently some of the high priests fucked up and a bunch of goddamn monsters got into the compound. We took care of it but still, it feels like a close call. I can't shake the feeling that this could have been worse. We didn't lose anyone, but Patrick got pretty beat up by a Skeleton. Damn thing didn't even have a weapon, he just used one of his arms as a club. Real fucked up shit.""",
                      'Urumbrior':  """Ser John came through this morning and roused the alarm. Apparently some of the high priests fucked up and a bunch of goddamn monsters got into the compound. We took care of it but still, it feels like a close call. I can't shake the feeling that this could have been worse. We didn't lose anyone, but Patrick got pretty beat up by a Skeleton. Damn thing didn't even have a weapon, he just used one of his arms as a club. Real fucked up shit."""
                      }

barracks_game_approach = """You apprach the small table and immediately recognize a chess board. The game seems to be mostly played out, there are three black pieces and three white pieces on the board. If you stare long enough, you can see the black pieces wobble slightly, as though they want to move but are stuck in place.
"""

barracks_game_lose = """"You were defeated by the worst self-playing chess pieces you've ever seen...wait...something's happening...
"""

barracks_game_timeout = """The game ends with no obvious victor. The game peices start shaking violently...
"""

barracks_lose_encounter = """The black king transforms in front you to become a young vampireling. At first, his expression is smug, but it quickly changes to hunger as the other two black peices become fearsome Snarl Demons. Brace for attack!
"""

barracks_win = """The dusty remains of the vampireling fall to the floor as you collapse into the nearby chair for a well deserved rest. Only for a moment.
"""

baracks_gold = """You pick up the bag and find that it's full of gold!
"""

###############################################################################
## The Mess  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   CONTAINS PLOT   ##
###############################################################################
mess_desc = """This room is some kind of dining hall, based on the long tables full of food. There's definitely a lot of food here. There are 3 tables on the floor and one head table elevated slightly above the others. On these tables you see Turky, Pork, Soup, Crackers, Wine, Cookies, and all sorts of other foods. You can see scrolls of parchment that got lef behind, people must've been reading or working while eating. Two are glittering slighly and are obviously spell scrolls. There is one accessible door in the room, a {}, the wall across from it is burried under a pile of rubble.
"""

mess_rubble_clear = """It takes all your strength but you manage to clear a whole in the rubble large enoough to fit through, it seems to lead to another room.
"""

mess_rubble_fail = """You try as hard as you can but just can't seem to move the rubble. It's too heavy.
"""

mess_plot_scroll = {'John': """Roland, \nI need to talk to you. I've been researching that ritual and I have some questions. It supposedly opens the gates of Apollo, which are an astral network between our universe and some other universe that... well the details are fuzzy. Not really fuzzy, more just confusing. Uninterpretable. The Diary of Ullong the great details his work with the ritual, for the week after he opened the gates, his entries transition from detailed accounts of his work into gibberish and chicken-scratch. The shift is really dramaic. A similar thing happened to Braeka the Vast, except she DIED before going totally mad. Please, let me know what you think.\n   -David """,
                    'Jaggard': """Roland, \nI need to talk to you! I've been doing some reseach into the legends and I think that thing that Ser John killed 200 years ago was a Sunderfoe. If I'm right, then killing it provoked powerful magic that could negatively interract with our enchantments. Think about it, he hasn't been looking so good lately, has he? The 400th aniversary of the liberation is coming up and that corresponds almost exactly with the alignment of Andomeda. Between the astral effects and the Sunderfoe curse, there is a chance he is in very real danger! Please find me soon, ITS URGENT! \n   -David """,
                    'Halenhadra': """Roland, \nI need to talk to you! I've been doing some reseach into the legends and I think that thing that Ser John killed 200 years ago was a Sunderfoe. If I'm right, then killing it provoked powerful magic that could negatively interract with our enchantments. Think about it, he hasn't been looking so good lately, has he? The 400th aniversary of the liberation is coming up and that corresponds almost exactly with the alignment of Andomeda. Between the astral effects and the Sunderfoe curse, there is a chance he is in very real danger! Please find me soon, ITS URGENT! \n   -David """,
                    'Ulldar': """Roland, \nI need to talk to you! I've been doing some reseach into the legends and I think that thing that Ser John killed 200 years ago was a Sunderfoe. If I'm right, then killing it provoked powerful magic that could negatively interract with our enchantments. Think about it, he hasn't been looking so good lately, has he? The 400th aniversary of the liberation is coming up and that corresponds almost exactly with the alignment of Andomeda. Between the astral effects and the Sunderfoe curse, there is a chance he is in very real danger! Please find me soon, ITS URGENT! \n   -David """,
                    'Lyestra': """Roland, \nI need to talk to you! I've been doing some reseach into the legends and I think that thing that Ser John killed 200 years ago was a Sunderfoe. If I'm right, then killing it provoked powerful magic that could negatively interract with our enchantments. Think about it, he hasn't been looking so good lately, has he? The 400th aniversary of the liberation is coming up and that corresponds almost exactly with the alignment of Andomeda. Between the astral effects and the Sunderfoe curse, there is a chance he is in very real danger! Please find me soon, ITS URGENT! \n   -David """,
                    'Urumbrior': """Roland, \nI need to talk to you! I've been doing some reseach into the legends and I think that thing that Ser John killed 200 years ago was a Sunderfoe. If I'm right, then killing it provoked powerful magic that could negatively interract with our enchantments. Think about it, he hasn't been looking so good lately, has he? The 400th aniversary of the liberation is coming up and that corresponds almost exactly with the alignment of Andomeda. Between the astral effects and the Sunderfoe curse, there is a chance he is in very real danger! Please find me soon, ITS URGENT! \n   -David """
                    }

mess_stained_scroll = """So we had a minor... invasion... the other day and in the chaos, the door to the armory collapsed. I heard something about a dragon, but these losers always exagerate. I was over in the temple, protecting the statue of Ser John. Lame assignment, but better than being in the Dining Hall apparently. I didn't even have to use my weapon. And after seeing what happened to Patrick... I definitely got lucky.
"""

mess_ornate_scroll = """By order of John of Ardshiama, everyone except the ruling council is hereby banned from the gate room. Due to an unfortunate incident, the gate room will remain closed until further notice. We hope this causes no inconvenience but be aware that debate on this issue will not be tolerated. Thank you for your continued cooperation \n    - High Priest Ruling Council
"""

###############################################################################
## The Armory #################################################################
###############################################################################
armory_desc = """This room is some kind of armory but the stock is very low. The torches are all out and there is dirt, dust, and rubble all over the room. On an armor stand in the back is a shield with an intersting crest on it. There are Daggers and Swords and War Hammers all over the room, some scattered on the floor, others still on the racks. On the wall in the back is a silvery key hanging from a nail. You can hear a whimpering coming from under the weapon stands, when you check it out, you a scared little man, hiding from you.
"""

armory_you_base = {"How are you still alive?": 2,
                   "What are you doing here?": 3,
                   "Shit, you look awful...": 4}

armory_qs = {"How long have you been in here?": 5,
             "How did you end up here?": 3,
             "What happened here?": 9,
             "What can you tell me about this place?": 7,
             "Help me or I'll feed you to the monsters": 8}

armory_qs2 = {"Ok, what is this place?": 10,
              "There are some strange rooms here...": 11,
              "How many people lived here?": 12,
              "What did you do here?": 13,
              "How do I get out?": 14}

armory_pass = {"Can you fight?": 15,
               "You got anything to give me?": 16,
               "Tell me your secrets!": 17}

armory_convo_you = {1: armory_you_base,
                    2: armory_qs,
                    3: {"You sure you weren't hiding?": 6,
                        "How long have you been in here?": 5,
                        "How did you end up here?": 3,
                        "What happened here?": 9,
                        "What can you tell me about this place?": 7,
                        "Help me or I'll feed you to the monsters": 8},
                    4: armory_you_base,
                    5: armory_qs,
                    6: armory_qs,
                    7: armory_qs2,
                    8: armory_pass,
                    9: {"Ok, what is this place?": 10,
                        "There are some strange rooms here...": 11,
                        "How many people lived here?": 12,
                        "What did you do here?": 13,
                        "How do I get out?": 14,
                        "Where did it come from?": 18},
                    10: {"What do you mean, you don't know why?": 19,
                         "What did you research?": 13},
                    11: {"Ok, what is this place?": 10,
                        "There are some strange rooms here...": 11,
                        "How many people lived here?": 12,
                        "What did you do here?": 13,
                        "How do I get out?": 14,
                        "Quirks?": 20},
                    12: armory_qs2,
                    13: {"Ok, what is this place?": 10,
                        "There are some strange rooms here...": 11,
                        "How many people lived here?": 12,
                        "What did you do here?": 13,
                        "How do I get out?": 14,
                        "What kind of work did he do?": 21},
                    14: armory_qs2,
                    15: armory_pass, 
                    16: armory_pass,
                    17: {"BETTER SECRETS!": 22},
                    18: armory_qs2,
                    19: armory_qs2,
                    20: {"Lava Lakes?": 23,
                         "Statues?": 23,
                         "Demons?": 23,
                         "Portals?": 23,
                         "Shrines?":23,
                         "Doors?": 23,
                         "Walls?": 23,
                         "Secret Rooms?": 23,
                         "Sandstorms?": 23,
                         "Candyland?": 23},
                    21: armory_qs2,
                    22: {"MORE SECRETS!": 24},
                    23: armory_qs2,
                    24: {"Ok we're good": 25,
                         "Ok, now tell me more about this cousin...": 26},
                    25: armory_you_base,
                    26: armory_you_base,
              'denial': armory_you_base}

armory_convo_him = {1: "ACK!...gods, you scared me...",
                    2: "...well I've been cooking rats...usually cooking rats, sometime I can't spare the fire... and I drink... well I won't tell you that... that's embarassing.",
                    3: "I got stuck here when the monsters attacked. I wasn't hiding, it was just coincidence... I wasn't hiding...",
                    4: "...yeah ...that's normal though",
                    5: "...I dunno. Can't see the sun. Hard to keep track of time. Feels like a while. But.. can't be sure...",
                    6: "I was... getting my sword. Then the roof collapsed.",
                    7: "Everything... maybe. I... lived here.",
                    8: "ACK! OK fine, I'll do anything, just tell me what you want. Pleasepleaseplease don't hurt me!",
                    9: "...there was a ... dragon ...",
                    10: "It's a research compound...We experiment with magic and... I don't really know why. We're all curious people and we wanted to know...",
                    11: "Yeah, we found this place, mostly like this, a few centuries ago. It's full of... strange magic. Things we don't know. We've been discovering hidden... quirks... ever since.",
                    12: "A few hundred. The mages council, the researchcers and their staffs, the guards, the service.",
                    13: " I... I worked. For the chief alchemist. His assistant",
                    14: "There are two doors, but they're both in the Antechamber. Just past the fountains or through the library.",
                    15: "Oh gods no, I'd be useless in a fight",
                    16: "No... unless you'd like some dead rats to eat?",
                    17: "Imadeoutwithmycousinonce...",
                    18: "Gate room, by the library. One of the reasons we live here permanently. It opens different portals... I guess a dragon got through... ",
                    19: "We're just curious! We find things, we learn how they work, there's no real purpose behind it! There's also no harm!",
                    20: "Lava lakes wih mysterious riddles, statues that seem to do nothing, demons, portals, shrines, doors that aren't doors, walls that aren't walls, secret rooms, sandstorms that affect the flow of time... It's like candyland...",
                    21: "His main focus was on a potion that could make you wildly rich. He succeeded, mildly.",
                    22: "Our main lab is hidden below a statue in the Temple. It's heavy to push but down there you can brew the Potion of Immaculate wealth and have all the money you need!",
                    23: "I don't know anything about it, I swear! Just rumors...",
                    24: "Ser John moved out master potion to the Kennel Chandelier! You have to pull the levers in order but if you do, it'll drop for you to collect! That's all I know I swear!",
                    25: "Thank you",
                    26: "No thank you...",
                    'denial': "I'm sorry, I really can't help you!"}

###############################################################################
## The Ice ####################################################################
###############################################################################
ice_desc = """The most notable feature of this room is the immediate sense of cold you feel upon entering. The floor is slick with ice, icicles hang from the ceiling and several objects in the room are frozen. Off to the side of the room is a table covered in snow under which you think you see a couple scrolls. On the other side of the room is a shelving unit with a couple books, some empty vials, and some strange looking bones. In the far corner is a large chunk of ice stuck to the wall; you can see something shiny inside it. In the vry center of the room is a hole in the ice, you can hear water slohing around inside it. It really is unusually cold in here...
"""

ice_bookshelf = """You make it to the bookshelf and see several books that are frozen shut and completely useless. Only three books seem to have been spared the worst of it. There are some odd bones on the shelves that are scarred and scratched up, it's only mildly disconcerting. 
"""

ice_reading = "1: Read the faded green book\n2: Read the blue and red book\n3: Read the scale-bound book\n4: Do something else\n>> "

ice_table = """You slide your way over to the table and dust off the top layer of ice flakes. On it is a small frozen quill and a bunch of paper scraps. Most of the papers on the desk have been ruined by the ice, but two are still legible, though only barely.
"""

ice_scroll1 = """I have been studdying the effects of different potions on my subjects intelligence and I believe I have perfected my work. When brewed properly, I can create a potion that drastically improves the subjects intelligence. It comes in the form of a sweet smelling blue liquid and it works wonders! The recipe is on the next page, but be careful; if you add tea leaves at the wrong point, it will have the opposite effect. Make you stupider. You can always tell because the stupid potion is a blue liquid that smells like strawberries.
"""

ice_scroll2 = """Well, it looks like the ice is here to stay. We tried to track down Giles but he's nowhere to be found and without understanding how he did this, we have no idea how to reverse it. It's kinda nice, really. On hot days we leave the doors open to cool the compound and cold water tastes way better than room temperature. Still, I wonder where Giles went...
"""

ice_scrolls = "1: Read the blue-stained scroll \n2: Read the ripped page \n3: Do something else \n>> "

ice_chunk = """You find yourself in front of the mysterious ice chunk. You are now close enough to make out the light inside, its a pair of shiny steel bracers. 
"""

ice_chunk_attack = """You bang and bang the ice with your {} but nothing seems to happen. It seems impervious to physical assault.
"""

ice_chunk_fireball = """You stand back and cast {} against the ice. It melts instantly and the bracers drop and clang against the ground.
"""

ice_chunk_magic_fire = """You take out your jar of magical fire and open it over the ice. It pours out like water and instantly melts the ice before dissapearing into the water. The bracers drop the gorund with a clang.
"""

ice_hole = """You slip over to the middle of the room, the source of the sloshing. You find yourself standing over a hole in the ice, looking down into deep, cold, water. All around you, you can see the stone floor through the ice, but looking down you would swear you were standing on the ice over a frozen lake. The water moves as if a breeze is blowing it and seems much bigger than just a 3x3 hole in the ground. But that's not the strangest part. The strangest part is that at the bottom of the hole, under maybe 15-20 feet of freezing water is a terrifying red mask.
"""

ice_hole_fail = """The very thought of diving into that water for it makes your bones hurt. You're not nearly tough enough for that. No. Just no. 
"""

ice_hole_pass = """You dive headfirst into the pitch dark water and immediately the cold hits you like a thousand daggers. You perservere and dive deeper and deeper until the amulet is finally within your grasp. Quickly, you pick it up and rise to the surface. Before heaving yourself out of the water, you chuck the amulet onto the suface, it skids into the corner of the room. Miserably cold and wet, you take a moment to rest before continuing.
"""

###############################################################################
## The Pit ####################################################################
###############################################################################
pit_b_fall = """Before you have a chance to do anything, you start falling! Still a little unsure of what is happening, you hit the ground with a mighty "THWACK!"
"""

pit_u_fall= """You can feel the small ledge in your fingers but you just can't grasp it fast enough. You fall and land in the bottom of the pit with a "THUD"
"""

pit_u_pass = """You gracefully leap and land perfectly balanced on the small ledge
"""

pit_u_no = """Yeah, it's way too far down to jump. That looks like it hurts. Not gonnna happen.
"""

pit_b_desc = """You are standing on a very small legde in the middle of a pit. Not in the center but midway up. Looking down, you can see the bottom, dark, wreathed in shadow. Looking up you can see the top, a much larger ledge on the wall across from you. You don't have many options here, you can turn around and return through the {} or you can jump down to the bottom. If you feel particularly spry, you could try to jump to the ledge, but it seems very difficult.
"""

pit_b_jump = """You leap from the ledge and land safely in the bottom of the pit.
"""

pit_b_dex_fail = """You summon all your strength and leap off the tiny ledge with the nimbleness of a rabbit escaping a fox. You feel as though you are flying through the air. Then, as suddenly as you took off, your face comes into contact with the opposing wall and you fall for a minute before hitting the ground in the lower pit with a sickening "THUD!"
"""

pit_b_dex_pass = """You summon all your strength and leap off the tiny ledge with the nimbleness of a rabbit escaping a fox. You feel as though you are flying through the air. Then, as suddenly as you took off, your fingers grasp the opposing edge and you hoist yourself over.
"""

pit_u_desc = """You are standing on a sizable ledge overlooking the pit. Looking down into the pit you can see a small ledge with a door and far far below it is the ground. On the wall behind you, on either side of the door are two stone gargoyles. Both of them have a arm outstreched, palm open, as though they are wating to be handed something.
"""

pit_l_desc = """You are at the bottom of a large pit. The ground is flat and earthen with a few small rocks scattered at the edges. There is the skeleton of a man lying strewn on the ground, he must've been some sort of prisoner down here. He's still wearing his satchel bag, it looks nice. In the dirt next to him is an old rusty key. Looking up, you can see two ledges. One is far far above you and seems impossible to reach, but the other is at the top of a partictularly rocky wall that you might be able to scale. Behind you is a door, a {}.
"""

pit_l_encounter = """Before you have a moment to take in your surroundings you hear a snarling coming from the shadows. Your are under attack!
"""

pit_l_victory = """After a rigorous few minutes, you finally have time to appreciate where you are.
"""

pit_l_climb = """You start the grueling climb and somehow manage to make it up to the first ledge. It's very small, you could try to balance up here, but there's a door you could also make it through
"""

pit_l_fail = """You start the grueling climb but just can't make it all the way. You're not strong enough.
"""

pit_gargoyle_pass = """The gargoyles hand closes around the stone sphere. After another moment his other hand moves and bangs the wall next to him. At that moment a rope falls from a small hole in the ceiling. It looks like you can climb through it.
"""

pit_gargoyl_fail = """The gargoyle's hand closes around the stone sphere and nothing happens. You think you just got screwed out of loot.
"""

###############################################################################
## Lava #######################################################################
###############################################################################
lava_desc = """The door leads you down a flight of stairs, as you descent further, the more refined stonework of the above compunds disapears, replaced with rough hewn rock. It looks natural, as though you are entereing some sort of cave. There is a bright light coming from the bottom and it's getting strangely hot for being so deep. \n\nYou emerge in a cavern on a small rocky beach overlooking a lava lake. The "beach" runs around the entire lake, a rather large distance, as the lake is easily 1000 feet across. You can see three sets of stairs, including the one you just walked down. Peering up them, you can see a {}, a {}, and a {}. In the chamber you can see a table covered in notes wth 3 jars sitting upon it. Curiously, there is a stone pier that leads about 100 feet into the lake. The heat out there must be unbearable. On the far sde of the lake you can make out what seems to be a, thankfully innactive, Iron Golem. Besides all that, there doesn't seem to be anything interesting down here. 
"""

lava_table = """A lof of the parchment on this table is burned or otherwise singed, but some of the scrolls are legible. One even seems to be written in draconic, that's unusual. Even more unusual are the three jars on the table. In one is a small green pixie, she looks angry. In the middle one is an enormous peiceing blue eyeball that swivels to watch you as you observe the table. In the last one is full of water with a lone piranha swimming inside, its rows of grisley teeth showing. All 3 jars are sitting atop the largest peice of parchment labled FINDINGS FOR DISCOVERER. Around this parchment are some other baubles: a watch, a latern, a water goblet, a comb, a ball of yarn, and a paintbrush.
"""

lava_findings = """FINDINGS FOR DISCOVERER-- I am writing this very fast because we are under attack. We discovered this lava pool and the stone bridge when trying to construct a health spa for our older mages. On the wall was carved a riddle that dissapeared as soon as it was written down. We have discovered 3 things - (1)Throwing the wrong thing into the lava is bad (2)Throwing the right thing into the lava is good (3)We can't tell the difference between good and bad - probably. Technically we don't even know that much, all we've managed to do is throw the wrong shit into the lava. We have all these things left, if you find this, continue our research! \n\n\n      "Four and Ninety teeth fly overhead yet no one who meets this monster ends up dead"  ~Good Luck
"""

lava_scroll_draconic = """I didn't tell Estaing but this magic is well known to my ancestors. Throwing in an eye of seeing is a surefire way to summon a dragon brood. I won't let him do it, obviously, but I also won't tell him what I know. 
"""

lava_scroll_golem = """Well, our iron golem stopped working today. Either the heat or old age, or maybe Estaing's magic is fading as he descends further into madness over this damn riddle. Regardless, I put in a request for the council to enchant the walkway so we don't cook to death throwing shit in the lava ourselves. Just seemed simpler than making a new golem.
"""

lava_scroll_diary = """I am at my wits end. I have thrown every kind of monster imaginable into that lake. Some with lots of teeth, some with no teeth but lost of claws, some with lots of both! I managed to get my hand on a pixie (poor thing is obviously pissed) and a piranha, I think the answer is to start breeding things and throw mutant monster offspring in there. Fayette thinks I've lost my mind. He came to me the other day and told me he thinks the answer is a comb! What a moron, they don't even fly! Flying Piranha Pixies. That has to be it.
"""

lava_brood = """You throw the eye into the lava and nothing happens... at first. Then the lava starts bubbling and churning until 4 dragons burst out of it and attack you!
"""

lava_fail = """You throw the {} into the lava and nothing happens
"""

lava_pixie = """You pry the top of the pxies jar open and she flies angrilly out at you! She moves to attack!
"""

lava_pass = """You toss the comb into the lava and immediatly the lava starts churning. After a moment, a great swell of lava rises above and takes on the crude shape of a face. It looks you up and down before speaking \n\n"Adventurer. Tell me your name" 
"""

lava_golem = """You approach the golem and notice that it is very finely crafted. Especially the left gauntlet, which seems both brutal and elegant at the same time. Upon closer inspection you see Orcish symbols. Of course! Orc smiths alone could have created such a beautiful but deadly gauntlet.
"""

lava_pass2 = """He responds with only a simple nod before returning to the lake. Moments later you can feel the earth rumbling beneath your feet. You see lava spit into the air and suddenly realize you're on a thin strip of stone 100 feet from solid ground over a lake of lava. Before you have time to panic, ground emerges from the lake. Not ground, not anymore, it's a stone pillar, a giant boulder, maybe a small thin mountain. It rises to be just above your head before stopping... in front of you lies a small ornately carved hole.
"""

lava_fail2 = """He gets an impatient look on his face but otherwise says nothing
"""

lava_swell = """You approach the swell of lava again, he repeats himself to you, though he seems more impatient now than before. \n\n"Adventurer. Tell me your name" 
"""

###############################################################################
## Vines ######################################################################
###############################################################################
vines_desc = """You have entered a dimly lit room of elegant, yet old and slightly decrepid, stonework. All four walls are covered in thick snaking vines and the stone tiles on the ground have been pushed up and aside by thick roots. In the center of the room stand three stone statues. One is {}. Another is {}. The third is {}. In the center of the three of them is a table with some scrolls on it. One is giving off a soft light, you recognize it as a spell scroll a wizard could learn from. Next to the scrolls is a {} that you could easily pick up. There are only two doors here, a {} and a {}.
"""

vines_reveal = """You cast {} at a blank section of the wall and the vines burn away. To your horror, they emit a screech as they wriggle and writhe in agony on the ground. But to your immense satisfaction it reveals a stash of gold in the wall. Small victories.
"""

vines_table = """The table is covered by dead leaves and insect-eaten parchment. After sorting through the rubbish, you can see a spell scroll, a medium sized book, and a couple legible scrolls, including one in dwarvish. 
"""

vines_scroll_dwarvish = """I have uncovered the secret of the elixer of fortitude! The potions master was trying to keep it a secret, he want's to have a demonstration at the session tomorrow, but I snuck in and read his notes. The proper elixer of fortitude is a steaming yellow liquid, but if you add quasit spit at the wrong time, it becomes a yellow liquid that seems more like a dense sludge than anything edible. I need to remember that for sessions. The sludgey one apparently makes you weaker....
"""

vines_scroll1 = """It's hard to say who's having less success: us here or those guys downstairs at the lake. We've scrubbed every square inch of this place and learned nothing about it. Why are these statues here? Why do they face each other? Why are they in the center of the room instead of off to the side? The world may never know because I CAN'T FIGURE IT OUT! Still, Estaing has his hands full downstairs. If anyone could solve that riddle, their name would be HERO forever.
"""

vines_scroll2 = """I think I have an idea but I'm afraid to bring it up. Or say it out loud. Or think it. Some of these mages are mind readers, I don't need that. But oh well, here goes: There's nothing here. You know, we got to these new digs and found this cool room with these impressive statues and assumed they were put here as a clue or a puzzle to protect treasure or monsters or an amazing magical secret. But let's be honest: reality is often mundane. These statues were put here for some stupid reason that was insignificant and we are wasting our time trying to assign meaning to the whims of men long dead. But try telling that to the high council when there's even the slightest possibility of treasure.
"""

vines_boots = """You hack away at some vines and suddenly the skeleton of a very dead man falls to the ground. You would be weirded out but he's wearing very nice boots...
"""

###############################################################################
## Library  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   CONTAINS PLOT   ##
###############################################################################
library_desc = """This room is a grand library, three stories with elegant wood floors and railings. You can see more bookshelves than you've ever seen before and there are tables everywhere full of notes and old parchment. Overhead is a strange looking chandelier. It resembles an umbrella hanging from the ceiling; there are 6 colored crytals - red, purple, blue, gree, yellow, and orange - all pointed to a very shiny and reflective sphere of light. Regardless, it's not giving off any light. It must be broken. Still, there is enough light to see with. The whole room looks strangely abandoned, yet there are no cobwebs or visible signs of decay either. It's as though everyone using it just left 15 minutes ago. {}
"""

library_first = """\n\nYou are on the first floor, which looks more like an archive than a library. There are complete skeletons of different beasts on display and maneqins displaying elaborate armors and wardrobes. One maneqin catches your eye, a smaller one wearing a fur sash. In a display case is what is obviously a wizards spell scroll next to an enormous tome. There are also two mysterious vials in a display case full of alchemy equipment. Behind you is a door, a {} and there is a staircase to take to the upper two levels."""

library_second = """\n\nYou are on the second floor, which clearly is the main research floor. There are books and scrolls and tomes everywhere, some left open to various pages, others dog-eared for people to return to. There is one particularly large table on the back wall that looks more official than the others. It might be worth looking at."""

library_third = """\n\nYou are on the third floor, which is more of an overflow space it seems. The books here are dustier, the space seems less used, and the topics seem more obscure. On an otherwise empty wall off to the side is a strange looking crystal mechanism, and across the room, next to a series of bookshelves is the floors only table."""

library_sash = """You approach the small maneqin and observe its fur sash closer. It looks to be wolf pelt, but it's definitely a single pelt making it much too big to be a wolf. It also looks a lot tougher than regular pelt. You kinda want it.
"""

library_elvish = """Our recipe for the perfect strength potion is done! We had a problem where we kept getting red liquid that turned crimson when we shook it. Turns out we were adding the xorn eyes too soon. We fixed it and now the potions produces a dense and viscous red liquid that grants increased strength to he drinker.
"""

library_gnomish = """I managed to fix the concils recipe for health potions. They were using dragon turtle blood like assholes. That stuff doesn't do anything but make poisons, in this case a brown liquid that looks sticky that hurts you. I pointed them towards drider venom, which when paired with dryad leaves creates a violet liquid with flecks of blue and red still floating in it that restores health.
"""

library_orcish = """I shared our sercret tribal recipe for long life elixirs. I know it was a bad idea but I kept making it for myself and they noticed. It was pretty good for them, all thier attempts backfired - produced an orange liquid that never stops moving. I dunno why, I'm no alchemist. But I showed them the right way and now theyre getting the same purple liquid that seems to sparkle when the light hits it just right as we do.
"""

library_gargoyles = """We did an analysis of the gargoyles outside and we got some weird voo-doo coming off from them. Expecially the {} one. Something strange going on with that one. We think they might respond to some sort of keystone. We just have no idea where to find one...
"""

library_plot_1 = {'John': """When Ser John first came to our doors 500 years ago, he was just a small boy. He was alone and looking for a place to sleep. The council, of course, turned him away immediately. That is when he unleashed a magical assault upon the entry gate that stunned the high council for its barbarity. It was quickly stopped and he became a ward of the compound. The source of his abilities was never made clear and seemed to fade with age, by the time he was a teenager, he was no more dangerous than any other child. But he underwent another remarkable transformation in his early twenties when he left the compound to find work as a mercernary. No one here expected him to survive, his farewell was rather emotional. Ten years later, the monster of the deep emerged and terrorized the coastal province. And who killed it and saved the world? Ser John. He came out of nowhere, still no one knows where he went for those 10 years, but when he came back he was a force to be reckoned with. He killed the monster and returned to the monastary a hero. After some time with the council they gave him immortality and he agreed to live here forever.""",
                  'Jaggard': """When Ser John first came to our doors 500 years ago, he was just a small boy. He was alone and looking for a place to sleep. The council, of course, turned him away immediately. That is when he unleashed a magical assault upon the entry gate that stunned the high council for its barbarity. It was quickly stopped and he became a ward of the compound. The source of his abilities was never made clear and seemed to fade with age, by the time he was a teenager, he was no more dangerous than any other child. But he underwent another remarkable transformation in his early twenties when he left the compound to find work as a mercernary. No one here expected him to survive, his farewell was rather emotional. Ten years later, the monster of the deep emerged and terrorized the coastal province. And who killed it and saved the world? Ser John. He came out of nowhere, still no one knows where he went for those 10 years, but when he came back he was a force to be reckoned with. He killed the monster and returned to the monastary a hero. After some time with the council they gave him immortality and he agreed to live here forever.""",
                  'Halenhadra': """When Ser John first came to our doors 500 years ago, he was just a small boy. He was alone and looking for a place to sleep. The council, of course, turned him away immediately. That is when he unleashed a magical assault upon the entry gate that stunned the high council for its barbarity. It was quickly stopped and he became a ward of the compound. The source of his abilities was never made clear and seemed to fade with age, by the time he was a teenager, he was no more dangerous than any other child. But he underwent another remarkable transformation in his early twenties when he left the compound to find work as a mercernary. No one here expected him to survive, his farewell was rather emotional. Ten years later, the monster of the deep emerged and terrorized the coastal province. And who killed it and saved the world? Ser John. He came out of nowhere, still no one knows where he went for those 10 years, but when he came back he was a force to be reckoned with. He killed the monster and returned to the monastary a hero. After some time with the council they gave him immortality and he agreed to live here forever.""",
                  'Lyestra': """When Ser John first came to our doors 500 years ago, he was just a small boy. He was alone and looking for a place to sleep. The council, of course, turned him away immediately. That is when he unleashed a magical assault upon the entry gate that stunned the high council for its barbarity. It was quickly stopped and he became a ward of the compound. The source of his abilities was never made clear and seemed to fade with age, by the time he was a teenager, he was no more dangerous than any other child. But he underwent another remarkable transformation in his early twenties when he left the compound to find work as a mercernary. No one here expected him to survive, his farewell was rather emotional. Ten years later, the monster of the deep emerged and terrorized the coastal province. And who killed it and saved the world? Ser John. He came out of nowhere, still no one knows where he went for those 10 years, but when he came back he was a force to be reckoned with. He killed the monster and returned to the monastary a hero. After some time with the council they gave him immortality and he agreed to live here forever.""",
                  'Ulldar': """When Ser John first came to our doors 500 years ago, he was just a small boy. He was alone and looking for a place to sleep. The council, of course, turned him away immediately. That is when he unleashed a magical assault upon the entry gate that stunned the high council for its barbarity. It was quickly stopped and he became a ward of the compound. The source of his abilities was never made clear and seemed to fade with age, by the time he was a teenager, he was no more dangerous than any other child. But he underwent another remarkable transformation in his early twenties when he left the compound to find work as a mercernary. No one here expected him to survive, his farewell was rather emotional. Ten years later, the monster of the deep emerged and terrorized the coastal province. And who killed it and saved the world? Ser John. He came out of nowhere, still no one knows where he went for those 10 years, but when he came back he was a force to be reckoned with. He killed the monster and returned to the monastary a hero. After some time with the council they gave him immortality and he agreed to live here forever.""",
                  'Urumbrior': """When Ser John first came to our doors 500 years ago, he was just a small boy. He was alone and looking for a place to sleep. The council, of course, turned him away immediately. That is when he unleashed a magical assault upon the entry gate that stunned the high council for its barbarity. It was quickly stopped and he became a ward of the compound. The source of his abilities was never made clear and seemed to fade with age, by the time he was a teenager, he was no more dangerous than any other child. But he underwent another remarkable transformation in his early twenties when he left the compound to find work as a mercernary. No one here expected him to survive, his farewell was rather emotional. Ten years later, the monster of the deep emerged and terrorized the coastal province. And who killed it and saved the world? Ser John. He came out of nowhere, still no one knows where he went for those 10 years, but when he came back he was a force to be reckoned with. He killed the monster and returned to the monastary a hero. After some time with the council they gave him immortality and he agreed to live here forever."""
                  }

library_plot_2 = {'John': """Of all the monsters in Sholan's domain, the Sunderfoe is a many-armed hybrid between shark and squid. The children of a dark, hidden universe, Sunderfoe are unpredictable and unfathomable killers. They act as wounded animals, thrashing and killing as though it's life is always on the line. Luckily, Sunderfoe don't occur very often, when they do, stories of their encounters echo down through centuries.  One legend states that an entire city fell into the sea with the appearance of a nearby Sunderfoe. Killing it is next to impossible, they are all but impervious to normal weapons and resist most magic. It is said that it requires the magic or material of their home universe to sufficiently damage it, but with their origins so mysterious and their occurence so rare, it is hard to verify.""",
                  'Jaggard': """Of all the monsters in Sholan's domain, the Sunderfoe is a many-armed hybrid between shark and squid. The unintedned child of dark magic, a Sunderfoe is only created when a dark ritual to summon a kraken goes wrong. Where a kraken is intelligent and capable of reason, a Sunderfoe is a wild beast of unimaginable power. It's only impulse is destruction and terror. Luckily, Sunderfoe don't occur very often, when they do, stories of their encounters echo down through centuries. But the worst part of the Sunderfoe is the dark magic associated with slaying it. Because bringing it into the world requires a great deal of dark energy, removing it from the world releases that energy back into it. The effects vary but are often devastating. One legend states that an entire city fell into the sea with the destruction of a nearby Sunderfoe. All this makes them incredibly terrifying beasts to encounter. """,
                  'Halenhadra': """Of all the monsters in Sholan's domain, the Sunderfoe is a many-armed hybrid between shark and squid. The unintedned child of dark magic, a Sunderfoe is only created when a dark ritual to summon a kraken goes wrong. Where a kraken is intelligent and capable of reason, a Sunderfoe is a wild beast of unimaginable power. It's only impulse is destruction and terror. Luckily, Sunderfoe don't occur very often, when they do, stories of their encounters echo down through centuries. But the worst part of the Sunderfoe is the dark magic associated with slaying it. Because bringing it into the world requires a great deal of dark energy, removing it from the world releases that energy back into it. The effects vary but are often devastating. One legend states that an entire city fell into the sea with the destruction of a nearby Sunderfoe. All this makes them incredibly terrifying beasts to encounter. """,
                  'Ulldar': """Of all the monsters in Sholan's domain, the Sunderfoe is a many-armed hybrid between shark and squid. The unintedned child of dark magic, a Sunderfoe is only created when a dark ritual to summon a kraken goes wrong. Where a kraken is intelligent and capable of reason, a Sunderfoe is a wild beast of unimaginable power. It's only impulse is destruction and terror. Luckily, Sunderfoe don't occur very often, when they do, stories of their encounters echo down through centuries. But the worst part of the Sunderfoe is the dark magic associated with slaying it. Because bringing it into the world requires a great deal of dark energy, removing it from the world releases that energy back into it. The effects vary but are often devastating. One legend states that an entire city fell into the sea with the destruction of a nearby Sunderfoe. All this makes them incredibly terrifying beasts to encounter. """,
                  'Lyestra': """Of all the monsters in Sholan's domain, the Sunderfoe is a many-armed hybrid between shark and squid. The unintedned child of dark magic, a Sunderfoe is only created when a dark ritual to summon a kraken goes wrong. Where a kraken is intelligent and capable of reason, a Sunderfoe is a wild beast of unimaginable power. It's only impulse is destruction and terror. Luckily, Sunderfoe don't occur very often, when they do, stories of their encounters echo down through centuries. But the worst part of the Sunderfoe is the dark magic associated with slaying it. Because bringing it into the world requires a great deal of dark energy, removing it from the world releases that energy back into it. The effects vary but are often devastating. One legend states that an entire city fell into the sea with the destruction of a nearby Sunderfoe. All this makes them incredibly terrifying beasts to encounter. """,
                  'Urumbrior': """Of all the monsters in Sholan's domain, the Sunderfoe is a many-armed hybrid between shark and squid. The unintedned child of dark magic, a Sunderfoe is only created when a dark ritual to summon a kraken goes wrong. Where a kraken is intelligent and capable of reason, a Sunderfoe is a wild beast of unimaginable power. It's only impulse is destruction and terror. Luckily, Sunderfoe don't occur very often, when they do, stories of their encounters echo down through centuries. But the worst part of the Sunderfoe is the dark magic associated with slaying it. Because bringing it into the world requires a great deal of dark energy, removing it from the world releases that energy back into it. The effects vary but are often devastating. One legend states that an entire city fell into the sea with the destruction of a nearby Sunderfoe. All this makes them incredibly terrifying beasts to encounter. """
                  }

library_compound = """The compound is 23 rooms large. We have a temple, a lab, a library, lots of places to ivestigate mysterious magic, dungeons, catacombs, kennels, living quarters, and everything you could need. We grow our own food outside. The gardens are in the front yard and the farm is out back. Here we live for learning and exploration, both along side of and apart from the gods. It is a good life.
"""

library_table_2 = """There are only a few scrolls on this table, it is exquisitely organized. One scroll looks like a diary page, another page looks like an invitation of some sort. It's surprisingly boring for such an ornate table.
"""

library_table_3 = """This desk is covered in scrolls and scrap paper. There are even some written in other languages; one is in Orcish and another in Gnomish. It's deffinitely messier than the other desk.
"""

library_puzzle_win = """The chandelier hums gently as it comes to life, filling the room with brilliant multi-colored light. Right on cue, one of the bookcases on floor swings open revealing a hidden door.
"""

library_puzzle_approach = """You slide a crystal rod into one of the slots and some of the chandelier lights come on. Maybe some combination of these rods will fix the chandelier.
"""

library_puzzle_inspect = """The mechanism seems very strange. It is made entirely out of teal crystal and set insde the wall. What you see is a teal crystal panel with 6 crystal rods hanging off it from short chains. There are also six slots in the panel, about the size of the crystal rods. That probably means something...
"""

###############################################################################
## Sanctum ####################################################################
###############################################################################
sanctum_desc = """This is a small room denoted by a single desk and a large round window overlooking a valley. You are very high up and jumping out of the window doesn't seem to be an option. But the desk is interesting enough to take over your attention. On is a large pile of gold, a pair of scrolls that look very official, and a spell scroll glowing vibrantly. That might be worth checking out.
"""

sanctum_master_spell = {"Instant Kill 4": """We did it. The high council wanted a way to immediatly kill an enemy so we made one. Instant Kill 4 is better than the previous 3 becuase it doesn't kill you (usually) but instead only hurts you a lot. It takes a powerful wizard to cast but it's a real game changer for us. Obviously it's safer to cast against weaker foes but if you're strong enough, you can take out some real nasty beasts.""",
                        "Firestorm 4": """When fireball just isnt enough for you, there's firestorm 4. You wanna talk shit loads of damage, we'll talk shit loads of damage. This thing does shit loads of damage! A terrifying amount of damage, really. Honestly, it's only drawback is not dealing even more damage. Oh, and that it takes one hell of a wizard to pull it off.""",
                        "Divine Inspiration 4": """Yes, the name is cheesy but we wanted to highlight how much better this makes you. Not only will it heal you, but it will give you damage and accuracy boosts as well. Basically makes you unkillable in battle, if you're talented enough to cast it. Sure we could have called it "Elegant Shield" or something like that but...""",
                        "Solar Rays 4": """So what we wanted to do was create a spell that was A) Easy to cast, B) kinda minimal at first, to save your energy, but C) got more intense over time to help kill more stubborn foes. So here is Solar Rays 4, only castable by master magicians, but perfectly suited to help you conserve energy in battle."""}

sanctum_scroll = """So we've hit a speed bump. We DID manage to perfect the potion of wealth. Drink it and the lint of your pocket turns to gold. Is wonderous. BUT it is identical to all our failed attempts. Every single missfire, every potion that turned the gold in your pocket to lead, looks, smells, tastes, exactly like our successful brew. So be careful. Unless you have gold to spare, it might not be worth the risk.
"""

###############################################################################
## Dungeon ####################################################################
###############################################################################
dugeon_desc = """You're in the dungeon. That much is obvious. It's small, basically just a dimly lit hallway with 6 cells. There's a door behind you, a {}, and a door across from you, a {}. Walking up and down the room you can see into the 6 cells. They're denoted by numbers etched into the stone next to them. Cell one has a fat old man, he smiles at you as you walk past but he says nothing. Cell two has a young mousey looking mage. She averts her eyes as you step past her. Cell 3 has a middle-aged man, a farmer by the looks of him. His dirt stained clothes are evident as he lies on the stone floor. Cell 4 has a cloaked figure, sleeping or resting. You cannot see their face and note the irregularity of their breathing. Cell 5 has a large pile of gold on the ground, it seems someone was using this cell as a bank vault. Cell 6 is empty except for a door of simple wood. There is an engraving on it, but you cannot read it from this distance. On the wall next to the exit are 4 keys. You imagine you could open 4 of these cells. On a table in between two cells is a horrific looking dagger.
"""

dungeon_celll1 = """You enter cell 1 to speak to the fat old man. Before you can open your mouth he jumps up and says "Shut yer yap and buy something!" that's when he lifts up his shirt and a number of interesting looking goods tumble out.
"""

dungeon_celll2 = """You enter cell 2 to speak to the young woman. As soon as you do, she exclaims "Oh thank you for coming for me! I was imprisoned for what I learned. If you let me, I can turn your gold into knowlege. Will you?" 
"""

dungeon_exp_accept = """She waves her hands and your gold flies out of your pocket and hovers in the air before you. You watch in amazement as each coin becomes a ball of golden that shoots into you skull. Her work done, the mage plops to ground for a short rest.
"""

dungeon_celll3 = """You approach the dirty looking farmer. He seems willing to talk to you.
"""

dungeon_celll4 = """You walk into cell 4 to investigate the mysterious figure. He doesn't seem to register your entrance so you step closer and pull off his cloak - A young dragon bursts from his disguise to attack you!
"""

dungeon_dragon_win = """Lesson learned. Dragons can polymorph.
"""

dungeon_celll5 = """You take one step into cell 5, to claim your gold, when an incredible gust of wind blows from out of nowhere, preventing you from entering! It will take all your might to fight this gale.
"""

dungeon_gold_pass = """You take one tiny step after another until you are standing right on top of the gold. For a moment it feels like you are about to be lifted off your feet, then the wind stops. The gold it yours for the taking!
"""

dungeon_gold_fail = """You try to fight the wind but you just can't make any progress.
"""

dungeon_celll6 = """You enter cell 6 and step closer towards the door. As you get near it, the inscription becomes clear.
"""

dungeon_mimic_win = """Did it look like a jar to you?
"""

dungeon_mimic_attack = """WHEN IT'S A MIMIC! You're under attack!
"""

dungeon_you_base = {'Who are you?': 2,                                        
            'What is this place?': 3,                                         
            'Tell me about Ser John.': 4}                                     

dungeon_you_qs = {"What is this place?": 3,                                           
          "Who is Ser John?": 4,                                              
          "Why are there monsters everywhere?": 19,                           
          "Where are all the people?": 20,                                    
          "Why am I here?": 21,                                               
          "Are you sure you can't do more?": 30}                              

dungeon_convo_you = {1: dungeon_you_base,                                             
                     2: {"Why are you here?": 5,                              
                         "Tell me about yourself": 6,                         
                         "Can you help me, Peter?": 7},                        
                     3: {"This place is pretty elaborate for a sleepy little cult": 10, 
                         "Tell me more about Cybils Watch": 26,               
                         "\"Used to be\"? Explain.": 27},                     
                     4: {"Anything reliable you can tell me?": 28,            
                         "Does Sunderfoe mean anything to you?": 29},         
                     5: {"No I'm sorry, I haven't": 8,                        
                         "Maybe": 9,                                          
                         "Yeah, he's back that way": 18},                     
                     6: {"No I'm sorry, I haven't": 8,                        
                         "Maybe": 9,                                          
                         "Yeah, he's back that way": 18},                     
                     7: dungeon_you_qs,                                               
                     8: {"Tell me about your son": 11,                        
                         "He's probably dead": 12},                           
                     9: {"I mean maybe": 15,                                  
                         "Sorry, no": 16,                                     
                         "Yeah man I totally saw him": 17},                   
                     10: dungeon_you_qs,                                              
                     11: {'Ok I will': 13,                                    
                          "Nah": 14},                                         
                     12: {'Ok I will': 13,                                    
                          "Nah": 14},                                         
                     13: dungeon_you_base,                                            
                     14: dungeon_you_base,                                            
                     15: dungeon_you_base,                                            
                     16: {'Why not?': 13,                                     
                          "Nah": 14},                                         
                     17: {"In the library": 18,                               
                          "In the temple": 18,                                
                          "Up your mother's butt! AHAHAHAHA": 15},            
                     18: dungeon_you_base,                                            
                     19: {"Why portals?": 23},                                   
                     20: dungeon_you_qs,                                              
                     21: {"I woke up on an altar...": 22},                    
                     22: dungeon_you_qs,                                              
                     23: {"Why did the come here?": 24,                       
                          "Why ban portals?": 25},                            
                     24: {'Tell me about Ser John': 4},                       
                     25: dungeon_you_qs,                                               
                     26: dungeon_you_qs,                                              
                     27: {'Tell me about Ser John': 4},                       
                     28: dungeon_you_base,                                            
                     29: dungeon_you_base,                                            
                     30: {"Yes please!": 31},                                
               'denial': dungeon_you_base}

dungeon_convo_him = {1: 'Hello...',
                     2: """My name is Peter, I'm a farmer from the valley.""",
                     3: """This is the compound of the Cybil's Watch. Or at least it used to be. My family has lived in its shadow for years and I never so much as hear a peep until recently. Then it expoded with activity. It's usually just a sleepy little cult.""",
                     4: """He's their leader. Been around for forever, in my dad's time and my granddads time. No idea how old he is, but if his paintings and statues are to be believed, he's still a young man. You hear all kinds of things about a man like that - that he can shoot lightning, or survive being cut in half - most of it's probably bull.""",
                     5: """They came into my home at night and took me and my son! I don't know where he is, please, have you seen him?""",
                     6: """My son and I live on a small farm, growing onions. The soil is good for it. My wife, Janet, died when our stove exploded mid-cooking. It was...devastating. I was really looking forward to that dinner. Since then it's just been me and Gideon. Please, he was taken by men into the compound, have you seen him?""",
                     7: """I don't know...maybe. I know some things about this place, some things I shouldn't.  I can't fight, but maybe I can answer your questions?""",
                     8: """Oh...I just hope he's ok...""",
                     9: """What do you mean maybe? Did you or didn't you?""",
                     10: """Well it's an old group, and they're rumored to be well funded. I've never seen beyond these doors so I can't explain much better than that.""",
                     11: """His name is Gideon, he's about this tall and had dark brown hair, please if you see him, come tell me!""",
                     12: """Maybe, but I can't live thinking that, will you please look for him?""",
                     13: """Oh thank you, gods bless you!""",
                     14: """Well, I.... I... I'll just look for him myself then. Screw you!""",
                     15: """Well you're no help at all!""",
                     16: """Oh no, I'm so worried, he's all I have since his mother died in that cooking explosion. Please will you help me find him?""",
                     17: """Oh thank the gods! Where is he?""",
                     18: """Ok, I'll go to him now!""",
                     19: """Well...the mages here were experimenting with portals. Or at least, thats what I overheard. A few weeks ago, before I was here, one went awry and some monsters got in. We heard the commotion from the farm. Scary stuff. I guess they didn't learn and now... here we are.""",
                     20: """My guess is killed and eaten. Maybe some escaped. We only survived becuase these cells are enchanted. But we spent about 8 hours staring into the eyes of those ... things ... wondering when the enchantment would wear off. Gods bless you stranger""",
                     21: """I don't even know who you are. You're not a prisoner, you're not one of them, and you're not a monster. You look like you know what you're doing though. Who are you?""",
                     22: """...I heard them talking about some sort of ritual last night. It sounds like you were it.""",
                     23: """Didn't you hear? The king banned portal research a couple of months ago. There were a lot of experienced, talented mages who were researching portals, and the king shut them down. Looks like they all came here.""",
                     24: """Because Ser John protects them""",
                     25: """Well because you rarely ever know that it's gonna open where you think it is. It's a tricky thing, right? Look what happened here. Could you imagine this disaster in the capital?""",
                     26: """They're an old cult, dating to just after unification. From what I hear, there's very little worship going on, just experimentation. They put discovery above all else. They're also very secretive. All of this I learned from my father and neighbors, and that's all anyone knows!""",
                     27: """Well, Cybils Watch was about discovery, but they're different now. They've been conducting nightime excursions into the surrounding towns and they arrested everyone you see in this room. None of that is very scientific. Ser John's gone off the deep end, if you ask me.""",
                     28: """Haha, sorry nope. I've never seen him and only hear about him second hand. Not somebody I'm looking to meet though.""",
                     29: """No, I can't say that it does""",
                     30: """Well... I found this key, I wanted to use it to escape but you seem like maybe you'll make better use of it. Do you want it?""",
                     31: """It's yours. Just make sure to clear the way for me please.""",
                     'denial': 'I really can\'t help you'}

###############################################################################
## Cliffs >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   CONTAINS PLOT   ##
###############################################################################
cliffs_desc = """You are standing on a steep looking cliffside. You can see three doors leading to what is hopefully safer ground. One door is {}, another is {}, and the last one is {}. The ground itself here is what holds your attention. It looks unstable, even dangerous in places. You can also see some places where it's... moving? You'll have to be very careful when walking through here. But by far, the most interesting thing here is just off the edge of the cliff. A perfectly reflective silver sphere is hovering, bobbing up and around right around eye level. In front of it is a table with a few books and scrolls, as well as a modest pile of gold.
"""

cliffs_infernal = """The Pit Beasts have been nesting here again. They always make me come to get rid of them. People say we look alike so we must think alike. Such bullshit. What they don't know is that I've discovered a way to brew a successful potion of charm using Pit Beast blood. The high mages have been producing this terrible salty smelling liquid that reminds me of seawater, it doesn't work at all. My brew is a bitter smelling sludge that reminds you of thick mud but hey, at least it works. 
"""

cliffs_peer = """You gaze off towards the horizon and see only trees. You're high enough up to see above them all, but still not quite near the clouds, this must be a small mountain. Looking up you can see the tall, austere walls of the compound, looking down, you can see the fires of a small settlement. 
"""

cliffs_sphere = {'John': """This floating sphere is some kind of container. We know that. We also know that it responds to ... feathers. We discovered that by misake actually, someone threw a chicken at it, and it seemed to like that. After some more experiementing, it just liked the feathers. But... well that doesn't help us. When we give it a feather, it accepts it, puts on a show, the gives us nothing. I'm starting to think it's all some sort of hoax. A prank by an old warlock. Feathers? For real? I'm out of ideas.""",
                 'Halenhadra': """This floating sphere is some kind of container. We know that. We also know that it responds to ... feathers. We discovered that by misake actually, someone threw a chicken at it, and it seemed to like that. After some more experiementing, it just liked the feathers. But... well that doesn't help us. When we give it a feather, it accepts it, puts on a show, the gives us nothing. I'm starting to think it's all some sort of hoax. A prank by an old warlock. Feathers? For real? I'm out of ideas.""",
                 'Jaggard': """This floating sphere is some kind of container. We know that. We also know that it responds to ... feathers. We discovered that by misake actually, someone threw a chicken at it, and it seemed to like that. After some more experiementing, it just liked the feathers. But... well that doesn't help us. When we give it a feather, it accepts it, puts on a show, the gives us nothing. I'm starting to think it's all some sort of hoax. A prank by an old warlock. Feathers? For real? I'm out of ideas.""",
                 'Urumbrior': """This floating sphere is some kind of container. We know that. We also know that it responds to ... feathers. We discovered that by misake actually, someone threw a chicken at it, and it seemed to like that. After some more experiementing, it just liked the feathers. But... well that doesn't help us. When we give it a feather, it accepts it, puts on a show, the gives us nothing. I'm starting to think it's all some sort of hoax. A prank by an old warlock. Feathers? For real? I'm out of ideas.""",
                 'Lyestra': """This floating sphere is some kind of container. We know that. We also know that it responds to ... feathers. We discovered that by misake actually, someone threw a chicken at it, and it seemed to like that. After some more experiementing, it just liked the feathers. But... well that doesn't help us. When we give it a feather, it accepts it, puts on a show, the gives us nothing. I'm starting to think it's all some sort of hoax. A prank by an old warlock. Feathers? For real? I'm out of ideas.""",
                 'Ulldar': """This floating sphere is some kind of container. We know that. We also know that it responds to ... feathers. We discovered that by misake actually, someone threw a chicken at it, and it seemed to like that. After some more experiementing, it just liked the feathers. But... well that doesn't help us. When we give it a feather, it accepts it, puts on a show, the gives us nothing. I'm starting to think it's all some sort of hoax. A prank by an old warlock. Feathers? For real? I'm out of ideas."""}

cliffs_accept = """The sphere begins moving towards your outstreched hand. It gets closer and closer, showing no signs of stopping or giving way. Then it makes contact with your fingertips. It's not a solid, but a dense and smooth liquid, whose inner turmoil is in sharp contrast with its serene surfact. It moves still closer, engulfing your hand, your wrist, and your lower arm. It's a strange feeling, not rough but constant and swirling. You feel the {} get lifted from your hand... a few moments later something lands in your palm. But the swirling inside gets stronger, more intense. Whatever is in your hand now isn't going anywhere but this thing is suddenly full of energy. Without even a ripple on its reflective exterior, your gift falls to the table and the sphere bursts into hundreds of small reflective drops, which hang around in the air like suspended water droplets. It's really a beautiful sight...
"""

###############################################################################
## Portal >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   CONTAINS PLOT   ##
###############################################################################
portal_desc = """You have entered a large round room, or what used to be a room. Now it is old and decrepid, with stone walls rumbling, revealing views of the surrounding area. There are the remains of columns circling the edge of room, and a ceiling that once must have been a magnificent dome. The floor is cracked, but made of solid stone, as though it was carved right into the mountainside. In the cener of the room is an... arch? That's not quite right but theres no better word. It's a freestanding stone triangle, wih sides of equal length. Its interior ie etirely taken up by a buzzing, vibrantly {} energy, that pops and crackles with electicity at random intervals. In front of the gate is a table and a bookshelf. Resting on the table is an {} and a couple scraps of parchment, the bookshelf is mostly empty excpet for some food and a couple vials of some stuff. You can see the glint of a red pendant necklce under a lot of dust. It looks like this room was emptied in a hurry.
"""

portal_int_riddle = """Twice the larger of two numbers is three more than five times the smaller and the sum of four times the larger and three times the smaller is seventy-one
"""

portal_tests = {"Strength": {'desc': 'You emerge in a vast red desert, with the oppressive heat of two suns and tall rocky spires carved by the fierce winds. Looking around, you see nothing of interest except a small pile of gold and the gate you came through, still crackling with energy. Except... no. There is something else here. You hear it before you see it, a faint banging and screaming barely audible over the winds. In front of you and adjacent to a cliffside is a large boulder. Upon inspection, it seems to be sealing some people inside a cave, or in this case, a tomb.',
                             'encounter': 'The sounds of the screams have drawn attention to you! You\'re under attack!',
                             'choice': 'Try to move the boulder',
                             'base': "You approach the boulder and start to push. As soon as gap appears the sound of screaming only gets louder. You can see arms start clawing their way out",
                             'Easy': "You manage to fully uncover the cave and a group of very grateful (and now quiet) people emerge",
                             'Medium': 'You manage to mostly uncover the cave so that most of the people trapped can clamor out, but the people still trapped scream even louder knowing their fate is sealed',
                             'Hard': 'You can only uncover a small part of the entrance so that one or two people have room to escape, but the people still trapped scream even louder knowing their fate is sealed',
                             'Killer': 'Try as you might, you just can\'t move this boulder! The people inside realize this and start screaming louder'},
                
               "Dexterity": {'desc': 'You emerge in a dense green jungle. The tallest trees you\'ve ever seen are all around you and the thick underbrush obscures the horizon. It isn\'t long after you appear that you hear noises coming from the brush around you. It\'s probably smart to hide up in the trees.',
                             'encounter': 'You are ambushed by your remainnig pursuers! En Garde!',
                             'choice': 'Get away in the treetops',
                             'base': 'You climb the trees just in time! As you balance on a thick branch, you see a large group of beasts surround the place you used to be standing. Your peace of mind is short lived, however, because they see you and begin climing the tree themselves! You must run to get away! \n\nRUN RUN RUN!',
                             'Easy': 'You managed to outrun and outwit most of your pursuers but a few still remain and are heading your way!',
                             'Medium': 'You managed to outmaneuver some of your pursuers but some were too smart for that. They\'re heading your way!',
                             'Hard': 'You managed to get away from a few of the beasts but most of them are still hot on your tail!',
                             'Killer': 'You barely made it two feet before falling, this fight is gonna be a doozy'},
                
            "Constitution": {'desc': 'You emerge in a strangely alien environment. The ground is rocky and a thick yellow fog hangs in the air. You cannot see more than a few hundred feet ahead of you. Most terrifying is that you cannot see the gate anywhere. What you do see is a series of rough, rock-hewn obelisks with writing on them. It seems they\'re here to guide your way back to the gat, though you cannot see it through the fog.',
                             'encounter': 'Your foes stand between you and the gate!',
                             'choice': 'Find your way through the fog',
                             'base': 'Something about this fog isn\'t right. You can feel it slowly poisoning your mind, you can see your surrpundings start to spin... You better find your way back fast',
                             'Easy': 'You made it through the fog but something tracked you! Get ready to fight!',
                             'Medium': 'You made it through the fog ok but it looks like you attracted a bit of attention to yourself, get ready to fight!',
                             'Hard': 'You escape, barely, but you\'ve alerted enemies all around you to your presence! Get ready!',
                             'Killer': 'You claw your way towards the gate when you notice the crowd of fiends gathering around you. You must look like easy pickings'},
                
            "Intelligence": {'desc': 'Your emerge in a small room of stone brick and to your horror, the gate switches off behind you. Looking around, the room has 8 walls, each wall containing a colunm of different colored fire - they may be doors of some kind. In front of you is a small wood table on which sits 8 vials of different colored potion and a modest pile of gold. A peice of paper on the table gives you the instructions: "On this table are 8 potions, each allowing you past a similar colored barrier of fire. Behind each barrier is a lever to reactivate the gate, but there are other things hiding back there as well. Two doors are safest, they are given by solving the riddle. Good luck"',
                             'encounter': 'Your foes are between you and the lever',
                             'choice': 'Try to reactivate the gate',
                             'base': 'You approach the table and read the riddle: {}'.format(portal_int_riddle),
                             'Easy': 'You walk through the fire and find only a small group of enemies waiting for you. This should be easy!',
                             'Medium': 'You walk through the fire and find a modest group of foes waiting for you. This shouldn\'t be too hard...',
                             'Hard': 'You walk through the fire and find a lot of monsters lying in wait... brace for attack!',
                             'Killer': 'You walk through the fire and find a huge group of deadly looking monsters waiting!'},
                
                "Charisma": {'desc': 'You emerge in a small round room, that seems, at first glance to be completely empty. It\'s very dark, you can\'t quite make out the edges of the room, but the glow of the gate illuminates enough to display a seal of some kind in the middle of the floor. It\'s a circle of runes enclosing a truly horrific visage: a smooth face wreathed in tentacles with peircing eyes that seem to gaze right through you.',
                             'encounter': 'The mindflayers surround you!',
                             'choice': 'Walk out onto the seal',
                             'base': 'As you step out onto the seal, you see movement in the corner of your eye. Suddenly, you feel an excuciating headache, punctuated by a strange sensation - as if something is yanking things out of your brain... It\'s a Mind Flayer! Testing your mental fortitude before it attempts to either enslave you or devour your brain! You must remember try your hardest to fight off this mental attack!',
                             'Easy': 'You demonstrated enough mental strength to convince all but one of the Mind Flayers to leave you be! The remaining one looks hungry...',
                             'Medium': 'You fought off their attack well enough that two of the hideous creatures abandon the attempt to capture you! The other two move in for the kill...',
                             'Hard': 'You did your best, and one Illithid turns back and disapears into the shadows, but the remaining 3 look hungry!',
                             'Killer': 'You tried but could not repel the mental attack. ALl four Illithids move in, expecting easy pickings...'}}

portal_win = """You step out of the gate and into the crumbling room. As you turn around, the energy begins humming and suddenly disapears before reapearing as a bright, crackling {}.
"""

portal_draconic = """I had a visionary moment the other day. Dragon fire! Giles cursed that room to never melt, but dragon fire is magical and should be able to melt it! Any magical fire would do, but dragon fire would be the coolest. I know Hubert took a jar of dragon fire with him when he checked out the tunnels under Kay'leth. I wonder what happened to it?
"""

portal_plot = {'John': """Well, we managed to get the gate up and running again. It's heavily enchanted but should function as expected. Not only does it allow travel to places we could only dream of, but it will respond to you actions on the other side! Allowing us to "program" it, for lack of a better word, to open and close and reveal secret pocket dimenstions or hidden objects based on... well you. Walk through the gate, pick up the right object, walk back through and BAM it chages to reveal a secret hideout or a stash of some kind. It's AMAZING. The only downside is it sometimes opens gates we weren't expecting, like the other day when those... things... got in. BUT it's all OK now.""",
               'Halenhadra': """Well, we managed to get the gate up and running again. It's heavily enchanted but should function as expected. Not only does it allow travel to places we could only dream of, but it will respond to you actions on the other side! Allowing us to "program" it, for lack of a better word, to open and close and reveal secret pocket dimenstions or hidden objects based on... well you. Walk through the gate, pick up the right object, walk back through and BAM it chages to reveal a secret hideout or a stash of some kind. It's AMAZING. The only downside is it sometimes opens gates we weren't expecting, like the other day when those... things... got in. BUT it's all OK now.""",
               'Jaggard': """Well, we managed to get the gate up and running again. It's heavily enchanted but should function as expected. Not only does it allow travel to places we could only dream of, but it will respond to you actions on the other side! Allowing us to "program" it, for lack of a better word, to open and close and reveal secret pocket dimenstions or hidden objects based on... well you. Walk through the gate, pick up the right object, walk back through and BAM it chages to reveal a secret hideout or a stash of some kind. It's AMAZING. The only downside is it sometimes opens gates we weren't expecting, like the other day when those... things... got in. BUT it's all OK now.""",
               'Urumbrior': """Well, we managed to get the gate up and running again. It's heavily enchanted but should function as expected. Not only does it allow travel to places we could only dream of, but it will respond to you actions on the other side! Allowing us to "program" it, for lack of a better word, to open and close and reveal secret pocket dimenstions or hidden objects based on... well you. Walk through the gate, pick up the right object, walk back through and BAM it chages to reveal a secret hideout or a stash of some kind. It's AMAZING. The only downside is it sometimes opens gates we weren't expecting, like the other day when those... things... got in. BUT it's all OK now.""",
               'Lyestra': """Well, we managed to get the gate up and running again. It's heavily enchanted but should function as expected. Not only does it allow travel to places we could only dream of, but it will respond to you actions on the other side! Allowing us to "program" it, for lack of a better word, to open and close and reveal secret pocket dimenstions or hidden objects based on... well you. Walk through the gate, pick up the right object, walk back through and BAM it chages to reveal a secret hideout or a stash of some kind. It's AMAZING. The only downside is it sometimes opens gates we weren't expecting, like the other day when those... things... got in. BUT it's all OK now.""",
               'Ulldar': """Well, we managed to get the gate up and running again. It's heavily enchanted but should function as expected. Not only does it allow travel to places we could only dream of, but it will respond to you actions on the other side! Allowing us to "program" it, for lack of a better word, to open and close and reveal secret pocket dimenstions or hidden objects based on... well you. Walk through the gate, pick up the right object, walk back through and BAM it chages to reveal a secret hideout or a stash of some kind. It's AMAZING. The only downside is it sometimes opens gates we weren't expecting, like the other day when those... things... got in. BUT it's all OK now.""",}

###############################################################################
## ANTECHAMBER ################################################################
###############################################################################
foyer_desc = """You walk into an enormous round room, complete with a domed roof and curved windows. It's really a beutiful place, full of natural light and clean stone floors. There are two doors directly opposite one another, a {} and a {}. Between them, on one wall, is a collection of tablets bearing strange writing. On the oher side are two more doors, a {} and a {}. Between them stands a woman, fully armored and holding a terrifying looking glaive. In the center of the room is a large boulder with an ornate sword sticking out of one side. Cliche? Yes. Cool? Deffinitely. 
"""

foyer_elvish = """The strength of the elves runs deep. It is more than mortal, it is a gift from the gods themselves. Where man is weak, we are mighty, where dwarves would tremble, we stand tall, where orcs bang their fists in vain, we pull open doors and unlock the secrets of the universe. The strength of the elves runs deep.
"""

foyer_orcish = """The Orc needs not to speak to impress his will. His very presence speaks for him. He can overpower the strongest elf with a glare, he can extract all the secrets of dwarves with a snarl, and he can open the gates of man with his silence. The Orc needs not speak to be known, he simple needs to be.
"""

foyer_gnomish = """Craftsmanship is the mark of the Elf, they say, but few have ever considered the Gnome. While elves use their long lives to perfect their craft - a tedious process of trial and error - the Gnome sees the craft as an extenstion os his identity. Inteeligence and creativity have always been proud Gnomish traits, and it is why our crafts stand the test of time.
"""

foyer_infernal = """Since the dawn of the earth, people have tried to knock us down! Thay have hated us, they have shunned us, they have scapegoated us, and to what avail?!? We still stand, proud and unbowed! We will not be pushed aside by society, not without picking it's pocket on the way over. We are a proud people and we will STAND... always.
"""

foyer_sword = """You approach th boulder to inspect the sword. It's a beautiful thing, really. Fine crafsmanship and still delicately polished. It is lodged quite firmly inside the boulder, but you may be able to pull it out...
"""

foyer_s_pass = """You give a mighty tug and the sword comes unsheathed instantly! The tip falls to the ground with a loud clang - it's heavier than you expected - before you lift it up and take a good look at this beautiful weapon.
"""

foyer_s_fail = """You try your hardest but the sword just doesn't budge.
"""

foyer_gate_lock = """You approach the gate but it refuses to let you through. You'll need a special key to unlock this door.
"""

foyer_gate_unlock = """Your GATE KEY soars out of your bag before disapearing into a ball of light and unlocking the gate before you.
"""

foyer_convo_you = {1: {"Who are you?": 2,
                       "Excuse me, how do I leave this godforsaken place?": 3,
                       "Where THE FUCK am I?": 4},
                   2: {"Your duties? I'm still a little unclear...": 5,
                       "Outside? I can leave?": 3},
                   3: {"Oh good, difficulty": 6,
                       "What kind of difficulty?": 7,
                       "They're locked...": 15},
                   4: {"Fair enough": 1,
                       "NO!, I WANNA KNOW NOW!": 1},
                   5: {"But you'll let me leave?": 10,
                       "Do you find yourself keeping things in or out more often?": 1},
                   6: {"Yes, I often feel most alive while getting stabbed": 1,
                       'What challenges do you face here?': 12},
                   7: {"Isn't it your job to keep them from getting out?": 13,
                       "Weaken? Have you been helping me?": 14},
                   8: {"Well, at the very least, someone could have warned the people in the valley... saved them": 9},
                   10: {"That's smart. Wouldn't it have been more wise to prevent all this in the first place? Lots of people died...": 8},
                   12: {},
                   13: {"There's a distinct lack of blood here though": 11},
                   11: {},
                   14: {},
                   15: {"Why hide it?": 16,
                        "Thank you": 1},
                   16: {},
                   'denial': {}}

foyer_convo_her = {1: "...",
                   2: "I am the Gatekeeper, charged with protecting the doorways to he outside. Many horrors have come my way as late, but nothing has prevented me from discharging my duties",
                   3: "The doors on either side of me lead to the outisde. From there you can leave, but not without difficulty.",
                   4: "A place of secrets. The people here have chared me with protecting those secrets. I will not disclose them to you.",
                   5: "I keep the status quo. What is inside, stays inside, what is outide, stays outside. The gats are mine to keep",
                   6: "Survival is always difficult. Often when we are content, we are slowly slipping towards towards death. Challenge keeps us alive",
                   7: "The beasts who conquered these walls have made it beyond them. I was not able to weaken them there so you will find them at their full strength",
                   8: "How so?",
                   9: "...perhaps... you are correct. Lives are more important than secrets. Go forth, with my blessing.",
                   10: "Courage is willingness to fight when necessary, wisdom is knowing when it is not necessary. I have little faith in your survival beyond these gates",
                   11: "I have enough magic at my command to keep a tidy work space",
                   12: "Always something new. The beauty of this place is a lack of monotony",
                   13: "My job is to protect the gates. For beasts of this nature, there are more ways out than these gates. I assure you, no beast made it past me",
                   14: "I have been helping myself. As beasts come to me, I kill them. Some run, then find you. Others find you first. You will not have that advantage outside",
                   15: "You will need the GATE KEY. I belive the high mages hid it beyond the Gate. Find the gate room, and you'll find the GATE KEY",
                   16: "I belive they were intending to keep everything trapped inside",
                   'denial': 'You will not convince me of anything, I promise you that'}

###############################################################################
## WATERFALLS #################################################################
###############################################################################
wfall_desc = """You make it to the peak of the trail and behold a small, but beautiful, waterfall. It spills down the cliffside into a pool of crystal clear water with 9 mysterious stones standing around its edge. Carved into the central one is an inscription, what looks like a riddle. The trail continues past the waterfall in both directions. In one direction you can see a gate off in the distance, a {}. The other direction, off in the distance, is a {}.
"""

wfall_riddle = """\nNine men went walking to the neighboring village. On the journey, they met {} merchant{}, who run{} the route regularly. The first man remarked, "The road must be safe then, for merchants only travel the safest roads". They next met {} beggar{}, who live{} under a tree along the road. The fourth man remarks "The road is clearly not safe, for beggars would be chased off by gaurds if the road was regularly patrolled". Night fell, the road became dark, and they saw {} owl{}, who nest{} in the tallest tree. The second man remarks "Now it cannot be safe, for owls are the watchmen of the devil", but he is quickly dismissed as overly superstitious. The came up and the men met {} gaurd{} who patroll{} the route at daybreak. "See friends," the seventh man remarks, "all things are better in the light". The ninth man, who has been silent for the entire journey, finally speaks 'Friends, our words this night have been based in fear, not fact. We should all try to avoid speculation. The facts alone are what is important".
"""

wfall_stone_press = """You press your hand to the stone and feel a slight buzzing. When you remove your hand, your handprint remains glowing on the stone.
"""

wfall_puzzle_solve = """The four stones rise into the air and hover for a moment before crashing down to the ground, sending a deep rumble through the earth. As the tremors subside, the waterfall begins to bend. Defying every law of physics, it starts to curve like a U just before it hits the water. But it doesn't stop at a U, it circles around to become an O. It starts swirling around in midair, faster and faster, until the center of the O changes to resemble a passageway, a small hole in a violent tempest.
"""

wfall_puzzle_fail = """As you touch the fourth stone, your handprints, previoulsy glowing a soft blue, change to a harsh red. Suddenly, the rocks explode! Witha violent bang rubble flies everywhere and you are lucky to escape unharmed.
"""

###############################################################################
## STATUE ROW #################################################################
###############################################################################
srow_desc = """You have walked into what looks like a statue garden. There are benches and headges and ornate statues, some of which seem very old. At the base of each statue is a chest, it seems as though people tried to empty the compound of valuables and didn't make it past here alive. Regardless, if you have the keys, you can probably get some pretty cool stuff.
"""

srow_dwarvish = """We made it out to the statue gardens with two of our most powerful artifacts but the beasts are closing in fast. In case anyone finds this, we have here he Orb of Thesselhydra which powers up spell-casting to insane levels, boosting your Dexterity, Intelligence, and Charisma. The high mages used to fight over it a lot. Also we have the Helm of Horrors, which increases your damage output, gives you a chance to stun your enemies, and adds to your constitution. It truly makes you a fearsome warrior.
"""

###############################################################################
## GARDEN #####################################################################
###############################################################################
garden_desc = """You wander into a beautiful garden, full of food and flowers and trees. There is even a table set for a nice outdoor brunch that is untouched by the chaos. The sun is shining and the breeze is blowing and the birds are chirping and you find it almost impossible to believe all the horror you have endured. The Garden is enclosed by cobblestone walls, but you can see two gates leading out, on is {} and another is {}. On the other side of the garden is {}. Your heart skips a beat. That must be the way out!
"""

###############################################################################
## EXXIT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   CONTAINS PLOT   ##
###############################################################################
exxit_desc = """You reach the main gates to the compound, finally! But awaiting you is one more test, for standing bellow the great arch is {}. You clench up in fear - the surrounding countryside is completely invisible to you. It is as though you and {}, {} are the only things in existence.
"""

bbeg_john = "a man in metalic-blue heavy armor, wielding a greatsword much too large for an average man. He stands maybe 6.5 feet tall, with long brown hair and the solid stance of an experienced warrior. But there's something... morose about his appearance. As though he has reached the end of a great tragedy"
bbeg_jaggard = "a robed figure, floating in the air. His robes flow in the breeze, causing you to wonder just how much space underneath them he takes up. There's a bristeling, crackling energy surrounding him and you know he must be angry about something"
bbeg_halenhadra = "an enormous spider, or what you thought was a spider. Upon closer inspection, you see that where a spider would have a face, this thing has the naked torso of a woman. It's utterly revolting, her dead eyes train on you and you feel a sickness overwhelm your soul. This... abomination, is unholy"
bbeg_urumbrior = "a tall, proud looking Half-Dragon, with pitch-black scales and gleaming green eyes. His silver plate armor shines in the moonlight and his breath illuminates him and his surroundings in a sickly green glow. He sees you and waits very patiently for you to draw nearer"
bbeg_lyestra = "a elderly, wrinkled old woman. But before even seeing her, you can smell her, the foul stench of rotting flesh, burning hair, and evil deeds. This is no ordinary woman, this is a true hag, a hag queen, kept alive by spite and misery"
bbeg_ulldar = "a small man, dressed in furs. His wooden helmet has two primitive eye holes carved in it, an two great antler mounted on top. His fingers are long and his fingernails even longer. Making matters creepier, they seem to be covered in blood"

attack_john = "Ser John swings at you with his greatsword!"
attack_jaggard = "Jaggard swoops in to swipe at you whis boney claws!"
attack_halenhadra = "The Spider-Queen stabs her great stinger at you!"
attack_urumbrior = "The Half-Dragon slashes at you with his greatsword!"
attack_lyestra = "The Hag-Queen grabs you around the kneck and chokes you with unnatural strenght"
attack_ulldar = "The Druid-King stabs at you with his fingernails!"

final_victory = {'John': "Ser John's defeated body slumps to the ground in defeat. His body slowly fades away until it is as though he was never here...",
                 'Jaggard': "Jaggard's frail body crumbles into dust before blowing away in the wind...",
                 'Halenhadra': "Halenhadra shrieks with pain and fury one last time before convulsing into a heap on the ground. Her body soon becomes dust, and blows away in the wind...",
                 'Urumbrior': "Panting, Urumbrior falls to the ground, still clucthing his weapon. He looks up at you with hatred before his body erupts in green flame, and he disapears forever...",
                 'Lyestra': "Lyestra howls in misery as her body seems to come undone at the seams. She falls apart into a pile of rotting flesh and bone before becoming absorbed into the earth...",
                 'Ulldar': "Ulldar Kang roars in horror and disbelief as he is slain. When his body hits he ground, the grass quickly consumes him, pulling his corpse deep within the earth..."}

exxit_convo_you = {'John': {1: {"So you're him?": 2,
                                "I'd like to leave, please": 3,
                                "Who are you?": 4,
                                "So what really happned here?": 5},
                            2: {"Not really, I just want to leave": 6,
                                "Yeah, I'm kind of looking forward to it": 7,
                                "Not without answers. I want to know what really happened here": 8},
                            3: {"You seem upset... ": 9,
                                "If you want to leave, leave. I won't stop you": 10,
                                "You'll be even more dissapointed after I kill you": 11},
                            4: {"Well what are the right ones?": 12,
                                "I think it matters": 13},
                            5: {'What kind of miracle?': 14,
                                "This is beyond disaster, this is a massacre": 15,
                                "Does it really end here?": 16},
                            6: {"Why not? What further harm could letting me leave do?": 17},
                            7: {"I think you of all people would understand how simple killing is": 18,
                                "Do you want to die?": 19},
                            8: {"What is the deal with this ritual?": 20,
                                "Why am I here?": 21,
                                "The Sunderfoe?": 22,
                                "How are you so powerful?": 23,
                                "How are you so old?": 23},
                            9: {"What happened last night?": 20,
                                'How many hundreds?': 24,
                                'What are you trying to accomplish?': 14},
                            10: {"What sort of compromise?": 25},
                            11: {"I think you mean strong!": 26},
                            12: {"No... I don't think I would": 27,
                                 "I... Maybe...": 28,
                                 "Hell yeah! Where?": 29},
                            13: {"Sunderfoe Slayer?": 22,
                                 "Ardshiama?": 30,
                                 "Feorixt the Fire of Eyes?": 31, 
                                 "Cybils Watch?": 32,
                                 "Master of the Unknowable?": 33},
                            14: {},
                            15: {"You're insane... You let this happen??": 34,
                                 "Oh cool, so you did this on purpose": 34},
                            16: {},
                            17: {"Ok then, let's get it over with": 26},
                            18: {"No, you're a monster": 34},
                            19: {},
                            20: {"What is the deal with this ritual?": 20,
                                 "Why am I here?": 21,
                                 "The Sunderfoe?": 22,
                                 "How are you so powerful?": 23,
                                 "How are you so old?": 23},
                            21: {"What is the deal with this ritual?": 20,
                                 "Why am I here?": 21,
                                 "The Sunderfoe?": 22,
                                 "How are you so powerful?": 23,
                                 "How are you so old?": 23},
                            22: {"What is the deal with this ritual?": 20,
                                 "Why am I here?": 21,
                                 "The Sunderfoe?": 22,
                                 "How are you so powerful?": 23,
                                 "How are you so old?": 23},
                            23: {"What is the deal with this ritual?": 20,
                                 "Why am I here?": 21,
                                 "The Sunderfoe?": 22,
                                 "How are you so powerful?": 23,
                                 "How are you so old?": 23},
                            24: {"What is the deal with this ritual?": 20,
                                 "Why am I here?": 21,
                                 "The Sunderfoe?": 22,
                                 "How are you so powerful?": 23,
                                 "How are you so old?": 23},
                            25: {"Unless I kill you, right?": 35},
                            26: {},
                            27: {"You deserve to die for what you've done": 26},
                            28: {},
                            29: {},
                            30: {"Sunderfoe Slayer?": 22,
                                 "Ardshiama?": 30,
                                 "Feorixt the Fire of Eyes?": 31, 
                                 "Cybils Watch?": 32,
                                 "Master of the Unknowable?": 33},
                            31: {"Sunderfoe Slayer?": 22,
                                 "Ardshiama?": 30,
                                 "Feorixt the Fire of Eyes?": 31, 
                                 "Cybils Watch?": 32,
                                 "Master of the Unknowable?": 33},
                            32: {"Sunderfoe Slayer?": 22,
                                 "Ardshiama?": 30,
                                 "Feorixt the Fire of Eyes?": 31, 
                                 "Cybils Watch?": 32,
                                 "Master of the Unknowable?": 33},
                            33: {"Sunderfoe Slayer?": 22,
                                 "Ardshiama?": 30,
                                 "Feorixt the Fire of Eyes?": 31, 
                                 "Cybils Watch?": 32,
                                 "Master of the Unknowable?": 33},
                            34: {"You deserve to die for that": 26},
                            35: {"Then I will kill you, and put an end to this": 26},
                            'denial': {}},
                   'Jaggard': {},
                   'Halenhadra': {},
                   'Urumbrior': {},
                   'Lyestra': {},
                   'Ulldar': {}}

exxit_convo_him = {'John': {1: "Hmmm",
                            2: "I am indeed, him. I suppose you want to kill me?",
                            3: "So would I. But life is full of dissapointment, it seems",
                            4: "What does it matter? You ask the wrong qestions",
                            5: "We tried for a miracle, and found a disaster... hard to belive this is how it ends. So... undignified. So... quiet",
                            6: "I can't let you do that",
                            7: "Hmm, I would too. But things aren't so simple",
                            8: "I can tell you anything. You won't be passing these gates. Ask away",
                            9: "I have spent HUNDREDS of years trying to accomplish something, trying to... last night my dream died... ",
                            10: "I can't leave. I am tied to this place. It is not normal to love as long as I have... it requires compromise.",
                            11: "You are a bold one",
                            12: "Who are -we-? We are weak men, serving weak gods. If you could meet a REAL god, would you?",
                            13: "Hmmph. I am John of Ardshiama, Sunderfoe Slayer, Emissary to Feorixt The Fire of Eyes, Leader of Cybils Watch and Master of the Unknowable!",
                            14: "I wanted to meet a god, face to face. Not those pussy gods Firellians worship, but a real GOD. A being of power beyond comprehension.",
                            15: "Hmm, magic in this sense is never simple. It requires sacrifice. You see a massacre, I see a show of faith",
                            16: "I have been preparing for this for 200 years. I don't have 200 years of patience anymore",
                            17: "The eyes are upon me. If you leave, my sacrifice is incomplete. One of us is going to die here. That is out of our hands. What we can control is who survives, and I ALWAYS SURVIVE",
                            18: "I kill out of necessity. It is never easy.",
                            19: "Don't be ridiculous",
                            20: "The ritual is to open a gate to another dimension. I recieve my powers from that dimension. My master lives there. I wanted to meet him... face to face. I can feel him calling me....",
                            21: "The bulk of the ritual is a slaughter meant to provoke the fabric of reality. When we die, our souls travel to another dimension. When lots of people die, the traffic, so to speak, can destabilize the fabric of our existence. We needed to weaken that fabric. To finally rip it, we needed a soul sent to our target dimension - a sacrifice for the gods there. They would rip open our gate to get to you, our special soul, consecrated so as to attract their attention. You, yourself, were selected because we found you first",
                            22: "A beast from our target dimension. A stillborn child that could not survive the riggors of that world but can thrive here. It was because of my... special connection that I was able to slay it. It requires a bit of home to be in any real danger",
                            23: "My mother was a very powerful warlock, who made a pact with a faraway beast. My father was repulsed by her, she used her given magic to seduce him, and I was born. The magic used to produce me flows in my veins. Where my mother needed to commune with her master, I always had it. At least, until I was a teenager. My powers dissapeared so I went looking for my mother. I never found her. Instead I found her notes, I contacted the dimension and I forged a pact of my own. A pact that has led us here.",
                            24: "At least 200, possibly more, who can remember that long?",
                            25: "My life is tied to this land, I don't leave and I don't die",
                            26: "Very well. We will fight to the death. EN GARDE!",
                            27: "Well, we have different interests",
                            28: "You can see my purpose then. We were so close... So much wasted... ",
                            29: "It's too late now... the opportunity is gone... ",
                            30: "A name I invented. I never met my mother and never had a home town.",
                            31: "My master, my teacher, my god. The source of all my powers and every blessing I have. His existence is beyond any of us. I was closer to him than any",
                            32: "A wayward group of scientists when I found them, they believed in discovery for the sake of discovery. They had no moral or ethical limitations, made my proposals simpler",
                            33: "The magic that flows through me is different than any in this world, it comes from a place that was not built for our life",
                            34: "It had to be done...",
                            35: "Ha, yes, that's right",
                            'denial': '...'},
                   'Jaggard': {},
                   'Halenhadra': {},
                   'Urumbrior': {},
                   'Lyestra': {},
                   'Ulldar': {}}
