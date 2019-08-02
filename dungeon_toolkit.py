# -*- coding: utf-8 -*-
"""
Created on Thu May 30 07:58:22 2019

@author: Devlin
"""

import os
import random as rn
import dungeon_spells as magic
from dungeon_divinity import foes
import numpy as np
import time

###############################################################################\
## CLASSES #####################################################################
###############################################################################/
class Door():
    def __init__(self, desc, transition, barred, unlock, short, rooma = None, roomb = None):
        self.desc = desc
        self.transition = transition
        self.barred = barred
        self.unlock = unlock
        self.short = short   
        self.rooma = rooma
        self.roomb = roomb
        self.locked = False
        
    def pass_through(self, user, croom):        
        pass_to = [room for room in [self.rooma, self.roomb] if room != croom][0]
        
        if self.locked == True:
            print(text_wrapper(self.barred, 80))        
            if 'key' in user.bag:
                linebreak()
                print('Use your key?')
                yn = intcheck("1 = Unlock the {}, 2 = No thanks: ".format(self.short))
                if yn == 1:
                    self.locked = False
                    user.bag.remove('key')
                    linebreak()
                    print(text_wrapper(self.unlock, 80))
            ## THIS FIXES THE UNFIXABLE GLITCH IN THE CLIFF. 
            user.proom = pass_to
            ## I DONT KNOW WHAT SORT OF FUCKERY WILL RESULT
            return croom
        
        else:        
            points = sorted([2, 1] * 11, reverse = True)                       
            while user.exp >= user.exp_goal:
                user.level_up(points[user.level])
                linebreak()
                print(user)
                linebreak()
            
            print(text_wrapper(self.transition, 80))
            user.proom = croom
            user.droom = pass_to
            return 'transit'
        
    def __str__(self):
        return self.rooma + ' <--' + self.short + '--> ' + self.roomb

###############################################################################
class Equipment():
    def __init__(self, name, desc, stat, bonus, race_req = None):
        self.name = name
        self.desc = desc
        self.stat = stat
        self.bonus = bonus
        self.race_req = race_req
        self.price = 75

###############################################################################
class Food():
    def __init__(self, name, desc, health):
        self.name = name
        self.desc = desc
        self.health = health
        self.price = 10
        
    def use(self, user):
        print('You eat the {} and regain some health'.format(self.name))
        user.health = min(self.health + user.health, user.max_health)
        print('Health: {}'.format(user.health))
        return True
    
###############################################################################    
class Holder():
    def __init__(self, holding):
        self.holding = holding
        self.name = holding.name
        self.desc = holding.desc
        self.price = holding.price
        
    def use(self, user):
        if user.race == self.holding.race_req or self.holding.race_req == None:
            if user.equipped == '':
                user.equipped = self.holding
                print("You have equipped the {}".format(self.holding.name))
                print("This gives you +{} to your {}".format(self.holding.bonus, self.holding.stat))
                user.score_modify(self.holding.stat, self.holding.bonus)
                return True
            else:
                print("You can only equip one item at a time\nYou'll have to pick one\n")
                print("Currently Equipped - {}: +{} {}".format(user.equipped.name, user.equipped.bonus, user.equipped.stat))
                print("Consider Equipping - {}: +{} {}".format(self.holding.name, self.holding.bonus, self.holding.stat))
                yn = intcheck("\n1 = Switch Items, 2 = Keep Your Current Item: ")
                if yn == 1:
                    inventory(user, 'add', user.equipped)
                    user.score_modify(user.equipped.stat, -1 * user.equipped.bonus)
                    print('You equipped the {}'.format(self.holding.name))
                    user.equipped = self.holding
                    user.score_modify(self.holding.stat, self.holding.bonus)
                    return True
                else:
                    print("You keep the {} equipped".format(user.equipped.name))
                    return False
        else:
            print('You are not allowed to equip this item')
            return False
        
