""" 01_Help_GUI_v1.py
Is building upon 01_Help_GUI.py and adding addition functionality by
implementing colours and an identifier into the GUI
"""

from tkinter import *
import random


class Opening:
    def __init__(self):
        print("hello world")

        # Formatting variables
        background_color = "white"

        # Quiz Main Screen GUI
        self.main_frame = Frame(width=300, height=300, bg=background_color)
        self.main_frame.grid()

        # Main quiz (row 0)
        self.main_quiz_label = Label(text="Māori Quiz",
                                          font=("Helvetica", "16", "bold",),
                                          bg=background_color, padx=10, pady=10)
        self.main_quiz_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Māori Quiz")
    something = Opening()
    root.mainloop()
