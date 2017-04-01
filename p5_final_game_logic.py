#Project 4. Darryl Mak #50693792
#Project 4 Game Logic
class InvalidMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass

class game_logic:
    def __init__(self, rows:int, columns:int, turn:str, start:str, won:str):
        '''Initializes the game with desired conditions'''
        self._rows= rows
        self._col= columns
        self._turn= turn
        self._starting= start
        self._way_won= won
        self._board=[]
        self._black=0
        self._white=0
        self._winner_is= 0
    
    
    def game_setup(self)->None:
        '''creates the board with proper columns and rows, places starting
         pieces '''
        self._create_board()
        self._starting_position(self._rows, self._col)

    def winner_is(self)->None:
        '''returns who the winner is. No winner if it returns 0.'''
        return self._winner_is
    
    def winner(self, way_won:str)-> str:
        '''Determines the winner'''
        if way_won=='>':
            if self.count_black(self._board) > self.count_white(self._board):
                self._winner_is = 'B'
            elif self.count_black(self._board) < self. count_white(self._board):
                self._winner_is = 'W'
            else:
                self._winner_is = 'NONE'
        else:
            if self.count_black(self._board) < self.count_white(self._board):
                self._winner_is = 'B'
            elif self.count_black(self._board) > self. count_white(self._board):
                self._winner_is = 'W'
            else:
                self._winner_is = 'NONE'
        return self._winner_is
    

    def check_all(self, board:[[]], turn:str)->bool:
        ''' Checks if player has any valid moves left'''
        valid_list=[]
        row=0
        while (row < self._rows):
            col =0
            while (col < self._col ):
                try:
                    self._check_validity(board, row , col , turn) == True
                except:
                    valid_list.append(0)
                else:
                    valid_list.append(1)
                col+= 1
            row +=1
        if 1 in valid_list:
            return True
        return False

    def is_game_over(self, board:[[]], turn:str)->bool:
        '''Check if the game is over'''
        if self.check_all(board, turn)==True:
            return False
        elif self.check_all(board, self._opposite_turn_str(turn))==True:
            self._turn= self._opposite_turn(turn)
            return False
        else:
            who_won=self.winner(self._way_won)
            return True
    
    def drop_piece(self, row:int, col:int)->None:
        '''drop a piece on the game board'''
        int_row=int(row)-1
        int_col=int(col)-1

        #check_validity
        self._check_validity(self._board, int_row, int_col, self._turn)
        short_directions= self._check_next_to_opp(int_row, int_col, self._turn)
        long_directions= self._check_all_directions(self._board,int_row,int_col, self._turn)
        final_list= self._final_flip_list(short_directions, long_directions)
        
        #actually changing board
        self._board[int_row][int_col]= self._turn
        self._flip_desired_directions(self._board, int_row, int_col, self._turn, final_list)

        
        #return opposite player        
        self._opposite_turn(self._turn)
        return self._board
    
    def count_black(self, board:[[int]])->int:
        '''counts the number of black pieces on the board'''
        black_count=0
        for row in board:
            for col in row:
                if col == 'B':
                    black_count +=1
        self._black= black_count
        return self._black
    
    def count_white(self, board:[[int]])->int:
        '''counts the number of white pieces on the board'''
        white_count=0
        for row in board:
            for col in row:
                if col == 'W':
                    white_count +=1
        self._white= white_count
        return self._white
    
    
    #for game_setup
    def _create_board(self)->list:
        '''create the board with adaquate number of columns, rows'''
        for row in range(self._rows):
            self._board.append([])
            for col in range(self._col):
                self._board[-1].append(0)
        return self._board

    #for get_setup
    def _starting_position(self, row:int, col:int)->None:
        '''puts the starting pieces on the board'''
        int_row=int(int(row)/2-1)
        int_col=int(int(col)/2-1)
        #could be written as different function
        if self._starting == 'B':

            self._board[int_row][int_col]= 'B'
            self._board[int_row][int_col+1]= 'W'
            self._board[int_row+1][int_col]= 'W'
            self._board[int_row+1][int_col+1]= 'B'
                
        elif self._starting == 'W':
            self._board[int_row][int_col]= 'W'
            self._board[int_row][int_col+1]= 'B'
            self._board[int_row+1][int_col]= 'B'
            self._board[int_row+1][int_col+1]= 'W'

    
    #for drop_piece
    def _opposite_turn(self, turn:'str')->str:
        '''Given whose turn it is, it returns the other player'''
        if turn=='B':
            self._turn='W'
            return self._turn
        elif turn=='W':
            self._turn='B'
            return self._turn
    
    #for drop_piece
    def _check_validity(self,board:[[]] ,row:int, col:int, turn:str)->bool:
        '''check on the validity of the move'''
        self._check_num_is_pos(row , col)
        self._check_free_space(row, col)
        short_directions= self._check_next_to_opp(row, col, turn)
        long_directions= self._check_all_directions(board, row, col, turn)
        final_list= self._final_flip_list(short_directions, long_directions)
        return True
        
        
    #for _check_validity, which is for drop_piece    
    def _check_num_is_pos(self, row:int, col:int)->None:
        '''Checkes to makes sure numbers aren't negative'''
        if row <= -1:
            raise InvalidMoveError()
        else:
            pass
        if col <= -1:
            raise InvalidMoveError()
        
    #for _check_validity, which is for drop_piece    
    def _check_free_space(self, row:int, col:int)->None:
        '''Checks to make desired space is blank'''
        if self._board[row][col] != 0:
            raise InvalidMoveError()
        else:
            pass
        
    #for _check_validity, which is for drop_piece    
    def _check_next_to_opp(self, row: int, col:int, turn:str)->None:
        '''checks if desired space has an opposite piece near it
        (8 directions)'''
        surround_pieces=[]
        surround_directions=[]
        directions=[(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1,-1)]
        opp_turn=self._opposite_turn_str(turn)
        ###         down    up       right   left    btright  tpright  btleft   tpleft
        # in terms of gameboard
        for direction in directions:
            new_row= row+ direction[0]
            new_col= col+ direction[1]
            if 0<= new_col< self._col and 0 <= new_row <self._rows:
                if self._board[new_row][new_col]== opp_turn:
                    surround_directions.append(direction)
            if 0<= new_col< self._col and 0 <= new_row <self._rows:
                surround_pieces.append(self._board[new_row][new_col])
        if opp_turn in surround_pieces:
            pass
            return surround_directions
        else:
            raise InvalidMoveError()
        
        
    #for _check_next_to_opp, which is for drop_piece
    def _opposite_turn_str(self, turn:'str')->str:
        '''Given whose turn it is, returns other player (just the string)'''
        if turn=='B':
            turn='W'
            return turn
        elif turn=='W':
            turn='B'
            return turn

    #for drop_piece    
    def _check_all_directions(self, board:[[]] ,row:int, col:int, turn:str)->list:
        '''checks each direction for presence of own pieces, returns a list of desired directions '''
        all_directions = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1,-1)]
        desired_directions=[]
        for direction in all_directions:
            if self._check_each_direction(board, row, col, turn, direction)==True:
                desired_directions.append(direction)

        if len(desired_directions) == 0:
           raise InvalidMoveError
        return desired_directions

    #for check_all_directions, for drop_piece
    def _check_each_direction(self, board:[[]] ,row:int, col:int, turn:str, direction:list)->None:
        '''check for player's own piece in a single direction exlcuding the pieces directly
        next to it'''
        multiplier=1
        new_row= row
        new_col= col
        while 0<= new_row < self._rows and 0<= new_col < self._col:
            try:
                new_row = row + ((direction[0]* multiplier)+direction[0])
                new_col = col + ((direction[1]* multiplier)+direction[1])
                if new_row == -1:
                    break
                if new_col == -1:
                    break
                if board[new_row][new_col]== turn:
                    return True                  
                    break
                else:
                    multiplier += 1
            except:
                pass
        return

    #for drop_piece
    def _final_flip_list(self, short_list:list ,long_list:list)->list:
        '''finds the directions to flip'''
        final_list=[]
        for direction in long_list:
            if direction in short_list:
                final_list.append(direction)
        if len(final_list)==0:
            raise InvalidMoveError
        return final_list
            
    
    #for drop_piece   
    def _flip_desired_directions(self, board:[[]], row:int, col:int, turn:str ,desire_direct: list)->None:
        '''flip pieces in all directions '''
        directions = desire_direct
        for direction in directions:
            self._flip_a_direction(board, row, col, turn, direction)
    
    #for flip_desired_direction, which is for drop_piece
    def _flip_a_direction(self, board:[[]] ,row:int, col:int, turn:str ,direction:list)->None:
        '''flip pieces in a single direction'''
        multiplier=1
        new_row= row
        new_col= col
        while 0<= new_row < self._rows and 0<= new_col < self._col:
            try:
                new_row = row + (direction[0]* multiplier)
                new_col = col + (direction[1]* multiplier)
                if new_row == -1:
                    break
                if new_col == -1:
                    break
                if board[new_row][new_col]==turn:
                    break
                else:
                    board[new_row][new_col] = turn
                    multiplier += 1
            except:
                pass
        return