###############################################################################
class Potion():
    def __init__(self, debug, desc, stat, bonus, mask):
        self.debug = debug
        self.desc = desc
        self.stat = stat
        self.bonus = bonus
        self.number = str(rn.randrange(1, 1000))
        self.number_listed = list(self.number)
        while len(self.number_listed) < 3:
            self.number_listed.insert(0, '0')
        self.final_number = ''.join(self.number_listed)
        self.name = '{} Vial #{}'.format(mask, self.final_number)
        self.price = 40
        
    def use(self, user):
        if self.bonus > 0 and self.stat != 'All':
            print('You drink the {} and recieve a +{} to {}'.format(self.desc, self.bonus, self.stat))
        elif self.stat == 'All':
            print('You drink the {} and feel a warmth throughout your whole body'.format(self.desc))
            print('You gain +{} to Strength, Dexterity, Constitution, and Intelligence'.format(self.bonus))
        else:
            print('POISONED! You drink the {} and your {} decreases by {}'.format(self.name, self.stat, -1 * self.bonus))
        
        if self.stat == 'All':    
            for i in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Charisma']:
                user.score_modify(i, self.bonus)
        else:
            user.score_modify(self.stat, self.bonus) 
            
        return True
            
###########################################################################################################################|
class Ritual():                                                                                                         ###|
    def __init__(self, name, vials, dish1, dish2, order):                                                               ###|
        self.name = name                                                                                                ###|
        self.vials = vials                                                                                              ###|
        self.dish1 = dish1                                                                                              ###|
        self.dish2 = dish2                                                                                              ###|
        self.order = order                                                                                              ###|
        self.ingredients = [self.vials, self.dish1, self.dish2]                                                         ###|
        self.ingredients_order = [self.ingredients[i] for i in self.order]                                              ###|  
                                                                                                                        ###|  
    def perform_ritual(self, user):                                                                                     ###|
        ingredients = [self.vials, self.dish1, self.dish2]                                                              ###|
        for i in range(len(ingredients)):                                                                               ###|
            if ingredients[i] not in user.bag:                                                                          ###|
                print("You don't have the necessary ingredients to perform the ritual")                                 ###|
                return False                                                                                            ###| 
            else:                                                                                                       ###|
                print(str(i + 1) + " - " + ingredients[i])                                                              ###|
                print('\nWhat order will you use them to consecrate the body?')                                         ###|
                first = intcheck('First use ... ') - 1                                                                  ###|
                second = intcheck('Second use... ') - 1                                                                 ###| 
                last = intcheck('Last use... ') - 1                                                                     ###|
                                                                                                                       ####/
                used_order = [first, second, last]                                                                    ####/
                if used_order == self.order:                                                                         ####/
                    return True                                                                                     ####/
                else:                                                                                              ####/
                    return False                                                                                  ####/
                                                                                                                 ####/
####################################################################################################################/
class Scroll():                                                                                                 ####|
    def __init__(self, flavor, wrap, language = 'Common', o_level = 0):                                         ####|
        self.flavor = flavor                                                                                    ####|
        self.wrap = wrap                                                                                        ####|
        self.language = language                                                                                ####|
        self.o_level = o_level                                                                                  ####|
                                                                                                                ####|
    def read(self, user):                                                                                       ####|  
        if self.language not in user.languages:                                                                 ####|
            print('You try to understand but you don\'t know {}'.format(self.language))                         ####|
        else:                                                                                                   ####|
            if self.o_level > 0:                                                                                ####|
                scroll_text = obscure_text(self.flavor, user.intelligence, self.o_level)                        ####|
            else:                                                                                               ####|
                scroll_text = self.flavor                                                                       ####|
                                                                                                                ####|
            print(text_wrapper(scroll_text, self.wrap))                                                         ####| 
                                                                                                                ####|
####################################################################################################################|                                                                                                                  
class Weapon():                                                                                                 ####/
    def __init__(self, name, flavor, damagemin, damagemax, rolls, category, stun = 0):                         ####/
        self.name = name                                                                                      ####/
        self.flavor = flavor                                                                                 ####/
        self.damagemin = damagemin                                                                          ####/
        self.damagemax = damagemax + 1                                                                     ####/
        self.rolls = rolls                                                                                ####/
        self.category = category                                                                         ####/
        self.stun = stun                                                                                ####/ 
        self.expected_damage = ((self.damagemax + self.damagemin) / 2) * self.rolls                    ####/ 
                                                                                                      ####/
