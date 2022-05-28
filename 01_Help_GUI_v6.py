""" 01_Help_GUI_v6.py
All is kept how it was originally programming still functions the same
however new GUI design has been implemented using the Azure Theme which gives
the GUI a more futuristic and less plain look.
"""

from tkinter import *
import tkinter.ttk as ttk
from functools import partial  # To prevent unwanted windows


class Opening:
    def __init__(self):
        # Formatting variables
        background_color = "White"

        # Quiz Main Screen GUI
        self.main_frame = Frame(width=400, height=400)
        self.main_frame.grid()

        # Main Quiz Heading (row 0)
        self.main_quiz_label = Label(self.main_frame,
                                     text="Māori Quiz",
                                     font=("Helvetica", "16", "bold"),
                                     padx=10, pady=10)
        self.main_quiz_label.grid(row=0)

        # Help button (row 1)
        self.help_button = ttk.Button(self.main_frame, text="Help",
                                      command=self.help)
        self.help_button.grid(row=1, pady=10)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):
        background = "goldenrod"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (i.e. help box)
        self.help_box = Toplevel()

        # If users press cross at the top, closes help window and 'releases'
        # help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,
                                                           partner))

        # set up GUI frame
        self.help_frame = ttk.Frame(self.help_box, width=300)
        self.help_frame.grid()

        # set up help heading (row 0)
        self.how_heading = ttk.Label(self.help_frame, text="Help/Instructions",
                                     font="Helvetica 10 bold")
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = ttk.Label(self.help_frame, text="", justify=LEFT,
                                   width=40)
        self.help_text.grid()

        # Dismiss button (row 2)
        self.dismiss_btn = ttk.Button(self.help_frame, text="Dismiss",
                                      command=partial(self.close_help,
                                                      partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Māori Quiz")
    # Importing azure theme into the GUI for new aesthetic look
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")
    something = Opening()
    root.mainloop()
