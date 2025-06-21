import random
class QuestionGenerator:
    def __init__(self, question, correct_answer, incorrect_answers, difficulty):
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.difficulty = difficulty
        self.all_choices = [self.correct_answer] + self.incorrect_answers
        random.shuffle(self.all_choices)
