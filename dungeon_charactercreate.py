# -*- coding: utf-8 -*-
"""
Created on Thu May 30 05:03:14 2019

@author: Devlin
"""

import random as rn
import dungeon_text as text
from dungeon_text import kit
import dungeon_spells as magic
import table_gen2 as tgen
import math

############################################################################################################################\
### THE CLASS ###############################################################################################################\
##############################################################################################################################\
class character():                                                                                                         ####\ 
    def __init__(self, name, strength, dexterity, constitution, intelligence, charisma, languages, role, race, pweapon):   ####|
        ## General Character Info #############################################################################################|
        self.name = name                                                                                                    ###/ 
        self.role = role                                                                                                   ###/ 
        self.race = race                                                                                                  ###/
        self.languages = languages                                                                                       ###/
        self.proom = 'altar room'                                                                                       ###/
        self.droom = 'altar room'                                                                                      ###/
        self.imortality = False                                                                                       ###/ 
                                                                                                                     ###/  
        ## Strength and Associated Values #############################################################################/
        self.strength = strength                                                                                   ###/
        self.smod = int((self.strength - 10) / 2)                                                                 ###/
        self.carry_bonus = 0                                                                                     ###/
        self.bagsize = max(self.smod * 2, 1) + self.carry_bonus                                                 ###/ 
        self.bag = []                                                                                          ###/
                                                                                                              ###/
        ## Dexterity and Associated Values #####################################################################/
        self.dexterity = dexterity                                                                          ###/
        self.dmod = int((self.dexterity - 10) / 2)                                                         ###/
                                                                                                           ###|
        ## Constitution and Associated Values ################################################################|
        self.constitution = constitution                                                                   ###|
        self.cmod = int((self.constitution - 10) / 2)                                                      ###|
        self.health = self.constitution * 10                                                               ###|
        self.max_health = self.constitution * 10                                                           ###|
        self.temp_hp = 0                                                                                   ###|
        self.health_bonus = 0                                                                              ###|
                                                                                                           ###|  
        ## Intelligence and Associated Values ################################################################|
        self.intelligence = intelligence                                                                   ###|
        self.imod = int((self.intelligence - 10) / 2)                                                      ###|
        self.level = 1                                                                                     ###|
        self.exp = 0                                                                                       ###|
        self.exp_goal = int((100 ** ((self.level/20) + 1))/((self.imod / 10) + 1))                         ###|
        self.total_exp = 0                                                                                 ###|
        self.exp_mod = 1                                                                                   ###|
        self.spells = []                                                                                   ###|
                                                                                                           ###|
        ## Charisma and Associated Values ####################################################################|
        self.charisma = charisma                                                                           ###|
        self.rmod = int((self.charisma - 10) / 2)                                                          ###|
        self.power_mod = 1                                                                                 ###| 
                                                                                                           ###|
        ## Equipped Item Values ##############################################################################|
        self.equipped = ''                                                                                 ###|
                                                                                                           ###|
        ## Gold and Treasure #################################################################################| 
        self.gold = 0                                                                                      ###|
                                                                                                           ###|
        ## Weapon and Combat #################################################################################|
        self.pweapon = pweapon                                                                             ###|
        self.weapon = False                                                                                ###|
        self.base_weapon = False                                                                           ###|
        self.dam_bonus = 0                                                                                 ###|
        self.acc_mod = 1                                                                                   ###|
        self.dam_mod = 1                                                                                   ###|
                                                                                                           ###|
        ## Invoke Divinity ###################################################################################|
        self.boon = False                                                                                  ###|
        self.shrines_found = []                                                                            ###|
        self.sacrifice = 0                                                                                 ###|
        self.piety = 1                                                                                     ###|
                                                                                                           ###|
    ##########################################################################################################|
    ##########################################################################################################|
    def drop_weapon(self):                                                                                 ###|
        self.weapon = self.base_weapon                                                                     ###|
                                                                                                           ###|
    ##########################################################################################################|
    ##########################################################################################################|
    def collect_gold(self, amt, array = False, index = False):                                            ###/
        self.gold += amt                                                                                 ###/ 
        print('You collect {} gold peices!'.format(amt))                                                ###/ 
        print('Gold: ' + str(self.gold))                                                               ###|
        if array != False and index != False:                                                           ###\
            del array[index]                                                                             ###\
                                                                                                          ###\
    ##########################################################################################################| 
    ##########################################################################################################|
    def bag_check(self):                                                                                   ###|
        bag_weight = len([thing for thing in self.bag if type(thing) != str])                              ###|
        if bag_weight < self.bagsize:                                                                      ###|
            return True                                                                                    ###|
        else:                                                                                              ###|
            return False                                                                                   ###|
                                                                                                           ###|
    ##########################################################################################################|
    ##########################################################################################################|
    def weapon_swap(self, new_weapon):
        if new_weapon.expected_damage == self.weapon.expected_damage:
            impact = 'have no impacy on'
        elif new_weapon.expected_damage > self.weapon.expected_damage:
            impact = 'make you stronger in'
        elif new_weapon.expected_damage < self.weapon.expected_damage:
            impact = 'make you weaker in'
    
        if new_weapon.category == self.pweapon or self.role == 'Warrior':
            preffered = ''
            bonus = '+' + str(max(self.dmod, 1)) + ' '
        else:
            preffered = 'not '
            bonus = ''
        
        if new_weapon.category == 'Clubs':
            stun_text = '\nThis weapon gives you a {}% chance to stun'.format(new_weapon.stun)
        else:
            stun_text = ''
    
        damage_text = "Give up you {} for the {}? This will {} combat"
        cat_text = "The {} is {}one of your preffered weapons so it will {}give you a {}damage bonus{}"
        print(damage_text.format(self.weapon.name, new_weapon.name, impact))
        print(cat_text.format(new_weapon.name, preffered, preffered, bonus, stun_text))
    
        yn = kit.intcheck("1 = Yes, 2 = No: ")
        if yn == 1 and self.role != 'Wizard':
            print('You are now equipped with a {}'.format(new_weapon.name))
            old_weapon = self.weapon
            self.weapon = new_weapon
            if old_weapon == self.base_weapon:
                return False
            else:
                return old_weapon
        elif self.role == 'Wizard':
            print('Wizards don\'t wield Weapons!')
            return new_weapon
        else:
            nt_text = "You decide to keep your {}. You can come back for the {} later"
            print(nt_text.format(self.weapon.name, new_weapon.name))
            return new_weapon
    
    ###########################################################################    
    ###########################################################################
    def learn_spell(self, new_spell):
        spell_slots = {'Wizard': 2,
                       'Sorcerer': 1,
                       'Brute': 0,
                       'Spy': 0,
                       'Warrior': 0}
        
        if len(self.spells) < spell_slots[self.role]:
            print(new_spell + ": " + magic.spell_desc[new_spell])
            self.spells.append(new_spell)
            print('You learned {}!'.format(new_spell))
        elif new_spell in self.spells:
            print('You already know that spell, smart guy')
        else:
            print("\n{}: {}".format(new_spell, magic.spell_desc[new_spell]))
            print('\nYou have no available spell slots')
            for e, i in enumerate(self.spells):
                print("{}: {} - {}".format(e + 1, i, magic.spell_desc[i]))
            print("3: Keep your current spells")
            yn = kit.intcheck("\nWhich spell will you replace?\n>> ")
            if yn in range(1, len(self.spells) + 1):
                self.spells[yn - 1] = new_spell
                print('You learned {}!'.format(new_spell))
    
    ###########################################################################
    ###########################################################################            
    def take_damage(self, dam):
        if self.role == 'Sorcerer':
            shrug_pct = int(self.level * (20/3))
            if shrug_pct > 67:
                s_dam = max(self.rmod, 2) * 2
            else:
                s_dam = max(self.rmod, 1) + 2

            if kit.percent_pass(shrug_pct) and dam <= s_dam:
                
                print('\n' + chr(8992) * 44)
                print('You magically absorb power from this attack!')
                print(chr(8993) * 44 + '\n')
                z = rn.randrange(1, 11) / 10
                self.health = min(self.max_health, int(self.health + (dam * z)))
                self.power_mod += (dam / s_dam) * (1 - z)
                dam = 0
                        
        if self.temp_hp > 0:
            if dam > self.temp_hp:
                dam -= self.temp_hp
                self.temp_hp = 0
                self.health -= int(dam)
            else:
                self.temp_hp -= dam
        else:
            self.health -= int(dam)
                                
    ##############################################################################|    
    ##############################################################################\
    def brute_check(self, flavor = False):                                      ###\ 
        boundary =  (self.level / 20) + .2                                      ###| 
        pct_health = self.health / self.max_health                              ###|
        health_check = pct_health <= boundary                                   ###| 
        weapon_check = self.weapon.category == self.pweapon                     ###|
        role_check = self.role == 'Brute'                                       ###|
        rage = 'You become enraged and start swinging with your full might'     ###|
                                                                                ###|
        if role_check and weapon_check and health_check:                        ###|
            if flavor:                                                          ###|
                print('\n' + '!'*58)                                            ###| 
                print(rage)                                                     ###|
                print('!'*58 + '\n')                                            ###|
                                                                                ###|
            return True                                                         ###| 
        else:                                                                   ###|
            return False                                                        ###|
                                                                                ###/
    ##############################################################################/
    ##############################################################################|
    def attack(self, foe):                                                     ###| 
        ## Base Damage ###########################################################|
        damage = self.smod + self.dam_bonus                                    ###|
                                                                               ###| 
        ## Preferred Weapon Bonus ################################################\
        if self.weapon.category == self.pweapon or self.role == 'Warrior':      ###\ 
            damage += max(self.dmod, 1)                                          ###\
                                                                                  ###\
        ## Damage Roll ###############################################################\  
        for i in range(self.weapon.rolls):                                          ###\
            damage += rn.randrange(self.weapon.damagemin, self.weapon.damagemax)     ###\
                                                                                      ###\  
        ## Accuracy Calculation ##########################################################\
        pct_chance = int(math.log(self.dexterity, 30) * 100 * self.acc_mod)             ###\
                                                                                         ###\  
        ## Spy Critical Hit Calculation #####################################################\
        critical = False                                                                   ###\
        if self.role == 'Spy':                                                              ###\
            pct_backstab = int((20/3) * self.level)                                          ###\
            if kit.percent_pass(pct_backstab) and self.pweapon == self.weapon.category:      ###|
                y = rn.randrange(80, 121)                                                    ###|
                backstab_damage = damage * (self.dexterity * (y / 30 / 100))                 ###|
                damage += int(backstab_damage)                                               ###|
                critical = True                                                              ###|
                                                                                             ###|     
        ## Final Damage ########################################################################\ 
        damage = max(int(damage * self.dam_mod), 1)                                           ###\ 
                                                                                               ###\
        ## Warrior Second Wind Calculation ########################################################\
        x = rn.randrange(40, 61) / 100                                                           ###\
        second_wind = int(x * damage * (1 + (self.level / 10)))                                   ###\ 
                                                                                                   ###\
        ## THE ATTACK #################################################################################\
        if kit.percent_pass(pct_chance):                                                             ###\ 
            print(self.weapon.flavor)                                                                 ###\
            foe.health -= damage                                                                       ###\
                                                                                                        ###\
            ## He ded #####################################################################################|
            if foe.health <= 0:                                                                         ###|
                if foe.level == 'Boss':                                                                 ###|
                    a = ''                                                                              ###|
                else:                                                                                   ###|
                    a = 'a '                                                                            ###|
                                                                                                        ###|
                print("You killed {}{}!\n".format(a, foe.name))                                         ###|
                self.exp += int(foe.experience * self.exp_mod)                                          ###|
                self.total_exp += int(foe.experience * self.exp_mod)                                    ###|
                if self.role == 'Warrior':                                                              ###|
                    self.health = min(self.health + second_wind, self.max_health)                       ###|  
                    print('You regain {} health from the thrill of the takedown!'.format(second_wind))  ###|
                                                                                                        ###|
            ## He not dad #################################################################################|
            else:                                                                                       ###|
                if critical:                                                                            ###|
                    print('\n' + chr(9587) * 67)                                                        ###| 
                    print('You land a precise hit on your foe\'s weak spot for critical damage!')       ###| 
                    print(chr(9587) * 67 + '\n')                                                        ###|
                if kit.percent_pass(self.weapon.stun):                                                  ###|
                    print('You stunned {}!\n'.format(foe.name))                                         ###|
                    foe.stunned = True                                                                  ###|
        else:                                                                                           ###|
            print('You Missed!\n')                                                                      ###|
                                                                                                        ###|
    #######################################################################################################|
    #######################################################################################################|    
    def brutal_swing(self, targets):                                                                    ###| 
        damage = self.smod + max(self.dmod, 1) + self.dam_bonus                                         ###|
                                                                                                        ###|
        for i in range(self.weapon.rolls):                                                              ###|  
            damage += rn.randrange(self.weapon.damagemin, self.weapon.damagemax)                        ###|
                                                                                                        ###|
        damage = damage * self.dam_mod                                                                  ###| 
                                                                                                        ###| 
        pct_chance = int(math.log(self.dexterity, 30) * 100 * self.acc_mod)                             ###|
        chance_to_hit = list(range(pct_chance))                                                         ###|
        chance_to_stun = list(range(self.weapon.stun))                                                  ###|
                                                                                                        ###|
        killed = []                                                                                     ###|
        stunned = []                                                                                    ###| 
        assault = targets.copy()                                                                        ###|
        dam_mult = rn.randrange(105, 151) / 100                                                         ###|
        print("You brutally swing your {}, striking every enemy in sight!".format(self.weapon.name))    ###|
        for foe in assault:                                                                             ###| 
            attack_move = rn.randrange(0, 100)                                                          ###|
            stun_move = rn.randrange(0, 100)                                                            ###|
            if attack_move in chance_to_hit:                                                            ###|
                foe.health -= max(int(damage * dam_mult), 1)                                            ###|
                dam_mult = dam_mult * .9                                                                ###|
                if foe.health <= 0:                                                                     ###|
                    killed.append(foe)                                                                  ###|
                    targets.remove(foe)                                                                 ###|
                    self.exp += int(foe.experience * self.exp_mod)                                      ###| 
                    self.total_exp += int(foe.experience * self.exp_mod)                                ###|
                else:                                                                                   ###|
                    if stun_move in chance_to_stun:                                                     ###| 
                        stunned.append(foe)                                                             ###|
                        foe.stunned = True                                                              ###|
            else:                                                                                       ###|
                print('You Missed the {}!\n'.format(foe.name))                                          ###|
                                                                                                        ###|
        for foe in killed:                                                                              ###|
            print("You killed the {}".format(foe.name))                                                 ###/
                                                                                                       ###/
        print()                                                                                       ###/
        for foe in stunned:                                                                          ###/
            print("You stunned the {}".format(foe.name))                                            ###/ 
                                                                                                   ###/
    ##################################################################################################|                                                                                               
    ##################################################################################################|
    def cast(self):
        pct_chance = int(math.log(self.intelligence, 30) * 100 * self.acc_mod)
        if kit.percent_pass(pct_chance):
            power = self.rmod * self.dam_mod + self.dam_bonus * self.power_mod
            self.power_mod = 1
            
            wiz_pct = int(self.level * (20/3))
            if self.role == 'Wizard' and kit.percent_pass(min(67, wiz_pct)):
                print('\n' + chr(8413) * 57)
                print("The other enemies in the room get a taste of your attack!")
                print(chr(8413) * 57 + '\n')
                
                x = rn.randrange(80, 121)
                base = (2 / x) * self.intelligence
                
                if wiz_pct > 67:
                    splash = base * (1 + ((self.level - 10) / 10))
                else:
                    splash = base
                    
                if pct_chance > 100:
                    splash = splash * (1 + ((pct_chance - 100) / 100))
                    
                return ['splash', power, splash]
            
            else:
                return ['hit', power]
        
        else:
            return ['miss']
    
    ##################################################################################################|
    ##################################################################################################|
    def score_modify(self, score, amt):                                                            ###\ 
        if score == 'Strength':                                                                     ###\
            self.strength = max(self.strength + amt, 1)                                              ###\
            self.smod = int((self.strength - 10) / 2)                                                 ###\
            self.bagsize = max(self.smod * 2, 1) + self.carry_bonus                                    ###\
                                                                                                        ###\
        elif score == 'Dexterity':                                                                       ###\
            self.dexterity = max(self.dexterity + amt, 1)                                                 ###\ 
            self.dmod = int((self.dexterity - 10) / 2)                                                     ###\
                                                                                                            ###\ 
        elif score == 'Constitution':                                                                        ###|
            self.constitution = max(self.constitution + amt, 1)                                              ###|
            self.cmod = int((self.constitution - 10) / 2)                                                    ###|
            self.max_health = (self.constitution * 10) + self.health_bonus                                   ###|
            if amt > 0:                                                                                      ###|
                self.health += amt * 10                                                                      ###|
                                                                                                             ###|
        elif score == 'Intelligence':                                                                        ###|
            self.intelligence = max(self.intelligence + amt, 1)                                              ###|
            self.imod = int((self.intelligence - 10) / 2)                                                    ###|
            self.exp_goal = int((100 ** ((self.level/20) + 1))/((self.imod / 10) + 1))                       ###|
        
        elif score == 'Charisma':
            self.charisma = max(self.charisma + amt, 1) 
            self.rmod = int((self.charisma - 10) / 2)
            
        elif score == 'Spirit of Thesselhydra':
            self.intelligence = max(self.intelligence + amt, 1)                                              ###|
            self.imod = int((self.intelligence - 10) / 2)                                                    ###|
            self.exp_goal = int((100 ** ((self.level/20) + 1))/((self.imod / 10) + 1))                       ###|
            self.charisma = max(self.charisma + amt, 1) 
            self.rmod = int((self.charisma - 10) / 2)
            self.dexterity = max(self.dexterity + amt, 1)                                                    ###| 
            self.dmod = int((self.dexterity - 10) / 2)

        elif score == 'Piety':
            self.piety += amt                                                     
            
        elif score == 'Visage of Horror':
            self.dam_bonus += amt
            self.weapon.stun += 2 * amt
            camt = max(amt - 3, 1)
            self.constitution = max(self.constitution + camt, 1)                                             ###|
            self.cmod = int((self.constitution - 10) / 2)                                                    ###|
            self.max_health = (self.constitution * 10) + self.health_bonus                                   ###|
            if camt > 0:                                                                                     ###|
                self.health += camt * 10                                                                     ###|
                                                                                                             ###|  
        elif score == 'Max Health':                                                                          ###|
            self.max_health = max(self.max_health + amt, 1)                                                  ###|
            self.health_bonus += amt                                                                         ###| 
                                                                                                             ###|
        elif score == 'Health':                                                                              ###| 
            self.health = min(max(self.health + amt, 1), self.max_health)                                    ###|
                                                                                                             ###|
        elif score == 'Gold':                                                                                ###|
            self.gold = max(self.gold + amt, 0)                                                              ###|
                                                                                                             ###|
        elif score == 'Damage':                                                                              ###|
            self.dam_bonus += amt                                                                            ###|
                                                                                                             ###\ 
        elif score == 'Experience':                                                                           ###\     
            self.exp_mod += amt                                                                                ###\
                                                                                                                ###\ 
        elif score == 'Bag Size':                                                                                ###\ 
            self.carry_bonus += amt                                                                               ###\
                                                                                                                   ###\
    ###################################################################################################################\
    ####################################################################################################################\
    def pray(self, god, flavor, array):                                                                               ###\
        print("You approach the shrine to pray...\n")                                                                  ###\
        print(kit.text_wrapper(flavor, 80))                                                                             ###\
        gh = kit.intcheck("\nWhat will you sacrifice?\n1 = Gold, 2 = Health, 3 = Nothing: ")                             ###\
        if gh == 1:                                                                                                       ###\ 
            while True:
                s_text = "How much gold will you sacrifice? (You have {}): "                                                   ###\ 
                tribute = min(self.gold, kit.intcheck(s_text.format(self.gold))) * self.piety                                                ###\ 
                if tribute > 600:
                    print('{} appreciates your zeal but sacrifices over 600 are too much!'.format(god))
                    if self.piety > 1:
                        print("Don't forget your equipement increases the strength of your sacrifice by {}x".format(self.piety))
                else:
                    self.gold -= tribute                                                                                             ###\
                    break
            print("You watch as {} gold peices fly out of your bag and dissapear into thin air".format(tribute))             ###|
            print("You feel a warmth thoughout your chest and weight lift off your shoulders")                               ###|
            self.boon = god                                                                                                  ###|
            self.sacrifice = (tribute / 4)                                                                                   ###|
            array.append(god)                                                                                                ###|  
        elif gh == 2:                                                                                                        ###| 
            while True:                                                                                                      ###|
                s_text = "How much health will you sacrifice? (You have {}): "                                               ###|
                self.sacrifice = kit.intcheck(s_text.format(self.health)) * self.piety                                       ###|
                if self.sacrifice >= self.health:                                                                            ###/
                    print("This will literally kill you. Rethink that")                                                     ###/
                elif self.sacrifice > 150:
                    print('{} appreciates your zeal but sacrifices over 150 are too much!'.format(god))
                    if self.piety > 1:
                        print("Don't forget your equipement increases the strength of your sacrifice by {}x".format(self.piety))
                else:                                                                                                      ###/
                    self.health -= self.sacrifice                                                                         ###/  
                    break                                                                                                ###/
            print("You pick up the ceremonial knife from the shrine and make a cut into your hand")                     ###/
            print("You feel pain at first but then a sudden warmth and feeling of peace")                              ###/  
            self.boon = god                                                                                           ###/
            array.append(god)                                                                                        ###/
        else:                                                                                                       ###/
            print("You decide to stop praying")                                                                    ###/
                                                                                                                  ###/
    ################################################################################################################|
    ################################################################################################################|
    def level_up(self, amt):                                                                                     ###|
        kit.pause_for_effect()                                                                                   ###|
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~You Level up!~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')       ###|
        points_to_give = amt                                                                                     ###|
        score_bonuses = [0, 0, 0, 0, 0]                                                                          ###|
        stats = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Charisma']                            ###|
        scores = [self.strength, self.dexterity, self.constitution, self.intelligence, self.charisma]            ###|
        print("Which stats will you give points to?")                                                            ###|  
        while points_to_give > 0:                                                                                ###|
            for i in range(5):                                                                                   ###|
                while True:                                                                                      ###|
                    print('\nPoints left: {}'.format(points_to_give))                                            ###|
                    s = kit.intcheck('{} ({}): '.format(stats[i], scores[i]))                                    ###|
                    if s <= points_to_give and s >= 0:                                                           ###|
                        score_bonuses[i] = s                                                                     ###|
                        points_to_give -= s                                                                      ###|
                        break                                                                                    ###|
                                                                                                                 ###|
        self.level += 1                                                                                          ###|
        self.exp -= self.exp_goal                                                                                ###|                                                                    
        self.exp_goal = int((100 ** ((self.level/20) + 1))/((self.imod / 10) + 1))                               ###|
                                                                                                                 ###|
        for i in range(5):                                                                                       ###| 
            self.score_modify(stats[i], score_bonuses[i])                                                        ###|
                                                                                                                 ###| 
    ################################################################################################################|
    ################################################################################################################\
    def __str__(self):                                                                                            ###\
        
        name_line = "{} the {} {}".format(self.name, self.race, self.role)
        lang_line = "\nYou speak {}".format(' and '.join(self.languages))
        exp_line = "\n\nLevel {}: {}/{} ({})".format(self.level, self.exp, self.exp_goal, self.total_exp)
        health_line = "\nHealth: {}/{}".format(self.health, self.max_health)
        weapon_line = "\nWielding: {}".format(self.weapon.name)
        gold_line = "\nGold: {}".format(self.gold)
        str_line = "\n\nStrength: {}".format(self.strength)
        dex_line = "\nDexterity: {}".format(self.dexterity)
        con_line = "\nConstitution: {}".format(self.constitution) 
        int_line = "\nIntelligence: {}".format(self.intelligence)
        cha_line = "\nCharisma: {}".format(self.charisma)  
        
        if self.equipped != '':
            eqp_line = "\nEquipped: {}".format(self.equipped.name)
        else:
            eqp_line = ''
        
        if self.brute_check():
            skill_line = "\nBrutal Swings: Ready"
        elif self.role == "Brute" and not self.brute_check():
            skill_line = "\nBrutal Swings: Not Ready"
        elif self.role == "Warrior":
            skill_line = "\nSecond Wind: Half Damage + {}%".format((self.level / 10) * 100)
        elif self.role == "Spy": 
            pct = int((20/3) * self.level)
            bsd = int(self.dexterity * (100 / 30))
            skill_line = "\nCrit Chance: {}%\nCrit Damage: Damage +{}%".format(pct, bsd)
        elif self.role == "Sorcerer" and len(self.spells) == 0:
            skill_line = "\nSpell Slot Open"
        elif self.role == "Sorcerer" and len(self.spells) > 0:
            skill_line = "\nSpell: {}".format(self.spells[0])
        elif self.role == 'Wizard':
            if len(self.spells) == 0:
                skill_line = "\nSpell Slots Open"
            elif len(self.spells) == 1:
                skill_line = "\nSpell 1: {}\nSpell Slot 2 Open".format(self.spells[0])
            else:
                skill_line = "\nSpell 1: {}\nSpell 2: {}".format(self.spells[0], self.spells[1]) 
                                                                                                               ###/
        character_desc = [name_line,                                                                          ###/
                          lang_line,                                                                         ###/
                          exp_line,                                                                         ###/
                          skill_line,                                                                      ###/ 
                          health_line,                                                                    ###/
                          weapon_line,                                                                   ###/
                          eqp_line,                                                                     ###/
                          gold_line,                                                                   ###/
                          str_line,                                                                   ###/
                          dex_line,                                                                  ###/
                          con_line,                                                                 ###/
                          int_line,                                                                ###/
                          cha_line]                                                               ###/
                                                                                                 ###/
        return ''.join(character_desc)                                                          ###/
                                                                                               ###/
