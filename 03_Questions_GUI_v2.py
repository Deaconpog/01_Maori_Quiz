"""" 03_Questions_GUI_v2.py
Begins the quiz for the user and gives them multiple choice answers
Version #2 - Code will ask a question and supply user with 4 possible answers
similar to version #1 this is a very rough version that has had no fine-tuning
nor is designed aesthetically appropriate yet"""

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
        self.option_selected = IntVar()
        self.options = self.radiobtns()
        self.display_options(self.qn)

    def question(self, qn):
        t = Label(root, text="Quiz in python Programming", width=50, bg="blue",
                  font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=question[qn], width=60, font=("times", 16, "bold"),
                   anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radiobtns(self):
        value = 0
        button = []
        y_value = 150
        while value < 4:
            btn = Radiobutton(root, text="", variable=self.option_selected,
                              value=value + 1, font=("times", 14, ))
            button.append(btn)
            btn.place(x=100, y=y_value)
            value += 1
            y_value += 40
        return button
    def display_options(self, qn):
        value = 0
        self.option_selected.set(0)
        self.ques['text'] = question[qn]
        for op in options[qn]:
            self.options[value]['text'] = op
            value += 1

quiz = Quiz()
root.mainloop()
