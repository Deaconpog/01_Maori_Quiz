"""" 05_Results_Screen_GUI_v3.py
Begins the quiz for the user and gives them multiple choice answers
Version #3 - This version of the code has implemented the previous code into
this version and made it so that all buttons work, however saving the file to
a .txt file does not keep the results and so the file has none of the results
from the user this needs to be fixed in the final version.
"""

from tkinter import *
import json  # .Json file needed to hold all the questions and answers
import random  # Import this in order to randomize the questions
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
        # Checks to see if the number of questions asked is the same as the
        # number of questions there are, and if so calls the display_result
        # function
        if self.qn == len(question):
            Display(self)
        else:
            self.quest.set(str(self.qnum) + ". " + question[self.qn])
            self.display_options(self.qn)


class Display:
    def __init__(self, r_result):
        # Stores the quiz results into variables
        self.score = int(r_result.correct / len(question) * 100)
        self.result = "Score:" + str(self.score) + "%"
        wc = len(question) - r_result.correct
        self.correct = "Number of correct answers:" + str(r_result.correct)
        self.wrong = "Number of incorrect answers:" + str(wc)
        # Destroys previous screens
        maori_q.destroy()
        result_gui = Tk()
        # Test to show it runs new screen
        print("Results")
        # Makes the screen a set size and cannot be changed
        result_gui.title("Result screen")
        result_gui.resizable(False, False)
        result_gui.geometry("650x450")
        self.result_frame = Frame(result_gui, bg="white")
        self.result_frame.pack(fill=BOTH, expand=YES)
        # Result page title
        result_title = Label(self.result_frame, text="Results of Māori Quiz",
                             width=50, bg="sky blue",
                             font=("Helvetica", 20, "bold"), pady=10)
        result_title.place(x=-100, y=0)

        # Return to main menu button restarts whole code
        self.export_button = Button(self.result_frame, text="Export Results",
                                    command=lambda: self.export(self,
                                                                r_result),
                                    width=20, bg="orange",
                                    font=("Helvetica", 16, "bold"))
        self.export_button.place(x=50, y=355)

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
                               width=50,bg="white",
                               font=("Helvetica", 15, "bold"))
        result_percent.place(x=30, y=175)

        # Exit button which quits whole quiz (need to alter in final version)
        quit_button = Button(self.result_frame, text="Exit",
                             command=result_gui.destroy, width=10,
                             bg="red", font=("Helvetica", 16, "bold"))
        quit_button.place(x=450, y=355)

    # Function needed to run the export button and contains all the important
    # and relevant details
    def export(self, previous, final_result):
        # Test to make sure function is called correctly
        print("total correct ans:", self.wrong)

        print(previous)  # For testing purposes
        background = "#a9ef99"  # Pale Green

        # disable export button
        previous.export_button.config(state=DISABLED)

        # sets up child window (i.e. export box)
        self.export_box = Toplevel()

        # If users press cross at the top, closes export window and 'releases'
        # export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             final_result))

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
                                  command=partial(lambda: self.save_result
                                  (previous)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export,
                                                    previous))
        self.cancel_button.grid(row=0, column=1)

    def save_result(self, previous):
        # Regular expression to check file name. Can be Upper or Lower case letters
        valid_char = "[A-Za-z0-9_]"  # Numbers or underscores
        has_error = "no"

        # This is all the results from the display class that has the % result
        # and the number of wrong + right answers
        number_correct = previous.correct
        number_wrong = previous.wrong
        percent_correct = previous.result

        # Is a value that puts all the previous varibles together for the .txt
        # file
        total = number_wrong + number_correct + percent_correct

        filename = self.filename_entry.get()
        print(filename)
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
            self.save_error_label.config(text=f"Invalid filename - {problem}")
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        else:
            # If there are no errors, generate text file and then close
            # dialogue. Add .txt suffix!

            filename = filename + ".txt"

            # Create file to hold data
            f = open(filename, "w+")

            # close file
            f.close()

            # close dialogue
            self.close_export(self)

    def close_export(self, previous):
        # Put export button back to normal
        self.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
quiz = Quiz()
maori_q.mainloop()
