# -*- coding: utf-8 -*-
"""
Created on Thu May 30 07:34:53 2019

@author: Devlin
"""

import dungeon_charactercreate as create
from dungeon_charactercreate import kit
from dungeon_charactercreate import tgen
import dungeon_games as gme
from dungeon_games import text
import dungeon_minigames as mini
import random as rn
import time

## Working on   
##              @Modify challenges to use dc and mods - maybe (combat only?)
##              +Rework combat to be more turn-based, multi-turn attacks, target swtching, spell combos, 
##              =finish writing lore
##              >rewrite armory convo to be prisoners son
#####################################################################################################\
################################################################################/                 \###
## Shorthand ##################################################################/                   \##
short_wrap = 40                                                                                     ## 
wrap = 80                                                                                           ##
mages = ["Wizard", "Sorcerer"]                                                                      ##
                                                                                                    ##
## THE GAME ###################################################################>-------------------<##
plot = gme.game_random                                                                              ##
                                                                                                    ##
## Weapons ####################################################################>-------------------<##
fists = kit.Weapon('Fists', text.flavor_fists, 1, 4, 1, 'Fists')                                    ##- Base
shortsword = kit.Weapon('Shortsword', text.flavor_shortsword, 1, 12, 1, 'Swords')                   ##- Altar
mace = kit.Weapon('Small Mace', text.flavor_mace, 1, 8, 2, 'Clubs', stun = 20)                      ##- Pantry
dagger = kit.Weapon('Small Dagger', text.flavor_dagger, 1, 8, 1, 'Daggers')                         ##- Altar
cutlass = kit.Weapon('Cutlass', text.flavor_cutlass, 1, 4, 4, 'Swords')                             ##- Catacombs
staff = kit.Weapon('Wood Staff', text.flavor_staff, 1, 6, 1, 'Staffs')                              ##- Altar
iron_staff = kit.Weapon('Serpentine Staff', text.flavor_staff, 1, 6, 2, 'Staffs')                   ##- Tower
ser_dagger = kit.Weapon('Serrated Dagger', text.flavor_dagger, 1, 4, 3, 'Daggers')                  ##- Vines
warhammer = kit.Weapon('War Hammer', text.flavor_hammer, 1, 4, 5, 'Clubs', stun = 33)               ##- Armory
longsword = kit.Weapon('Longsword', text.flavor_longsword, 1, 8, 3, 'Swords')                       ##- Armory
club = kit.Weapon('Club', text.flavor_club, 1, 4, 2, 'Clubs', stun = 10)                            ##- Altar
broadsword = kit.Weapon('Broadsword', text.flavor_broadsword, 1, 10, 3, 'Swords')                   ##- Antechamber
ornate_staff = kit.Weapon('Ornate Staff', text.flavor_ornate, 1, 20, 1, 'Staffs')                   ##- Portal
dread_dagger = kit.Weapon('Dreadful Dagger', text.flavor_dread, 1, 10, 2, 'Daggers')                ##- Dungeon
                                                                                                    ##
## Equipment ##################################################################>-------------------<##>------------<
amulet = kit.Equipment('Opal Amulet', text.equipment_amulet, 'Strength', 1)                         ##- Antechamber
mask = kit.Equipment('Red Mask', text.equipment_mask, 'Charisma', 1)                                ##- Ice
bracelet = kit.Equipment('Azure Beads', text.equipment_beads, 'Intelligence', 1)                    ##- Gloves
bracers = kit.Equipment('Steel Bracers', text.equipment_bracers, 'Damage', 3)                       ##- Ice
gold_ring = kit.Equipment('Ring of Iron Will', text.equipment_ring, 'Constitution', 1)              ##- Underwater
boots = kit.Equipment('Leather Boots', text.equipment_boots, 'Dexterity', 1)                        ##- Vines 
satchel = kit.Equipment('Shoulder Satchel', text.equipment_satchel, 'Bag Size', 5)                  ##- Pit
shield = kit.Equipment('Iron Shield', text.equipment_shield, 'Max Health', 50)                      ##- Armory
belt = kit.Equipment('Belt of Skill', text.equipment_belt, 'Dexterity', 3, 'Human')                 ##- Barracks
sash = kit.Equipment('Fur Sash', text.equipment_sash, 'Constitution', 3, 'Gnome')                   ##- Library 
bones = kit.Equipment('Crown of Bone', text.equipment_bones, 'Experience', .2, 'Orc')               ##- Cliffs
light = kit.Equipment('Crown of Light', text.equipment_light, 'Experience', .2, 'Elf')              ##- Cliffs
red_pendant = kit.Equipment('Red Pendant', text.equipment_pendant, 'Charisma', 3, 'Elf')            ##- Portal
fire = kit.Equipment('Crown of Fire', text.equipment_fire, 'Experience', .2, 'Tiefling')            ##- Cliffs
gloves = kit.Equipment('Expert\'s Gloves', text.equipment_gloves, 'Strength', 3, 'Tiefling')        ##- Dungeon
iron_crown = kit.Equipment('Iron Crown', text.equipment_iron, 'Experience', .2, 'Human')            ##- Cliffs
green_crown = kit.Equipment('Green Crown', text.equipment_green, 'Experience', .2, 'Gnome')         ##- Cliffs
gauntlet = kit.Equipment('Gauntlet of Burden', text.equipment_gauntlet, 'Intelligence', 3, 'Orc')   ##- Lava
helm = kit.Equipment('Helm of Horrors', text.equipment_helm, 'Visage of Horror', 5)                 ##- Srow
orb = kit.Equipment('Orb of Thesselhydra', text.equipment_orb, 'Spirit of Thesselhydra', 2)         ##- Srow
cross = kit.Equipment('Holy Tome', text.equipment_tome, 'Piety', 1)                                 ##- Dungeon
                                                                                                    ##
## Player #####################################################################>-------------------<##
start = time.time()                                                                                 ##                                                                                                
hero = create.char_create()                                                                         ## 
hero.base_weapon = fists                                                                            ##
hero.weapon = fists                                                                                 ##
kit.linebreak()                                                                                     ##
print(hero)                                                                                         ##
kit.linebreak()                                                                                     ##
print(text.prologue)                                                                                ##
                                                                                                    ##
begginer_weapons = {'Warrior': shortsword,                                                          ## 
                    'Spy': dagger,                                                                  ##
                    'Sorcerer': staff,                                                              ##
                    'Brute': club,                                                                  ##
                    'Wizard': dagger}                                                               ##
                                                                                                    ##
###############################################################################\                   /##
################################################################################\                 /##/
####################################################################################################/
####################################################################################################\
## THE ALTAR ###################################################################/                 \##\
###############################################################################/                   \##
class Altar():
    
    here = 'altar room'
    door1 = plot.altar_door1  
    door2 = plot.altar_door2 
    transitions = {1: door1,
                   2: door2} 
    
    wall1 = plot.altar_wall 
    wall2= rn.choice(text.wall_ornaments) 
    investigation = {4: kit.text_wrapper(text.altar_altar, wrap),
                     5: kit.text_wrapper(text.altar_roof, wrap)}
    
    key = False
    
    spell = "Witch Bolt 0"
    
    vials = plot.ritual.vials
    dish1 = plot.ritual.dish1
    dish2 = plot.ritual.dish2
    
    weapon_available = begginer_weapons[hero.role]
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: 'Investigate the vials (INT)',
               4: 'Investiagte the altar',
               5: 'Investigate the roof',
               6: 'Pick up the {}'.format(weapon_available.name)}     
        
    ## ENTER #############################################################################################
    def enter(self, protag):
        if protag.role in mages:
            self.options[7] = 'Learn Witch Bolt'
                
        while True:
            if plot.victory == True:
                desc = text.altar_ritual.format(plot.bbeg.name, plot.bbeg.title)
                if self.vials in protag.bag:
                    self.options[8] = 'Perform Ritual'
            else:
                if self.weapon_available != False:
                    w = text.altar_weapon.format(self.weapon_available.name)
                else:
                    w = ''
                
                desc = text.altar_desc.format(self.door1.desc, self.door2.desc, self.wall1, self.wall2, w)
            
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 3:
                if kit.challenge(protag, 'Intelligence', 18):
                    print(kit.text_wrapper(text.altar_vials.format(self.vials, self.dish1, self.dish2), wrap))
                    if choice == 3:
                        yn = kit.intcheck("1 = Add All to Bag, 2 = No Thanks: ")
                        if yn == 1:
                            del self.options[3]
                            del self.challenges[3]
                            kit.inventory(protag, 'add', self.vials)
                            kit.inventory(protag, 'add', self.dish1)
                            kit.inventory(protag, 'add', self.dish2)
                else:
                    print(kit.text_wrapper(text.altar_stupid, wrap))
            
            elif choice in self.investigation.keys():
                print(self.investigation[choice])
                if choice == 5 and self.key == False:
                    yn = kit.intcheck('Try to grab the key (DEX)?\n1 = Yes, 2 = No: ')
                    if yn == 1 and kit.challenge(protag, 'Dexterity', 22):
                        print('You leap up and grab the key!')
                        kit.inventory(protag, 'add', 'key')
                        self.key = True
                    elif yn == 1 and not kit.challenge(protag, 'Dexterity', 22):
                        print('You try to grab the key but can\'t jump high enough')
                
            elif choice == 6:
                self.weapon_available = protag.weapon_swap(self.weapon_available)
                kit.weapon_fix(self.weapon_available, self.options, 6)
            
            elif choice == 7:
                protag.learn_spell(self.spell)
                
            elif choice == 8:
                evil = plot.ritual.perform_ritual(protag)
                if evil:
                    print(kit.text_wrapper(plot.altar_complete, wrap))
                    protag.imortality = True
                    return 'finished'
                else:
                    print('Nothing Happens')
            
            else:
                kit.handle_it(protag, choice)     

###############################################################################
## THE ANTECHAMBER ############################################################
###############################################################################                   
class Antechamber():
    
    weapon_available = broadsword
    
    here = 'antechamber'
    door1 = plot.foyer_door1
    door2 = plot.foyer_door2 
    transitions = {1: door1,
                  2: door2}
    
    gate1 = plot.foyer_gate1
    gate2 = plot.foyer_gate2
    gates = {3: gate1,
             4: gate2}
    
    items = {amulet.name: amulet}
    plot.items_populate(items, food = 4, potions = 2)
    
    reading = {8: kit.Scroll(text.foyer_elvish, wrap, language = 'Elvish'),
               9: kit.Scroll(text.foyer_orcish, wrap, language = 'Orcish'),
               10: kit.Scroll(text.foyer_gnomish, wrap, language = 'Gnomish'),
               11: kit.Scroll(text.foyer_infernal, wrap, language = 'Infernal')}
    
    bens = {8: ('Elf', 'Strength'),
            9: ('Orc', 'Charisma'),
            10: ('Gnome', 'Intelligence'),
            11: ('Tiefling', 'Constitution')}
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: text.door_option.format(gate1.short),
               4: text.door_option.format(gate2.short),
               5: 'Try to get the sword',
               6: 'Pick up items',
               7: 'Talk to the Gatekeeper',
               8: 'Read the Elegant Scroll',
               9: 'Read the Stone Tablet',
               10: 'Read the Wood Carving',
               11: 'Read the Ornate Black Tome'}
    
    convo_challenge= {8: 23}
    
    convo_ends = {10: 'heal'}
    
    ## ENTER ##################################################################
    def enter(self, protag):
        if protag.role in mages:
            self.options[12] = 'Learn Payday 4'
    
        while True:
            desc = text.foyer_desc.format(self.door1.desc, self.door2.desc, self.gate1.desc, self.gate2.desc)
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.gates.keys():
                if 'GATE KEY' in protag.bag:
                    print(kit.text_wrapper(text.foyer_gate_unlock, wrap))
                    self.transitions[choice] = self.gates[choice]
                    protag.bag.remove('GATE KEY')
                    del self.gates[choice]
                else:
                    print(kit.text_wrapper(text.foyer_gate_lock, wrap))
                    
            elif choice == 5 and protag.role != 'Warrior':
                print('Only a true warrior can even try to wield that sword')
            
            elif choice == 5 and protag.role == "Warrior":
                print(kit.text_wrapper(text.foyer_sword, wrap))
                yn = kit.intcheck('Pull the sword?\n1 = Yes, 2 = No: ')
                
                if yn == 1 and kit.challenge(protag, "Strength", 25):
                    print(kit.text_wrapper(text.foyer_s_pass, wrap))
                    self.weapon_available = protag.weapon_swap(self.weapon_available)
                    del self.options[5]
                    if self.weapon_available != False:                                                                         #| 
                        self.options[13] = 'Pick up the {}'.format(self.weapon_available.name) 
                
                elif yn == 1 and not kit.challenge(protag, "Strength", 25):
                    print(kit.text_wrapper(text.foyer_s_fail, wrap))
            
            elif choice == 6:
                kit.item_pickup(protag, self.items, self.options, 6)
                
            elif choice == 7:
                gatekeeper = kit.conversation(text.foyer_convo_you, text.foyer_convo_her, protag.charisma, self.convo_challenge, self.convo_ends)
                if gatekeeper == 'heal':
                    print("She lifts her hands and you feel a surge of healing energy engulf you")
                    protag.health = protag.max_health
                
            elif choice in self.reading.keys():
                self.reading[choice].read(protag)
                if self.bens[choice][0] == protag.race:
                    print("Your {} increases by 2!".format(self.bens[choice][1]))
                    protag.score_modify(self.bens[choice][1], 2)
            
            elif choice == 12:
                protag.learn_spell("Pay Day 4")
                
            elif choice == 13:
                self.weapon_available = protag.weapon_swap(self.weapon_available)
                kit.weapon_fix(self.weapon_available, self.options, 13)
                
            else:
                kit.handle_it(protag, choice) 
    
