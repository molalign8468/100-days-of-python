
class QuestionBrain:
    def __init__(self, question_list):
        self.question_list = question_list  
        self.score = 0                   
        self.question_number = 0          
   
    def next_question(self):
        current_question = self.question_list[self.question_number] 
        self.question_number += 1                                 
        print(f"Difficulty Level {current_question.difficulty}")
        choice = int(input(f"{self.question_number}. {current_question.question}\n" 
                           f" 0. {current_question.all_choices[0]}\n"
                           f" 1. {current_question.all_choices[1]}\n"
                           f" 2. {current_question.all_choices[2]}\n"
                           f" 3. {current_question.all_choices[3]}: "))
        user_answer = current_question.all_choices[choice]
        correct_ans = current_question.correct_answer
        self.check_answer(user_answer, correct_ans)
        print("\n")

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right")
        else:
            print("You lost it ") 
        print(f"The correct answer was {correct_answer}")
        print(f"Your Score is {self.score}/{self.question_number}") 
    def still_has_question(self):
        return len(self.question_list) > self.question_number