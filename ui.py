from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz:QuizBrain):
        self.quiz_brain = quiz

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score = 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height = 250)
        self.question = self.canvas.create_text(150, 125, text="Question", width=250, font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column = 0, columnspan=2, pady=20)

        img1 = PhotoImage(file="./images/true.png")
        img2 = PhotoImage(file="./images/false.png")
        self.button1 = Button(text="click me", image=img1, command=self.true_func)
        self.button2 = Button(text="click me", image=img2, command=self.false_func)
        self.button1.grid(row = 2, column = 0)
        self.button2.grid(row = 2, column = 1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if(self.quiz_brain.still_has_questions()):
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the Quiz")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")


    def true_func(self):
        if(self.quiz_brain.check_answer("True") == True):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score : {self.quiz_brain.score}/{self.quiz_brain.question_number}")
        self.window.after(1000, self.next_question)

    def false_func(self):
        if(self.quiz_brain.check_answer("False") == True):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score : {self.quiz_brain.score}/{self.quiz_brain.question_number}")
        self.window.after(1000, self.next_question)