###############################################################################
## THE ARMORY #################################################################
###############################################################################                    
class Armory():
    
    here = 'armory'
    door1 = text.door_broken_wall
    transitions = {1: door1}
    
    weapon1 = longsword
    weapon2 = warhammer
    weapon3 = shortsword
    weapon4 = dagger
    weapons = {2: weapon1,
               3: weapon2,
               4: weapon3,
               5: weapon4}
    
    items = {shield.name: shield,
             'Key': 'key'}
    
    options = {1: text.door_option.format(door1.short),
               2: 'Pick up the {}'.format(weapon1.name),
               3: 'Pick up the {}'.format(weapon2.name),
               4: 'Pick up the {}'.format(weapon3.name),
               5: 'Pick up the {}'.format(weapon4.name),
               6: 'Collect Items',
               7: 'Talk to the coward'}
    
    ## ENTER ##################################################################
    def enter(self, protag):
        while True:
            desc = text.armory_desc
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.weapons.keys():
                self.weapons[choice] = protag.weapon_swap(self.weapons[choice])
                kit.weapon_fix(self.weapons[choice], self.options, choice)
            
            elif choice == 6:
                kit.item_pickup(protag, self.items, self.options, 6)
            
            elif choice == 7:
                kit.conversation(text.armory_convo_you, text.armory_convo_him, plot.dungeon_quest , {8: 22})
            
            else:
                kit.handle_it(protag, choice) 
                
###############################################################################
## THE BARRACKS ###############################################################
###############################################################################                    
class Barracks():
    
    chess_foes = []
    chess_loss = False
    
    here = 'barracks'
    door1 = plot.barracks_door1
    door2 = plot.barracks_door2
    transitions = {1: door1,
                   2: door2}
    
    items = {belt.name: belt}
    plot.items_populate(items, food = 0, potions = 2)
    
    game_victory = False
    investigation = {5: "It's a candle.",
                     6: kit.text_wrapper(text.barracks_game_approach, wrap)}
    
    reading = {4: kit.Scroll(plot.barracks_note, wrap, language = 'Gnomish'),
               7: kit.Scroll(plot.barracks_book1, wrap),
               8: kit.Scroll(plot.barracks_book2, wrap)}
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: 'Pick up the items',
               4: 'Read the note',
               5: 'Inspect the candle',
               6: 'Inspect the Game',
               7: 'Read the small book',
               8: 'Read the leather bound book'}
    
    desc = text.barracks_desc.format(door1.desc, door2.desc)
    
    ## ENTER ##################################################################
    def enter(self, protag):        
        while True:
            if self.chess_loss == True and self.chess_foes != False:
                chess_continue = kit.run_encounter(text.encounter_cont, protag, [2, 1], self.chess_foes, self.transitions, text.barracks_win, ['Snarl Demon', 'Vampireling'])
                if chess_continue == True:
                    self.chess_foes = False
                elif chess_continue == False:
                    return 'death'
                else:
                    self.chess_foes = chess_continue[1]
                    fleeing_door = chess_continue[0]
                    return fleeing_door.pass_through(protag, self.here)
            
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, self.desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 3:
                kit.item_pickup(protag, self.items, self.options, 3)
            
            elif choice in self.investigation.keys():
                print(self.investigation[choice])
                if choice == 6:
                    print('Do you want to play?')
                    yn = kit.intcheck("1 = Yes, 2 = No way that's crazy: ")
                    if yn == 1:
                        print("You approach the board and sit down to play white (lowercase)")
                        chess_game = mini.play_chess(mini.chessboard, mini.whites, mini.blacks, 10)
                        if chess_game == 0:
                            print("A heavy bag THUNKS down on the center table in recogntion of your victory!")
                            self.options[9] = 'Pick up the bag'                            
                        elif chess_game == 1:
                            print(kit.text_wrapper(text.barracks_game_lose, wrap))
                            self.chess_loss = True
                        else:
                            print(kit.text_wrapper(text.barracks_game_timeout, wrap))
                            self.chess_loss = True
                        
                        del self.options[6]
                                                                    
            elif choice in self.reading.keys():
                self.reading[choice].read(protag)
            
            elif choice == 9:
                print(kit.text_wrapper(text.baracks_gold, wrap))
                protag.collect_gold(200, self.options, 9)
            
            else:
                kit.handle_it(protag, choice) 

###############################################################################
## THE CATACOMBS ##############################################################
###############################################################################                    
class Catacombs():
    
    coffin_foes = []
    ghouls = []
    
    
    weapon_available = cutlass
    
    bonfire_lit = False
    
    here = 'catacombs'
    door1 = plot.catacombs_door1
    door2 = plot.catacombs_door2
    door3 = plot.catacombs_door3
    transitions = {1: door1,
                   2: door2,
                   3: door3}
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: text.door_option.format(door3.short),
               4: 'Open a Stone Sarcophagus',
               5: 'Open a Stone Sarcophagus',
               6: 'Open a Stone Sarcophagus',
               7: 'Open a Stone Sarcophagus'}
    
    to_open = kit.avoid_duplicates(4, list(range(4, 8)))
    opened = []
    
    desc = text.catacombs_desc.format(door1.desc, door2.desc, door3.desc)
    
    ## ENTER ##################################################################
    def enter(self, protag):
        while True:
            if len(self.opened) == 4 and self.bonfire_lit == False:
                bonfire_fight = kit.run_encounter(text.catacombs_ghoul_encounter, protag, [2], self.ghouls, self.transitions, text.catacombs_ghoul_victory, ['Ghoul'])
                if bonfire_fight == True:
                    self.bonfire_lit = True
                    self.options[10] = 'Approach the lit Bonfire'
                elif bonfire_fight == False:
                    return 'death'
                else:
                    self.ghouls = bonfire_fight[1]
                    fleeing_door = bonfire_fight[0]
                    return fleeing_door.pass_through(protag, self.here)
            
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, self.desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.to_open and choice not in self.opened:
                if choice == self.to_open[0]:
                    print(kit.text_wrapper(text.catacombs_coffin1, wrap))
                    protag.collect_gold(75)
                    self.opened.append(choice)
                    
                elif choice == self.to_open[1]:
                    print('You push the lid open and hear movement......')
                    coffin_fight = kit.run_encounter(text.catacombs_coffin2, protag, [1], self.coffin_foes, self.transitions, text.encounter_victory, ['Skeleton'])
                    if coffin_fight == True:
                        self.opened.append(choice)
                    elif coffin_fight == False:
                        return 'death'
                    else:
                        self.coffin_foes = coffin_fight[1]
                        fleeing_door = coffin_fight[0]
                        return fleeing_door.pass_through(protag, self.here)
                    
                elif choice == self.to_open[2]:
                    coffin_text = text.catacombs_coffin3.format(self.weapon_available.name)
                    print(kit.text_wrapper(coffin_text, wrap))
                    self.weapon_available = protag.weapon_swap(self.weapon_available)
                    self.opened.append(choice)
                    if self.weapon_available != False:
                        self.options[8] = 'Pickup the {}'.format(self.weapon_available.name)
                        
                elif choice == self.to_open[3]:
                    print(kit.text_wrapper(text.catacombs_coffin4, wrap))
                    self.opened.append(choice)
                    if protag.role in mages:
                        protag.learn_spell(plot.catacombs_spell)
                        self.options[9] = 'Learn {}'.format(plot.catacombs_spell)
            
            elif choice in self.to_open and choice in self.opened:
                print(text.catacombs_opened)

            elif choice == 8:
                self.weapon_available = protag.weapon_swap(self.weapon_available)
                kit.weapon_fix(self.weapon_available, self.options, 8)
                
            elif choice == 9:
                protag.learn_spell(plot.catacombs_spell)
                
            elif choice == 10:
                print(kit.text_wrapper(text.catacombs_bonfire, wrap))
                if protag.gold >= 100:
                    print('Will you throw 100 Gold Peices into the fire?')
                    yn = kit.intcheck('1 = Yes, 2 = No thanks: ')
                    if yn == 1:
                        protag.gold -= 100
                        print('You toss 100 gold pieces into the fire, they instantly disintegrate')
                        protag.health = min(protag.max_health, protag.health + 25)
                        print('The bonfire heals you magically')
                        print('Health: {}'.format(protag.health))
                
                else:
                    print("You don't have enough gold to satisfy the bonfire")
            
            else:
                kit.handle_it(protag, choice) 
                
###############################################################################
## THE CLIFF ##################################################################
###############################################################################                    
class Cliff():
    
    here = 'cliff'
    
    door1 = plot.cliff_door1
    door2 = plot.cliff_door2
    door3 = plot.cliff_door3
    transitions = {0: door1,
                   1: door2,
                   2: door3}
     
    options = {0: {1: text.door_option.format(door1.short),
                   2: 'Walk out onto the cliff'},
               1: {1: text.door_option.format(door2.short),
                   2: 'Walk out onto the cliff'},
               2: {1: text.door_option.format(door3.short),
                   2: 'Walk out onto the cliff'},
               3: {2: 'Walk out onto the cliff',
                   3: 'Read the Infernal Scroll',
                   4: 'Read the silver book',
                   5: 'Read the tattered notebook',
                   6: 'Collect the gold',
                   7: 'Peer off the edge',
                   8: 'Read the notes on the sphere'}}
    
    reading = {3: kit.Scroll(text.cliffs_infernal, wrap, language = 'Infernal'),
               4: kit.Scroll(plot.cliff_lore1, wrap),
               5: kit.Scroll(plot.cliff_lore2, wrap),
               8: kit.Scroll(plot.cliff_crown, wrap)}
    
    crowns = {'Human': iron_crown,
              'Gnome': green_crown,
              'Elf': light,
              'Orc': bones,
              'Tiefling': fire}
    
    zone = False
    
    starts = {'dungeon': 0,
              'library': 1,
              'portal': 2,
              'table': 3,
              'cliff': 0}
    
    ret_coords = [[4, 0], [0, 4], [4, 8], [8, 4]]
    
    cliff = mini.Board(9)
    
    ## ENTER ##################################################################
    def enter(self, protag):
        self.zone = self.starts[protag.proom]
        
        while True:
            s_row = self.ret_coords[self.zone][0]
            s_col = self.ret_coords[self.zone][1]
            choices = self.options[self.zone]
            desc = text.cliffs_desc.format(self.door1.desc, self.door2.desc, self.door3.desc)
            kit.door_check(protag, self.transitions)
            choice = kit.consider(choices, desc)
            
            if choice == 1:
                return self.transitions[self.zone].pass_through(protag, self.here)
            
            elif choice == 2:
                walk = mini.floor_puzzle(protag, s_row, s_col, self.cliff, 8, self.ret_coords)
                if walk in [0, 1, 2, 3]:
                    self.zone = walk
                elif walk == 'death':
                    return 'death'
            
            elif choice in self.reading.keys() and self.zone == 3:
                self.reading[choice].read(protag)
                if choice == 8 and plot.tower_item in protag.bag:
                    print("\nHold the {} out towards the sphere?".format(plot.tower_item))
                    yn = kit.intcheck("1 = Yes, 2 = No: ")
                    if yn == 1:
                        protag.bag.remove(plot.tower_item)
                        print(kit.text_wrapper(text.cliffs_accept.format(plot.tower_item), wrap))
                        choices[9] = 'Pick up the {}'.format(self.crowns[protag.race].name)
                                    
            elif choice == 6 and self.zone == 3:
                protag.collect_gold(125, choices, 6)
            
            elif choice == 7 and self.zone == 3:
                print(kit.text_wrapper(text.cliffs_peer, wrap))
                
            elif choice == 9:
                kit.single_item_pickup(protag, self.crowns[protag.race], choices, 9)
            
            else:
                kit.handle_it(protag, choice) 
                
