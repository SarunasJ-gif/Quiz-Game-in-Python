from tkinter import *
from quiz_brain import QuizBrain

COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text_question = self.canvas.create_text(150, 125, text="This is question",
                                                     fill=COLOR,
                                                     width=280,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_label = Label(text=f"Score: 0", bg=COLOR, fg="white", font=("Arial", 10, "italic"))
        self.score_label.grid(column=1, row=0)
        true_image = PhotoImage(file="buttons/true.png")
        false_image = PhotoImage(file="buttons/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.push_true_button)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.push_false_button)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_question():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.text_question, text=text)
        else:
            self.canvas.itemconfig(self.text_question, text=f"Game is over. Your score are: {self.quiz_brain.score}")
            self.true_button.config(status="disable")
            self.false_button.config(status="disable")

    def push_true_button(self):
        if self.quiz_brain.check_answer("True"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def push_false_button(self):
        if self.quiz_brain.check_answer("False"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
