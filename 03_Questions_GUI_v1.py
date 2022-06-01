"""" 03_Questions_GUI_v1.py
Begins the quiz for the user and gives them multiple choice answers
Version #1 - Code will ask a question and the GUI is very rough and not
designed beautifully however it is designed to work and function before more
fine-tuning is done
"""

from tkinter import *
from tkinter import messagebox as mb
import json

root = Tk()
root.geometry("800x500")
root.title("Quiz")
with open('quiz.JSON') as f:
    obj = json.load(f)
question = (obj['questions'])
options = (obj['options'])
ans = (obj['answers'])

print(question)
print(options)
print(ans)


class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)

    def question(self, qn):
        t = Label(root, text="Quiz in python Programming", width=50, bg="blue",
                  font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=question[qn], width=60, font=("times", 16, "bold"),
                   anchor="w")
        qn.place(x=70, y=100)
        return qn


quiz = Quiz()
root.mainloop()