###############################################################################
## THE DUNGEON ################################################################
###############################################################################                    
class Dungeon():
    
    door_mimic = [plot.dungeon_mimic]
    poly_dragon = []
    
    here = 'dungeon'
    door1 = plot.dungeon_door1
    door2 = plot.dungeon_door2
    transitions = {1: door1,
                   2: door2}
    
    weapon_available = dread_dagger
    weapons = {3: weapon_available}
    
    potion1 = plot.potion_gen()
    potion2 = plot.potion_gen()
    potion3 = plot.potion_gen()
    
    for_sale = [potion1, potion2, potion3, 'key', gloves, cross, 'Carved Stone Ball']
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: 'Pick up the {}'.format(weapon_available.name),
               4: 'Open cell 1', 
               5: 'Open cell 2', 
               6: 'Open cell 3',
               7: 'Open cell 4', 
               8: 'Open cell 5', 
               9: 'Open cell 6'
               }
    
    convo_rewards = {31: 'key',
                     13: 'quest'}
    convo_blocks = {30: 23,
                    19: 15}
    
    keys = 4
    cells = {4: False, 5: False, 6: False, 7: False, 8: False, 9: False}
    
    ## Shop ###################################################################
    def shop(self, shopper):
        p_names = []
        prices = []
        for product in self.for_sale:
            if type(product) == str:
                price = 150 - (5 * shopper.rmod)
                print('A {} for {}gp'.format(product, price))
                p_names.append(product.lower())
                prices.append(price)
            else:
                price = max(5, (product.price * 2) - (5 * shopper.rmod))
                print('{} for {}gp'.format(product.name, price))
                p_names.append(product.name.lower())
                prices.append(price)
                
        while True:
            picked = input('\n"What would you like?"\n>> ').lower()
            if picked not in p_names and picked != 'nothing':
                print('"I\'m sorry, we dont\'t sell that here"')
                print("*** type 'nothing' to leave")
            elif picked == 'nothing':
                print('Come again Soon!')
                break
            else:
                spot = p_names.index(picked)
                you_want = self.for_sale[spot]
                sale_price = prices[spot]
                    
                if shopper.gold >= sale_price and shopper.bag_check:
                    shopper.gold -= sale_price
                    kit.inventory(shopper, 'add', you_want)
                    del self.for_sale[spot]
                    break
                elif shopper.gold < sale_price:
                    print('"I\'m sorry, you can\'t afford that one"')
                elif not shopper.bag_check:
                    print('That item is too heavy for you right now!')
                else:
                    print('Something went wrong')
                    break
                    
    ###########################################################################
    def sell(self, seller):
        selling = [crap for crap in seller.bag if type(crap) != str]
        s_names = [crap.name for crap in selling]
        print(*s_names, sep = '\n')
        print('What would you like to sell?')
        while True:
            sold = input('>> ')
            if sold not in s_names and sold != 'nothing':
                print("You can't sell that!")
                print("*** type 'nothing' to leave")
            elif sold == 'nothing':
                print('"Come again soon!"')
                break
            else:
                item_selling = selling[s_names.index(sold)]
                retail_price = item_selling.price
                price_mod = (retail_price / 20) * seller.rmod
                sale_price = int(retail_price + price_mod)
                print('This will sell for {}gp'.format(sale_price))
                yn = kit.intcheck("Is that ok?\n1 = Yes, 2 = No: ")
                if yn == 1:
                    seller.gold += sale_price
                    seller.bag.remove(item_selling)
                    self.for_sale.append(item_selling)
                    break
                else:
                    print('"Come again soon!"')
                    break
            
    
    ## ENTER ##################################################################
    def enter(self, protag):            
        while True:
            desc = text.dugeon_desc.format(self.door1.desc, self.door2.desc)
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.weapons.keys():
                self.weapons[choice] = protag.weapon_swap(self.weapons[choice])
                kit.weapon_fix(self.weapons[choice], self.options, choice)
            
            elif choice in self.cells.keys() and not self.cells[choice] and self.keys > 0:
                print('You unlocked Cell {}'.format(choice - 3))
                self.options[choice] = 'Investigate Cell {}'.format(choice - 3)
                self.cells[choice] = True
                self.keys -= 1
                if self.keys == 0:
                    for i in [key for key in self.cells if self.cells[key] == False]:
                        del self.options[i]
            
            elif choice == 4 and self.cells[4]:
                print(kit.text_wrapper(text.dungeon_celll1, wrap))
                yn = kit.intcheck("Buying or Selling?\n1 = Buying, 2 = Selling: ")
                if yn == 1:
                    self.shop(protag)
                elif yn == 2:
                    self.sell(protag)
                else:
                    print('"Come again soon!"')
                
            elif choice == 5 and self.cells[5]:
                print(kit.text_wrapper(text.dungeon_celll2, wrap))
                yn = kit.intcheck("Give up all your gold?\n1 = Yes, 2 = NO!: ")
                if yn == 1:
                    print(kit.text_wrapper(text.dungeon_exp_accept, wrap))
                    amt = protag.gold
                    protag.gold -= amt
                    protag.exp += amt
                    
            elif choice == 6 and self.cells[6]:
                print(kit.text_wrapper(text.dungeon_celll3, wrap))
                prisoner = kit.conversation(text.dungeon_convo_you, text.dungeon_convo_him, protag.charisma, self.convo_blocks, self.convo_rewards)
                if prisoner == 'key':
                    kit.inventory(protag, 'add', 'key')
                elif prisoner == 'quest':
                    plot.dungeon_quest = 1
            
            elif choice == 7 and self.cells[7]:
                print(kit.text_wrapper(text.dungeon_celll4, wrap))
                poly_fight = kit.run_encounter(text.dungeon_celll4, protag, [1], self.poly_dragon, self.transitions, text.dungeon_dragon_win, ['Young Dragon'])
                if poly_fight == True:
                    self.poly_dragon = False
                    del self.options[7]
                elif poly_fight == False:
                    return 'death'
                else:
                    self.poly_dragon = poly_fight[1]
                    fleeing_door = poly_fight[0]
                    return fleeing_door.pass_through(protag, self.here)
            
            elif choice == 8 and self.cells[8]:
                print(kit.text_wrapper(text.dungeon_celll5, wrap))
                yn = kit.intcheck("Collect the gold? (CON)\n1 = Yeah, 2 = No I don't like gold: ")
                if yn == 1 and kit.challenge(protag, 'Constitution', 25):
                    print(kit.text_wrapper(text.dungeon_gold_pass, wrap))
                    protag.collect_gold(200, self.options, 8)
                    
                elif yn == 1 and not kit.challenge(protag, 'Constitution', 25):
                    print(kit.text_wrapper(text.dungeon_gold_fail, wrap))
                
            elif choice == 9 and self.cells[9]:
                print(kit.text_wrapper(text.dungeon_celll6, wrap))
                input("When is a door not a door?\n>> ")
                door_fight = kit.run_encounter(text.dungeon_mimic_attack, protag, [], self.door_mimic, self.transitions, text.dungeon_mimic_win)
                if door_fight == True:
                    self.door_mimic = False
                    del self.options[9]
                elif door_fight == False:
                    return 'death'
                else:
                    self.door_mimic = door_fight[1]
                    fleeing_door = door_fight[0]
                    return fleeing_door.pass_through(protag, self.here)
            
            else:
                kit.handle_it(protag, choice) 
    
###############################################################################
## THE EXXIT ##################################################################
###############################################################################                    
class Exxit():
    
    foes = [plot.bbeg]
    
    here = 'exxit'
    door1 = text.door_end
    transitions = {1: door1}
    
    options = {1: text.door_option.format(door1.short)}
    
    fight = False
    
    ## ENTER ##################################################################
    def enter(self, protag):
        if not self.fight:
            self.options[2] = 'Talk to {}'.format(plot.bbeg.name)
        else:
            self.options[2] = 'Fight {}'.format(plot.bbeg.name)
        
        while True:
            if plot.victory == True:
                self.options[3] = 'Go Home'
            
            desc = text.exxit_desc.format(plot.bbeg.desc, plot.bbeg.name, plot.bbeg.title)
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 2:
                if self.fight != True:
                    talk = kit.conversation(plot.exxit_you, plot.exxit_him, 0, {}, {26: 'fight'})
                    if talk == 'fight':
                        self.fight = True
                        final_fight = kit.run_encounter(plot.exxit_fight, protag, [], self.foes, self.transitions, plot.exxit_win)
                        if final_fight == True:
                            plot.victory = True
                            del self.options[2]
                        elif final_fight == False:
                            return 'death'
                        else:
                            self.foes = final_fight[1]
                            fleeing_door = final_fight[0]
                            return fleeing_door.pass_through(protag, self.here)
                else:
                    final_fight = kit.run_encounter(plot.exxit_fight, protag, [], self.foes, self.transitions, plot.exxit_win)
                    if final_fight == True:
                        plot.victory = True
                        del self.options[2]
                    elif final_fight == False:
                        return 'death'
                    else:
                        self.foes = final_fight[1]
                        fleeing_door = final_fight[0]
                        return fleeing_door.pass_through(protag, self.here)
           
            elif choice == 3:
                return 'finished'
            
            else:
                kit.handle_it(protag, choice) 
    
###############################################################################
## THE FOUNTAINS ##############################################################
###############################################################################                    
class Fountains():   
    
    here = 'fountains'    
    door1 = plot.fountain_door1
    door2 = plot.fountain_door2
    door3 = plot.fountain_door3
    door4 = text.door_underwater
    transitions = {1: door1,
                   2: door2,
                   3: door3}
    
    all_faces = kit.avoid_duplicates(3, text.fountain_faces)
    face1 = all_faces[0]
    face2 = all_faces[1]
    face3 = all_faces[2]
    investiagtion = {4: kit.text_wrapper(text.fountain_faces_inv.format(face1, face2, face3), wrap),
                     5: kit.text_wrapper(text.fountain_inv, wrap)}
    
    faces = {7: kit.Scroll(text.fountain_infernal, wrap, language = 'Infernal'),
             10: kit.Scroll(text.fountain_murmur, wrap)}   
    
    desc = text.fountain_desc.format(door1.desc, door2.desc, door3.desc)
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: text.door_option.format(door3.short),
               4: 'Investigate the faces',
               5: 'Investigate the fountain'}
    
    challenge = 25
    
    convo_ends = {28: 'reduce'}
    convo_challenge = {27: 22,
                       18: 18}
    
    ## ENTER ##################################################################
    def enter(self, protag): 
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, self.desc)
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.investiagtion.keys():
                print(self.investiagtion[choice])
                if choice == 5:
                    self.options[6] = 'Swim through the tunnel (CON)'
                elif choice == 4:
                    self.options[7] = 'Listen to the gibbering face'
                    self.options[8] = 'Listen to the whispering face'
                    self.options[10] = 'Listen to the murmuring face'
                    if protag.role in mages:
                        self.options[9] = 'Approach the glowing face'
            
            elif choice == 6:
                if kit.challenge(protag, 'Constitution', self.challenge):
                    return self.door4.pass_through(protag, self.here)
                else:
                    print("You try to swim through the tunnel but can't hold your breath long enough")
            
            elif choice in self.faces.keys():
                self.faces[choice].read(protag)
                
            elif choice == 9:
                print(kit.text_wrapper(text.fountain_glowing, wrap))
                protag.learn_spell(plot.fountain_spell)
                
            elif choice == 8:
                print(kit.text_wrapper(text.fountain_whisper, wrap))
                convo = kit.conversation(text.fountain_convo_you, text.fountain_convo_face, protag.charisma, self.convo_challenge, self.convo_ends)
                if convo == 'reduce':
                    self.challenge = 18
            
            else:
                kit.handle_it(protag, choice) 

###############################################################################
## THE GARDEN #################################################################
###############################################################################                    
class Garden():
    
    here = 'garden'
    door1 = plot.garden_door1
    door2 = plot.garden_door2
    door3 = text.door_end
    transitions = {1: door1,
                   2: door2,
                   3: door3}
    
    items = {}
    plot.items_populate(items, food = 15, potions = 0)
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: text.door_option.format(door3.short),
               4: 'Pick up some food'}
    
    ## ENTER ##################################################################
    def enter(self, protag):
        while True:
            desc = text.garden_desc.format(self.door1.desc, self.door2.desc, self.door3.desc)
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 4:
                kit.item_pickup(protag, self.items, self.options, 4)
            
            else:
                kit.handle_it(protag, choice) 
                
