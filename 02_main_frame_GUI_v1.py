""" 02_main_frame_GUI_v1.py
Basic tkinter template copied from the 00_tkinter_template.py
and based on the planning done in Trello (component 2 - slide 19)
buttons are there but none work
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows
import random


class Opening:
    def __init__(self):
        # Formatting variables
        background_color = "White"

        # Quiz Main Screen GUI
        self.main_frame = Frame(width=500, bg=background_color, pady=0)
        self.main_frame.grid()

        # Main Quiz Heading (row 0)
        self.main_quiz_label = Label(self.main_frame,
                                     text="Māori Quiz",
                                     font="Helvetica 18 bold",
                                     bg="sky blue",
                                     pady=10, padx=100)
        self.main_quiz_label.grid(row=0)

        # User instructions (row 1)
        self.start_instructions = Label(self.main_frame,
                                        text="To begin quiz please press "
                                             "'Start'",
                                        font="Helvetica 12 italic", wrap=250,
                                        justify=LEFT, bg=background_color,
                                        padx=10, pady=10)
        self.start_instructions.grid(row=1)

        # Start up button
        self.start_up = Button(self.main_frame, text="Start",
                               font="Helvetica 14 bold",
                               bg="light green", padx=50, pady=5)
        self.start_up.grid(row=2, column=0)

        # Scoreboard / Help button frame / Close button (row 3)
        self.other_options_frame = Frame(self.main_frame)
        self.other_options_frame.grid(row=3, pady=10)

        # Scoreboard button also will lead to export button
        self.scoreboard_button = Button(self.other_options_frame,
                                        text="Scoreboard", font="Helvetica 14 "
                                                                "bold",
                                        bg="orange", padx=10, pady=10)
        self.scoreboard_button.grid(row=0, column=0)

        # Help button will open up help details
        self.help_button = Button(self.other_options_frame,
                                  font="Helvetica 14 bold",
                                  text="Help",
                                  bg="orange", pady=10, padx=10)
        self.help_button.grid(row=0, column=1)

        # Close button will close the program and GUI
        self.close_button = Button(self.other_options_frame,
                                   font="Helvetica 14 "
                                        "bold",
                                   text="Close", bg="red", padx=10, pady=10)
        self.close_button.grid(row=0, column=2)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Māori Quiz")
    something = Opening()
    root.mainloop()
