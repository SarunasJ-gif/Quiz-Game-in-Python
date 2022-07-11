from tkinter import *

COLOR = "#375362"


class QuizInterface:
    def __init__(self):
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
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)




        self.window.mainloop()