###############################################################################
## THE ICE ####################################################################
###############################################################################                    
class Ice():

    here = 'ice'
    door1 = plot.ice_door1
    door2 = plot.ice_door2
    door3 = plot.ice_door3
    transitions = {1: door1,
                   2: door2,
                   3: door3}
    
    books = {1: kit.Scroll(plot.ice_book1, wrap),
             2: kit.Scroll(plot.ice_book2, wrap),
             3: kit.Scroll(plot.ice_book3, wrap)}
    
    scrolls = {1: kit.Scroll(text.ice_scroll1, wrap, o_level = 20),
               2: kit.Scroll(text.ice_scroll2, wrap, o_level = 20)}
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: text.door_option.format(door3.short),
               4: 'Approach the Bookshelf',
               5: 'Approach the Table',
               6: 'Inspect that Chunk of Ice',
               7: 'Inspect the hole in the floor'}
    
    whacked = False
    
    ## ENTER ##################################################################
    def enter(self, protag):
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, text.ice_desc)
            saving_throw = rn.randrange(1, 21) + protag.dmod
            if saving_throw < 12 and choice not in ['stats', 'bag']:
                print('\nYou slip on the ice and go sliding out of control!\n')
                choice = rn.choice(list(self.options.keys()))
                
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 4:
                while True:
                    kit.top_screen(text.ice_bookshelf)
                    reading = kit.intcheck(text.ice_reading)
                    if reading in self.books:
                        self.books[reading].read(protag)
                    else:
                        break
            
            elif choice == 5: 
                while True:
                    kit.top_screen(text.ice_table)
                    reading = kit.intcheck(text.ice_scrolls)
                    if reading in self.scrolls:
                        self.scrolls[reading].read(protag)
                    else:
                        break
    
            elif choice == 6:
                print(kit.text_wrapper(text.ice_chunk, wrap))
                fire_spells = [s for s in protag.spells if 'Fire' in s]
                if self.whacked and len(fire_spells) > 0:
                    cast = kit.intcheck("Cast {}?\n1 = Yes, 2 = No: ".format(fire_spells[0]))
                    if cast == 1:
                        print(kit.text_wrapper(text.ice_chunk_fireball.format(fire_spells[0]), wrap))
                        self.options[9] = 'Pick up the Bracers'
                        del self.options[6]
                elif self.whacked and 'Jar of Magical Fire' in protag.bag:
                    jar = kit.intcheck("Use your Jar of Magical Fire?\n1 = Ok, 2 = No: ")
                    if jar == 1:
                        print(kit.text_wrapper(text.ice_chunk_magic_fire, wrap))
                        protag.bag.remove("Jar of Magical Fire")
                        self.options[9] = 'Pick up the Bracers'
                        del self.options[6]
                else:
                    hit = kit.intcheck("Whack the ice?\n1 = DUH, 2 = Nah: ")
                    if hit == 1:
                        print(kit.text_wrapper(text.ice_chunk_attack.format(protag.weapon.name), wrap))
                        self.whacked = True
            
            elif choice == 7:
                print(kit.text_wrapper(text.ice_hole, wrap))
                dive = kit.intcheck("Dive for the mask? (CON)\n1 = Yeah let's try, 2 = Not now: ")
                if dive == 1 and kit.challenge(protag, 'Constitution', 20):
                    print(kit.text_wrapper(text.ice_hole_pass, wrap))
                    self.options[8] = 'Pick up the mask'
                    del self.options[7]
                elif dive == 1 and not kit.challenge(protag, 'Constitution', 20):
                    print(kit.text_wrapper(text.ice_hole_fail, wrap))
                    
            elif choice == 8:
                kit.single_item_pickup(protag, mask, self.options, 8)

            elif choice == 9:
                kit.single_item_pickup(protag, bracers, self.options, 9)
                    
            else:
                kit.handle_it(protag, choice) 
    
###############################################################################
## THE KENNEL #################################################################
###############################################################################                    
class Kennel():
    
    wolves_lever = []
    drake_lever = []
    
    here = 'kennel'
    door1 = plot.kennel_door1
    door2 = plot.kennel_door2
    door3 = plot.kennel_door3
    transitions = {1: door1,
                   2: door2,
                   3: door3}
    
    levers = kit.avoid_duplicates(7, list(range(1, 8)))
    to_pull = [4, 5, 6]
    pull_order = kit.avoid_duplicates(3, to_pull)
    pulled = []
    
    lever_order = []                               # All my list comprehensions
    for i in pull_order:                           # threw errors in this part
        l = to_pull.index(i) + 1                   # so I'm stuck using these
        lever_order.append(l)                      # ugly loops. Sorry
    
    worded = kit.wordify(lever_order)
    
    chandelier = False
    scroll = plot.kennel_scroll.format(*worded)
    investigation = {7: kit.text_wrapper(scroll, wrap),
                     8: kit.text_wrapper(text.kennel_cage_challenge, wrap)}
    
    items = {}
    plot.items_populate(items, food = 0, potions = 3)
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: text.door_option.format(door3.short),
               4: 'Pull the first lever',
               5: 'Pull the second lever',
               6: 'Pull the third lever',
               7: 'Read the parchment in the first cage',
               8: 'Investigate the second cage'}
    
    desc = text.kennel_desc.format(door1.desc, door2.desc, door3.desc)        
    
    ## ENTER ##################################################################
    def enter(self, protag):        
        while True:    
            if self.pulled == self.pull_order and self.chandelier == False:
                self.options[11] = 'Collect the vial'
                print('\n' + kit.text_wrapper(text.kennel_chandelier, wrap))
                self.chandelier = True
            
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, self.desc)
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.to_pull and choice not in self.pulled:
                if self.levers[choice] == 1:
                    print(kit.text_wrapper(text.kennel_lever1, wrap))
                    lever1_fight = kit.run_encounter(text.kennel_wolves, protag, [3], self.wolves_lever, self.transitions, text.kennel_wolf_victory, ['Wolf'])
                    if lever1_fight == True:
                        self.pulled.append(choice)
                    elif lever1_fight == False:
                        return 'death'
                    else:
                        self.wolves_lever = lever1_fight[1]
                        fleeing_door = lever1_fight[0]
                        return fleeing_door.pass_through(protag, self.here)
                
                elif self.levers[choice] == 2:
                    print(kit.text_wrapper(text.kennel_lever2, wrap))
                    lever2_fight = kit.run_encounter(text.kennel_drake, protag, [1], self.drake_lever, self.transitions, text.kennel_drake_victory, ['Drake'])
                    if lever2_fight == True:
                        self.pulled.append(choice)
                    elif lever2_fight == False:
                        return 'death'
                    else:
                        self.drake_lever = lever2_fight[1]
                        fleeing_door = lever2_fight[0]
                        return fleeing_door.pass_through(protag, self.here)
                
                elif self.levers[choice] == 3:
                    print(kit.text_wrapper(text.kennel_lever3, wrap))
                    self.pulled.append(choice)
                    self.options[9] = 'Pickup Potions'
                
                elif self.levers[choice] == 4:
                    print(kit.text_wrapper(text.kennel_lever4, wrap))
                    self.pulled.append(choice)
                    protag.collect_gold(35)
                
                elif self.levers[choice] == 5:
                    print(kit.text_wrapper(text.kennel_lever5, wrap))
                    self.pulled.append(choice)
                    self.door1.locked = True
                
                elif self.levers[choice] == 6:
                    print(kit.text_wrapper(text.kennel_lever6, wrap))
                    self.pulled.append(choice)
                    if kit.challenge(protag, 'Dexterity', 14):
                        print(kit.text_wrapper(text.kennel_dex_dodge, wrap))
                    else:
                        print(kit.text_wrapper(text.kennel_dex_fail, wrap))
                        protag.health -= 10
                        if protag.health < 0:
                            return 'death'
                        else:
                            print('Health: {}'.format(protag.health))
                
                elif self.levers[choice] == 7:
                    print(kit.text_wrapper(text.kennel_lever7, wrap))
                    self.pulled.append(choice)
                    if protag.role in mages:
                        self.options[10] = 'Learn {}'.format(plot.kennel_spell)
            
            elif choice in self.to_pull and choice in self.pulled:
                print(text.kennel_pulled)
                
            elif choice in self.investigation.keys():
                print(self.investigation[choice])
                if choice == 8 and protag.race == 'Gnome':
                    print(kit.text_wrapper(text.kennel_size_win, wrap))
                    protag.collect_gold(75)
                    del self.options[8]
                elif choice == 8 and protag.race != 'Gnome':
                    print(kit.text_wrapper(text.kennel_size_lose, wrap))
                
            elif choice == 9:
                kit.item_pickup(protag, self.items, self.options, 9)
            
            elif choice == 10:
                protag.learn_spell(plot.kennel_spell)
                
            elif choice == 11:
                master_potion = kit.Potion('Masterwork Potion', 'beatiful navy-blue liquid', 'All', 1, 'Enchanting')
                kit.single_item_pickup(protag, master_potion, self.options, 11)
            
            else:
                kit.handle_it(protag, choice) 

###############################################################################
## THE LAB ####################################################################
###############################################################################                    
class Lab():
    
    here = 'lab'
    door1 = text.door_statue
    transitions = {1: door1}
    
    master_potion = kit.Potion('Potion of Immaculate Wealth', 
                               'brilliantly beautiful gold liquid', 
                               'Gold', 
                               500, 
                               'Beautiful')
    items = {}
    plot.items_populate(items, food = 0, potions = 4)
    
    alchemy = ['mushrooms', 'twigs and vines', 'yellow berries', 'red goop',
               'apple slices', 'pummice stones', 'obsidian shards', 'crumpled parchment',
               'glass beads', 'blue paint', 'vinegar', 'silver peices', 'black beetles',
               'green slugs', 'grey moths', 'loamy soil', 'worms and grubs']   
    experiment = kit.avoid_duplicates(5, alchemy)
    experiment_instr = text.lab_experiment_scroll.format(experiment[0], 
                                                         experiment[1], 
                                                         rn.choice(alchemy), 
                                                         experiment[2], 
                                                         experiment[3], 
                                                         experiment[4])
    experiment_scroll = kit.Scroll(experiment_instr, wrap, o_level = 27)
    
    options = {1: text.door_option.format(door1.short),
               2: 'Pick up items',
               3: 'Pick up gold',
               4: 'Read the scroll',
               5: 'Read the heavy book'}
    
    desc = text.lab_desc
    
    ## Experiment #############################################################
    def lab_experiment(self):
        print(kit.text_wrapper(text.lab_run_experiment, wrap))
        for ingredient in self.alchemy:
            print(ingredient)
                
        print('\nPerform the experiment?')
        yn = kit.intcheck('1 = Yes, 2 = No Thanks: ')
        if yn == 1:
            attempt = []
            while len(attempt) < 5:
                while True:
                    adding = input("\nLet's add: ")
                    if adding in self.alchemy:
                        attempt.append(adding)
                        print('You throw all the {} into the bubling solution'.format(adding))
                        self.alchemy.remove(adding)
                        break
                    else:
                        print("You don't have that ingredient")
                    
            if attempt == self.experiment:
                print('SUCCESS!')
                self.options[8] = 'Pick up {}'.format(self.master_potion.name)
            else:
                print('Your attempt explodes in a fume of foul smelling smoke')    
    
    ## ENTER ##################################################################
    def enter(self, protag):                
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, self.desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 2:
                kit.item_pickup(protag, self.items, self.options, 2)
            
            elif choice == 3:
                protag.collect_gold(80, self.options, 3)
            
            elif choice == 4:
                self.experiment_scroll.read(protag)
                print('On the back you see a small not scribbled...')
                print("\n\n   {} moved \n      master potion \n    to kennel\n\n".format(plot.bbeg.name))
                self.options[6] = 'Try the experiment'
            
            elif choice == 5:
                print(kit.text_wrapper(plot.lab_book, wrap))
            
            elif choice == 6:
                self.lab_experiment()
            
            elif choice == 8:    
                kit.single_item_pickup(protag, self.master_potion, self.options, 8)
            
            else:
                kit.handle_it(protag, choice) 
                