#########################################################################################################/
## FUNCTIONS ###########################################################################################/
#######################################################################################################/
def avoid_duplicates(n, source):
    if len(source) < n:
        n = len(source) 
    
    final = []
    for i in range(n):
        while True:
            item = rn.choice(source)
            if item not in final:
                final.append(item)
                break
    
    return final

# Usage - 9: master, gme
#####################################################################################\
def challenge(user, skill, level):                                                  ##\
    skills = {'Strength': user.strength,                                             #|
              'Dexterity': user.dexterity,                                           #|
              'Constitution': user.constitution,                                     #|
              'Intelligence': user.intelligence,                                     #|
              'Charisma': user.charisma}                                             #|
                                                                                     #|
    if skills[skill] >= level:                                                       #|
        return True                                                                  #|
    else:                                                                            #|
        return False                                                                 #|
                                                                                     #|
# Usage - 21: master                                                                ##/                                                                                     
#####################################################################################/                                                                                  
def consider(array, room_desc):
    
    top_screen(room_desc)
    
    print("You consider the possibilities...")
    final = max(array.keys()) + 1
    for i in range(0, final):
        try:
            print(str(i) + ": " + array[i])
        except KeyError:
            pass
    
    other = ['bag', 'stats']
    while True:
        picked = intcheck("Pick the number of your choice > ", special = other)
        linebreak()
        if array.get(picked) != None or picked in other:
            break
        else:
            notnow()

    return picked

###############################################################################
def conversation(your_tree, their_tree, score = 0, locked = {}, fancy = {}):
    node = 1
    base = your_tree[1]
    at_base = False
    saying = '...'
    while True:
        they_say = their_tree[node]
        top_screen(saying)
        print('\n"{}"\n'.format(text_wrapper(they_say, 80)))
        linebreak()
        if node in fancy.keys():
            return fancy[node]
        else:        
            if at_base == False:
                responses = [key for key in your_tree[node]]        
            else:
                node = 1
                responses = [key for key in base]
       
        n = len(responses)
        responses.insert(n, 'Ask Something Else')
        n += 1
        for i in range(n):
            print('{}: {}'.format(i + 1, responses[i]))
        
        said = intcheck("Pick the number of your response: ", special = ['goodbye'])
        if said == 'goodbye':
            return 0
        elif said == n:
            at_base = True
        elif said > n:
            notnow()
        else:
            at_base = False
            saying = responses[said - 1]
            node = your_tree[node][saying]
            if node in locked.keys() and score < locked[node]:
                node = 'denial'
                
###############################################################################
def door_check(user, doors_array):
    locked = [1 for key in doors_array if doors_array[key].locked == True]

    if 'key' not in user.bag:
        if len(locked) == len(doors_array):
            print("A sudden burst of light engulfs the room, dazing you a moment")
            print("When you recover, floating before you is a silver key")
            inventory(user, 'add', 'key')
            
###############################################################################
def doors_are_for_chumps(dude, destination):
    dude.droom = destination
    return 'transit'

