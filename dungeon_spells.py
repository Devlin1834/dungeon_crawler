# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:18:46 2019

@author: Devlin
"""

# Important note about damage rolls                                #
#                                                                  # 
# Here, because rn.randrange returns from [x, y)                  ##
# y is one larger than max damage                                 ##
# so to find the die roll, subtract one from max                  ##
# FOR BOOSTS
# ONE TIME CAST VS REPEATED CAST? - currently on repeated

import random as rn
import dungeon_foes as foes

###############################################################################
def flavor_print(text, splash):
    if splash == 1:
        print(text)
        
###############################################################################
def damage_roll(base, rolls, die):
    damage = base
    for i in range(rolls):
        damage += rn.randrange(1, die)
        
    return damage

###############################################################################
def bene_cap(stat, bonus, flavor, splash = 1):
    cap = 5 * bonus
    if stat < cap:
        stat += bonus    
        flavor_print(flavor, splash)
    else:
        print("You already have obtained the maximum effect from this spell!")
        
###############################################################################
def witch_bolt(user, power, foe, level, s_factor = 1):
    damage = damage_roll(power, 1, 9)
        
    foe.health -= int(damage * s_factor)
    
    flavor_print("You shoot a bolt of arcane energy at your foe!", s_factor)

###############################################################################
def increase_acc_self(user, power, level):   
    base = {1: .04,
            2: .08,
            3: .12}
    
    
    flavor = {1: "Your fist glows and your weapon begins to gravitate to your foe",
              2: "Your arm glows and your weapon begins to gravitate to your foe",
              3: "Your body glows and your weapon begins to gravitate to your foe"}
    
    mod = max(1, power)
    benefit = (base[level] * mod)
    bene_cap(user.acc_mod, benefit, flavor[level])

###############################################################################
def increase_dam_self(user, power, level):
    base = {1: .05,
            2: .1, 
            3: .15}
    
    flavor = {1: "Your weapon glows a aggressive yellow and your arms become stronger",
              2: "Your weapon glows a violent orange and your arms become stronger",
              3: "Your weapon glows a deadly red and your arms become stronger"}    
    
    mod = max(1, power)
    benefit = (base[level] * mod)
    bene_cap(user.dam_mod, benefit, flavor[level])

###############################################################################    
def decrease_acc_foe(user, power, foe, level, s_factor = 1):
    base = {1: .04,
            2: .06,
            3: .1}
    
    flavor = {1: "Your foe seems dazed and unaware of where you are",
              2: "Your foe reels back confused and dizzy",
              3: "Your foe loses all sense of balance and attacks like a drunk hobbit"}
    
    mod = max(1, power)
    benefit = (base[level] * mod)
    bene_cap(foe.acc_mod, benefit, flavor[level], s_factor)

###############################################################################    
def decrease_dam_foe(user, power, foe, level, s_factor = 1):
    caps = {1: 5,
            2: 7,
            3: 9}
    
    mod = min(caps[level], max(power, 1))
    
    base = {1: .2,
            2: .45,
            3: .7}
    
    flavor = {1: "Your foe has their strength sapped and has trouble lifting their arms",
              2: "Your foe has their strengh sapped and attacks you with minimal effort",
              3: "Your foe slumps on the ground for a moment before struggling to stand up again"}
    
    if foe.dam_mod > .01:
        foe.dam_mod -= ((base[level]  * (mod / caps[level])) * s_factor)
        flavor_print(flavor[level], s_factor)
    else:
        print('Their Damage Can\'t Go Any Lower!')

###############################################################################    
def fireball(user, power, foe, level, s_factor = 1):    
    damage = damage_roll(power, level, 13)
        
    foe.health -= int(damage * s_factor)
    
    flavor = {1: "A small fireball erupts from your hand and singes your foe",
              2: "A fireball spits from your hand and burns your foe",
              3: "A fireball roars from your hand and engulfs your foe before disapearing"}
    
    flavor_print(flavor[level], s_factor)

###############################################################################        
def magic_missle(user, power, foe, level, s_factor = 1):
    m_base = {1: 0.009,
              2: 0.0167,
              3: 0.033}
    
    d_base = {1: 5,
              2: 9,
              3: 13}
    
    foe.acc_mod += (m_base[level] * s_factor * power)
    damage = damage_roll(power, 2, d_base[level])
        
    foe.health -= int(damage * s_factor)
    
    flavor = {1: "A dizzying bolt of energy shoots from your fingertips",
              2: "A dizzying blast of energy shoots from your fingertips",
              3: "A dizzying rocket of energy shoots from your fingertips"}
   
    flavor_print(flavor[level], s_factor)

###############################################################################    
def acid_splash(user, power, foe, level, s_factor = 1):
    m_base = {1: .0167,
              2: .033,
              3: .05}
    
    d_base = {1: 5,
              2: 9, 
              3: 13}
    
    damage = damage_roll(power, 2, d_base[level])
    if foe.dam_mod > .1:
        foe.dam_mod -= (m_base[level] * s_factor * power)
        
    foe.health -= int(damage * s_factor)
    
    flavor = {1: "A corrosive flow of acid runs from your fingertips",
              2: "A corrosive spout of acid shoots from your fingertips",
              3: "A corrosive wave of acid runs erupts your fingertips"}
    
    flavor_print(flavor[level], s_factor)

###############################################################################    
def heal(user, power, level):
    base = {1: .03,
            2: .08,
            3: .13}
    
    mod = max(1, power)
    benefit = base[level] * mod
    factor = int(user.health + (user.max_health * benefit))
    user.health = min(user.max_health, factor)
    
    flavor = {1: "You are engulfed in a soothing aura",
              2: "You are engulfed in an orange sphere of healing energy",
              3: "You are engulfed in a blue aura of healing energy"}
    
    print(flavor[level])

###############################################################################    
def blessing(user, power, level):
    base = {1: .01,
            2: .025, 
            3: .04}
    
    mod = max(1, power)
    benefit = base[level] * mod
    cap = 5 * benefit
    factor = int(user.health + (user.max_health * benefit))
    user.health = min(factor, user.max_health)
    user.acc_mod = min(cap, user.acc_mod + benefit)
    user.dam_mod = min(cap, user.dam_mod + benefit)
    
    print("You wave your hands, raining twinkling light over yourself")

###############################################################################    
def life_drain(user, power, foe, level, s_factor = 1):
    damage = damage_roll(power, level, 7)
        
    damage = int(damage * s_factor)
        
    foe.health -= damage
    user.health = min(user.max_health, user.health + damage)
    
    flavor = {1: "You extend your arm, sucking the life from your foe",
              2: "You extend both arms, sucking the life from your foe",
              3: "A sound like a jet jet stream engulfs the room as your foe's life gets sucked out of them"}
    
    flavor_print(flavor[level], s_factor)

###############################################################################    
def instant_kill(user, power, foe, level, s_factor = 1):
    if s_factor == 1:
        damage = foe.health
    
        foe.health -= damage
        user.health -= damage
        print("A black ball forms in your hand and explodes, hurting you and killing your foe")
        
###############################################################################    
def demon_fire(user, power, foe, level, s_factor = 1):
    damage = damage_roll(power, 6, 9)
        
    foe.health -= int(damage * s_factor)
    
    flavor_print("The room becomes engulfed in fire that devours your foe", s_factor)

###############################################################################        
def divine_gift(user, power, level):
    mod = max(1, power)
    benefit = .1 * mod
    factor = int(user.health + (user.max_health * benefit))
    user.health = min(factor, user.max_health)
    if factor > user.max_health:
        user.temp_hp = int(50 * benefit)
    user.acc_mod += (benefit / 2)
    user.dam_mod += benefit
    print("The roof opens up and a ray of divine light shines upon you")

###############################################################################    
def solar_rays(user, power, foe, level, s_factor = 1):
    user.dam_mod = user.dam_mod * 1.25
    damage = damage_roll(power, 1, 21)
        
    foe.health -= int(damage * s_factor)
    
    flavor_print("A devastating ray of sunlight erupts from your fingertips that intensifies over time", s_factor)

###############################################################################
def payday(user, power, foe, level, s_factor = 1):
    damage = damage_roll(power, 1, 7)
        
    foe.health -= int(damage * s_factor)
    
    flavor_print("A blast of golden energy shoots from your staff, but it doesn't seem to do much damage", s_factor)
    
    if foe.health <= 0:
        user.gold += foe.experience
        print("Upon killing your foe, it explodes into {} gold peices!".format(foe.experience))

###############################################################################
## Foe Spells #################################################################
###############################################################################        
def inflict_wounds(caster, target, team):
    damage = damage_roll(0, 3, 7)
    
    mod = max(1 - (target.rmod / 10), .1)
    target.dam_bonus = max(-5, target.dam_bonus - 1)      
    print("It looks at you fiecely and gashes appear in your arms! You find it harder to fight now")
    return int(damage * mod)

###############################################################################    
def eyebite(caster, target, team):
    damage = damage_roll(0, 8, 9)
    
    mod = max(1 - (target.rmod / 10), .1)
    caster.acc_mod += (1 - mod)    
    print("Its eyes light up and you feel an intense pain throughout your body")
    return int(damage * mod)

###############################################################################
def cloud_of_daggers(caster, target, team):
    mod = max(1 - (target.rmod / 10), .1)
    damage = damage_roll(0, 3, 11)
        
    caster.health += int(damage * mod)
    print("You get a weak feeling inside you - your foe seems to be getting stronger!")
    return int(damage * mod)

###############################################################################
def lich_life(caster, target, team):
    mod = max(1 - (target.rmod / 10), .1)
    pct_taking = (1 - (caster.health / caster.mhealth)) / (len(team) + 1)
    taken = 0
    for mate in team:
        gonna_take = mate.health * pct_taking * mod
        if int(gonna_take) < mate.health:
            taken += gonna_take
            mate.health -= int(gonna_take)
    
    damage = int(target.health * pct_taking * mod)
    taken += damage   
    caster.health += taken
    print("He sucks the life from the room, inclding you!")
    return damage

###############################################################################
def tri_roar(caster, target, team):
    mod = max(1 - (target.rmod / 10), .1)
    benefit = .5 * mod
    
    caster.acc_mod -= benefit
    caster.dam_mod += benefit    
    print("All three heads roar at once giving it the courage to attack more firecely!")
    return 0

###############################################################################
def noble_roar(caster, target, team):
    mod = max(1 - (target.rmod / 10), .1)
    benefit = .25 * mod
    
    for mate in team:
        mate.acc_mod -= benefit
        mate.dam_mod += benefit
    print("It roars a majetsic roar, all the enemies in the room seem bolsered by")
    return 0

###############################################################################
def glare(caster, target, team):
    mod = min(target.rmod / 10, .9) * .3
    target.dam_mod = target.dam_mod * (mod + .6)
    print('It looks at you with peircing yellow eyes and your will to fight drains out of you')
    return 0

###############################################################################
def psionic_bolt(caster, target, team):
    mod = max(1 - (target.rmod / 10), .1)
    damage = damage_roll(0, 6, 7)
        
    save = rn.randrange(1, 21) + target.rmod
    
    print("It shoots a blast of telekinetic force at you!")
    if damage == 36 and save < 15:
        target.intelligence -= 1
        print("It rattles around in your brain, undoing your very identity!")
    
    return int(damage * mod)

###############################################################################
def eldritch_horror(caster, target, team):
    mod = max(1 - (target.rmod / 10), .1)
    multiple = 1 - (mod / 6)
    target.acc_mod = target.acc_mod * multiple
    
    print('A giant shadow covers the path as you feel the vision of a great monstonisty upon your soul!')
    
    return int((len(team) - 1) * mod * 2)

###############################################################################
## Invoke Divinity ############################################################    
###############################################################################
def illenstar(user, foes_list):
    """Create a gust of wind to blow away foes with an exp level based on sacrifice"""
    
    encounter_exps = {}
    for foe in foes_list:
        encounter_exps[foe.experience] = foe
    
    exps_sorted = sorted(encounter_exps.keys())
    total_exp = sum(encounter_exps.keys())
    exp_threshold = total_exp * (user.sacrifice/150)
    if exp_threshold >= total_exp:
        exp_threshold = total_exp - max(exps_sorted)
    
    if len([foe for foe in foes_list if foe.experience < exp_threshold]) == 0:
        print("Your sacrifice wasn't enough to produce any notable effect!")
    elif len(foes_list) == 1:
        print("A stong gust of wind blows through the room but it's not enough to dislodge the {}".format(foes_list[0].name))
    else:
        gust_targets = []    
        while sum(gust_targets) < exp_threshold and len(exps_sorted) > 0:       
            new_target = exps_sorted[0]         
            if new_target + sum(gust_targets) > exp_threshold:
                break
            else:
                gust_targets.append(new_target)
                del exps_sorted[0]
            
        print("A sudden gale blasts open all the doors and the room fills with hurrican force winds!")
        for target_exp in gust_targets:
            target = encounter_exps[target_exp]
            print("The {} got picked up by wind and carried away!".format(target.name))
            foes_list.remove(target)

###############################################################################
def sholan(user, foes_list):
    """takes all foes in a room and meshes them into one with an exp level 
       lower than their sum, based on sacrifice"""
       
    bosses = [i for i in foes_list if i.level == 'Boss']
    
    all_baddies = foes_list.copy()
    for baddie in all_baddies:
        foes_list.remove(baddie)
    
    if len(bosses) < 1:       
        encounter_exp = sum([foe.experience for foe in foes_list])
        factor = 1 - min((user.sacrifice/150), .9)
        exp_target = encounter_exp * factor
        
        walk_time = [abs(exp_target - exp[1]) for exp in foes.foes_exp]    
        location = walk_time.index(min(walk_time))
        new_foe = foes.foes_exp[location][0]
        
        blueprint = [foes.foe_blueprints[new_foe]]
        created_foe = [foes.Enemy(*i) for i in blueprint][0]
                    
        foes_list.append(created_foe)
        for foe in foes_list:
            foe.stunned = True
    
    else:
        foes_list.append(foes.tarrasque)
        
    for foe in foes_list:
        foe.stunned = True
    
    print("\nEnormous ghostly hands appear on both sides of the room. Your enemies")
    print("suddenly gravitate towards each other. Your vision gets a little blurry")
    print("and your foes melt into each other, becoming a ball of molten flesh and")
    print("steel. Gradually it begins to assume a new form, you can see a face in")
    print("the chaos, then legs, then arms. Finally a new foe drops from the air.")
    print("A {} now stands before you, confused, but ready for battle!".format(foes_list[0].name))    

###############################################################################
def nirani(user, foes_list):
    """The room erupts in fire and all foes take damage based on sacrifice"""
    
    damage = damage_roll(user.level, 4, 21)
    
    damage = int(damage * (user.sacrifice / 150))
    
    print("A firestorm errupts around you and engulfs all your foes!")
    firestorm = foes_list.copy()
    for foe in firestorm:
        foe.health -= damage
        if foe.health <= 0:
            print("The {} turned to ash in the firestorm!".format(foe.name))
            foes_list.remove(foe)
            
###############################################################################
def daltos(user, foes_list):
    """The room becomes covered in a thick foliage that reduces foes accuracy 
       and damage based on sacrifice"""
    
    factor = (user.sacrifice / 150) * .75
    for foe in foes_list:
        foe.acc_mod += factor
        foe.dam_mod -= factor
    
    print("The ground begins to shake and suddenly roots and vines start shooting")
    print("out from cracks in the floor! Before long the room is filled with a dense")
    print("folliage that makes it extremely difficult for your foes to hit you or")
    print("deal any significant damage! Amazingly, your {} finds its way through".format(user.weapon.name))
    print("the brush with almost no difficulty")

###############################################################################
def theofen(user, foes_list):
    """Heals you based on sacrifice, stuns low level foes"""
    
    factor = user.sacrifice / 150
    benefit = int(user.max_health * factor)
    user.health += benefit
    
    print("Rays of light shoot out from your eyes and you feel your wounds closing up")
    if user.health > user.max_health:
        diff = user.health - user.max_health
        user.temp_hp = diff
        user.health -= diff
        print("You recieve a protective barrier of pure energy around your body")
        
    encounter_exp = sum([foe.experience for foe in foes_list])
    threshold = encounter_exp * factor
    for foe in foes_list:
        if foe.experience <= threshold:
            foe.stunned = True
            print("The dazzling light stunned the {}".format(foe.name))
    
###############################################################################
def aaramesh(user, foes_list):
    """Deals a lot of damage to the highest level foe in the room. Damage based
       on sacrifice"""
    
    encounter_exps = {}
    for foe in foes_list:
        encounter_exps[foe.experience] = foe    
    exps_sorted = sorted(encounter_exps.keys(), reverse = True)
    
    damage = damage_roll(user.level, 12, 21)
  
    damage = int(damage * (user.sacrifice / 150))
    
    target_exp = exps_sorted[0]
    target = encounter_exps[target_exp]
    
    print("A ghostly figure appears before you, tall and strong with alien blue skin.")
    print("He has the head of a lion but the body of a man, with two sets of arms that")
    print("end in razor sharp claws and muscles enough to rip a drake in half. He roars")
    print("and charges at the {}!\n".format(target.name))
    target.health -= damage
    if target.health <= 0:
        print("The spirit of Aaramesh dealt a fatal blow to the {}!".format(target.name))
        foes_list.remove(target)

###############################################################################
## Maintenance ################################################################
###############################################################################   
combat_bonus = {"Give Accuracy": increase_acc_self,
                "Give Damage": increase_dam_self,
                "Heal": heal,
                "Blessing": blessing,
                "Divine Inspiration": divine_gift}  

combat_attack = {"Decrease Accuracy": decrease_acc_foe,
                 "Decrease Damage": decrease_dam_foe,
                 "Fireball": fireball,
                 "Magic Missle": magic_missle,
                 "Acid Splash": acid_splash,
                 "Life Drain": life_drain,
                 "Instant Kill": instant_kill,
                 "Firestorm": demon_fire,
                 "Solar Rays": solar_rays,
                 "Pay Day": payday,
                 "Witch Bolt": witch_bolt}  

foe_spells = {"Inflict Wounds": inflict_wounds,
              "Eyebite": eyebite,
              "Cloud of Daggers": cloud_of_daggers,
              "Lich Life": lich_life,
              "Tri-Roar": tri_roar,
              "Glare": glare,
              "Psionic Bolt": psionic_bolt,
              "Eldritch Horror": eldritch_horror}

invocations = {"Illenstar": illenstar,
               "Sholan": sholan,
               "Nirani": nirani,
               "Daltos": daltos,
               "Theofen": theofen,
               "Aaramesh": aaramesh}

spell_desc = {"Give Accuracy 1": 'Increase your own accuracy for this combat',
              "Give Accuracy 2": 'Increase your own accuracy for this combat',
              "Give Accuracy 3": 'Increase your own accuracy for this combat',
              "Give Damage 1": 'Increase your own damage for this combat',
              "Give Damage 2": 'Increase your own damage for this combat',
              "Give Damage 3": 'Increase your own damage for this combat',
              "Decrease Accuracy 1": 'Decrease your foe\'s accuracy',
              "Decrease Accuracy 2": 'Decrease your foe\'s accuracy',
              "Decrease Accuracy 3": 'Decrease your foe\'s accuracy',
              "Decrease Damage 1": 'Decrease your foe\'s damage',
              "Decrease Damage 2": 'Decrease your foe\'s damage',
              "Decrease Damage 3": 'Decrease your foe\'s damage',
              "Fireball 1": 'Deal damage with a small fireball',
              "Fireball 2": 'Deal damage with a medium sized fireball',
              "Fireball 3": 'Deal damage with a huge fireball',
              "Magic Missle 1": 'Deal damage and decrease your foe\'s accuracy',
              "Magic Missle 2": 'Deal damage and decrease your foe\'s accuracy',
              "Magic Missle 3": 'Deal damage and decrease your foe\'s accuracy',
              "Acid Splash 1": 'Deal damage and decrease your foe\'s damage',
              "Acid Splash 2": 'Deal damage and decrease your foe\'s damage',
              "Acid Splash 3": 'Deal damage and decrease your foe\'s damage',
              "Heal 1": "Heals you by a % of max health",
              "Heal 2": "Heals you by a % of max health",
              "Heal 3": "Heals you by a % of max health",
              "Blessing 1": "Gives you a bonus to Damage and Accuracy and restores your Health",
              "Blessing 2": "Gives you a bonus to Damage and Accuracy and restores your Health",
              "Blessing 3": "Gives you a bonus to Damage and Accuracy and restores your Health",
              "Life Drain 1": "Deals damage to your foe and heals you by the same amount",
              "Life Drain 2": "Deals damage to your foe and heals you by the same amount",
              "Life Drain 3": "Deals damage to your foe and heals you by the same amount",
              "Instant Kill 4": "Deals damage to both you and your foe equal to your foe's current health",
              "Firestorm 4": "Summons a cloud of fire that engulfs your foe",
              "Divine Inspiration 4": "Gives you huge bonuses to health, accuracy, and damage",
              "Solar Rays 4": "Deals damage and gives you a damage bonus that stacks every time you cast it",
              "Pay Day 4": "Deals a small amount of damage but gives you 100 gold if it kills a foe",
              "Witch Bolt 0": "A very basic spell taught to young students"}


level_1 = [key for key in spell_desc if '1' in key]
level_2 = [key for key in spell_desc if '2' in key]
level_3 = [key for key in spell_desc if '3' in key]
power_spells = [key for key in spell_desc if '4' in key and key != "Pay Day 4"]