###############################################################################
## THE LAVA ###################################################################
###############################################################################                    
class Lava():
    
    pixies = [plot.lava_pixie_fight]
    brood = []
    
    here = 'lava'
    door1 = plot.lava_door1
    door2 = plot.lava_door2
    door3 = plot.lava_door3
    door4 = text.door_wall_hole
    transitions = {1: door1,
                   2: door2,
                   3: door3}
    
    reading = {6: kit.Scroll(text.lava_findings, wrap),
               7: kit.Scroll(text.lava_scroll_diary, short_wrap, o_level = 25),
               8: kit.Scroll(text.lava_scroll_draconic, wrap, language = 'Draconic'),
               9: kit.Scroll(text.lava_scroll_golem, wrap)}
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: text.door_option.format(door3.short),
               4: 'Check out the table',
               5: 'Check out the golem'}
    
    desc = text.lava_desc.format(door1.desc, door2.desc, door3.desc)
    to_burn = ['pixie', 'eye', 'piranha', 'watch', 'lantern', 'comb', 'paintbrush', 'water goblet', 'ball of yarn']
    
    puzzle = 'nevermind'
    
    ## Burn ###################################################################
    def burn(self):
        print("What would you like to throw into the lava?")
        while True:
            burning = input('>> ').lower()
            if burning not in self.to_burn and burning != 'nevermind':
                print("You don't see that on the table")
                print("\n***Hint! for the pixie just type 'pixie'. 'eye' for the eye and 'piranha' for the pirhana")
                print("'nevermind' will let you exit")
            else:
                break
            
        if burning == 'comb':
            print(kit.text_wrapper(text.lava_pass, wrap))
            response = input('\n>> ').lower()
            if response == 'your name':
                print(kit.text_wrapper(text.lava_pass2, wrap))
                return 'open'
            else:
                print(kit.text_wrapper(text.lava_fail2, wrap))
                return 'swell'
        elif burning == 'eye':
            self.to_burn.remove('eye')
            print(kit.text_wrapper(text.lava_brood, wrap))
            return 'eye'
        elif burning == 'nevermind':
            return 'nevermind'
        else:
            self.to_burn.remove(burning)
            print(kit.text_wrapper(text.lava_fail, wrap))
            return 'nevermind'
            
    ## ENTER ##################################################################
    def enter(self, protag):
        self.door4.rooma = self.here
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, self.desc)
        
            if choice in self.transitions.keys():
                print("You climb the seeminly endless stairs to reach the door...")
                return self.transitions[choice].pass_through(protag, self.here)
        
            elif choice == 4:
                print(kit.text_wrapper(text.lava_table, wrap))
                self.options[6] = 'Read FINDINGS'
                self.options[7] = 'Read the burnt paper'
                self.options[8] = 'Read the Draconic Writing'
                self.options[9] = 'Read the crumpled scroll'
                if self.pixies != False:
                    self.options[10] = 'Free the Pixie'
            
                if self.puzzle == 'nevermind':
                    self.options[11] = 'Throw something in the lava'
            
            elif choice == 5:
                print(kit.text_wrapper(text.lava_golem, wrap))
                yn = kit.intcheck("Bang on the golem? (STR)\n1 = Hell yeah, 2 = No fuckin way: ")
                if yn == 1:
                    if kit.challenge(protag, 'Strength', 28):
                        print('The orcish gauntlet fell off!')
                        self.options[12] = 'Pick up the gauntlet'
                        del self.options[5]
                    else:
                        print("You bang it as hard as you can but it seems impervious to your assault")
        
            elif choice in self.reading.keys():
                self.reading[choice].read(protag)
            
            elif choice == 10:
                print(kit.text_wrapper(text.lava_pixie, wrap))
                self.to_burn.remove('pixie')
                del self.options[10]
            
                pixie_fight = kit.run_encounter(text.lava_pixie, protag, [], self.pixies, self.transitions, text.encounter_victory)
                if pixie_fight == True:
                    self.pixies = False
                elif pixie_fight == False:
                    return 'death'
                else:
                    self.pixies = pixie_fight[1]
                    fleeing_door = pixie_fight[0]
                    return fleeing_door.pass_through(protag, self.here)
        
            elif choice == 11 and self.puzzle == 'nevermind':
                self.puzzle = self.burn()
                if self.puzzle == 'eye':
                
                    brood_fight = kit.run_encounter(text.lava_brood, protag, [3, 1], self.brood, self.transitions, text.encounter_victory, ['Drakeling', 'Drake'])
                    if brood_fight == True:
                        self.brood = False
                        self.puzzle = 'nevermind'
                    elif brood_fight == False:
                        return 'death'
                    else:
                        self.brood = brood_fight[1]
                        fleeing_door = brood_fight[0]
                        return fleeing_door.pass_through(protag, self.here)
            
                elif self.puzzle == 'swell':
                    self.options[11] = 'Return and speak to the swell again'
           
                elif self.puzzle == 'open':
                    self.options[11] = text.door_option.format(self.door4.short)
                    self.transitions[11] = self.door4
        
            elif choice == 11 and self.puzzle == 'swell':
                print(kit.text_wrapper(text.lava_swell, wrap))
                response = input('\n>> ').lower()
                if response == 'your name':
                    print(kit.text_wrapper(text.lava_pass2, wrap))
                    self.puzzle = 'open'
                    self.options[11] = text.door_option.format(self.door4.short)
                    self.transitions[11] = self.door4
                else:
                    print(kit.text_wrapper(text.lava_fail2, wrap))
            
            elif choice == 12:
                kit.single_item_pickup(protag, gauntlet, self.options, 12)
            
            else:
                kit.handle_it(protag, choice) 

###############################################################################
## THE LIBRARY ################################################################
###############################################################################                    
class Library():
    
    here = 'library'
    door1 = plot.library_door1
    door2 = plot.library_door2
    door3 = plot.library_door3
    door4 = text.door_bookshelf
    transitions = {1: door1,
                   2: door3,
                   3: door2}
    
    floors = {'upit': 3,
              'antechamber': 2,
              'cliff': 1,
              'sanctum': 3,
              'library': 2}
    
    items = {}
    plot.items_populate(items, food = 0, potions = 2)

    floor = 1
    gg_place = {4: 'left', 5: 'right'}[plot.pit_gargoyle]
    
    reading = {
               1: {4: kit.Scroll(plot.library_lore1, wrap),
                   5: kit.Scroll(text.library_elvish, wrap, language = 'Elvish')},
               
               2: {4: kit.Scroll(plot.library_lore2, wrap),
                   5: kit.Scroll(plot.library_lore3, wrap),
                   6: kit.Scroll(plot.library_lore4, wrap),
                   9: kit.Scroll(plot.library_plot1, wrap),
                   10: kit.Scroll(plot.library_plot2, wrap, language = "Infernal"),
                   11: kit.Scroll(text.library_gargoyles.format(gg_place), wrap)},
               
               3: {4: kit.Scroll(plot.library_lore5, wrap),
                   5: kit.Scroll(plot.library_lore6, wrap),
                   9: kit.Scroll(text.library_gnomish, wrap, language = 'Gnomish'),
                   10: kit.Scroll(text.library_compound, wrap),
                   11: kit.Scroll(text.library_orcish, wrap, language = 'Orcish')}
               }
    
    spells = {1: plot.library_spell3,
              2: plot.library_spell1,
              3: plot.library_spell2}
    
    floor_options = {1: {1: text.door_option.format(door1.short),
                         2: 'Go to the second floor',
                         3: 'Go to the third floor',
                         4: 'Read the heavy tome',
                         5: 'Read the elven scroll',
                         6: 'Go look at the fur sash',
                         7: 'Take the vials'},
                     
                     2: {1: text.door_option.format(door3.short),
                         2: 'Go to the first floor',
                         3: 'Go to the third floor',
                         4: 'Read the ornate red book',
                         5: 'Read the aged yellow book',
                         6: 'Read the square blue book',
                         7: 'Check out the table'},
                     
                     3: {1: text.door_option.format(door2.short),
                         2: 'Go to the first floor',
                         3: 'Go to the second floor',
                         4: 'Read the old diary',
                         5: 'Read the leather-bound book',
                         6: 'Check out the table',
                         7: 'Inspect the mechanism'}
                     }
    
    floor_desc = {1: text.library_first.format(door3.desc),
                  2: text.library_second.format(door1.desc),
                  3: text.library_third.format(door2.desc)}
    
    chandelier = False
    
    ## Mechanism ##############################################################
    def mechanism(self, desc):
        activation = {1: [0, 1, 2, 3],
                      2: [0, 1, 3, 4],
                      3: [2, 3, 4, 5],
                      4: [1, 2, 3, 4],
                      5: [0, 2, 3, 5],
                      6: [1, 2, 3, 5]}
        
        slots = [False, False, False, False, False, False]
        state = [False, False, False, False, False, False]
        lights = ['Red', 'Purple', 'Blue', 'Green', 'Yellow', 'Orange']
        slot_names = ['Slot ' + str(i) for i in range(1, 7)]
        onoff = {True: 'ON', False: 'OFF'}
        fullno = {True: 'Full', False: 'Empty'}
        
        
        print(kit.text_wrapper(text.library_puzzle_approach, wrap))
        
        while True:
            kit.top_screen(desc)
            
            display = [[onoff[i]] for i in state]
            status = [[fullno[i]] for i in slots]
            tgen.table_gen(['On?'], lights, display)
            tgen.table_gen(['Full?'], slot_names, status)
            
            if sum(state) == 6:
                print(kit.text_wrapper(text.library_puzzle_win, wrap))
                return True
            else:
                while True:
                    slot = kit.intcheck("\nWhich slot will you interact with?\n>> ")
                    if slot not in activation.keys() and slot != 0:
                        print('There are only 6 slots, typing 0 will exit')
                    else:
                        break
        
                if slot == 0:
                    return False
                else:
                    space = slot - 1
                    slots[space] = not slots[space]
                    
                    for i in activation[slot]:
                        state[i] = not state[i]
   
    ## ENTER ##################################################################
    def enter(self, protag): 
        self.floor = self.floors[protag.proom]
        while True:
            desc = text.library_desc.format(self.floor_desc[self.floor])
            options = self.floor_options[self.floor]
            if protag.role in mages:
                options[8] = 'Learn {}'.format(self.spells[self.floor])
            
            kit.door_check(protag, self.transitions)
            choice = kit.consider(options, desc)
            
            if choice == 1:
                return self.transitions[self.floor].pass_through(protag, self.here)
            
            elif choice in [2, 3]:
                if choice == 2 and self.floor == 1:
                    self.floor = 2
                elif choice == 2 and self.floor in [2, 3]:
                    self.floor = 1
                elif choice == 3 and self.floor in [1, 2]:
                    self.floor = 3
                elif choice == 3 and self.floor == 3:
                    self.floor = 2
            
            elif choice == 6 and self.floor == 1:
                print(kit.text_wrapper(text.library_sash, wrap))
                kit.single_item_pickup(protag, sash, options, 6)
                
            elif choice == 6 and self.floor == 3:
                print(kit.text_wrapper(text.library_table_3, wrap))
                options[9] = 'Read the Gnomish Scroll'
                options[10] = 'Read the old scroll'
                options[11] = 'Read the Orcish Scroll'
                    
            elif choice == 7 and self.floor == 1:
                kit.item_pickup(protag, self.items, options, 7)
            
            elif choice == 7 and self.floor == 2:
                print(kit.text_wrapper(text.library_table_2, wrap))
                options[9] = 'Read the long, thin scroll'
                options[10] = 'Read the ornate scroll'
                options[11] = 'Read the old scroll'
                
            elif choice == 7 and self.floor == 3 and not self.chandelier:
                print(kit.text_wrapper(text.library_puzzle_inspect, wrap))
                yn = kit.intcheck("1 = Fiddle with the mechanism, 2 = Walk away: ")
                if yn == 1:
                    puzzle = self.mechanism(desc)
                    if puzzle == True:
                        self.chandelier = True
                        options[7] = text.door_option.format(self.door4.short)
            
            elif choice == 7 and self.floor == 3 and self.chandelier:
                return self.door4.pass_through(protag, self.here)
                    
            elif choice in self.reading[self.floor].keys():
                self.reading[self.floor][choice].read(protag)
            
            elif choice == 8 and protag.role in mages:
                protag.learn_spell(self.spells[self.floor])
            
            else:
                kit.handle_it(protag, choice) 

###############################################################################
## THE MESS ###################################################################
###############################################################################                    
class Mess():
    
    here = 'mess'
    door1 = plot.mess_door1
    rubble_door = text.door_broken_wall
    transitions = {1: door1}
    
    items = {}
    plot.items_populate(items, food = 11, potions = 0)
    
    reading = {3: kit.Scroll(plot.mess_scroll, short_wrap),
               4: kit.Scroll(text.mess_ornate_scroll, wrap),
               5: kit.Scroll(text.mess_stained_scroll, short_wrap, language = 'Orcish'),
               7: kit.Scroll(plot.mess_book, wrap)}
    
    spells = {8: plot.mess_spell1,
              9: plot.mess_spell2}
    
    options = {1: text.door_option.format(door1.short),
               2: 'Pick up food',
               3: 'Read the ale-stained parchment',
               4: 'Read the ornate scroll',
               5: 'Read the singed parchment',
               6: 'Try to clear the rubble',
               7: 'Read the book'}
    
    desc = text.mess_desc.format(door1.short)
    
    ## ENTER ##################################################################
    def enter(self, protag):                            
        if protag.role in mages:
            self.options[8] = 'Learn {}'.format(plot.mess_spell1)
            self.options[9] = 'Learn {}'.format(plot.mess_spell2)
            
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, self.desc)            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 2:
                kit.item_pickup(protag, self.items, self.options, 2)
            
            elif choice in self.reading.keys():
                self.reading[choice].read(protag)
            
            elif choice == 6:
                if kit.challenge(protag, 'Strength', 25):
                    print(kit.text_wrapper(text.mess_rubble_clear, wrap))
                    self.options[10] = 'Pass through the rubble'
                    self.transitions[10] = self.rubble_door
                    del self.options[6]
                else:
                    print(kit.text_wrapper(text.mess_rubble_fail, wrap))
            
            elif choice in self.spells.keys() and protag.role in mages:
                protag.learn_spell(self.spells[choice])
            
            else:
                kit.handle_it(protag, choice) 
                                
