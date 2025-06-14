class QuestionBrain:
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_no = 0
        self.score = 0
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.question} (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def still_has_question(self):
        return len(self.question_list) > self.question_no

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower() :
            self.score += 1 
            print("You got it right")
        else:
            print("You Lose it ")
        print(f"The correct answer was {correct_answer}")
        print(f"Your Score is {self.score}/{self.question_no}")
