class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
    def still_running(self):
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(answer, current_question.answer)
        
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print('Correct!')
            self.score += 1
        else:
            print('Incorrect!')
        print(f'Your score is {self.score}/{self.question_number}.')