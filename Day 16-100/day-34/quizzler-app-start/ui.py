from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)


        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 12, "bold")
        )
        self.score_label.grid(row=0, column=1, sticky="e")


        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.card_question = self.canvas.create_text(
            150, 125,
            text="Question text goes here",
            width=280,
            fill=THEME_COLOR,
            font=("Arial", 18, "italic")
        )


        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")


        self.true_button = Button(
            image=self.true_img,
            highlightthickness=0,
            bd=0,
            command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(
            image=self.false_img,
            highlightthickness=0,
            bd=0,
            command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def true_pressed(self):
        print("True")

    def false_pressed(self):
        print("False")

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.card_question,text=q_text)










