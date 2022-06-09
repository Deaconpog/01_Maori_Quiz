""" 06_Full_Quiz_v1.py
"""

from tkinter import *
import json  # .Json file needed to hold all the questions and answers
import random  # Import this in order to randomize the questions
from functools import partial  # To prevent unwanted windows
import re


class Opening:
    def __init__(self, start_gui):
        # Formatting variables
        background_color = "White"

        # Quiz Main Screen GUI
        self.main_frame = Frame(width=460, height=225, bg=background_color,
                                pady=0)
        self.main_frame.grid()

        # Main Quiz Heading (row 0)
        self.main_quiz_label = Label(self.main_frame,
                                     text="Māori Mythology Quiz",
                                     font="Helvetica 16 bold",
                                     bg="sky blue",
                                     pady=10, padx=190)
        self.main_quiz_label.place(x=0, y=0)

        # User instructions (row 1)
        self.start_instructions = Label(self.main_frame,
                                        text="To begin please press 'Start'",
                                        font="Helvetica 10 italic",
                                        bg=background_color,
                                        padx=10, pady=10)
        self.start_instructions.place(x=140, y=50)

        # Start up button
        self.start_up = Button(self.main_frame, text="Start",
                               font="Helvetica 10 bold",
                               bg="light green", padx=50, pady=5,
                               command=self.start_quiz)
        self.start_up.place(x=160, y=80)

        # Help button will open up help details
        self.help_button = Button(font="Helvetica 10 bold",
                                  text="Help",
                                  bg="orange", pady=10, padx=10,
                                  command=self.help, width=10)
        self.help_button.place(x=90, y=150)

        # Close button will close the program and GUI
        self.close_button = Button(font="Helvetica 10 "
                                        "bold",
                                   text="Close", bg="orange red", padx=10,
                                   pady=10,
                                   command=start_gui.destroy, width=10)
        self.close_button.place(x=290, y=150)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Kia ora, welcome to the \n Māori "
                                          "Mythology Quiz, to begin \n please "
                                          "press start, and you will \n be "
                                          "given 15 multi-choice \n questions "
                                          "after answering all \n your score "
                                          "will be shown at the end \n and "
                                          "you will be able to \n export your "
                                          "results to a.txt file. ")

    def start_quiz(self):
        start_gui.destroy()
        self.start()

    def start(self):
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

            # Is the radio buttons which are used as the input buttons in the
            # quiz
            def radiobtns(self):
                value = 0
                button = []
                y_value = 150
                while value < 4:
                    btn = Radiobutton(maori_quiz, text="",
                                      variable=self.option_selected,
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
                # Exit button which quits whole quiz (need to alter in final
                # version)
                quit_button = Button(self.main_frame, text="Exit",
                                     command=maori_quiz.destroy, width=10,
                                     bg="red", font=("Helvetica", 16, "bold"))
                quit_button.place(x=450, y=355)

            # Compares answer received to the available answer in the .JSON
            # file
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

        class Display:
            def __init__(self, r_result):
                # Stores the quiz results into variables
                self.score = int(r_result.correct / len(question) * 100)
                self.result = "Score: " + str(self.score) + "%"
                wc = len(question) - r_result.correct
                self.correct = "Number of correct answers: " + str(
                    r_result.correct)
                self.wrong = "Number of incorrect answers: " + str(wc)
                # Destroys previous screens
                maori_quiz.destroy()
                result_gui = Tk()
                # Test to show it runs new screen
                print("Results")
                result_gui.title("Result screen")
                result_gui.resizable(False, False)
                result_gui.geometry("650x350")
                self.result_frame = Frame(result_gui, bg="white")
                self.result_frame.pack(fill=BOTH, expand=YES)
                # Result page title
                result_title = Label(self.result_frame,
                                     text="Results of Māori Quiz",
                                     width=50, bg="sky blue",
                                     font=("Helvetica", 20, "bold"), pady=10)
                result_title.place(x=-100, y=0)

                # Return to main menu button restarts whole code
                self.export_button = Button(self.result_frame,
                                            text="Export Results",
                                            command=lambda: self.export(self,
                                                                        r_result),
                                            width=20, bg="orange",
                                            font=("Helvetica", 16, "bold"))
                self.export_button.place(x=50, y=275)

                # Number of questions correct label
                result_correct = Label(self.result_frame,
                                       text=f"{self.correct}",
                                       width=50, bg="white",
                                       font=("Helvetica", 15, "bold"))
                result_correct.place(x=30, y=75)

                # Number of questions incorrect label
                result_wrong = Label(self.result_frame, text=f"{self.wrong}",
                                     width=50,
                                     bg="white",
                                     font=("Helvetica", 15, "bold"))
                result_wrong.place(x=30, y=125)

                # Number of questions incorrect label
                result_percent = Label(self.result_frame,
                                       text=f"{self.result}",
                                       width=50, bg="white",
                                       font=("Helvetica", 15, "bold"))
                result_percent.place(x=30, y=175)

                # Exit button which quits whole quiz (need to alter in final
                # version)
                quit_button = Button(self.result_frame, text="Exit",
                                     command=result_gui.destroy, width=10,
                                     bg="red", font=("Helvetica", 16, "bold"))
                quit_button.place(x=450, y=275)

            def export(self, previous, final_result):
                # Testing purposes
                print("total correct ans:", self.correct)

                print(previous)  # For testing purposes
                background = "goldenrod"

                # disable export button
                previous.export_button.config(state=DISABLED)

                # sets up child window (i.e. export box)
                self.export_box = Toplevel()

                self.export_box.resizable(False, False)

                # If users press cross at the top, closes export window and
                # 'releases'
                # export button
                self.export_box.protocol('WM_DELETE_WINDOW',
                                         partial(self.close_export,
                                                 final_result))

                # set up GUI frame
                self.export_frame = Frame(self.export_box, width=300,
                                          bg=background)
                self.export_frame.grid()

                # set up export heading (row 0)
                self.how_heading = Label(self.export_frame,
                                         text="Export Instructions",
                                         font="arial 10 bold", bg=background)
                self.how_heading.grid(row=0)

                # Export text (label, row 1)
                self.export_text = Label(self.export_frame,
                                         text="Enter a filename in the box"
                                              " below and press the Save "
                                              "button to save your "
                                              "results to a .txt file.",
                                         justify=LEFT, width=40, bg=background)
                self.export_text.grid()

                # Warning text (label, row 2)
                self.export_text = Label(self.export_frame,
                                         text="If the filename you enter below"
                                              " already exists, it's contents "
                                              "will be replaced with your "
                                              "calculation history."
                                         , justify=LEFT, bg="light salmon",
                                         # Pink
                                         fg="maroon", font="Arial 10 italic",
                                         padx=10, pady=10,
                                         wrap=225)
                self.export_text.grid(row=2, pady=10)

                # Filename entry box (row 3)
                self.filename_entry = Entry(self.export_frame, width=20,
                                            font="Arial 14 bold",
                                            justify=CENTER)
                self.filename_entry.grid(row=3, pady=10)

                # Error Message labels (row 4)
                self.save_error_label = Label(self.export_frame, text="",
                                              fg="maroon",
                                              bg=background)
                self.save_error_label.grid(row=4)

                # Save / Cancel Frame (row 5)
                self.save_cancel_frame = Frame(self.export_frame)
                self.save_cancel_frame.grid(row=5, pady=10)

                # Save and Cancel Buttons (row 0 of save_cancel_frame)
                self.save_button = Button(self.save_cancel_frame, text="Save",
                                          command=partial(
                                              lambda: self.save_result
                                              (previous)), bg="orange")
                self.save_button.grid(row=0, column=0)

                self.cancel_button = Button(self.save_cancel_frame,
                                            text="Cancel",
                                            command=partial(self.close_export,
                                                            previous),
                                            bg="orange")
                self.cancel_button.grid(row=0, column=1)

            def save_result(self, previous):
                # Regular expression to check file name. Can be Upper or Lower
                # case letters
                valid_char = "[A-Za-z0-9_]"  # Numbers or underscores
                has_error = "no"

                number_correct = previous.correct
                number_wrong = previous.wrong
                percent_correct = previous.result

                total = (number_correct, "\n", number_wrong, "\n",
                         percent_correct)

                filename = self.filename_entry.get()
                print(filename)
                for letter in filename:
                    if re.match(valid_char, letter):
                        continue  # If the letter is valid, goes back and
                        # checks the next

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
                    self.save_error_label.config(
                        text=f"Invalid filename - {problem}")
                    # Change entry box background to pink
                    self.filename_entry.config(bg="#ffafaf")
                    print()
                else:
                    # If there are no errors, generate text file and then close
                    # dialogue. Add .txt suffix!

                    filename = filename + ".txt"

                    # Create file to hold data
                    f = open(filename, "w+")

                    for item in total:
                        f.write(item)

                    # close file
                    f.close()

                    # close dialogue
                    self.close_export(self)

            def close_export(self, previous):
                # Put export button back to normal
                self.export_button.config(state=NORMAL)
                self.export_box.destroy()

        # All the code needed to run the quiz Questions, options, and answers
        # also this allows the .JSON file to be randomized while keeping
        # answers and questions the same.
        maori_quiz = Tk()
        with open('quiz.JSON') as file:
            obj = json.load(file)
        question = (obj['questions'])
        options = (obj['options'])
        ans = (obj['answers'])
        zi = zip(question, options, ans)
        lis = list(zi)
        random.shuffle(lis)
        question, options, ans = zip(*lis)

        quiz = Quiz()
        maori_quiz.mainloop()


class Help:
    def __init__(self, partner):
        background = "goldenrod"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (i.e. help box)
        self.help_box = Toplevel()

        self.help_box.resizable(False, False)

        # If users press cross at the top, closes help window and 'releases'
        # help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,
                                                           partner))

        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help/Instructions",
                                 font="Helvetica 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid()

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10,
                                  bg="orange", font="Helvetica 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    start_gui = Tk()
    start_gui.title("Māori Quiz")
    start_gui.geometry("460x225")
    start_gui.resizable(False, False)
    Opening(start_gui)
    start_gui.mainloop()