#################################################################################################/ 
### CREATION ###################################################################################/
###############################################################################################/
races = {'Human': {'scores': [1, 0, 0, 1, 0],
                   'Language': 'Choose One'}, 
         'Gnome': {'scores': [-1, 3, -1, 0, 1],
                   'Language': 'Gnomish'}, 
         'Orc': {'scores': [2, 0, 2, -1, -1],
                 'Language': 'Orcish'}, 
         'Elf': {'scores': [0, 1, -1, 2, 0],
                  'Language': 'Elvish'},
         'Tiefling': {'scores': [-1, 1, 0, 0, 2],
                      'Language': 'Infernal'}}

roles = {'Warrior': {'Weapon': 'All',
                     'Skill': 'Regains health on the kill, can use every weaopn'},
         'Spy': {'Weapon': 'Daggers',
                 'Skill': 'Gets a bonus to accuracy and evasion, extra accuracy becomes a chance to crit'},
         'Brute': {'Weapon': 'Clubs',
                   'Skill': 'Can attack all enemies at once when in danger'},
         'Wizard': {'Weapon': 'None',
                    'Skill': '2 Spell Slots, can deal splash damage with spells'},
         'Sorcerer': {'Weapon': 'Staffs',
                      'Skill': '1 Spell Slot, has chance to shrug off low damage attacks'}}
        
