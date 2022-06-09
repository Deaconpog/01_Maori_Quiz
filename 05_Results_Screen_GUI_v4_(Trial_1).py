"""" 05_Results_Screen_GUI_v4_(Trial_1).py
Begins the quiz for the user and gives them multiple choice answers
Version #4_Trial_1 - Does not use any export function and instead simply
exports the results when button is pressed the export function has been removed
and because of this the code has been significantly shortened, however this has
taken away the user's ability to create their own .txt file.
"""

from tkinter import *
import json
# .Json file needed to hold all the questions and answers
import random  # Import this in order to randomize the questions
from functools import partial  # To prevent unwanted windows
import re


class Quiz:
    def __init__(self):
        # Quiz Main Screen GUI
        self.main_frame = Frame(width=650, height=450, bg="white",
                                pady=0)
        self.main_frame.grid()

        self.qnum = 1
        self.quest = StringVar()
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
        title = Label(self.main_frame, text="Māori Quiz", width=50,
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
        if self.check_ans(self.qn):
            self.correct += 1
        self.qn += 1
        self.qnum += 1
        if self.qn == len(question):
            Display(self)
        else:
            self.quest.set(str(self.qnum) + ". " + question[self.qn])
            self.display_options(self.qn)
    # Displays the result that the user has received displays this in a
    # mini-box however and ideally needs to be on another page


class Display:
    def __init__(self, r_result):
        # Stores the quiz results into variables
        self.score = int(r_result.correct / len(question) * 100)
        self.result = "Score: " + str(self.score) + "%"
        wc = len(question) - r_result.correct
        self.correct = "Number of correct answers: " + str(r_result.correct)
        self.wrong = "Number of incorrect answers: " + str(wc)
        # Destroys previous screens
        maori_q.destroy()
        result_gui = Tk()
        # Test to show it runs new screen
        print("Results")
        result_gui.title("Result screen")
        result_gui.resizable(False, False)
        result_gui.geometry("650x350")
        self.result_frame = Frame(result_gui, bg="white")
        self.result_frame.pack(fill=BOTH, expand=YES)
        # Result page title
        result_title = Label(self.result_frame, text="Results of Māori Quiz",
                             width=50, bg="sky blue",
                             font=("Helvetica", 20, "bold"), pady=10)
        result_title.place(x=-100, y=0)

        # Return to main menu button restarts whole code
        self.export_button = Button(self.result_frame, text="Export Results",
                                    command=lambda: (self.result_txt,
                                                     print("Test to make sure "
                                                           "file is saved")),
                                    width=20, bg="orange",
                                    font=("Helvetica", 16, "bold"))
        self.export_button.place(x=50, y=275)

        # Number of questions correct label
        result_correct = Label(self.result_frame,
                               text="Will export file to a .txt file in your "
                                    "folder, called "
                                    "'Results_of_Māori_Quiz.txt'",
                               width=50, bg="white", justify=CENTER, wrap=200,
                               fg="maroon",
                               font=("Helvetica", 10, "bold"))
        result_correct.place(x=-10, y=210)

        # Number of questions correct label
        result_correct = Label(self.result_frame, text=f"{self.correct}",
                               width=50, bg="white",
                               font=("Helvetica", 15, "bold"))
        result_correct.place(x=30, y=75)

        # Number of questions incorrect label
        result_wrong = Label(self.result_frame, text=f"{self.wrong}", width=50,
                             bg="white",
                             font=("Helvetica", 15, "bold"))
        result_wrong.place(x=30, y=125)

        # Number of questions incorrect label
        result_percent = Label(self.result_frame, text=f"{self.result}",
                               width=50, bg="white",
                               font=("Helvetica", 15, "bold"))
        result_percent.place(x=30, y=175)

        # Exit button which quits whole quiz (need to alter in final version)
        quit_button = Button(self.result_frame, text="Exit",
                             command=result_gui.destroy, width=10,
                             bg="red", font=("Helvetica", 16, "bold"))
        quit_button.place(x=450, y=275)

        number_correct = self.correct
        number_wrong = self.wrong
        percent_correct = self.result

        total = (number_correct, "\n", number_wrong, "\n",
                 percent_correct)

        self.result_txt = "Results_of_Māori_Quiz.txt"

        # Export button made to be called when pressed and simply saves results
        # as a .txt file to system.
        # Create file to hold data
        f = open(self.result_txt, "w+")

        for item in total:
            f.write(item)


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

# main routine
quiz = Quiz()
maori_q.mainloop()
