# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:26:34 2019

@author: Devlin
"""

import random as rn
import dungeon_text as text
import dungeon_toolkit as kit
import dungeon_spells as magic
import dungeon_foes as foes

## Final Bosses ###############################################################
BOSSES = {'John': foes.BBEG('Ser John', text.bbeg_john, 'The Sunderfoe Slayer', 225, 13, 6, text.statue_john, text.attack_john, 'Eldritch Horror', 15),
          'Jaggard': foes.BBEG('Jagard', text.bbeg_jaggard, 'The Lich King', 210, 11, 8, text.statue_john, text.attack_jaggard, '', 20),
          'Halenhadra': foes.BBEG('Halenhadra', text.bbeg_halenhadra, 'The Spider Queen', 215, 21, 4, text.statue_john, text.attack_halenhadra, '', 20),
          'Ulldar': foes.BBEG('Ulldar Kang', text.bbeg_ulldar, 'The Druid King', 265, 13, 5, text.statue_john, text.attack_ulldar, '', 20),
          'Lyestra': foes.BBEG('Lyestra', text.bbeg_lyestra, 'The Haq Queen', 230, 5, 15, text.statue_john, text.attack_lyestra, '', 20),
          'Urumbrior': foes.BBEG('Urumbrior', text.bbeg_urumbrior, 'The Heir of Darkness', 235, 7, 10, text.statue_john, text.attack_urumbrior, '', 20)}

###############################################################################\
## THE CLASS ##################################################################|
###############################################################################/
class Game():
      
    ###########################################################################
    def doors_generate(self, paths, locks):       
        door_range = len(text.door_short)
        array = {}
        
        for way in paths:
            index = rn.randrange(0, door_range)
        
            description = text.door_desc[index]
            trans_text = text.door_trans[index]
            bar_text = text.door_barred[index]
            unlock_text = text.door_unlock[index]
            short_text = text.door_short[index]
            
            d = kit.Door(description, trans_text, bar_text, unlock_text, short_text)
            d.rooma = paths[way][0]
            d.roomb = paths[way][1]
            if way in locks:
                d.locked = True
            
            array[way] = d
            
        return array
                
    ###########################################################################
    def potion_gen(self):
        potion_range = len(text.potion_names)
        index = rn.randrange(0, potion_range)
            
        real = text.potion_names[index]
        description = text.potion_flavors[index]
        effecting = text.potion_stats[index]
        effect = rn.randrange(text.potion_lower[index], text.potion_upper[index])
        huh = rn.choice(text.potion_masks)
        
        return kit.Potion(real, description, effecting, effect, huh)
    
    ###########################################################################
    def food_gen(self):
        food_range = len(text.food_names)
        index = rn.randrange(0, food_range)
        
        name = text.food_names[index]
        desc = text.food_flavor[index]
        heal = rn.randrange(1, 26)
        
        return kit.Food(name, desc, heal)
    
    ###########################################################################
    def items_populate(self, array, food = 0, potions = 0):
        
        funcs = {0: self.food_gen,
                 1: self.potion_gen}
        
        r = [food, potions]
        
        for i in range(2):
            for x in range(r[i]):
                while True:
                    obj = funcs[i]()
                    if obj.name not in array.keys():
                        array[obj.name] = obj
                        break
    
    ###########################################################################
    def __init__(self, game_id):      
   
    ##########################\ 
    ### __init__ Game Setup ###################################################
    ##########################/
        
        ## Plot ##
        self.game_id = game_id
        self.ritual = text.game_rituals[self.game_id]
        self.game_lore = kit.avoid_duplicates(21, text.lore)
        self.statuary = kit.avoid_duplicates(9, text.statues)
        self.bbeg = BOSSES[self.game_id]
        
        ## Shrines ##
        self.shrines = ['temple', 'uwater', 'lava', 'wfall', 'pantry', 'upit']
        self.gods = kit.avoid_duplicates(6, ['Illenstar', 'Nirani', 'Aaramesh', 'Daltos', 'Theofen', 'Sholan'])
        self.god_rooms = {}
        for i in range(6):
            self.god_rooms[self.shrines[i]] = self.gods[i]        
        
        ## Doors ##
        connections = {1: ['altar room', 'temple'],
                       2: ['altar room', 'fountains'],
                       3: ['temple', 'catacombs'],
                       4: ['temple', 'tower'],
                       5: ['fountains', 'pit'],
                       6: ['fountains', 'antechamber'],
                       7: ['catacombs', 'pantry'],
                       8: ['catacombs', 'ice'],
                       9: ['pantry', 'kennel'],
                       10: ['kennel', 'ice'],
                       11: ['ice', 'lava'],
                       12: ['lava', 'dungeon'],
                       13: ['lava', 'vines'],
                       14: ['dungeon', 'cliff'],
                       15: ['cliff', 'library'],
                       16: ['cliff', 'portal'],
                       17: ['vines', 'lpit'],
                       18: ['library', 'upit'],
                       19: ['kennel', 'barracks'],
                       20: ['barracks', 'mess'],
                       21: ['antechamber', 'wfall'],
                       22: ['antechamber', 'srow'],
                       23: ['srow', 'garden'],
                       24: ['wfall', 'garden'],
                       25: ['antechamber', 'library']}
        
        locked = [6, 12, 16, 19]
        
        self.doors = self.doors_generate(connections, locked)
        
    #####################\     
    ### __init__ Rooms ########################################################
    #####################/
     
        ## Altar Room ##
        self.altar_wall = rn.choice(text.wall_ornaments)
        self.altar_door1 = self.doors[1]
        self.altar_door2 = self.doors[2]
        self.altar_complete = text.altar_evil[self.game_id]
        
        ## Temple ##
        self.temple_statue1 = self.statuary[0]
        self.temple_statue2 = self.bbeg.statue
        self.temple_phrase = rn.choice(text.temple_passphrases)
        self.temple_door1 = self.doors[1]
        self.temple_door2 = self.doors[3]
        self.temple_door3 = self.doors[4]
                
        ## Fountain ## 
        self.fountain_door1 = self.doors[2]
        self.fountain_door2 = self.doors[5]
        self.fountain_door3 = self.doors[6]
        self.fountain_spell = rn.choice(magic.level_1)
        
        ## Underwater ##
        
        ## Tower ##
        self.tower_door1 = self.doors[4]
        self.tower_contents = text.tower_builds[self.game_id][0]
        self.tower_interest = text.tower_builds[self.game_id][1]
        self.tower_int_inv = text.tower_builds[self.game_id][2]
        self.tower_scroll = text.tower_builds[self.game_id][3]
        self.tower_item = text.tower_builds[self.game_id][4]
        self.tower_book = self.game_lore[0]
        self.tower_spell1 = rn.choice(magic.level_1)
        self.tower_spell2 = rn.choice(magic.level_1)
        
        ## Lab ##
        self.lab_book = self.game_lore[1] 
        
        ## Catacombs ##
        self.catacombs_door1 = self.doors[3]
        self.catacombs_door2 = self.doors[7]
        self.catacombs_door3 = self.doors[8]
        self.catacombs_spell = rn.choice(magic.level_1)
        
        ## Pantry ##
        self.pantry_door1 = self.doors[7]
        self.pantry_door2 = self.doors[9]
        self.pantry_book = self.game_lore[2]
        self.pantry_wall = foes.wall
        
        ## Kennel ##
        self.kennel_door1 = self.doors[9]
        self.kennel_door2 = self.doors[10]
        self.kennel_door3 = self.doors[19]
        self.kennel_spell = rn.choice(magic.level_2)
        self.kennel_scroll = text.kennel_plot_scroll[self.game_id]
        
        ## Barracks ##
        self.barracks_door1 = self.doors[19]
        self.barracks_door2 = self.doors[20]
        self.barracks_note = text.barracks_plot_note[self.game_id]
        self.barracks_book1 = self.game_lore[3]
        self.barracks_book2 = self.game_lore[4]
        
        ## Mess ##
        self.mess_door1 = self.doors[20]
        self.mess_spell1 = rn.choice(magic.level_2)
        self.mess_spell2 = rn.choice(magic.level_3)
        self.mess_scroll = text.mess_plot_scroll[self.game_id]
        self.mess_book = self.game_lore[5]
        
        ## Ice ##
        self.ice_door1 = self.doors[8]
        self.ice_door2 = self.doors[10]
        self.ice_door3 = self.doors[11]
        self.ice_book1 = self.game_lore[6]
        self.ice_book2 = self.game_lore[7]
        self.ice_book3 = self.game_lore[8]
        
        ## The Pit ##
        self.pitl_door = self.doors[17]
        self.pitb_door = self.doors[5]
        self.pitu_door = self.doors[18]
        self.pit_gargoyle = rn.choice([4, 5])
        
        ## Lava ##
        self.lava_door1 = self.doors[11]
        self.lava_door2 = self.doors[12]
        self.lava_door3 = self.doors[13]
        self.lava_pixie_fight = foes.pixie
        
        ## Vines ##
        self.vines_door1 = self.doors[13]
        self.vines_door2 = self.doors[17]
        self.vines_statue1 = self.statuary[1]
        self.vines_statue2 = self.statuary[2]
        self.vines_statue3 = self.statuary[3]
        self.vines_spell = rn.choice(magic.level_2)
        self.vines_lore = self.game_lore[9]
        
        ## Library ##
        self.library_door1 = self.doors[15]
        self.library_door2 = self.doors[18]
        self.library_door3 = self.doors[25]
        self.library_spell1 = rn.choice(magic.level_2)
        self.library_spell2 = rn.choice(magic.level_3)
        self.library_spell3 = rn.choice(magic.level_2)
        self.library_lore1 = self.game_lore[10]
        self.library_lore2 = self.game_lore[11]
        self.library_lore3 = self.game_lore[12]
        self.library_lore4 = self.game_lore[13]
        self.library_lore5 = self.game_lore[14]
        self.library_lore6 = self.game_lore[15]
        self.library_plot1 = text.library_plot_1[self.game_id]
        self.library_plot2 = text.library_plot_2[self.game_id]
        
        ## Sanctum ##
        self.sanctum_spell = rn.choice(magic.power_spells)
        
        ## Dungeon ##
        self.dungeon_door1 = self.doors[12]
        self.dungeon_door2 = self.doors[14]
        self.dungeon_mimic = foes.mimic
        self.dungeon_quest = 0
        
        ## Cliff ##
        self.cliff_door1 = self.doors[14]
        self.cliff_door2 = self.doors[15]
        self.cliff_door3 = self.doors[16]
        self.cliff_lore1 = self.game_lore[16]
        self.cliff_lore2 = self.game_lore[17]
        self.cliff_crown = text.cliffs_sphere[self.game_id]
        
        ## Portal ##
        self.portal_door1 = self.doors[16]
        self.portal_lore1 = self.game_lore[18]
        self.portal_lore2 = self.game_lore[19]
        self.portal_lore3 = self.game_lore[20]
        self.portal_plot = text.portal_plot[self.game_id]
        
        ## Antechamber ##
        self.foyer_door1 = self.doors[6]
        self.foyer_door2 = self.doors[25]
        self.foyer_gate1 = self.doors[21]
        self.foyer_gate2 = self.doors[22]
        
        ## Waterfall ##
        self.wfall_door1 = self.doors[21]
        self.wfall_door2 = self.doors[24]
        
        ## Statue Row ##
        self.srow_door1 = self.doors[22]
        self.srow_door2 = self.doors[23]
        self.srow_statue1 = self.statuary[4]
        self.srow_statue2 = self.statuary[5]
        self.srow_statue3 = self.statuary[6]
        self.srow_statue4 = self.statuary[7]
        self.srow_statue5 = self.statuary[8]
        
        ## Garden ##
        self.garden_door1 = self.doors[24]
        self.garden_door2 = self.doors[23]
        
        ## Exxit ##
        self.victory = False
        self.exxit_you = text.exxit_convo_you[self.game_id]
        self.exxit_him = text.exxit_convo_him[self.game_id]
        self.exxit_fight = "{} Challenges You!".format(self.bbeg.title)
        self.exxit_win = text.final_victory[self.game_id]

###############################################################################\
## THE GAMES ##################################################################|
###############################################################################/
game_keys = ['John']
random_game_index = rn.choice(game_keys)

## Game Initiation ############################################################
game_random = Game(random_game_index)