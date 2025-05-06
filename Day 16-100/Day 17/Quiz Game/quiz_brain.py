class QuizBrain:
    def __init__(self: object, q_list: list) -> None:
        self.question_list = q_list
        self.question_number = 0
        self.score = 0


    def check_answer(self: object, choice: str, correct_answer: str) -> None:
        if choice.lower() in correct_answer.lower():
            self.score +=1
            print("Correct 🙂")
        else:
            print("Incorrect 🙁")
        print(f"Your score is: {self.score}/{self.question_number}\n")

    
    def next_question(self: object) -> None:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (T-true/F-false): ")
        self.check_answer(choice=user_answer, correct_answer=current_question.answer)

    
    def still_has_question(self: object) -> bool:
        return len(self.question_list) > self.question_number
            
    

    