##############################################################################><############|#
def encounter_build(user, encounter, enemies, foe_set):                                    #|#
    difficulties = {'Easy':  30,                                                           #|#
                    'Medium': 40,                                                          #|#
                    'Hard': 60,                                                            #|# 
                    'Killer': 70}                                                          #|#
                                                                                           #|#
    base = max(user.total_exp, 20)                                                         #|#
    if type(encounter) == str and encounter in difficulties.keys():                        #|#
        exp_target = int((np.log10(base) * difficulties[encounter])  + np.sqrt(base))      #|#
    else:                                                                                  #|#
        exp_target = int((np.log10(base) * difficulties['Medium'])  + np.sqrt(base))       #|#
                                                                                           #|# 
    ## All Details Hardcoded #################################################><############|#
    if type(encounter) == list and foe_set != False:                                       #|#
        enemies_raw = []                                                                   #|# 
        for i in range(len(encounter)):                                                    #|#
            for n in range(encounter[i]):                                                  #|#
                enemies_raw.append(foe_set[i])                                             #|#
                                                                                           #|#
    ## Quanities Generated, Foes Provided or Not #############################><############|#
    else:                                                                                  #|#
        exps = {}                                                                          #|#
        if foe_set != False:                                                               #|#
            for foe in foe_set:                                                            #|#
                exps[foes.foe_blueprints[foe][6]] = foe                                    #|# 
        else:                                                                              #|#
            for foe in foes.foes_exp:                                                      #|#
                exps[foe[1]] = foe[0]                                                      #|#
                                                                                           #|#
        exp_build = rand_build(exp_target, source = list(exps.keys()))                     #|#
        enemies_raw = [exps[i] for i in exp_build]                                         #|#
                                                                                           #|#
    ## Finalizing the List ###################################################><############|#    
    for raw in enemies_raw:                                                                #|#
        blueprint = [foes.foe_blueprints[raw]]                                             #|#
        this_foe = [foes.Enemy(*i) for i in blueprint][0]                                  #|# 
        enemies.append(this_foe)                                                           #|#
                                                                                           #|#                                                                                     
    return enemies                                                                         #|#
                                                                                           #|#
##############################################################################><############|#
def handle_it(guy, selection):
    if selection == 'stats':
        print(guy)
    elif selection == 'bag':
        inventory(guy, 'check')
    else:
        notnow()

###############################################################################        
def health_bar_gen(body, th = False):
    if th == True:
        base = body.temp_hp
        c = '[|]'
    else:
        base = body.health
        c = '|'
        
    words = body.name + "'s Health-------"
    max_l = round(140 - len(words), -1)
    
    represent = int(base / (max_l / len(c))) + 1
    n_bars = int(base / represent)
       
    return c * n_bars  

###############################################################################
def intcheck(string, special = []):
    while True:
        value = input(string)
        if value.lower() in special:
            some_number = value
            break
        else:
            try:
                some_number = int(value)
            except ValueError:
                notnow()
            else:
                break
    
    return some_number 

##############################################################################\/#################\
##############################################################################/\################|#\
def inventory(user, cmd, item = None):                                                         #|##\
                                                                                               #|###\
    ## Adding Items ##########################################################><################|####\
    if cmd == 'add' and item != None:                                                               ##\
        if type(item) == Equipment:
            x = Holder(item)
        else:
            x = item
            
        user.bag.append(x)                                                                           ##\
        if type(item) == str:                                                                         ##\ 
            print('You added {} to your bag'.format(item))                                             ##\
        else:                                                                                           ##\  
            print('You added {} to your bag'.format(item.name))                                          ##\
                                                                                                          ##\
    ## Checking, Using, and Dropping Items ###################################><#############################\
    elif cmd == 'check':                                                                                    ##\ 
                                                                                                             ##\
        ## Checking ##########################################################><################################\
        print('In your bag, you have...')                                                                      ##\
        if len(user.bag) == 0:                                                                                  ##\
            print('Nothing!')                                                                                    ##\
        else:                                                                                                     ##\
            for thing in user.bag:                                                                                 ##\
                if type(thing) == str:                                                                              ##\
                    print(thing.capitalize())                                                                        ##\
                else:                                                                                                #|# 
                    print(thing.name + ": " + thing.desc)                                                            #|# 
                                                                                                                     #|#  
        ## User Action #######################################################><######################################|#            
        print('\nWould you like to use something, drop something, or exit?')                                         #|#
        while True:                                                                                                  #|# 
            doing = input('>> ').lower()                                                                             #|#
            acceptable = ['use ', 'drop', 'exit']                                                                    #|#
            if doing[:4] in acceptable:                                                                              #|#
                break                                                                                                #|#
            else:                                                                                                    #|#
                print("That's not an available bag action")                                                          #|#
                print("Try typing 'use...' or 'drop...' followed by the item of interest")                           #|#
                print("Or 'exit' if you want to quit")                                                               #|#
                                                                                                                     #|#
        ## User Input Interpretation #########################################><######################################|#
        action = doing[:4]                                                                                           #|#
        if action[3] == ' ':                                                                                         #|#
            action = action[:3]                                                                                      #|#
                                                                                                                     #|#   
        focus = doing[4:]                                                                                            #|#
        try:                                                                                                         #|#
            if focus[0] == ' ':                                                                                      #|#
                focus = focus[1:]                                                                                    #|#
        except IndexError:                                                                                           #|#
            focus = 'exit'                                                                                           #|#
                                                                                                                     #|#   
        ## Bag Interaction ###################################################><######################################|#
        bag_inv = [thing for thing in user.bag if type(thing) != str]                                                #|# 
        interactable = [thing.name.lower() for thing in bag_inv]                                                     #|#
                                                                                                                     #|#   
        if focus in interactable:                                                                                    #|#
            location = interactable.index(focus)                                                                     #|#
            using = bag_inv[location]                                                                                #|#
            print('\nYou will {} {} and never be able to get it back.\nAre you sure?'.format(action, focus))         #|#
            yn = intcheck("1 = Yes, 2 = Nevermind: ")                                                                #|#
            print('\n')                                                                                              #|#
            if yn == 1 and action == 'use':                                                                          #|# 
                used = using.use(user)                                                                               #|#
                if used:                                                                                             #|#
                    user.bag.remove(using)                                                                           #|#
            elif yn == 1 and action == 'drop':                                                                       #|#
                user.bag.remove(using)                                                                               #|#
            else:                                                                                                    #|#
                print('You can come back for it later')                                                              #|#
                                                                                                                     #|#
        ## Going Home ########################################################><######################################|#        
        elif focus == 'exit':                                                                                        #|#
            print('Back to the game!')                                                                               #|#
        else:                                                                                                        #|#
            print("Some items can't be used or dropped.\nDon't worry, it won't count towards your weight limit!")    #|#
                                                                                                                     #|#
