"""" 05_Results_Screen_GUI_v1.py
Begins the quiz for the user and gives them multiple choice answers
Version #1 - In this version the code opens a result screen there are both an
exit and export button however only the exit button works and on the result
screen there is also none of the user's results shown, the export button does
not work at all and needs to be more properly worked on.
"""

from tkinter import *
import json # Used as file to hold questions, and answers
import random # To randomize quiz questions
from functools import partial  # To prevent unwanted windows
import re

# All the code needed to run the quiz Questions, options, and answers also this
# allows the .JSON file to be randomized while keeping answers and questions
# the same.
maori_q = Tk()
maori_q.title("Quiz")
with open('quiz.JSON') as file:
    obj = json.load(file)
question = (obj['questions'])
options = (obj['options'])
ans = (obj['answers'])
zi = zip(question, options, ans)
lis = list(zi)
random.shuffle(lis)
question, options, ans = zip(*lis)


class Quiz:
    def __init__(self):
        # Quiz Main Screen GUI
        self.main_frame = Frame(width=650, height=450, bg="white",
                                pady=0)
        self.main_frame.grid()
        # Question number
        self.qnum = 1
        self.quest = StringVar()
        self.qn = 0
        self.ques = self.question(self.qn)
        # radio buttons makes sure they run accordingly
        self.option_selected = IntVar()
        self.options = self.radiobtns()
        self.display_options(self.qn)
        self.next_step_buttons()

        self.correct = 0

    # This is the title of the quiz and also the question number
    def question(self, qn):
        # Title of quiz
        title = Label(self.main_frame, text="Maori Quiz", width=50,
                      bg="sky blue",
                      font=("Helvetica", 20, "bold"), pady=10)
        title.place(x=-100, y=0)
        self.quest.set(str(self.qnum) + ". " + question[qn])
        # Gives which question number it is
        qn = Label(self.main_frame, textvariable=self.quest, width=60,
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
            btn = Radiobutton(maori_q, text="", variable=self.option_selected,
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
                             command=maori_q.destroy, width=10,
                             bg="red", font=("Helvetica", 16, "bold"))
        quit_button.place(x=450, y=355)

    # Compares answer received to the available answer in the .JSON file
    def check_ans(self, qn):
        if self.option_selected.get() == ans[qn]:
            return True

    # If the answer is correct adds a point to the total correct score
    # (self.correct)
    def next_btn(self):
        # Adds one to the number of correct for the user if correct, and also
        # adds one to question number
        if self.check_ans(self.qn):
            self.correct += 1
        self.qn += 1
        self.qnum += 1
        # Checks to see if the number of questions asked is the same as the
        # number of questions there are, and if so calls the display_result
        # function
        if self.qn == len(question):
            self.display_result()
        else:
            self.quest.set(str(self.qnum) + ". " + question[self.qn])
            self.display_options(self.qn)

    # Calls the export class in order to carry on export screen code
    def export(self, r_results):
        Export(self, r_results)

    def display_result(self):
        # Destroys previous screens
        maori_q.destroy()
        # Stores the quiz results into variables
        score = int(self.correct / len(question) * 100)
        result = "Score:" + str(score) + "%"
        wc = len(question) - self.correct
        correct = "Number of correct answers:" + str(self.correct)
        wrong = "Number if incorrect answers:" + str(wc)
        result_gui = Tk()
        # Test to show it runs new screen
        print("Results")
        # Creating the result screen
        result_gui.title("Result screen")
        # Makes the screen a set size
        result_gui.resizable(False, False)
        result_gui.geometry("650x450")
        result_frame = Frame(result_gui)
        result_frame.pack(fill=BOTH, expand=YES)
        # Main heading for the result screen
        result_title = Label(result_frame, text="Results", width=50,
                             bg="sky blue",
                             font=("Helvetica", 20, "bold"), pady=10)
        result_title.place(x=-100, y=0)

        # Exit button which quits whole quiz (need to alter in final version)
        quit_button = Button(result_frame, text="Exit",
                             command=result_gui.destroy, width=10,
                             bg="red", font=("Helvetica", 16, "bold"))
        quit_button.place(x=450, y=355)

        # Return to main menu button restarts whole code
        export_button = Button(result_frame, text="Export Results",
                               command=lambda: print("Export"),
                               width=20, bg="orange",
                               font=("Helvetica", 16, "bold"))
        export_button.place(x=50, y=355)

# Main routine
quiz = Quiz()
maori_q.mainloop()