###############################################################################  
###############################################################################
def char_create():
    kit.pause_for_effect()
    kit.linebreak(big = True)
    print("Let's Create a Character")
    print("\nFirst we'll get stats")
    print(text.stats_explanation)
    kit.pause_for_effect()
    
    sets = []
    for i in range(5):
        stats = []
        for stat in range(5):
            rolls = [rn.randrange(1, 7) for roll in range(4)]
            stats.append(sum(rolls) - min(rolls))
        sets.append(stats)
        
    snames = ['Set 1', 'Set 2', 'Set 3', 'Set 4']
    rname = ['Roll 1', 'Roll 2', 'Roll 3', 'Roll 4', 'Roll 5']
    int_lists = [[str(s) for s in i] for i in sets]        
    
    kit.linebreak(big = True)
    print("\nPick one of these sets to apply to your stats")
    tgen.table_gen(rname, snames, int_lists)
    
    while True:
        pick = kit.intcheck("Input the number of your choice: ")
        if pick - 1 in range(4):
            break
    
    set_choice = sets[pick - 1]
    
    to_fill = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Charisma']
    order = []
    
    for i in to_fill:
        print('Which score should be assigned to ' + i + '?\n')
        print(*set_choice, sep = '\n')
        while True:
            try:
                choice = int(input(">> "))
            except ValueError:
                print("That's not one of your rolls")
            else:
                if choice not in set_choice:
                    print("That's not one of your rolls")
                else:
                    order.append(choice)
                    set_choice.remove(choice)
                    break
    
    ##-----------------------------------------------------------------------##   
    all_races = [key for key in races]
    langs = [races[key]['Language'] for key in races]
    skill_mods = [races[key]['scores'] for key in races]
    for i in range(5):
        skill_mods[i] = [str(x) for x in skill_mods[i]]
    for i in range(5):
        skill_mods[i].insert(0, langs[i])
    rnames = [x for x in to_fill]
    rnames.insert(0, 'Language')
    
    while True:
        kit.pause_for_effect()
        kit.linebreak(big = True)
        print(text.races_explanation)
        tgen.table_gen(rnames, all_races, skill_mods)
        race = input("\n>> ")
        if race not in races.keys():
            print("That's not a valid race")
        else:
            print(kit.text_wrapper(text.races_flavor[race], 80))
            n = ['n' for i in [race] if i in ['Orc', 'Elf']]
            yn = kit.intcheck("\nPlay as a{} {}?\n1 = Yes, 2 = No: ".format(''.join(n), race))
            if yn == 1:
                break
        
    skills = [x + y for x,y in zip(order, races[race]['scores'])]
    
    bonus_langs = ['Gnomish', 'Orcish', 'Elvish', 'Infernal', 'Dwarvish', 'Draconic']
    linguistics = ['Common']
    if races[race]['Language'] == 'Choose One':
        print('\nYou get to pick one language from this list:')
        print(*bonus_langs, sep = '\n')
        
        while True:
            new_lang = input('\n>> ')
            if new_lang not in bonus_langs:
                print('No one speaks that here')
            else:
                break
        
        linguistics.append(new_lang)
    
    else:
        linguistics.append(races[race]['Language'])
        
    
    ##-----------------------------------------------------------------------##    
    while True:
        kit.pause_for_effect()
        kit.linebreak(big = True)
        print(text.classes_explanation)
        for key in roles:
            print('\n-' + key + '-')
            print('Preffered Weapon: ' + roles[key]['Weapon'])
            print('Class Skill: ' + roles[key]['Skill'])
        role = input("\n>> ")
        if role not in roles.keys():
            print("That' not a valid class")
        else:
            print(kit.text_wrapper(text.classes_flavor[role], 80))
            yn = kit.intcheck("\nPlay as a {}?\n1 = Yes, 2 = No: ".format(role))
            if yn == 1:
                break
    
    ##-----------------------------------------------------------------------##
    kit.pause_for_effect()
    kit.linebreak(big = True)
    name = input("\nNow your name >> ")
    
    finished = character(name, 
                         skills[0], 
                         skills[1], 
                         skills[2], 
                         skills[3], 
                         skills[4], 
                         linguistics, 
                         role, 
                         race, 
                         roles[role]['Weapon'])
    return finished