#Project 5. Darryl Mak #50693792
#Project 5 Dialog
import tkinter
DEFAULT_FONT = ('Times New Roman', 12)

class OthelloDiag:
    def __init__(self):
        self._dialog_window = tkinter.Tk()

#Cheesy Line
        title = tkinter.Label(
            master = self._dialog_window, text = 'O, Hello! This is Othello.',
            font = DEFAULT_FONT)

        title.grid(
            row = 0, column = 0, columnspan = 2, padx = 5, pady = 5,
            sticky = tkinter.W)
        
#Row Line
        row_label = tkinter.Label(
            master = self._dialog_window, text = 'Select number of rows:',
            font = DEFAULT_FONT)

        row_label.grid(
            row = 1, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        self._row_entry = tkinter.Spinbox(
            master = self._dialog_window, width = 5, font = DEFAULT_FONT,
            values=(4,6,8,12,16), wrap=True)
        
        self._row_entry.grid(
            row = 1, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

#Column Line
        column_label = tkinter.Label(
            master = self._dialog_window, text = 'Select number of columns:',
            font = DEFAULT_FONT)

        column_label.grid(
            row = 2, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        self._column_entry = tkinter.Spinbox(
             master = self._dialog_window, width = 5, font = DEFAULT_FONT,
            values=(4,6,8,12,16), wrap=True)

        self._column_entry.grid(
            row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

#Go First Line
        go_first_label = tkinter.Label(
            master = self._dialog_window, text = 'Select Who Goes First:',
            font = DEFAULT_FONT)

        go_first_label.grid(
            row = 3, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)
        
        self._go_first_entry = tkinter.Spinbox(
            master = self._dialog_window, width = 5, font = DEFAULT_FONT,
            values=('Black','White'), wrap=True)
        
        self._go_first_entry.grid(
            row = 3, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

#Starting Postion Line
        start_pos_label = tkinter.Label(
            master = self._dialog_window, text = 'Which Piece is Top-Left:',
            font = DEFAULT_FONT)

        start_pos_label.grid(
            row = 4, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        self._start_pos_entry = tkinter.Spinbox(
            master = self._dialog_window, width = 5, font = DEFAULT_FONT,
            values=('Black','White'), wrap=True)
        
        self._start_pos_entry.grid(
            row = 4, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

#Determining winner Line        
        deter_winner_label = tkinter.Label(
            master = self._dialog_window, text = 'How is the Game Won:',
            font = DEFAULT_FONT)

        deter_winner_label.grid(
            row = 5, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        self._deter_winner_entry = tkinter.Spinbox(
            master = self._dialog_window, width = 5, font = DEFAULT_FONT,
            values=('>','<'), wrap=True)
        
        self._deter_winner_entry.grid(
            row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)


#OK/Cancel Buttons
        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(6, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)


      #Attributes that will carry information

        self._ok_clicked = False
        self._row = ''
        self._column = ''
        self._first=''
        self._top_left=''
        self._how_won=''


    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()


       #Retrieve information
    def was_ok_clicked(self) -> bool:
        '''Returns whether the okay button was clicked'''
        return self._ok_clicked


    def get_row(self) -> str:
        '''Returns row entry '''
        return self._row

    
    def get_column(self) -> str:
        '''Returns column entry '''
        return self._column

    
    def get_first(self)->str:
        '''Returns first entry '''
        return self._first


    def get_top_left(self)->str:
        '''Returns color of top-left position '''
        return self._top_left


    def get_how_won(self)->str:
        '''Returns how the game is won'''
        return self._how_won


    #Command Handlers

    def _on_ok_button(self) -> None:
        '''stores all the important values'''
        self._ok_clicked = True
        self._row = int(self._row_entry.get())
        self._column = int(self._column_entry.get())
        self._first= self._convert_bw(self._go_first_entry.get())
        self._top_left= self._convert_bw(self._start_pos_entry.get())
        self._how_won= self._deter_winner_entry.get()
        self._dialog_window.destroy()
    
    def _on_cancel_button(self) -> None:
        '''Destroys window is cancel is pressed'''
        self._dialog_window.destroy()

        #for _on_okay_button
    def _convert_bw(self,color:str)->str:
        '''converts 'Black', 'White', to 'B','W' '''
        if color== 'Black':
            new_color='B'
        else:
            new_color='W'
        return new_color

if __name__ == '__main__':
   dialog = OthelloDiag()
   dialog.show()

#Heavily based off of dialog box on Professor Thornton's lecture
#on March 8th,2016