##############################################################################\/########################################
##############################################################################/\#######################################/   
def item_pickup(user, items_array, options_array, index):
       
    item_options = {0: "Return to game"}
    item_choices = {}
    item_keys = {}
    for key in items_array:
        key_list = list(items_array.keys())
        i = key_list.index(key) + 1
        item_choices[i] = items_array[key]
        item_options[i] = "Add {} to your bag".format(key)
        item_keys[i] = key
    
    while len(items_array) > 0:
        pickup = consider(item_options, "You see the following items around you...")
        if pickup == 0:
            break
        elif pickup in item_options.keys():
            picking = item_choices[pickup]
            if user.bag_check() or type(item_choices[pickup]) == str:
                inventory(user, 'add', item = picking)
                del items_array[item_keys[pickup]]
                del item_options[pickup]
            else:
                print("You can't bear the weight of adding that to your bag right now")
        else:
            handle_it(user, pickup)
                                            
    if len(items_array) == 0:
        del options_array[index] 
        
###############################################################################    
def linebreak(big = False):
    w = 100
    if big == False:
        print('-'*w)
    else:
        print('_'*w)
        print('|'*w)
        print('-'*w)

###################################################################################\
def notnow():                                                                     ##\
    print('Not a good idea right now')                                             #|
                                                                                  ##/
###################################################################################/
def obscure_text(text, level, degree):
    
    skill = 1 - (min(degree, level) / degree)
    
    listed = list(text.upper())
    length = len(listed)
    nchar = int(skill * length)
    
    for i in range(nchar):
        while True:
            to_obscure = rn.randrange(1, length)
            if listed[to_obscure] != '#':
                break
        
        listed[to_obscure] = '#'
    
    return ''.join(listed) 

###############################################################################
def percent_pass(n):
    probability = list(range(n))
    event = rn.randrange(0, 100)
    
    if event in probability:
        return True
    else:
        return False

###################################################################################\
def pause_for_effect():                                                           ##\ 
    input('\nENTER\n\n')                                                           #|
    os.system('cls')                                                               #|
                                                                                  ##/ 
