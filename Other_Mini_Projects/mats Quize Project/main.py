from data import question
from quastion import QuestionGenerator
from quastionBrain import QuestionBrain
questions =[QuestionGenerator(items["question"],items["correct_answer"],items["incorrect_answers"],items["difficulty"]) for items in question]
question_brain = QuestionBrain(questions)
while question_brain.still_has_question():
    question_brain.next_question()
