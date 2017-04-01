#Project 5. Darryl Mak #50693792
#Project 5 Winner Pop-Up
import tkinter
class WinnerWindow:
    def __init__(self):
        self._root_window = tkinter.Toplevel()

        #Score
        score_frame = tkinter.LabelFrame(
            master = self._root_window, text = 'Final Score:',
            font = 'Times')
        
        score_frame.grid(
            row = 1, column = 0, padx = 20, pady = 5,
            sticky = tkinter.W +tkinter.S)
        
        #Score:Black
        self._black_score_text= tkinter.StringVar()
        self._black_score_text.set('Black: ')
        
        black_score= tkinter.Label(
            master= score_frame, textvariable= self._black_score_text , font='times')

        black_score.grid(
            row=0, column=0, padx=10, pady=0, sticky= tkinter.W)
        
        #Score:White
        self._white_score_text= tkinter.StringVar()
        self._white_score_text.set('White: ')
        
        
        white_score= tkinter.Label(
            master= score_frame, textvariable= self._white_score_text , font='times')

        white_score.grid(
            row=0, column=1, padx=10, pady=0, sticky= tkinter.W)
        self._winner_text = tkinter.StringVar()
        self._winner_text.set('''YOU SHOULDN'T SEE THIS''')


        winner_label = tkinter.Label(
            master = self._root_window, textvariable = self._winner_text,
            font = 'Times')

        winner_label.grid(
            row = 0, column = 0, padx = 20, pady = 20,
            sticky = tkinter.N+tkinter.W+ tkinter.S + tkinter.E)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def start(self) -> None:
        self._root_window.grab_set()
        self._root_window.wait_window()


if __name__ == '__main__':
    WinnerWindow().start()
