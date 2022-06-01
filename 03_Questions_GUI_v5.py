"""" 03_Questions_GUI_v5.py
Begins the quiz for the user and gives them multiple choice answers
Version #5 - Code will ask a question and supply user with 4 possible answers
version 5 has tidied up a lot of code and the GUI itself making it more
appropriate
Built upon previous versions this is still a very rough version greater and
more in depth work/fine-tuning will be done once all code has been assembled.
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
        self.option_selected = IntVar()
        self.options = self.radiobtns()
        self.display_options(self.qn)
        self.next_step_buttons()

        self.correct = 0

    # This is the title of the quiz and also the quetion number
    def question(self, qn):
        # Title of quiz
        t = Label(root, text="Quiz in python", width=50, bg="blue",
                  font=("times", 20, "bold"))
        t.place(x=0, y=2)
        # Gives which question number it is
        qn = Label(root, text=question[qn], width=60,
                   font=("times", 16, "bold"),
                   anchor="w")
        qn.place(x=70, y=100)
        return qn

    # Is the radio buttons which are used as the input buttons in the quiz
    def radiobtns(self):
        value = 0
        button = []
        y_value = 150
        while value < 4:
            btn = Radiobutton(root, text="", variable=self.option_selected,
                              value=value + 1, font=("times", 14,))
            button.append(btn)
            btn.place(x=100, y=y_value)
            value += 1
            y_value += 40
        return button

    # Next to the buttons gives the possible answers
    def display_options(self, qn):
        value = 0
        self.option_selected.set(0)
        self.ques['text'] = question[qn]
        for op in options[qn]:
            self.options[value]['text'] = op
            value += 1

    # 'Next' button and a exit button to quit quiz
    def next_step_buttons(self):
        # Acts as the next button
        next_button = Button(root, text="Next", command=self.next_btn,
                             width=10, bg="lime", fg="white",
                             font=("times", 16, "bold"))
        next_button.place(x=200, y=380)
        # Exit button which quits whole quiz (need to alter in final version)
        quit_button = Button(root, text="Exit", command=root.destroy, width=10,
                             bg="red", fg="white",
                             font=("times", 16, "bold"))
        quit_button.place(x=360, y=380)

    # Compares answer received to the available answer in the .JSON file
    def check_ans(self, qn):
        if self.option_selected.get() == ans[qn]:
            return True

    # If the answer is correct adds a point to the total correct score
    # (self.correct)
    def next_btn(self):
        if self.check_ans(self.qn):
            self.correct += 1
        self.qn +=1
        if self.qn == len(question):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct / len(question) * 100)
        result = "Score:" + str(score) + "%"
        wc = len(question) - self.correct
        correct = "Number of correct answers:" + str(self.correct)
        wrong = "Number if incorrect answers:" + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))


quiz = Quiz()
root.mainloop()