###############################################################################
## THE PANTRY #################################################################
###############################################################################                    
class Pantry():
    
    wall_attack = [plot.pantry_wall]
    
    here = 'pantry'
    door1 = plot.pantry_door1
    door2 = plot.pantry_door2
    door3 = text.door_wall_hole 
    transitions = {1: door1,
                   2: door2}
    
    weapon_available = mace
    
    items = {bracelet.name: bracelet}
    plot.items_populate(items, food = 7, potions = 0)
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: 'Pick up items',
               4: 'Pick up the {}'.format(weapon_available.name),
               5: 'Read the moldy book',
               6: 'Talk to the wall'}
    
    moldy_book = kit.Scroll(plot.pantry_book, wrap)
    
    convo_challenge = {23: 25,
                       11: 15}
    
    convo_ends = {24: 'fight',
                  25: 'open'}
    
    desc = text.pantry_desc.format(weapon_available.name, door1.desc, door2.desc)
    turn_back = False
    
    ## ENTER ##################################################################
    def enter(self, protag):
        self.door3.rooma = self.here
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, self.desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 3:
                kit.item_pickup(protag, self.items, self.options, 3) 
            
            elif choice == 4 and self.weapon_available != False:
                self.weapon_available = protag.weapon_swap(self.weapon_available)
                kit.weapon_fix(self.weapon_available, self.options, 4)
                
            elif choice == 5:
                self.moldy_book.read(protag)
            
            elif choice == 6:
                if self.turn_back == False:
                    print(kit.text_wrapper(text.pantry_wall, wrap))
                    self.turn_back = True
                else:
                    print(kit.text_wrapper(text.pantry_wall2, wrap))
                    wall_talk = kit.conversation(text.pantry_convo_you, text.pantry_convo_wall, protag.charisma, self.convo_challenge, self.convo_ends)
                    if wall_talk == 'open':
                        print(kit.text_wrapper(text.pantry_pass, wrap))
                        self.options[7] = text.door_option.format(self.door3.short)
                        self.transitions[7] = self.door3
                        del self.options[6]
                    elif wall_talk == 'fight':
                        wall_fight = kit.run_encounter(text.pantry_wall_encounter, protag, plot.mess_encounter, self.wall_attack, self.transitions, text.encounter_victory)
                        if wall_fight == True:
                            self.wall_attack = False
                            del self.options[6]
                        elif wall_fight == False:
                            return 'death'
                        else:
                            self.wall_attack = wall_fight[1]
                            fleeing_door = wall_fight[0]
                            return fleeing_door.pass_through(protag, self.here)
            
            else:
                kit.handle_it(protag, choice) 

###############################################################################
## THE PIT BOTTOM #############################################################
###############################################################################                    
class Pit_Bottom():
    
    here = 'lpit'
    door1 = plot.pitl_door
    transitions = {1: door1}
    
    options = {1: text.door_option.format(door1.short),
               2: 'Take the dead man\'s bag',
               3: 'Try to climb up to the ledge (STR)',
               4: 'Pick up the key'}
    
    ## ENTER ##################################################################
    def enter(self, protag):            
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, text.pit_l_desc.format(self.door1.desc))
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 2:
                print('Ew, it looks like he kept food in here')
                kit.single_item_pickup(protag, satchel, self.options, 2)
                
            elif choice == 3 and kit.challenge(protag, 'Strength', 20):
                print(kit.text_wrapper(text.pit_l_climb, wrap))
                yn = kit.intcheck("1 = Try to Balance on the Ledge, 2 = Go Through the Door: ")
                if yn == 2:
                    return kit.doors_are_for_chumps(protag, 'fountains')
                else:
                    return kit.doors_are_for_chumps(protag, 'pit')
            
            elif choice == 3 and not kit.challenge(protag, 'Strength', 25):
                print(kit.text_wrapper(text.pit_l_fail, wrap))
            
            elif choice == 4:
                kit.single_item_pickup(protag, 'key', self.options, 4)
            
            else:
                kit.handle_it(protag, choice) 
            
###############################################################################
## THE PIT ####################################################################
###############################################################################                    
class Pit():
    
    here = 'pit'
    door1 = plot.pitb_door
    transitions = {1: door1}
    
    options = {1: text.door_option.format(door1.short),
               2: 'Jump to the bottom',
               3: 'Try to Jump to the top (DEX)'}
    
    ## ENTER ##################################################################
    def enter(self, protag):
        if not kit.challenge(protag, 'Dexterity', 20):
            print(kit.text_wrapper(text.pit_b_fall, wrap))
            protag.health -= 10
            if protag.health < 0:
                return 'death'
            else:
                return kit.doors_are_for_chumps(protag, 'lpit')
        
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, text.pit_b_desc.format(self.door1.desc))
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 2:
                print(kit.text_wrapper(text.pit_b_jump, wrap))
                return kit.doors_are_for_chumps(protag, 'lpit')
            
            elif choice == 3 and kit.challenge(protag, 'Dexterity', 30):
                print(kit.text_wrapper(text.pit_b_dex_pass, wrap))
                return kit.doors_are_for_chumps(protag, 'upit')
            
            elif choice == 3 and not kit.challenge(protag, 'Dexterity', 30):
                print(kit.text_wrapper(text.pit_b_dex_fail, wrap))
                protag.health -= 20
                if protag.health <= 0:
                    return 'death'
                else:
                    return kit.doors_are_for_chumps(protag, 'lpit')
            
            else:
                kit.handle_it(protag, choice) 

###############################################################################
## THE PIT TOP ################################################################
###############################################################################                    
class Pit_Top():
    
    here = 'upit'
    door1 = plot.pitu_door
    door2 = text.door_wall_hole
    transitions = {1: door1}
    
    options = {1: text.door_option.format(door1.short),
               2: 'Jump down towards the small ledge',
               3: 'Jump all the way down to the bottom'}
    
    ## ENTER ##################################################################
    def enter(self, protag):
        self.door2.rooma = self.here
        if 'Carved Stone Ball' in protag.bag:
            self.options[4] = 'Give the Carved Stone Ball to the left Gargoyle'
            self.options[5] = 'Give the Carved Stone Ball to the right Gargoyle'
            
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, text.pit_u_desc.format(self.door1.desc))
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 2 and kit.challenge(protag, 'Dexterity', 25):
                print(kit.text_wrapper(text.pit_u_pass, wrap))
                return kit.doors_are_for_chumps(protag, 'pit')
            
            elif choice == 2 and not kit.challenge(protag, 'Dexterity', 25):
                print(kit.text_wrapper(text.pit_u_fall, wrap))
                protag.health -= 10
                if protag.health < 0:
                    return 'death'
                else:
                    return kit.doors_are_for_chumps(protag, 'lpit')
            
            elif choice == 3:
                print(kit.text_wrapper(text.pit_u_no, wrap))
                
            elif choice in [4, 5]:
                if choice == plot.pit_gargoyle: 
                    print(kit.text_wrapper(text.pit_gargoyle_pass, wrap))
                    self.options[6] = 'Shimmy your way up the rope'
                    self.transitions[6] = self.door2
                else:
                    print(kit.text_wrapper(text.pit_gargoyl_fail, wrap))
                
                del self.options[4]
                del self.options[5]

            else:
                kit.handle_it(protag, choice) 
    
###############################################################################
## THE PORTAL #################################################################
###############################################################################                    
class Portal():

    gate_foes = []
    
    here = 'portal'
    door1 = plot.portal_door1
    transitions = {1: door1}
    
    weapon_available = ornate_staff
    weapons = {2: weapon_available}
    
    items = {red_pendant.name: red_pendant}
    plot.items_populate(items, food = 4, potions = 2)
    
    rankings = {4: 'Easy',
                3: 'Medium',
                2: 'Hard',
                1: 'Killer',
                0: 'Killer'}
    
    gate_gold = {0: 50,
                 1: 100,
                 2: 150,
                 3: 200,
                 4: 250}
    
    gate_colors = {'Strength': 'red', 
                  'Constitution': 'yellow', 
                  'Dexterity': 'green', 
                  'Intelligence': 'blue', 
                  'Charisma': 'purple'}    
    
    gate_index = 0
    gates = kit.avoid_duplicates(5, list(gate_colors.keys()))
    key_pickup = False
    
    reading = {3: kit.Scroll(plot.portal_lore1, wrap),
               4: kit.Scroll(plot.portal_lore2, wrap),
               5: kit.Scroll(plot.portal_lore3, wrap),
               6: kit.Scroll(text.portal_draconic, wrap, language = 'Draconic'),
               7: kit.Scroll(plot.portal_plot, wrap)}
    
    options = {1: text.door_option.format(door1.short),
               2: 'Pick up the {}'.format(weapon_available.name),
               3: 'Read the heavy book',
               4: 'Read the blue book',
               5: 'Read the purple book',
               6: 'Read the crinkled scroll',
               7: 'Read the notebook',
               8: 'Pick up Items'}
    
    ###########################################################################    
    def str_puzzle(self, solver):
        words = ['heave', 'ho', 'shove', 'push', 'go', 'move', 'work']
        triggers = [rn.choice(words) for i in range(10)]
        print("\n***Enter the given word as fast as possible to move the boulder")
        score = 0
        for i in range(10):
            kit.pause_for_effect()
            time.sleep(rn.randrange(1, 6))
            print("\n\n{}".format(triggers[i].upper()))
            start = time.time()
            response = input('\n>> ').lower()
            if response == triggers[i]:
                score += (time.time() - start)
            else:
                score += 10
        
        boost = 60 / score
        taurs = 4 - min(3, int(boost / 2))
        self.gate_foes = [[mini.foes.Enemy(*i) for i in mini.foes.minotaur][0] for x in range(taurs)]
        
        level = int((solver.strength + boost) / 5)
        if level > 4:
            print('You feel a warm energy engulf you as your health is restored')
            deficit = solver.max_health - solver.health
            solver.health += int(deficit * .5)
            
        return self.rankings[min(4, level)]
    
    ###########################################################################    
    def dex_puzzle(self, solver):
        print('***Enter your direction as fast as you can to stay away from your pursuers!')
        print('   Make a mistake or take to long and you\'ll fall! (Case Sensetive - sorry)')
        branches = {0: ['Dodge', 'Turn', 'Keep On'],
                    1: ['Climb', 'Veer', 'Duck'],
                    2: ['Jump', 'Leap', 'Swerve'],
                    3: ['Dodge', 'Veer', 'Jump'],
                    4: ['Turn Left', 'Turn Right', 'Keep On'],
                    5: ['Maintain Course', 'Parkour', 'Vine Swing'],
                    6: ['Ascend', 'Vault', 'Scale'],
                    7: ['Leap to the next tree', 'Somersault through the air'],
                    8: ['Realize that all attempts to outrun death are futile and surrender to the inescapable grasp of the reaper']}
        
        distance = 0
        while True:
            kit.pause_for_effect()
            print(' or '.join(branches[distance]) + '?')
            start = time.time()
            answer = input('\n>> ')
            end = time.time()
            delta = int(end - start)
            if delta < (solver.dexterity - (2 * distance)) / 5 and answer in branches[distance]:
                print('\nYou {}!\n'.format(answer))
                distance = min(distance + 1, 8)
            else:
                print('\nYou fell!\n')
                break
        
        level = int((solver.dexterity + distance) / 5)
        if level > 4:
            print('You feel a warm energy engulf you as your health is restored')
            deficit = solver.max_health - solver.health
            solver.health += int(deficit * .5)
            
        return self.rankings[min(4, level)]
    
    ###########################################################################
    def con_puzzle(self, solver): #Ogre
        print("***Find your way back to the gate! The fog will confuse your senses so be careful")
        directions = ['Right', 'Left', 'Straight']
        path = [rn.choice(directions) for i in range(20)]
        riddles = {'Left': "The penitent man knows that he who follows the honest path finds his goal more completely than others, for he has followed the wrong path before. He must change directions and avoid the other for only what is left will do",
                   'Right': "Let those who meander lost be aware, here their luck changes for the better. It is wrong that must be avoided above all else. The wrong is the source of all trials, only its opposite can ensure success.",
                   'Straight': "Behold, your path is true! Many will doubt, many will be unaware of their own success. Few have the clarity of vision to stay true to their own direction. Continue to do what is right and you will be successful"}
        
        correct = 0
        turns = 0
        score = 10
        kit.pause_for_effect()
        while correct < 6 and turns < 20:
            o_text = kit.obscure_text(riddles[path[turns]], solver.constitution, score)
            print(kit.text_wrapper(o_text, wrap))
            print(' or '.join(directions) + "?")
            you = input('\n>> ')
            kit.pause_for_effect()
            if you == path[turns]:
                correct += 1
                score += 5
            else:
                score += 10
            turns += 1
       
        boost = 6 * (correct/turns)
        level = int((solver.constitution + boost) / 5)
        if level > 4:
            print('You feel a warm energy engulf you as your health is restored')
            deficit = solver.max_health - solver.health
            solver.health += int(deficit * .5)
            
        return self.rankings[min(4, level)]
        
    ###########################################################################
    def int_puzzle(self, solver): #Shield Gaurdian
        print("***Pick the number of the potion you'll drink")
        potions = {'3': 'The Red Potion',
                   '4': 'The Green Potion',
                   '5': 'The Blue Potion',
                   '7': 'The Yellow Potion',
                   '9': 'The Orange Potion',
                   '11': 'The Purple Potion',
                   '14': 'The Black Potion',
                   '18': 'The White Potion'}
        
        kit.pause_for_effect()
        while True:
            print(kit.text_wrapper(text.portal_int_riddle, wrap))
            print("\nWhich potion will you drink?\n")
            for key in potions:
                print("{}: Vial #{}".format(potions[key], key))
            
            pick = input('\nWhich number vial?\n>> ')
            if pick in potions.keys():
                print("You drink the potion from vial #{}".format(pick))
                break
            
        if pick in [14, 5]:
            boost = 6
        else:
            boost = 0
            
        level = int((solver.intelligence + boost) / 5)
        if level > 4:
            print('You feel a warm energy engulf you as your health is restored')
            deficit = solver.max_health - solver.health
            solver.health += int(deficit * .5)
            
        return self.rankings[min(4, level)]
    
    ###########################################################################
    def cha_puzzle(self, solver): #Mind Flayer
        print('***The Mind Flayers sense your weakness! Answer the questions to hold onto your sanity!')
        questions = {"What's your name?": solver.name.lower(),
                     "What color is the gate?": "purple",
                     "What weapon do you have?": solver.weapon.name.lower(),
                     "What object was on the table?": 'ornate staff red pendant potions vials',
                     "What race are you?": solver.race.lower(),
                     "What are you?": solver.role.lower(),
                     "Was there a talking wall?": 'yes yeah yup you bet',
                     "What shape is the gate supposed to be?": 'arch triangle',
                     "What kingdom is this?": "galenia",
                     "Who is in charge here?": plot.bbeg.name.lower(),
                     "What is on the floor below you?": 'seal'}
        
        bonus = 0
        goal = 40
        for i in range(6):
            kit.pause_for_effect()
            deficit = max(goal - (solver.charisma + bonus), 0)
            bar = '[' + '=' * (solver.charisma + bonus) + ' ' * deficit + ']'
            print('Sanity: ' + bar)
            q = rn.choice(list(questions.keys()))
            print('QUICK!')
            print(q)
            resp = input('\n>> ').lower()
            if resp in questions[q] or questions[q] in resp:
                bonus += 2
            else:
                bonus -= 1
                
        boost = max(0, bonus / 2)            
        level = int((solver.charisma + boost) / 5)
        if level > 4:
            print('You feel a warm energy engulf you as your health is restored')
            deficit = solver.max_health - solver.health
            solver.health += int(deficit * .5)
        
        illithids = 5 - min(4, level)
        self.gate_foes = [[mini.foes.Enemy(*i) for i in mini.foes.mind_flayer][0] for x in range(illithids)]
        
        
        return self.rankings[min(4, level)]
        
    
    ###########################################################################
    def gate(self, focus, traveler):                
        puzzles = {'Strength': self.str_puzzle, 
                  'Constitution': self.con_puzzle, 
                  'Dexterity': self.dex_puzzle, 
                  'Intelligence': self.int_puzzle, 
                  'Charisma': self.cha_puzzle}
        
        desc = text.portal_tests[focus]['desc']
        
        choices = {1: 'Return through the Gate'}
        
        if self.gate_index <= 4:
            choices[2] = text.portal_tests[focus]['choice']
        
        if self.gate_gold[self.gate_index] > 0:
            choices[3] = 'Pick up gold'
            
        if self.gate_index > 4 and self.key_pickup == False:
            choices[4] = 'Pick up the GATE KEY'
            
        victory = False

        while True:
            action = kit.consider(choices, desc)
            
            if action == 1:
                return victory
            
            elif action == 2:
                print(kit.text_wrapper(text.portal_tests[focus]['base'], wrap))
                attempt = puzzles[focus](traveler)
                print(kit.text_wrapper(text.portal_tests[focus][attempt], wrap))
                gate_fight = kit.run_encounter(text.portal_tests[focus]['encounter'], traveler, attempt, self.gate_foes, self.transitions, text.encounter_victory)
                if gate_fight == True:
                    self.gate_foes = []
                    victory = True
                    del choices[2]
                    if self.gate_index == 4:
                        choices[4] = 'Pick up the GATE KEY'
    
                elif gate_fight == False:
                    return 'death'
                else:
                    self.gate_foes = gate_fight[1]
                    return False
            
            elif action == 3:
                traveler.collect_gold(self.gate_gold[self.gate_index], choices, 3)
                self.gate_gold[self.gate_index] = 0
                
            elif action == 4:
                kit.single_item_pickup(traveler, 'GATE KEY', choices, 4)
                self.key_pickup = True
                
            else:
                kit.handle_it(traveler, action) 
    
    ## ENTER ##################################################################
    def enter(self, protag):
        while True:
            c_gate = self.gates[min(4, self.gate_index)]
            color = self.gate_colors[c_gate]
            self.options[9] = 'Pass through the {} gate'.format(color)
            
            desc = text.portal_desc.format(color, self.weapon_available.name)
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.weapons.keys():
                self.weapons[choice] = protag.weapon_swap(self.weapons[choice])
                kit.weapon_fix(self.weapons[choice], self.options, choice)
                
            elif choice in self.reading.keys():
                self.reading[choice].read(protag)
                
            elif choice == 8:
                kit.item_pickup(protag, self.items, self.options, 8)
                
            elif choice == 9:
                test = self.gate(c_gate, protag)
                if test == True:
                    self.gate_index += 1
                    new_color = self.gate_colors[self.gates[min(4, self.gate_index)]]
                    print(kit.text_wrapper(text.portal_win.format(new_color), wrap))
                elif test == 'death':
                    return 'death'
                else:
                    print("You step back into the dark room... nothing has changed")
                
            else:
                kit.handle_it(protag, choice) 
    
