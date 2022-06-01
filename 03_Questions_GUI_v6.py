"""" 03_Questions_GUI_v6.py
Begins the quiz for the user and gives them multiple choice answers
Version #6 - Code will ask a question and supply user with 4 possible answers
version 5 has tidied up a lot of code and the GUI itself making it more
appropriate
Built upon previous versions this is being more fine-tuned and questions are
now added tp the .JSON file the quiz is also being altered in terms of
colouration and size to be more appropriate.
"""

from tkinter import *
from tkinter import messagebox as mb
import json

root = Tk()
root.title("Quiz")
with open('quiz.JSON') as f:
    obj = json.load(f)
question = (obj['questions'])
options = (obj['options'])
ans = (obj['answers'])


class Quiz:
    def __init__(self):
        background_color = "white"
        # Quiz Main Screen GUI
        self.main_frame = Frame(width=650, height=450, bg=background_color,
                                pady=0)
        self.main_frame.grid()

        self.qn = 0
        self.ques = self.question(self.qn)
        self.option_selected = IntVar()
        self.options = self.radiobtns()
        self.display_options(self.qn)
        self.next_step_buttons()

        self.correct = 0

    # This is the title of the quiz and also the question number
    def question(self, qn):
        # Title of quiz
        t = Label(self.main_frame, text="Maori Quiz", width=50, bg="sky blue",
                  font=("Helvetica", 20, "bold"), pady=10)
        t.place(x=-100, y=0)
        # Gives which question number it is
        qn = Label(self.main_frame, text=question[qn], width=60,
                   font=("Helvetica", 16, "bold"),
                   anchor="w", bg="white")
        qn.place(x=50, y=75)
        return qn

    # Is the radio buttons which are used as the input buttons in the quiz
    def radiobtns(self):
        value = 0
        button = []
        y_value = 150
        while value < 4:
            btn = Radiobutton(root, text="", variable=self.option_selected,
                              value=value + 1, font=("Helvetica", 14),
                              bg="white")
            button.append(btn)
            btn.place(x=80, y=y_value)
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
        next_button = Button(self.main_frame, text="Next",
                             command=self.next_btn,
                             width=10, bg="light green",
                             font=("Helvetica", 16, "bold"))
        next_button.place(x=50, y=355)
        # Exit button which quits whole quiz (need to alter in final version)
        quit_button = Button(self.main_frame, text="Exit",
                             command=root.destroy, width=10,
                             bg="red", font=("Helvetica", 16, "bold"))
        quit_button.place(x=450, y=355)

    # Compares answer received to the available answer in the .JSON file
    def check_ans(self, qn):
        if self.option_selected.get() == ans[qn]:
            return True

    # If the answer is correct adds a point to the total correct score
    # (self.correct)
    def next_btn(self):
        if self.check_ans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(question):
            self.display_result()
        else:
            self.display_options(self.qn)

    # Displays the result that the user has received displays this in a
    # mini-box however and ideally needs to be on another page
    def display_result(self):
        score = int(self.correct / len(question) * 100)
        result = "Score:" + str(score) + "%"
        wc = len(question) - self.correct
        correct = "Number of correct answers:" + str(self.correct)
        wrong = "Number if incorrect answers:" + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))


quiz = Quiz()
root.mainloop()
