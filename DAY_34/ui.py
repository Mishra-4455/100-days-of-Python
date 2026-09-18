from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f"Score: 0", padx=20, pady=20, bg=THEME_COLOR, fg="white", font=("Ariel", 15, "italic"))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question goes here?", font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.tick_png= PhotoImage(file="images/true.png")
        self.correct = Button(image=self.tick_png, highlightthickness=0, width=100, height=97, padx=20, pady=20, command=self.check_right)
        self.correct.grid(column=0,row=2)

        self.cross_png= PhotoImage(file="images/false.png")
        self.incorrect = Button(image=self.cross_png, highlightthickness=0, width=100, height=97, padx=20, pady=20, command=self.check_wrong)
        self.incorrect.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "You have reached the end of the Quiz")
            self.correct.config(state="disabled")
            self.incorrect.config(state="disabled")

    def check_right(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def check_wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, answer: bool):        
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        self.score.config(text=f"Score: {self.quiz.score}")