###############################################################################
## THE SANCTUM ################################################################
###############################################################################                    
class Sanctum():
    
    here = 'sanctum'
    door1 = text.door_bookshelf
    transitions = {1: door1}
    
    master_spell = plot.sanctum_spell
    
    reading = {2: kit.Scroll(text.sanctum_master_spell[master_spell], wrap),
               3: kit.Scroll(text.sanctum_scroll, wrap)}
    
    options = {1: text.door_option.format(door1.short),
               2: 'Read the notebook',
               3: 'Read the scroll',
               4: 'Pick up the gold'}
    
    ## ENTER ##################################################################
    def enter(self, protag):
        if protag.role in mages:
            self.options[5] = 'Learn {}'.format(self.master_spell)
        
        while True:
            desc = text.sanctum_desc
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.reading.keys():
                self.reading[choice].read(protag)
            
            elif choice == 4:
                protag.collect_gold(125, self.options, 4)
            
            elif choice == 5:
                protag.learn_spell(self.master_spell)
            
            else:
                kit.handle_it(protag, choice) 
    
###############################################################################
## THE SHRINE #################################################################
############################################################################### 
class Shrine():
    
    here = 'shrine'
    door1 = text.door_wall_hole
    
    options = {1: text.door_option.format(door1.short),
               2: 'Pray at the shrine'}
    
    prayed = []
    
    ## ENTER ##################################################################
    def enter(self, protag):
        god = plot.god_rooms[self.door1.rooma]
        if god not in protag.shrines_found:
            protag.shrines_found.append(god)
        
        while True:
            choice = kit.consider(self.options, text.shrine_desc[god])
            
            if choice == 1:
                return self.door1.pass_through(protag, self.here)
            
            elif choice == 2 and god not in self.prayed:
                protag.pray(god, text.shrine_prayer[god], self.prayed)
                
            elif choice == 2 and god in self.prayed:
                print('You have already prayed to {}'.format(god))
                print('Anymore and you\'ll just seem needy')
            
            else:
                kit.handle_it(protag, choice) 

###############################################################################
## STATUE ROW #################################################################
###############################################################################                    
class StatueRow():

    here = 'srow'
    door1 = plot.srow_door1
    door2 = plot.srow_door2
    
    transitions = {1: door1,
                   2: door2}
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: 'Read the sealed note'}
    
    reading = {3: kit.Scroll(text.srow_dwarvish, wrap, language = 'Dwarvish')}
    
    for i in range(4, 8):
        options[i] = 'Open Chest {}'.format(i - 2)
    
    master_potion = kit.Potion('Master Potion 2', 'A shimmering green vial, with the strong scent of mint', 'All', 1, 'Freezing')
    
    chests = kit.avoid_duplicates(4, [master_potion, orb, helm, 'gold'])
    locked=['', '', '', '', True, True, True, True]
    statues = [plot.srow_statue1, plot.srow_statue2, plot.srow_statue3, plot.srow_statue4]
    
    ## ENTER ##################################################################
    def enter(self, protag):        
        while True:
            desc = text.srow_desc
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.reading.keys():
                self.reading[choice].read(protag)
            
            elif choice in range(4, 8) and self.locked[choice]:
                chest = list(range(4, 8)).index(choice)
                if 'key' in protag.bag:
                    print(kit.text_wrapper(self.statues[chest], wrap))
                    protag.bag.remove('key')
                    self.locked[choice] = False
                    print('You unlocked Chest {}!'.format(choice - 2))
                    if self.chests[chest] == 'gold':
                        print('You find a large pile of gold!')
                        self.options[choice] = 'Pick up the Gold'
                    else:
                        n = self.chests[chest].name
                        print('You find the {}!'.format(n))
                        self.options[choice] = 'Pick up the {}'.format(n)
                else:
                    print("You're all out of keys!")
                    
            elif choice in range(4, 8) and not self.locked[choice]:
                chest = list(range(4, 8)).index(choice)
                if self.chests[chest] == 'gold':
                    protag.collect_gold(500, self.options, choice)
                else:
                    kit.single_item_pickup(protag, self.chests[chest], self.options, choice)
                    
            else:
                kit.handle_it(protag, choice) 
        
###############################################################################
## THE TEMPLE #################################################################
###############################################################################                    
class Temple():
    
    here = 'temple'
    door1 = plot.temple_door1
    door2 = plot.temple_door2
    door3 = plot.temple_door3
    door4 = text.door_statue
    door5 = text.door_wall_hole
    transitions = {1: door1,
                   2: door2,
                   3: door3}
    
    wall = rn.choice(text.wall_ornaments)
    
    left_statue = plot.temple_statue1
    right_statue = plot.temple_statue2
    hatch = rn.randrange(4, 6)
    
    passed = False
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: text.door_option.format(door3.short),
               4: 'Investigate the left statue',
               5: 'Investigate the right statue',
               6: 'Try to read the columns',
               7: 'Try to read the floor',
               8: 'Approach the Fresco'}

    investigation = {4: kit.text_wrapper(left_statue, wrap),
                     5: kit.text_wrapper(right_statue, wrap)}
    
    reading = {6: kit.Scroll(text.temple_columns.format(plot.temple_phrase), short_wrap, o_level = 25),
               7: kit.Scroll(text.temple_floor, short_wrap, o_level = 25)}
    
    desc = text.temple_desc.format(door1.desc, door2.desc, door3.desc, wall)
    
    ## ENTER ##################################################################
    def enter(self, protag):
        self.door5.rooma = self.here
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, self.desc)
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.investigation.keys():
                print(self.investigation[choice])
                if choice == self.hatch:
                    print(text.temple_challenge)
                    yn = kit.intcheck("1 = Push the Statue, 2 = No Thanks: ")
                    if yn == 1 and kit.challenge(protag, 'Strength', 20):
                        print(text.temple_hatch)
                        self.options[9] = text.door_option.format(self.door4.short)
                        self.transitions[9] = self.door4
                    elif yn == 1 and not kit.challenge(protag, 'Strength', 20):
                        print('The statue won\'t budge')
            
            elif choice == 8 and self.passed == False:
                kit.suspense(text.temple_fresco, delays = [0, 3, 7, 5, 5, 5, 5, 7])
                password = input('\n>> ').upper()
                if password == plot.temple_phrase:
                    print(kit.text_wrapper(text.temple_accept, wrap))
                    self.options[10] = text.door_option.format(self.door5.short)
                    self.transitions[10] = self.door5
                    self.passed = True
                    del self.options[8]
                else:
                    print(kit.text_wrapper(text.temple_fail, wrap))
            
            elif choice in self.reading.keys():
                self.reading[choice].read(protag)
            
            else:
                kit.handle_it(protag, choice)  

