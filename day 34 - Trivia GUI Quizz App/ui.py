from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game !")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_image(150, 125)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=290,
            text="Some Random Text",
            font=("Arial", 18, "italic")
        )

        true_button_img = PhotoImage(file="images/true.png")
        false_button_img = PhotoImage(file="images/false.png")

        # plans to add a button to restart the whole app
        # refresh_img = PhotoImage(file="images/refresh.png")
        # self.refresh_button = Button(image=refresh_img, highlightthickness=0, )
        # self.refresh_button.grid(column=0, row=0, padx=35, pady=35)

        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.true_press)
        self.true_button.grid(column=0, row=2, padx=35, pady=35)

        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.false_press)
        self.false_button.grid(column=1, row=2, padx=35, pady=35)

        self.score_label = Label(text=f"Score :", font=("Arial", 15, "bold"), bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You are at the END of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
