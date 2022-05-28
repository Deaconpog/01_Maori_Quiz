""" 02_main_frame_GUI_v2_(Trial2).py
Basic tkinter template copied from the 00_tkinter_template.py
and based on the planning done in Trello (component 2 - slide 19)
buttons are there but only close button works now as other buttons are being
developed as separate components
Will be used as a trial (Trial2) and I will ask one user to see if there are
ways to improve on this different version and whether it is worse/better than
trial 1.
"""

from tkinter import *
import tkinter.ttk as ttk
from functools import partial  # To prevent unwanted additional windows
import random


class Opening:
    def __init__(self):
        # Formatting variables
        background_color = "White"

        # Quiz Main Screen GUI
        self.main_frame = Frame(width=350, height=200)
        self.main_frame.grid()

        # Main Quiz Heading (row 0)
        self.main_quiz_label = Label(self.main_frame,
                                     text="Māori Quiz",
                                     font="Helvetica 16 bold")
        # Where the main label is located
        self.main_quiz_label.place(x=125, y=0)

        # User instructions (row 1)
        self.start_instructions = ttk.Label(text="To begin please press "
                                                 "'Start'",
                                            font="Helvetica 10 italic",
                                            justify=LEFT)
        # Where the instructions label is located
        self.start_instructions.place(x=100, y=50)

        # Start up button
        self.start_up = ttk.Button(text="Start", command=self.start_quiz)
        # Where start button is located
        self.start_up.place(x=135, y=75)

        # Scoreboard button also will lead to export button
        self.scoreboard_button = ttk.Button(text="Scoreboard",
                                            command=self.scoreboard)
        # Where scoreboard button is located
        self.scoreboard_button.place(x=35, y=150)

        # Help button will open up help details
        self.help_button = ttk.Button(text="Help", command=self.help)
        # Where help button is located
        self.help_button.place(x=135, y=150)

        # Close button will close the program and GUI
        self.close_button = ttk.Button(text="Close", command=root.destroy)
        # Where close button is located
        self.close_button.place(x=235, y=150)

    def start_quiz(self):
        print("Testing function to ensure 'start' works correctly")

    def help(self):
        print("Testing function to ensure 'help' works correctly")

    def scoreboard(self):
        print("Testing function to ensure 'scoreboard' works correctly")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Māori Quiz")
    # Importing azure theme into the GUI for new aesthetic look
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")
    something = Opening()
    root.mainloop()
