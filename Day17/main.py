from data import question_data
from question_model import Question
from quiz_brain import QuestionBrain
question_bank = [Question(question["question"],question["correct_answer"]) for question in question_data]
quiz = QuestionBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