###############################################################################
## THE TOWER ##################################################################
###############################################################################                    
class Tower():
    
    here = 'tower'    
    door1 = plot.tower_door1
    transitions = {1: door1}
    
    drop = False
    plot_item = plot.tower_item
    items = {'Key': 'key'}
    plot.items_populate(items, food = 5, potions = 1)

    spells = {10: plot.tower_spell1,
              11: plot.tower_spell2}
    
    weapon_available = iron_staff
    weapons = {5: weapon_available}
    
    entry = text.tower_entry.format(door1.short)    
    
    options = {1: text.door_option.format(door1.short),
               2: 'Investigate the {}'.format(plot.tower_interest),
               3: 'Investigate the table',
               4: 'Pick up Items',
               5: 'Pick up the {}'.format(weapon_available.name)
               }
    
    ritual_scroll = text.tower_scroll_ritual.format(plot.ritual.name, plot.ritual.ingredients_order[0], plot.ritual.ingredients_order[1], plot.ritual.ingredients_order[2])
    investigation = {2: kit.text_wrapper(plot.tower_int_inv, wrap),
                     3: kit.text_wrapper(text.tower_table, wrap)}
    
    reading = {6: kit.Scroll(plot.tower_scroll, wrap),
               7: kit.Scroll(ritual_scroll, wrap),
               8: kit.Scroll(text.tower_scroll_diary, short_wrap, language = 'Elvish'),
               9: kit.Scroll(plot.tower_book, wrap)}
    
    ## ENTER ##################################################################
    def enter(self, protag):
        print(kit.text_wrapper(self.entry, wrap))        
        while True:
            desc = plot.tower_contents.format(self.weapon_available.name)
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.investigation.keys():
                print(self.investigation[choice])
                if choice == 3:
                    self.options[6] = 'Read Scroll 1'
                    self.options[7] = 'Read Scroll 2'
                    self.options[8] = 'Read Scroll 3'
                    self.options[9] = 'Read the green book'
                    if protag.role in mages:
                        self.options[10] = 'Learn {}'.format(plot.tower_spell1)
                        self.options[11] = 'Learn {}'.format(plot.tower_spell2)
                
                elif choice == 2 and self.drop == False:
                    if self.plot_item not in protag.bag:
                        if len(self.items) == 0:
                            self.options[4] = 'Pick up Items'
                        self.items[self.plot_item] = self.plot_item
                        self.drop = True
            
            elif choice == 4:
                kit.item_pickup(protag, self.items, self.options, 4)   
                    
            elif choice in self.weapons.keys():
                self.weapons[choice] = protag.weapon_swap(self.weapons[choice])
                kit.weapon_fix(self.weapons[choice], self.options, choice)
                
            elif choice in self.reading.keys():
                self.reading[choice].read(protag)
            
            elif choice in self.spells.keys() and protag.role in mages:
                protag.learn_spell(self.spells[choice])
                    
            else:
                kit.handle_it(protag, choice) 
                
###############################################################################
### TRANSIT ###################################################################
###############################################################################
class Transit():

    encounters = {'fountains': 'Easy',
                  'catacombs': 'Medium',
                  'lab': 'Easy',
                  'mess': 'Hard',
                  'dungeon': 'Hard',
                  'lpit': 'Medium',
                  'wfall': 'Killer',
                  'srow': 'Killer', 
                  'garden': 'Killer',
                  'antechamber': 'Hard'}
    
    foes = {}
    
    def enter(self, protag):
        destination = protag.droom
        
        if destination in self.encounters.keys() and destination not in self.foes.keys():
            self.foes[destination] = []
        
        if destination in self.foes.keys() and self.foes[destination] != False:
            diff = self.encounters[destination]
            baddies = self.foes[destination]
            start = text.encounter_intro
            end = text.encounter_victory
            
            fight = kit.run_encounter(start, protag, diff, baddies, {1: text.door_holder}, end)
            if fight == True:
                self.foes[destination] = False
                return destination
            elif fight == False:
                return 'death'
            else:
                self.foes[destination] = fight[1]
                return protag.proom
        
        else: 
            return destination
    
###############################################################################
## THE UNDERWATER #############################################################
###############################################################################                    
class Underwater():
    
    weapon_available = club
    
    here = 'uwater'
    door1 = text.door_underwater
    door2 = text.door_wall_hole
    transitions = {1: door1,
                   2: door2}
    
    options = {1: 'Return through the {}'.format(door1.short),
               2: text.door_option.format(door2.short),
               3: 'Collect items',
               4: 'Pick up the {}'.format(weapon_available.name),
               5: 'Pick up the gold coins',
               6: 'Investigate the twinkle'}
    
    items = {"Key": 'key'}
    plot.items_populate(items, food = 3, potions = 2)
    
    jar = True
    
    ## ENTER ##################################################################
    def enter(self, protag):  
        self.door2.rooma = self.here
        if kit.challenge(protag, 'Dexterity', 25) and self.jar:
            self.options[7] = 'Jump and try to grab the magical fire'
            
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, text.underwater_desc)
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice == 3:
                kit.item_pickup(protag, self.items, self.options, 3)                   
            
            elif choice == 4 and self.weapon_available != False:
                self.weapon_available = protag.weapon_swap(self.weapon_available)
                kit.weapon_fix(self.weapon_available, self.options, 4)
                    
            elif choice == 5:
                protag.collect_gold(50, self.options, 5)
                
            elif choice == 6:
                print(kit.text_wrapper(text.underwater_ring, wrap))
                kit.single_item_pickup(protag, gold_ring, self.options, 6)
                
            elif choice == 7:
                print("You leap with all you might and manage to grab the jar!")
                print("You feel no heat coming from the fire so you feel safe adding it to your bag")
                kit.single_item_pickup(protag, 'Jar of Magical Fire', self.options, 7)
                self.jar = False
            
            else:
                kit.handle_it(protag, choice) 

###############################################################################
## THE VINES ##################################################################
###############################################################################                    
class Vines():
    
    here = 'vines'
    door1 = plot.vines_door1
    door2 = plot.vines_door2
    transitions = {1: door1,
                   2: door2}
    
    weapon_available = ser_dagger
    weapons = {3: weapon_available}
    
    reading = {6: kit.Scroll(text.vines_scroll_dwarvish, wrap, language = 'Dwarvish'),
               7: kit.Scroll(text.vines_scroll1, short_wrap),
               8: kit.Scroll(text.vines_scroll2, short_wrap),
               9: kit.Scroll(plot.vines_lore, wrap)}
    
    spell1 = plot.vines_spell
    spells = {10: spell1}
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: 'Pick up the {}'.format(weapon_available.name),
               4: 'Check out the table',
               5: 'Hack away at some vines'}
    
    dropped = False
    burned = False
    
    ## ENTER ##################################################################
    def enter(self, protag):
        desc = text.vines_desc.format(plot.vines_statue1[15:], plot.vines_statue2[15:], plot.vines_statue3[15:], self.weapon_available.name, self.door1.desc, self.door2.desc)
        fire_spells = [s for s in protag.spells if 'Fire' in s]
        if protag.role in mages:
            self.options[10] = 'Learn {}'.format(self.spell1)
            if len(fire_spells) > 0 and self.burned == False:
                self.options[11] = 'Cast {} at the wall'.format(fire_spells[0])
        
        while True:
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
        
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
        
            elif choice in self.weapons.keys():
                self.weapons[choice] = protag.weapon_swap(self.weapons[choice])
                kit.weapon_fix(self.weapons[choice], self.options, choice)
        
            elif choice == 4:
                print(kit.text_wrapper(text.vines_table, wrap))
                self.options[6] = 'Read the Dwarvish Scroll'
                self.options[7] = 'Read the diary page'
                self.options[8] = 'Read the note'
                self.options[9] = 'Read the medium-sized book'
            
            elif choice == 5:
                if self.dropped == False and rn.choice([1, 2, 3, 4]) == 1:
                    print(kit.text_wrapper(text.vines_boots, wrap))
                    self.options[12] = 'Steal the dead man\'s boots'
                    self.dropped = True
                else:
                    wall = rn.choice(text.wall_ornaments)
                    print(kit.text_wrapper('You hack away at some vines, revealing ' + wall, wrap))
            
            elif choice in self.reading.keys():
                self.reading[choice].read(protag)
        
            elif choice in self.spells.keys() and protag.role in mages:
                protag.learn_spell(self.spells[choice])
        
            elif choice == 11 and len(fire_spells) > 0:
                print(kit.text_wrapper(text.vines_reveal.format(fire_spells[0]), wrap))
                protag.collect_gold(80, self.options, 11)
                self.burned = True
        
            elif choice == 12 and self.options.get(12) != None:
                kit.single_item_pickup(protag, boots, self.options, 12)
        
            else:
                kit.handle_it(protag, choice) 

###############################################################################
## THE WATERFALL ##############################################################
###############################################################################                    
class Waterfall():

    here = 'wfall'
    door1 = plot.wfall_door1
    door2 = plot.wfall_door2
    door3 = text.door_wall_hole
    transitions = {1: door1,
                   2: door2}
    
    stones = kit.avoid_duplicates(9, list(range(1, 10)))
    to_touch = list(range(4, 13))
    touch_order = kit.avoid_duplicates(4, to_touch)
    touched = []
    
    stone_order = []
    for i in touch_order:
        l = to_touch.index(i) + 1
        stone_order.append(l)
    
    worded = kit.wordify(stone_order)
    
    reading = {3: kit.Scroll(text.wfall_riddle.format(*worded), wrap)}
    
    options = {1: text.door_option.format(door1.short),
               2: text.door_option.format(door2.short),
               3: 'Read the stone slab'}
    
    for i in range(4, 13):
        options[i] = 'Touch stone {}'.format(i - 3)
        
    puzzle = False
    
    ## ENTER #############################################################################################
    def enter(self, protag):
        self.door3.rooma = self.here
        while True:
            if self.touched == self.touch_order and self.puzzle == False:
                self.transitions[13] = self.door3
                self.options[13] = text.door_option.format(self.door3.short)
                print(kit.text_wrapper(text.wfall_puzzle_solve, wrap))
                self.puzzle = True
            elif len(self.touched) == 4 and self.touched != self.touch_order:
                print(kit.text_wrapper(text.wfall_puzzle_fail, wrap))
                self.puzzle = 'wrong'
            
            desc = text.wfall_desc.format(self.door1.desc, self.door2.desc)
            kit.door_check(protag, self.transitions)
            choice = kit.consider(self.options, desc)
            
            if choice in self.transitions.keys():
                return self.transitions[choice].pass_through(protag, self.here)
            
            elif choice in self.reading.keys():
                self.reading[choice].read(protag)
            
            elif choice in range(4, 13) and self.puzzle == False:
                print(kit.text_wrapper(text.wfall_stone_press, wrap))
                self.touched.append(choice)
                del self.options[choice]
            
            else:
                kit.handle_it(protag, choice) 
    
###############################################################################
## THE END ####################################################################
############################################################################### 
class Finished():
    
    ## ENTER #############################################################################################
    def enter(self, protag):
        kit.linebreak(big = True)
        print(protag)
        print("Shrines Found: {}/6".format(len(protag.shrines_found)))
        kit.linebreak(big = True)
        end = time.time()
        if protag.health > 0:
            print('\nYOU WIN!\n')
        else:
            print('\nTry again\n')
            
        
        score = 0
        score += protag.total_exp / 10
        score += protag.gold
        score += protag.strength + protag.dexterity + protag.constitution + protag.intelligence + protag.charisma
        score += protag.max_health
        score += protag.imortality * 500
        score += plot.victory * 500
        score += protag.dam_bonus
        score += protag.level * 10
        print('\nSCORE: {}'.format(score))
        duration = (end - start) / 60
        seconds = (duration - int(duration)) * 60
        print('Duration: {} minutes, {} seconds!'.format(int(duration), int(seconds)))
        

###############################################################################
## THE DEATH ##################################################################
###############################################################################         
class Death():

    quips = [
            "You lose"
            ]
    
    ## ENTER ##################################################################
    def enter(self, protag):
        
        kit.linebreak(big = True)
        print(rn.choice(self.quips))
        return 'finished'
        
###############################################################################
## THE SCRIPT #################################################################
###############################################################################  
class Script():
    
    scenes = {
            'altar room': Altar(),
            'catacombs': Catacombs(),
            'lab': Lab(),
            'pantry': Pantry(),
            'lpit': Pit_Bottom(),
            'pit': Pit(),
            'upit': Pit_Top(),
            'mess': Mess(),
            'garden': Garden(),
            'wfall': Waterfall(),
            'srow': StatueRow(),
            'barracks': Barracks(),
            'library': Library(),
            'sanctum': Sanctum(),
            'uwater': Underwater(),
            'shrine': Shrine(),
            'vines': Vines(),
            'tower': Tower(),
            'fountains': Fountains(),
            'transit': Transit(),
            'armory': Armory(),
            'dungeon': Dungeon(),
            'lava': Lava(),
            'ice': Ice(),
            'cliff': Cliff(),
            'kennel': Kennel(),
            'portal': Portal(),
            'antechamber': Antechamber(),
            'exxit': Exxit(),
            'temple': Temple(),
            'death': Death(),
            'finished': Finished()
            }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def run_scene(self, scene_name):
        val = Script.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.run_scene(self.start_scene)
      
###############################################################################
## THE ENGINE #################################################################
############################################################################### 
class Engine():
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self, player):
        
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.run_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter(player)
            current_scene = self.scene_map.run_scene(next_scene_name)
        
        current_scene.enter(player) 
    
###############################################################################
## TIME TO PLAY ###############################################################
############################################################################### 
d_script = Script('altar room')
d_game = Engine(d_script)
d_game.play(hero)   