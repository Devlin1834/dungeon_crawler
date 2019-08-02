# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:48:03 2019

@author: Devlin
"""
import random as rn
import math

###############################################################################
class Enemy():
    def __init__(self, name, health, damagemax, rolls, flavor, level, experience, spell = None, spell_ratio = 0):
        self.name = name
        self.health = health
        self.mhealth = health
        self.damagemin = 1
        self.damagemax = damagemax
        self.rolls = rolls
        self.flavor = flavor
        self.acc_mod = 1    # Bigger means less accuracy, unlike player
        self.dam_mod = 1    # Bigger means more damage, just like player
        self.stunned = False
        self.experience = experience
        self.level = level
        self.spell = spell
        self.spell_ratio = spell_ratio
    
    ## STRATEGIZING ###########################################################    
    def strategize(self, foe):
        if self.stunned == False:    
            pct_base = {'Spy': 15,
                        'Brute': 30,
                        'Warrior': 30,
                        'Wizard': 30,
                        'Sorcerer': 30}
             
            pct_chance = int(math.log(foe.dexterity, pct_base[foe.role]) * 50)  
            chance_to_miss = list(range(pct_chance))
            attack_move = rn.randrange(0, 100)
            if attack_move not in chance_to_miss:
                move = list(range(self.spell_ratio))
                strategy = rn.randrange(0, 100)
                if strategy in move:
                    return 'cast'
                else:
                    return 'attack'
            else:
                print(self.name + " missed!")
                return 'miss'
        else:
            print("{} is stunned and can't attack!".format(self.name))
            self.stunned = False
            return 'miss'
        
    ## ATACKING ###############################################################
    def attack(self, foe):
        if self.level == 'Boss':
            t = ''
            if self.name in ['Lyestra', 'Halenhadra']:
                h = 'her'
            else:
                h = 'his'
        else:
            t = 'The '
            h = 'its'
        
        damage = 0
        for i in range(self.rolls):
            damage += rn.randrange(self.damagemin, self.damagemax)
            
        damage = int(damage * self.dam_mod)           
        print('\n{}{} attacks you with all {} might!'.format(t, self.name, h))
        print(self.flavor)
        foe.take_damage(damage)
            
###############################################################################
class BBEG(Enemy):
    def __init__(self, name, desc, title, health, damagemax, rolls, statue, flavor, spell, spell_ratio):
        self.name = name
        self.desc = desc
        self.title = title
        self.health = health
        self.mhealth = health
        self.damagemin = 1
        self.damagemax = damagemax
        self.rolls = rolls
        self.statue = statue
        self.acc_mod = 1    # Bigger means less accuracy, unlike player
        self.dam_mod = 1    # Bigger means more damage, just like player
        self.flavor = flavor
        self.spell = spell
        self.spell_ratio = spell_ratio
        self.stunned = False
        self.level = 'Boss'
        self.help = [True for i in range(4)]
        self.experience = 450

    def call_for_help(self):
        health_ratio = round(self.health/self.mhealth, 2)

        if health_ratio < .75 and self.help[0]:
            self.help[0] = False
            self.health += int(.1 * self.mhealth)
            return 'Easy'
        elif health_ratio < .5 and self.help[1]:
            self.help[1] = False
            self.health += int(.2 * self.mhealth)
            return 'Medium'
        elif health_ratio < .25 and self.help[2]:
            self.help[2] = False
            self.health += int(.3 * self.mhealth)
            return 'Hard'
        elif health_ratio < .1 and self.help[3]:
            self.help[3] = False
            self.health += int(.5 * self.mhealth)
            return 'Killer'
        else:
            return 'None'
        
###############################################################################
pixie = Enemy('Pixie', 4, 11, 4, 'The pixie shoots you with a magical ray of light! It really hurts!', 0, 4)
mimic = Enemy('Mimic', 75, 11, 2, 'It outstreches...somehing...and smacks you across the face with it!', 3, 108)
wall = Enemy("Wall", 130, 1, 0, "It just sits there...", 0, 0)
tarrasque = BBEG("Tarrasque", '', '', 350, 11, 10, '', "It stomps like a beast possesed by murderous rage, all while swinging its tail and gnashing it's teeth!", '', 0)
pit_m = [["Pit Monster", 65, 5, 3, 'It swipes at you from the safety of its pit!', 3, 87.5]]
mind_flayer = [["Mind Flayer", 35, 5, 4, 'It wants to eat your brain!', 3, 150, 'Psionic Bolt', 65]]
minotaur = [["Minotaur", 60, 7, 6, "It swings its mighty battle axe with ferocious strength!", 3, 123]]

foe_blueprints = {'Skeleton': [25, 7, 1, 'SMACK!', 1],
                  'Wolf': [10, 9, 2, 'KERPOW!', 1],
                  'Snarl Demon': [16, 13, 1, 'KAPLASH!', 1],
                  'Drakeling': [21, 5, 2, 'FIRE BLAST!', 1],
                  'Goblin': [15, 7, 2, 'SCHWING', 1],
                  'Ghoul': [43, 7, 3, 'Ghostly claws come from nowhere and cut into your skin', 2],
                  'Manticore': [25, 11, 3, 'You lose track of one of the heads and it strikes!', 2],
                  'Shadow Demon': [34, 9, 3, 'He pops out of a dark corner and surpises you with a THWACK', 2],
                  'Drake': [37, 5, 5, 'He shoots fire at you with deadly accuracy!', 2],
                  'Goblin Chief': [36, 13, 2, 'He charges at you with ferocity and hatred', 2],
                  'Vampireling': [67, 7, 5, 'Its sharp fingernails cut you slightly but it feels like a much deeper wound', 3, "Inflict Wounds", 33],
                  'Chimera': [46, 7, 7, 'It jabs you with its poisonous tail', 3, "Tri-Roar", 25],
                  'Floating Eyes': [57, 21, 2, 'You BEHOLD as the eyes shoot lasers at you, burning your skin', 3, "Eyebite", 10],
                  'Young Dragon': [52, 9, 5, 'He breaths fire with no effort at all, scorching the ground, and you with it', 3, "Glare", 10],
                  'Goblin Mercenary': [61, 13, 3, 'He takes precise aim and swings right at your most vulnerable point', 3, "Inflict Wounds", 33],
                  'Lich': [71, 9, 8, 'He holds a finger up and drains all the life from the room', 4, "Lich Life", 20],
                  'Adult Dragon': [99, 9, 6, 'Fire erupts from his mouth but only to distract you as he swipes at you with his enormous claws', 4, "Glare", 20],
                  'Mummy': [81, 11, 6, 'He breathes a cloud of spores that slow you down just long enouch for him to wrap his hands around your neck', 4, "Cloud of Daggers", 25],
                  'Sphynx': [85, 21, 5, 'He grabs you in it\'s mouth and tosses you around the room', 4, "Glare", 20],
                  'Jewled Skull': [90, 5, 12, 'It disapeares into thin air, a moment later you\'re struck by a bolt of lightning', 4, "Eyebite", 25]}

for key in foe_blueprints:
    foe = foe_blueprints[key]
    foe.insert(0, key)
    exp = int(foe[1] + ((foe[2] / 2) * foe[3] * foe[5]))
    foe.insert(6, exp)
    
foes_exp = [[key, foe_blueprints[key][6]] for key in foe_blueprints]

all_foes = list(foe_blueprints.keys())