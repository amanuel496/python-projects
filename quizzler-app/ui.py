from tkinter import *
from typing import Any

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_STYLE = "Arial"
FONT_SIZE = 20
RED_BG = "red"
GREEN_BG = "green"
WHITE_BG = "white"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.canvas = Canvas(width=300, height=250)
        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=lambda: self.on_click("true"))
        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=lambda: self.on_click("false"))
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text=self.get_next_question(), fill=THEME_COLOR, font=(FONT_STYLE, FONT_SIZE, "italic")
        )
        self.config_ui()

        self.window.mainloop()

    def config_ui(self):
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_btn.grid(row=2, column=0)

        self.false_btn.grid(row=2, column=1)

        self.score_label.grid(row=0, column=1)

    def set_question(self, question):
        self.canvas.config(bg=WHITE_BG)
        self.canvas.itemconfig(self.question_text, text=question)

    def get_next_question(self):
        question = self.quiz.next_question()
        return question

    def on_click(self, user_answer):
        if self.quiz.still_has_questions():
            question = self.get_next_question()

            if self.quiz.check_answer(user_answer):
                self.give_feedback(True)
                score = self.quiz.score
                self.score_label.config(text=f"Score: {score}", fg="white", bg=THEME_COLOR)
            else:
                self.give_feedback(False)
            self.window.after(1000, self.set_question, question)

        else:
            self.give_feedback(self.quiz.check_answer(user_answer))
            self.window.after(1000, self.set_question, "You've reached the end of the quiz.")

    def give_feedback(self, is_right: bool) -> Any:
        if is_right:
            self.canvas.config(bg=GREEN_BG)
        else:
            self.canvas.config(bg=RED_BG)
