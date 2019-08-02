# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 03:51:30 2018

@author: Devlin
"""
import dungeon_toolkit as kit
import dungeon_text as text
import dungeon_foes as foes
import random as rn

# TODO - reverse [y, x]
# TODO - move preview function
# TODO - pawn 2 sqares first move, proper check/checkmate, full board, change your mind before moving

###############################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#  
###############################################################################
class Board():
    def __init__(self, size):
        self.size = size
        self.board = [['   ' for i in range(self.size)] for i in range(self.size)]
        self.raw = True
        
        ## Minesweeper ##
        self.danger = []
        self.unique = []
        self.unique_counts = []
        self.uncovered = []
        self.truth = {}
        
        ## Chess ##
        
    ###########################################################################    
    def isblank(self, row, col):
        if self.board[row][col] == '   ':
            return True
        else:
            return False

    ###########################################################################        
    def dangerfie(self, holes, return_coords, star = False):      
        ## [Y, X] because I'm stupid and too lazy to swap it
        tiles = []
        for y in range(self.size):
            for x in range(self.size):
                tiles.append([y, x])
                
        all_spaces = tiles.copy()
            
        for space in return_coords:
            tiles.remove(space)
            for buddy in self.locate_neighbors(space[0], space[1]):
                tiles.remove(buddy)
    
        self.danger = kit.avoid_duplicates(holes, tiles)
        
        warnings = []
        for pit in self.danger:
            for neighbor in self.locate_neighbors(pit[0], pit[1]):
                warnings.append(neighbor)
    
        self.unique = []
        for pair in warnings:
            if pair not in self.unique:
                self.unique.append(pair)
            
        self.unique_counts = []
        for u in self.unique:
            if star ==  False:
                score = 0
                for pair in warnings:
                    if u == pair:
                        score += 1
                self.unique_counts.append(' {} '.format(score))
            else:
                self.unique_counts.append(' + ')
        
        self.raw = False
        for i in self.danger:
            name = kit.stringify(i)
            self.truth[name] = ' ! '
        for i in self.unique:
            name = kit.stringify(i)
            place = self.unique.index(i)
            self.truth[name] = self.unique_counts[place]
        for i in return_coords:
            name = kit.stringify(i)
            self.truth[name] = ' X '
        all_names = [kit.stringify(i) for i in all_spaces]
        for i in all_names:
            if i not in self.truth.keys():
                self.truth[i] = '   '
                        
    ###########################################################################    
    def locate_neighbors(self, r, c):
        start = [r, c]
        neighbors = []
        raw = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        for i in raw:
            neighbor = [n + o for n, o in zip(i, start)]
            neighbors.append(neighbor)
        
        illegal = []
        for pair in neighbors:
            for val in pair:
                if val not in range(self.size) and pair not in illegal:
                    illegal.append(pair)
                    
        for pair in illegal:
            neighbors.remove(pair)
        
        return neighbors
    
    ###########################################################################
    def __str__(self):
        divider_len = (self.size * 4) + 1
        columns = [str(i) for i in range(1, self.size + 1)]
        letters = list('ABCDEFGHIJKLMNPQRSTUVWXYZ')
        rows = [' {}  '.format(letters[i]) for i in range(self.size)]
        contents = ['\n      ' + '   '.join(columns) + '\n']
        for i in range(self.size):
           contents.append('    ' + '-'*divider_len + '\n')
           contents.append(rows[i] + '|' + '|'.join(self.board[i]) + '|\n')
        contents.append('    ' + '-'*divider_len + '\n')
        
        return ''.join(contents)

###############################################################################\
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###############################################################################/
class Piece():
    def __init__(self, piece, color, location):
        self.piece = piece
        self.color = color
        self.location = location
        
        if self.piece == 'Pawn':
            self.n_pawn = ' #{}'.format(self.location[1] + 1)
        else:
            self.n_pawn = ''
        
        if self.piece == 'Knight':
            self.p_id = 'N'
        else:
            self.p_id = self.piece[0]
            
        sides = {'Black': 'Kings ',
                 'White': 'Queens '}
        
        if self.location[1] < 3 and self.piece != 'Pawn':
            self.side = sides[self.color]
        elif self.location[1] > 4 and self.piece != 'Pawn':
            both = list(sides.keys())
            both.remove(self.color)
            self.side = sides[both[0]]
        else:
            self.side = ''
            
       
        if self.color == 'White':
            self.name = ' {} '.format(self.p_id.lower())
        else:
            self.name = ' {} '.format(self.p_id)
        
        self.long_name = '{}{}{}'.format(self.side, self.piece, self.n_pawn)
    
    ###########################################################################    
    def takeable(self, board, location):
        row = location[0]
        col = location[1]
        a = board[row][col]
        m = a[1]
        
        opts = {m.lower(): 'White',    
                m.upper(): 'Black'}    
            
        if opts[m] == self.color or m == ' ':
            return False
        else:
            return True
        
    ###########################################################################
    def options(self, game, checked = [], raw = False):
        board = game.board
        open_spaces = []
        row = self.location[0]
        col = self.location[1]
        
        from_edge = {'Top': row,
                     'Bottom': 7 - row,
                     'Left': col,
                     'Right': 7 - col}
        
        ## Rook and Queen.a ###################################################
        if self.piece in ['Rook', 'Queen']:
            # Raw moves #######################################################
            h_moves = [[row, i] for i in range(8) if i != col]
            v_moves = [[i, col] for i in range(8) if i != row]
            all_moves = h_moves + v_moves
            
            # No Jumping! #####################################################
            left = [-1]
            right = [8]
            top = [-1]
            bottom = [8]
            
            for t in all_moves:
                y = t[0]
                x = t[1]
                if not game.isblank(y, x) and x < col:
                     left.append(x)
                elif not game.isblank(y, x) and x > col:
                    right.append(x)
                elif not game.isblank(y, x) and y > row:
                    bottom.append(y)
                elif not game.isblank(y, x) and y < row:
                    top.append(y)
                    
            left_lim = max(left)
            right_lim = min(right)
            top_lim = max(top)
            bottom_lim = min(bottom)
            
            moves_iterable = all_moves.copy()
            for t in moves_iterable:
                y = t[0]
                x = t[1]
                if x < left_lim or x > right_lim or y < top_lim or y > bottom_lim:
                    all_moves.remove(t)                   
            
            # Append Legal Moves ############################################## 
            for m in all_moves:
                if game.isblank(m[0], m[1]) or self.takeable(board, m):
                    open_spaces.append(m)
        
        ## Bishop and Queen.b #################################################
        if self.piece in ['Bishop', 'Queen']:
            # Raw Moves #######################################################
            move_lims = {'NE': min(from_edge['Top'], from_edge['Right']),  
                         'NW': min(from_edge['Top'], from_edge['Left']),
                         'SE': min(from_edge['Bottom'], from_edge['Right']),
                         'SW': min(from_edge['Bottom'], from_edge['Left'])}
            
            ne = [[row - i, col + i] for i in range(1, move_lims['NE'] + 1)]
            nw = [[row - i, col - i] for i in range(1, move_lims['NW'] + 1)]
            se = [[row + i, col + i] for i in range(1, move_lims['SE'] + 1)]
            sw = [[row + i, col - i] for i in range(1, move_lims['SW'] + 1)]
            forecast = [ne, nw, se, sw]
            
            # No Jumping! #####################################################
            steps = []
            for heading in forecast:
                heading_names = list(move_lims.keys())
                place = forecast.index(heading)
                this_heading = heading_names[place]
                barriers = [move_lims[this_heading]]
                for tile in heading:
                    y = tile[0]
                    x = tile[1]
                    if not game.isblank(y, x):
                        barriers.append(abs(y - row))
                steps.append(min(barriers))
            
            ne_move = [[row - i, col + i] for i in range(1, steps[0] + 1)]
            nw_move = [[row - i, col - i] for i in range(1, steps[1] + 1)]
            se_move = [[row + i, col + i] for i in range(1, steps[2] + 1)]
            sw_move = [[row + i, col - i] for i in range(1, steps[3] + 1)]
            all_moves = ne_move + nw_move + se_move + sw_move
            
            for m in all_moves:
                if game.isblank(m[0], m[1]) or self.takeable(board, m):
                    open_spaces.append(m)
        
        ## Knight #############################################################            
        if self.piece == 'Knight':
            for flip in range(2):
                for stem in (-2, 2):
                    for tail in (-1, 1):
                        if flip == 0:
                            y = stem + row
                            x = tail + col
                            if 7 >= y >= 0 and 7 >= x >= 0:
                                if self.takeable(board, [y, x]) or game.isblank(y, x):
                                    open_spaces.append([y, x])
                        
                        elif flip == 1:
                            y = tail + row
                            x = stem + col
                            if 7 >= y >= 0 and 7 >= x >= 0:
                                if self.takeable(board, [y, x]) or game.isblank(y, x):
                                    open_spaces.append([y, x])
        
        ## Pawn ###############################################################                        
        if self.piece == 'Pawn':
            directions = {'White': 1, 'Black': -1}
            a = directions[self.color]
            y = row + a
            
            if game.isblank(y, col):
                open_spaces.append([y, col])
            
            other_team = list(directions.keys())
            other_team.remove(self.color)

            if self.takeable(board, [y, (col + 1)]):
                open_spaces.append([y, (col + 1)])
            
            if self.takeable(board, [y, (col - 1)]):
                open_spaces.append([y, (col - 1)])
            
        
        ## King ###############################################################            
        if self.piece == 'King':
            for i in (-1, 1):  
                for j in (-1, 1):     
                    for k in (-1, 1): 
                        if i == j and j == k:
                            y = row
                            x = col + j
                        elif i == k:
                            y = row + i
                            x = col
                        else:
                            y = row + i
                            x = col + j
                        
                        coords = [y, x]
                        illegal = [c for c in coords if c > 7 or c < 0]                            
                        
                        if coords not in checked and len(illegal) == 0:
                            if game.isblank(y, x) or self.takeable(board, coords):
                                open_spaces.append(coords)                       

        ## FINISHED ###########################################################
        if raw == False:
            tiles = []
            for piece in sorted(open_spaces, key = lambda x: x[0]):
                row = piece[0]
                col = piece[1] + 1
                letters = list('ABCDEFGH')
                chessletter = letters[row]       
                place = chessletter + str(col)
                tiles.append(place)
        
            return tiles
        
        else:
            return open_spaces
    
    ###########################################################################
    def move(self, board, target):
        letters = list('ABCDEFGH')
        row = letters.index(target[0])
        col = int(target[1]) - 1
        
        c_row = self.location[0]
        c_col = self.location[1]
        board[c_row][c_col] = '   '
        
        old = board[row][col]
        board[row][col] = self.name
        self.location = [row, col]
    
        return old
    
###############################################################################
#-----------------------------------------------------------------------------#
###############################################################################
# Each list in the list is a row, the index of the list is the column
# So i[0] is row number - 1 and i[1] is col number - 1
chessboard = Board(8)

r = Piece('Rook', 'White', [0, 7])
b = Piece('Bishop', 'White', [0, 6])
k = Piece('King', 'White', [0, 4])
n = Piece('Knight', 'White', [0, 2])
p1 = Piece('Pawn', 'White', [1, 4])
p2 = Piece('Pawn', 'White', [1, 3])
q = Piece('Queen', 'White', [0, 3])
whites = [r, b, k, p1, p2, q, n]
for p in whites:
    chessboard.board[p.location[0]][p.location[1]] = p.name
  
R = Piece('Rook', 'Black', [7, 0])
B = Piece('Bishop', 'Black', [7, 1])
K = Piece('King', 'Black', [7, 3])
N = Piece('Knight', 'Black', [7, 2])
P1 = Piece('Pawn', 'Black', [6, 3])
P2 = Piece('Pawn', 'Black', [6, 6])
Q = Piece('Queen', 'Black', [7, 4])
blacks = [R, B, K, P1, P2, Q, N]
for p in blacks:
    chessboard.board[p.location[0]][p.location[1]] = p.name
    
###############################################################################
def checkcheck(team, layout):
    threatened = []
    for mate in team:
        possibles = mate.options(layout, raw = True)
        for coords in possibles:
            threatened.append(coords)
            
    return threatened

###############################################################################
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
###############################################################################
def play_chess(game, white, black, timer):
    """Whites are players, blacks are rng"""
    turns = timer
    
    white_pieces = {}
    black_pieces = {}
    for piece in white:
        white_pieces[piece.name] = piece
    for piece in black:
        black_pieces[piece.name] = piece
    
    white_checked = checkcheck(white, game)
    black_checked = checkcheck(black, game)
    while K in black and k in white and turns > 0:
        kit.pause_for_effect()
        print(game)
        print("TURNS LEFT: {} ".format(turns))
        if turns % 2 == 1:
            print('Whites Turn')
            white_names = [piece.long_name for piece in white]
            if k.location not in black_checked:
                print('\nWhich piece will you move?')
                print(', '.join([p.long_name for p in white]))
                while True:
                    chosen = input('>> ')
                    if chosen in white_names:
                        location = white_names.index(chosen)
                        your_move = white[location]
                        if len(your_move.options(game, black_checked)) == 0:
                            print("You can't move the {}!".format(chosen))
                        else:
                            break
            
            else:
                print('CHECK! You must move your king!')
                your_move = k
            
            print('\nWhere will you move your piece?')
            choices = your_move.options(game, black_checked)
            if your_move == k and len(choices) == 0:
                print('CHECKMATE! You lose')
                return 1
            
            print(', '.join(choices))
                
            while True:
                destination = input('>> ')
                if destination in choices:
                    break
            
            final_move = your_move.move(game.board, destination)
            if final_move in black_pieces.keys():
                taken = black_pieces[final_move]
                black.remove(taken)
                print('You took {}'.format(taken.long_name))
                
            white_checked = checkcheck(white, game)                    
            turns -= 1
        
        else:
            while True:
                if K.location not in white_checked:
                    moving_piece = rn.choice(black)
                else:
                    moving_piece = K
            
                black_choices = moving_piece.options(game, white_checked)
                if len(black_choices) == 0:
                    if moving_piece == K:
                        print('CHECKMATE! You Win!')
                        return 0
                else:
                    break
                
            going = rn.choice(black_choices)
            print('Black is moving their {} to {}'.format(moving_piece.long_name, going))
           
            
            final_move = moving_piece.move(game.board, going)
            if final_move in white_pieces.keys():
                taken = white_pieces[final_move]
                white.remove(taken)
                print('You lost your {}'.format(taken.long_name))
                
            black_checked = checkcheck(black, game)            
            turns -= 1
    
    if turns == 0 and K in black and k in white:
        return 2
    elif K in black and k not in white:
        return 1
    elif k in white and K not in black:
        return 0
    
###############################################################################
###############################################################################
###############################################################################
minefield = Board(12)
rc = [[6, 6]]
sr = 0
sc = 5

###############################################################################\
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
###############################################################################/
def floor_puzzle(walker, start_row, start_col, floor, holes, return_coords = [], star = False):
    field = [[foes.Enemy(*i) for i in foes.pit_m][0] for x in range(holes)]
    if floor.raw == True:
        floor.dangerfie(holes, return_coords, star)
        
    for x in range(floor.size):
        for i in range(floor.size):
            if floor.board[x][i] == ' @ ':
                floor.board[x][i] = ' . '
        
    n_row = start_row
    n_col = start_col
    old_space = [n_row, n_col]
    floor.uncovered.append(old_space)
    turn = 0
    while True:
        kit.pause_for_effect()
        ## Put the mask on ####################################################
        for i in range(floor.size):
            for x in range(floor.size):
                if [i, x] not in floor.uncovered:
                    floor.board[i][x] = ' . '  
        
        ## Put an X on all special spaces #####################################            
        for i in return_coords:
            i_row = i[0]
            i_col = i[1]
            floor.board[i_row][i_col] = ' X '
        
        ## Put your character symbol ##########################################
        floor.board[n_row][n_col] = ' @ '
    
        ## Reveal the board around you ########################################
        c_tile = [n_row, n_col] 
        if c_tile not in floor.unique and c_tile not in floor.danger:
            for i in floor.locate_neighbors(n_row, n_col):
                floor.uncovered.append(i)
                i_row = i[0]
                i_col = i[1]
                name = kit.stringify(i)
                floor.board[i_row][i_col] = floor.truth[name]
        else:
            floor.uncovered.append(c_tile)
            o_name = kit.stringify(old_space)
            o_row = old_space[0]
            o_col = old_space[1]
            floor.board[o_row][o_col] = floor.truth[o_name]
            
        
        print(floor)
        if [n_row, n_col] in floor.unique:
            n_name = kit.stringify(c_tile)
            print("\nThe space you curretly occupy is a{}\n".format(floor.truth[n_name]))
        else:
            print('\n\n')
        
        ## Returns ############################################################
        if c_tile in floor.danger:
             monster = field[0]
             fight = kit.run_encounter(text.encounter_intro, walker, [], [monster], {1: text.door_holder}, text.encounter_victory)
             if fight == True:
                kit.pause_for_effect()
                field.remove(monster)
                floor.danger.remove(c_tile)
                c_name = kit.stringify(c_tile)
                floor.truth[c_name] = '   '
                print(floor)
             elif fight == False:
                 return 'death'
             else:
                 return 10  
        elif c_tile in return_coords and turn != 0:
            return return_coords.index(c_tile)
        
        ## Player movement ####################################################        
        moves = ['up', 'down', 'left', 'right']
        if n_row == 0:
            moves.remove('up')
        elif n_row == 8:
            moves.remove('down')
        elif n_col == 0:
            moves.remove('left')
        elif n_col == 8:
            moves.remove('right')
            
        print('How will you move?')
        for i in moves:
            print(i.capitalize())
        while True:
            step = input('>> ').lower()
            if step not in moves:
                print('You can\'t go that way')
            else:
                old_space = c_tile
                m_vals = {'up': -1, 'down': 1, 'left': -1, 'right': 1}
                if step in ['up', 'down']:
                    n_row += m_vals[step]
                elif step in ['left', 'right']:
                    n_col += m_vals[step]
                turn += 1
                break            
        
###############################################################################    
if __name__ == '__main__':
    print('What should we playtest?\n1. Chess\n2. Minesweeper')
    playing = kit.intcheck('\n>> ')
    if playing == 1:
        play_chess(chessboard, whites, blacks, 10)
    elif playing == 2:
        floor_puzzle(sr, sc, minefield, 25, rc)