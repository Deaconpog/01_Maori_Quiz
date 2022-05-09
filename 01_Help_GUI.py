""" Is based off of original Tkinter template (00_Tkinter_template.py)
 with only class name being altered
 """

from tkinter import *
import random


class Opening:
    def __init__(self, parent):
        print("hello world")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Māori Quiz")
    something = Opening(root)
    root.mainloop()
