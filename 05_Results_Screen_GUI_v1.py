"""" 05_Results_Screen_GUI_v1.py
Begins the quiz for the user and gives them multiple choice answers
Version #1 - Code will ask a question and supply user with 4 possible answers
these questions will be randomized and there will be 15 questions instead of 20
this is because the test otherwise has too many questions.
also gives user their results not in the form of a small text box
"""

from tkinter import *
import json
import random
from functools import partial  # To prevent unwanted windows
import re

root = Tk()
root.title("Quiz")
with open('quiz.JSON') as file:
    obj = json.load(file)
question = (obj['questions'])
options = (obj['options'])
ans = (obj['answers'])
zi = zip(question, options, ans)
lis = list(zi)
random.shuffle(lis)
question, options, ans = zip(*lis)

new_lis = slice(lis[:5])


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
        t = Label(self.main_frame, text="Maori Quiz", width=50, bg="sky blue",
                  font=("Helvetica", 20, "bold"), pady=10)
        t.place(x=-100, y=0)
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
        self.qnum += 1
        if self.qn == len(question):
            self.display_result()
        else:
            self.quest.set(str(self.qnum) + ". " + question[self.qn])
            self.display_options(self.qn)

    # Displays the result that the user has received displays this in a
    # mini-box however and ideally needs to be on another page
    def display_result(self):
        score = int(self.correct / len(question) * 100)
        result = "Score:" + str(score) + "%"
        wc = len(question) - self.correct
        correct = "Number of correct answers:" + str(self.correct)
        wrong = "Number if incorrect answers:" + str(wc)

    def 


class Export:
    def __init__(self, partner, calc_history):
        # print(calc_history)  # For testing purposes
        background = "#a9ef99"  # Pale Green

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window (i.e. export box)
        self.export_box = Toplevel()

        # If users press cross at the top, closes export window and 'releases'
        # export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a filename in the box below and "
                                      "press the Save button to save your "
                                      "calculation history to a text file.",
                                 justify=LEFT, width=40, bg=background,
                                 wrap=250)
        self.export_text.grid()

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame,
                                 text="If the filename you enter below "
                                      "already exists, it's contents will be "
                                      "replaced with your calculation history."
                                 , justify=LEFT, bg="#ffafaf",  # Pink
                                 fg="maroon", font="Arial 10 italic",
                                 padx=10, pady=10,
                                 wrap=225)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message labels (row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history
                                  (partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export,
                                                    partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):
        # Regular expression to check file name. Can be Upper or Lower case letters
        valid_char = "[A-Za-z0-9_]"  # Numbers or underscores
        has_error = "no"

        filename = self.filename_entry.get()
        # print(filename)
        for letter in filename:
            if re.match(valid_char, letter):
                continue  # If the letter is valid, goes back and checks the next

            elif letter == " ":  # Otherwise, find problem
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":  # Describe problem
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".
                                         format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        else:
            # If there are no errors, generate text file and then close
            # dialogue. Add .txt suffix!

            filename = filename + ".txt"

            # Create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            for item in calc_history:
                f.write(item + "/n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


quiz = Quiz()
root.mainloop()