###################################################################################/                                                                              
def rand_build(n, source = False):
    picked = []
    
    if source == False or type(source) != list:
        pick_from = list(range(1, n + 1))
    else:
        pick_from = source
    
    while sum(picked) < n:
        to_go = n - sum(picked)
        possibles = [i for i in pick_from if i <= to_go]
        
        if len(possibles) == 0:
            break
        
        while True:
            x = rn.choice(possibles)
            if sum(picked) + x <= n:
                break
        
        picked.append(x)
        
    return picked

##############################################################################\/#################\        
##############################################################################/\################|#
def run_encounter(intro, user, encounter, enemies, doors, victory, foe_set = False):           #|#
    ##  -  encounter is either a list of enemy counts or a difficulty setting                  #|#
    ##  -  foe_set is a list of enemies to build the encounter with                            #|#
    ##  -  doors is a dictionary of doors to flee through                                      #|#
    ##  -  enemies is a list either given in the room or placed as an input                    #|#
    ##  -  user is the player                                                                  #|# 
    ##  -  intro and victory are text theming                                                 /#|#
    ##########################################################################\/################|#
    ## Creating an Enemies List ##############################################/\################|#
    if enemies == []:                                                                          #|#
        enemies = encounter_build(user, encounter, enemies, foe_set)

    ## Spellcasting Setup ####################################################><################|#        
    if user.role == 'Sorcerer' and len(user.spells) > 0:                                       #|#
        spellcasting = ' or Cast {}(3)'.format(user.spells[0])                                 #|#
    elif user.role == 'Wizard' and len(user.spells) > 0:                                       #|#     
        spellcasting = ''                                                                      #|#
        n = 3                                                                                  #|#
        for i in user.spells:                                                                  #|#
            spellcasting += ' or Cast {}({})'.format(i, n)                                     #|#
            n += 1                                                                             #|#
    else:                                                                                      #|#
        spellcasting = ''                                                                      #|#
                                                                                               #|#
    ##########################################################################\/################|#                                                                                           
    ## THE ENCOUNTER #########################################################/\################|#
    while len(enemies) > 0 and user.health > 0:                                                #|#
        target = enemies[0]                                                                    #|#
                                                                                               #|#
        ## Invocation Setup ##################################################><################|#
        if user.boon != False:                                                                 #|#
            divinity = ' or Invoke the Divinity of {}(5)'.format(user.boon)                    #|#
        else:                                                                                  #|#
            divinity = ''                                                                      #|#

        ## The Top Screen ####################################################><################|#
        top_screen(intro)                                                                      #|#
        health_bar = health_bar_gen(user)
        if user.temp_hp > 0:
            thb = '\nMagical Shield: ' + health_bar_gen(user, th = True)
        else:
            thb = ''
        h_str = space_maintain(3, str(user.health), after = False)
        print("\nHealth: {} - {}{}".format(h_str, health_bar, thb))                            #|#
        for foe in enemies:                                                                    #|#
            f_str = space_maintain(3, str(foe.health), after = False)
            foe_bar = health_bar_gen(foe)
            print('{}\'s Health: {} - {}'.format(foe.name, f_str, foe_bar))                    #|#
                                                                                               #|#
        print("\nAttack(1) or Run(2){}{}".format(spellcasting, divinity))                      #|#
        action = input("> ")                                                                   #|#
                                                                                               #|#
        ## Attacking #########################################################><################|#
        if action == "1":                                                                      #|#
            if user.brute_check(flavor = True):                                                #|#
                user.brutal_swing(enemies)                                                     #|#
            else:                                                                              #|#
                user.attack(target)                                                            #|#
                if target.health <= 0:                                                         #|#
                    enemies.remove(target)                                                     #|#
                                                                                               #|#
        ## Running ###########################################################><################|#    
        elif action == "2":                                                                    #|#
            available_doors = [key for key in doors if doors[key].locked == False]             #|#
            if len(available_doors) > 0:                                                       #|#
                flee_to = rn.choice(available_doors)                                           #|#
                score = 2                                                                      #|#
                break                                                                          #|#
            else:                                                                              #|#
                print("All the doors are locked!. You can't run!")                             #|#
                                                                                               #|#
        ## Spellcasting ######################################################><################|#
        elif action in [str(i + 3) for i in range(len(user.spells))]:                          #|#
            location = ['3', '4'].index(action)                                                #|#
            pick = user.spells[location]                                                       #|#
            casting = pick[:-2]                                                                #|#
            lvl = int(pick[-1])                                                                #|#
            if casting in magic.combat_bonus.keys():                                           #|# 
                magic.combat_bonus[casting](user, user.rmod, lvl)                              #|#
            else:                                                                              #|#
                cast_attempt = user.cast()                                                     #|#
                if cast_attempt[0] == 'miss':                                                  #|#
                    print('Your attack narrowly misses the {}\'s chest!'.format(target.name))  #|#
                                                                                               #|#
                elif cast_attempt[0] in ['hit', 'splash']:                                     #|#
                    attack_power = cast_attempt[1]                                             #|# 
                    magic.combat_attack[casting](user, attack_power, target, lvl)              #|#
                                                                                               #|#
                    ## Damage ################################################><################|#
                    if target.health <= 0:                                                     #|#
                        print('You killed {}!'.format(target.name))                            #|#
                        user.exp += int(target.experience * user.exp_mod)                      #|#
                        user.total_exp += int(target.experience * user.exp_mod)                #|#
                        enemies.remove(target)                                                 #|#
                                                                                               #|#\ 
                    ## Splash Attack ###########################################################|##\
                    if cast_attempt[0] == 'splash' and len(enemies) > 1:                       #\\##\
                        for splashed in [i for i in enemies if i != target]:                   ##\\##\
                            splash_attack = cast_attempt[2]                                    ###############\
                            magic.combat_attack[casting](user, attack_power, splashed, lvl, splash_attack)  ##|
                                                                                               ###############/
                            if splashed.health <= 0:                                           ##//##/
                                print('You killed {}!'.format(splashed.name))                  #//##/
                                user.exp += int(splashed.experience * user.exp_mod)            #|##/
                                user.total_exp += int(splashed.experience * user.exp_mod)      #|#/
                                enemies.remove(splashed)                                       #|#
                                                                                               #|#
        ## Invoke Divinity ###################################################><################|#
        elif action == '5' and user.boon != False:                                             #|#
            magic.invocations[user.boon](user, enemies)                                        #|#
            user.boon = False                                                                  #|#
            user.sacrifice = 0                                                                 #|#
                                                                                               #|#
        ## Catch-all #########################################################><################|#        
        else:                                                                                  #|#
            print("{} mocks your indecision!".format(rn.choice(enemies).name))                 #|#
            user.take_damage(rn.choice([1, 2]))                                                #|#
                                                                                               #|#
        ## Enemies Turn ########################################################################|#                                                                                     
        linebreak()                                                                            #|#
        for foe in enemies:                                                                    #|#
            if foe.level == 'Boss':
                calling = foe.call_for_help()
                if calling != 'None':
                    print('{} is calling for help!'.format(foe.name))
                    enemies = encounter_build(user, calling, enemies, foe_set)
                    enemies.reverse()
                    break                    
            
            strat = foe.strategize(user)                                                       #|#
            if strat == 'attack':                                                              #|#
                foe.attack(user)                                                               #|#
            elif strat == 'cast':                                                              #|#
                curse = magic.foe_spells[foe.spell](foe, user, enemies)                        #|#
                user.take_damage(curse)                                                        #|#
                                                                                               #|#                                                                     
    ##########################################################################\/################|#                                                                                           
    ## Results Evaluation ####################################################/\################|#
    if user.health <= 0:                                                                       #|#
        print('uh oh')                                                                         #|#
        score = 1                                                                              #|#
    elif len(enemies) == 0:                                                                    #|#
        score = 0                                                                              #|# 
        linebreak()                                                                            #|#
        print(text_wrapper(victory, 80))                                                       #|#
        print("Health: {}".format(user.health))                                                #|#
                                                                                               #|#
    ## Temporary Modifiers Reset #############################################><################|#
    user.dam_mod = 1                                                                           #|#
    user.acc_mod = 1                                                                           #|#
    user.temp_hp = 0                                                                           #|#
    user.power_mod = 1                                                                         #|#
                                                                                               #|#
    if user.equipped == 'Steel Bracers':                                                       #|#
        user.dam_bonus = 3                                                                     #|#
    elif user.dam_bonus < 0:                                                                   #|#
        user.dam_bonus = 0                                                                     #|#
                                                                                               #|#
    ## Returns ###############################################################><################|#
    if score == 1:                                                                             #|#
        return False                                                                           #|#
    elif score == 2:                                                                           #|#        
        return doors[flee_to], enemies                                                         #|#
    else:                                                                                      #|#
        return True                                                                            #|#
                                                                                               #|# 
