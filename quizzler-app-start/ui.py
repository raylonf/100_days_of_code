from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300)
        self.text_canvas = self.canvas.create_text(150, 130, text='Some question here',width=280, fill='black', font=('Arial', 18,'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = 0
        self.score_label = Label(text=f'Score: {self.score}', bg=THEME_COLOR, fg='white', font=('Arial', 11), highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        image_correct_button = PhotoImage(file='images/true.png')
        self.correct_button = Button(image=image_correct_button, highlightthickness=0, command=self.correct_answer)
        self.correct_button.grid(column=0, row=2)

        image_incorrect_button = PhotoImage(file='images/false.png')
        self.incorrect_button = Button(image=image_incorrect_button, highlightthickness=0, command=self.incorrect_answer)
        self.incorrect_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.return_color_canvas()
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_canvas, text=q_text)
        else:
            self.canvas.itemconfig(self.text_canvas, text="You've reached the end of the questions")
            self.correct_button.config(state='disabled')
            self.incorrect_button.config(state='disabled')

    def incorrect_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer='false'))


    def correct_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer='true'))


    def return_color_canvas(self):
        self.canvas.config(bg='white')

    def give_feedback(self, is_right):
        if is_right:
            self.score += 1
            self.canvas.config(bg='green')
            self.score_label.config(text=f'Score: {self.score}')

        else:
            self.canvas.config(bg='red')

        self.window.after(200, func=self.get_next_question)






