""" 01_Help_GUI_v4.py
The GUI has further been improved implementing functools preventing multiple
screens from being opened at the same time.
"""

from tkinter import *
from functools import partial  # To prevent unwanted windows


class Opening:
    def __init__(self):
        # Formatting variables
        background_color = "white"

        # Quiz Main Screen GUI
        self.main_frame = Frame(width=300, height=300,
                                bg=background_color,
                                pady=10)
        self.main_frame.grid()

        # Main Quiz Heading (row 0)
        self.main_quiz_label = Label(self.main_frame,
                                     text="Māori Quiz",
                                     font=("Helvetica", "16", "bold",),
                                     bg=background_color, padx=10,
                                     pady=10)
        self.main_quiz_label.grid(row=0)

        # Help button (row 1)
        self.help_button = Button(self.main_frame, text="Help",
                                  font=("Helvetica", "14"), padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help?")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):
        background = "goldenrod"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (i.e. help box)
        self.help_box = Toplevel()

        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help/Instructions",
                                 font="Helvetica 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid()

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10,
                                  bg="orange", font="Helvetica 10 bold",
                                  command=self.close_help)
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Māori Quiz")
    something = Opening()
    root.mainloop()