##############################################################################\/################|#
##############################################################################/\#################/
def single_item_pickup(user, item, array, location):
    if type(item) == str:
        n = item
    else:
        n = item.name
    
    yn = intcheck("Pick up the {}?\n1 = Yes, 2 = No: ".format(n))
    if yn == 1:
        if user.bag_check() or type(item) == str:
            inventory(user, 'add', item)
            del array[location]
        elif not user.bag_check():
            print("You can't bear the weight of adding {} to your bag right now".format(n))    

###############################################################################
def space_maintain(n, string, after = True):
    if len(string) > n:
        return string
    else:
        x = list(string)
        while len(x) < n:
            if after:
                x.append(' ')
            else:
                x.insert(0, ' ')
        
        return ''.join(x)

###############################################################################
def stringify(l):
    s = [str(i) for i in l]

    return ''.join(s)                                                            
                                                                                               
###############################################################################                                                                                               
def suspense(text_list, delay = 1, delays = False):
    if delays == False:
        for i in text_list:
            time.sleep(delay)
            print(text_wrapper(i, 80))
            if text_list.index(i) + 1 != len(text_list):
                print('...')
    elif len(text_list) == len(delays):
        for i in range(len(delays)):
            time.sleep(delays[i])
            print(text_wrapper(text_list[i], 80))
            if i != len(delays) - 1:
                print('...')
    else:
        print('delay broken')
        for i in text_list:
            print(i)

