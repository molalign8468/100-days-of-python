import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        try:
            self.true_image = tkinter.PhotoImage(file="./images/true.png")
            self.false_image = tkinter.PhotoImage(file="./images/false.png")
        except tkinter.TclError:
            print("Image files not found. Using text buttons as a fallback.")
            self.true_image = None
            self.false_image = None
            
        self.score_label = tkinter.Label(self.window, text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12))
        self.score_label.grid(column=1, row=0, pady=20)

        self.canvas = tkinter.Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Hello hello",
            width=280,
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_btn = tkinter.Button(self.window, image=self.true_image, highlightthickness=0, bd=0, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2)

        self.false_btn = tkinter.Button(self.window, image=self.false_image, highlightthickness=0, bd=0, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz.\nYour final score is {self.quiz.score}/{self.quiz.question_number}.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)