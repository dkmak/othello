#Project 5. Darryl Mak #50693792
#Project 5 GUI

import p5_final_game_logic
import tkinter
import point
import p5_dialog
import p5_winner

class OthelloGUI:
    '''GUI for the actual Othello game'''
    def __init__(self,class_info:'class of info'):

        self._root_window = tkinter.Tk()
        
        full_line= tkinter.Label(
            master= self._root_window, text='FULL OTHELLO' , font='times')
        
        full_line.grid(
            row = 0, column = 0, padx = 20, pady = 5,
            sticky = tkinter.W +tkinter.S)
        
        #Score
        score_frame = tkinter.LabelFrame(
            master = self._root_window, text = 'Score:',
            font = 'Times')
        
        score_frame.grid(
            row = 1, column = 0, padx = 20, pady = 5,
            sticky = tkinter.W +tkinter.S)
        
        #Score:Black
        self._black_score_text= tkinter.StringVar()
        self._black_score_text.set('Black: 2')
        
        black_score= tkinter.Label(
            master= score_frame, textvariable= self._black_score_text , font='times')

        black_score.grid(
            row=0, column=0, padx=10, pady=0, sticky= tkinter.W)
        
        #Score:White
        self._white_score_text= tkinter.StringVar()
        self._white_score_text.set('White: 2')
        
        
        white_score= tkinter.Label(
            master= score_frame, textvariable= self._white_score_text , font='times')

        white_score.grid(
            row=0, column=1, padx=10, pady=0, sticky= tkinter.W)
        
        
        #Turn
        turn_frame = tkinter.LabelFrame(
            master = self._root_window, text = 'Turn:',
            font = 'Times', labelanchor='ne')
        
        turn_frame.grid(
            row = 1, column = 1, padx = 20, pady = 5,
            sticky = tkinter.E +tkinter.S)

        self._turn_text= tkinter.StringVar()
        self._turn_text.set('Turn: {}'.format(self._convert_bw(class_info._turn)))
        
        turn = tkinter.Label(
            master = turn_frame, textvariable=self._turn_text,
            font = 'Times')

        turn.grid(
            row = 0, column = 0, padx = 5, pady = 0,
            sticky = tkinter.W +tkinter.S)
        
        
        #Canvas
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 400, height = 400,
            background = '#006633')
        
        self._canvas.grid(row=2, column=0, padx=20, pady=10,
                          columnspan=2,
                          sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.columnconfigure(0, weight=0)
        self._root_window.columnconfigure(1, weight = 4)
        self._root_window.rowconfigure(2, weight = 4)
        

        self._canvas.bind('<Button-1>', self._on_canvas_clicked)


    def start(self) -> None:
        '''Starts Application'''
        self._root_window.mainloop()

    
    #binding functions
    def _on_canvas_clicked(self, event:tkinter.Event)->None:
        '''When Canvas is clicked, place new piece, redraw board '''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        
        click_point = point.from_pixel(
            event.x, event.y, width, height)
        self._update_topline()
        place_piece=self._return_proper_space(click_point,class_info._rows,
                                          class_info._col)
        self._take_turn(place_piece,class_info)
        self._display_pieces()
        self._display_if_over(class_info.is_game_over(class_info._board, class_info._turn))
        self._update_topline()
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''When canvas is resized, redraw board'''
        self._update_board(class_info._rows,class_info._col,'#000000')
        
    
    #part of on_canvas_clicked
    def _take_turn(self, info:list, game:'class of info')->None:
        '''take a turn on the board'''
        try:
            game.drop_piece(info[0],info[1])
        except:
            pass        
    
    
    def _return_proper_space(self, point:'Point class',user_rows:int, user_col:int)->None:
        '''returns the proper space that has been clicked by user'''
        canvas_width = self._canvas.winfo_width()
        #print(canvas_width)
        canvas_height = self._canvas.winfo_height()
        for row in range(user_rows):
            upper = (row+1)/user_rows
            lower = row/user_rows
            if lower < point._frac_y < upper:
                desired_row=row+1
    
        for col in range(user_col):
            upper = (col+1)/user_col
            lower = col/user_col
            if lower < point._frac_x < upper:
                desired_column =col+1
        return desired_row, desired_column
        
    #part of _on_canvas_resized
    def _update_board(self, user_rows:int, user_col:int ,color:str) -> None:
        '''redraws lines'''
        self._canvas.delete(tkinter.ALL)
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        for row in range(user_rows-1):
            row+=1
            self._canvas.create_line(
                0,
                canvas_height * (row/user_rows),
                canvas_width,
                canvas_height*(row/user_rows),
                fill = color)
        for col in range(user_col-1):
            col+=1
            self._canvas.create_line(
                canvas_width*(col/user_col),
                0, canvas_width*(col/user_col),
                canvas_height, fill=color)
        self._display_pieces()
        


    def _update_topline(self)->None:
        '''update the topline with the correct number of pieces, turn'''
        b_count= class_info.count_black(class_info._board)
        w_count= class_info.count_white(class_info._board)
        self._black_score_text.set('Black: {}'.format(b_count))
        self._white_score_text.set('White: {}'.format(w_count))
        turn= class_info._turn
        self._turn_text.set('Turn: {}'.format(self._convert_bw(turn)))

    def _convert_bw(self,color:str)->str:
        '''converts 'Black', 'White', to 'B','W' '''
        if color== 'B':
            new_color='Black'
        else:
            new_color='White'
        return new_color
    
    #part of _update_board
    def _display_pieces(self)->None:
        '''display pieces on board'''
        
        row=0
        while (row < class_info._rows):
            col =0
            while (col < class_info._col ):
                if( class_info._board[row][col] == 0 ):
                    pass
                elif( class_info._board[row][col] == 'B'):
                    self._draw_oval((row+1,col+1),class_info._rows,class_info._col,'#000000')
                else:            
                    self._draw_oval((row+1,col+1),class_info._rows,class_info._col,'#FFFFFF')
                col+= 1
            row+=1
                
    #part of _draw_oval
    def _draw_oval(self, location:tuple, user_rows:int, user_col:int, color:str)->None:
        '''draw a single oval in a desired place'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        top_left_x= (location[1]-1) / user_col
        top_left_y= (location[0]-1)/user_rows
        right_bottom_x= location[1]/user_col
        right_bottom_y= location[0]/user_rows
        top_left_point=point.from_frac(top_left_x,top_left_y)
        
        right_bottom_point=point.from_frac(right_bottom_x,right_bottom_y)
        self._canvas.create_oval(top_left_point.pixel(canvas_width,canvas_height)[0],
                                 top_left_point.pixel(canvas_width,canvas_height)[1],
                                 right_bottom_point.pixel(canvas_width,canvas_height)[0],
                                 right_bottom_point.pixel(canvas_width,canvas_height)[1],
                                 outline = 'black', fill = color)


    def _display_if_over(self, game_over:bool)->None:
        '''brings up WinnerWindow if game is over'''
        if game_over ==False:
            pass
        else:
            who_won=class_info.winner(class_info._way_won)
            b_count= class_info.count_black(class_info._board)
            w_count= class_info.count_white(class_info._board)
            
            win_window= p5_winner.WinnerWindow()
            self._letter_to_word(win_window ,who_won)
            self._final_score(win_window,b_count,w_count)
            win_window.start()
            
    def _letter_to_word(self, win_window:'window class', letter:str)->None:
        '''Based on who is winner, set win_window string'''
        if letter == 'B':
            win_window._winner_text.set(''''BLACK' wins!!!''')
        elif letter == 'W':
            win_window._winner_text.set(''''WHITE' wins!!!''')
        else:
            win_window._winner_text.set('''NO ONE wins!!!''')

    def _final_score(self, win_window:'window_class', b_score:int, w_score:int)->None:
        '''Display final count of black, white pieces'''
        win_window._black_score_text.set('Black: {}'.format(b_score))
        win_window._white_score_text.set('White: {}'.format(w_score))  
#Functions
    
def call_logic_class(inputs:'list of user input')-> None:
    '''Calls an (Othello)game logic class '''
    gl_mod=p5_final_game_logic
    new_game= gl_mod.game_logic(inputs[0],inputs[1],inputs[2],inputs[3],inputs[4])
    return new_game

def get_dialog_info()->list:
    '''get info from dialog box'''
    dialog = p5_dialog.OthelloDiag()
    dialog.show()
    row=dialog.get_row()
    column=dialog.get_column()
    first=dialog.get_first()
    top_left=dialog.get_top_left()
    how_won=dialog.get_how_won()
    info=[row, column, first, top_left, how_won]
    return info

if __name__ == '__main__':
    class_info=call_logic_class(get_dialog_info())
    class_info.game_setup()
    app = OthelloGUI(class_info)
    app.start()
            