###############################################################################                                                                                               
def text_wrapper(text, nchar):
    if nchar == 'offset':
        nchar = 60
        offset = ' ' * 10
    else:
        offset = ''
        
    text = offset + text
    
    end = len(text)
    listed = list(text)
    nbreaks = int(end/nchar) + 1
    margin = int(nchar / 5)
    for i in range(1, nbreaks):
        space = i * nchar
        start_space = space - margin
        end_space = space + margin
        segment = listed[start_space:end_space]
        j_seg = ''.join(segment)
        break_space = j_seg.find(' ')
        if break_space == -1:
            listed.insert(space, '-\n')
            listed.insert(space + 1, offset)
        else:
            final_space = start_space + break_space + 1
            listed.insert(final_space, '\n')
            listed.insert(final_space + 1, offset)
    
    return ''.join(listed) 

###############################################################################
def top_screen(room_desc):
    pause_for_effect()
    
    linebreak(big = True)
    print(text_wrapper(room_desc, 80))
    linebreak()

###################################################################################\
def weapon_fix(weapon, array, index):                                             ##\
    if weapon == False:                                                            ##\
        del array[index]                                                            #|
    else:                                                                           #| 
        array[index] = 'Pick up the {}'.format(weapon.name)                        ##/
                                                                                  ##/
###################################################################################/
def wordify(array):
    
    words = {1: 'a',
             2: 'two',
             3: 'three',
             4: 'four',
             5: 'five',
             6: 'six',
             7: 'seven',
             8: 'eight',
             9: 'nine'}
    
    worded = []
    for i in range(len(array)):
        for key in words:
            if array[i] == key:
                worded.append(words[key])
                
    a = {True: 's',
         False: ''}
    
    b = {'s': '',
         '': 's'}
    
    plurals = [a[i != 1] for i in array]            
    conjugation = [b[i] for i in plurals]
    
    final = []
    for i in range(len(array)):
        final.append(worded[i])
        final.append(plurals[i])
        final.append(conjugation[i])
            
    return final