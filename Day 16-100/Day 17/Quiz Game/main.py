from quiz_brain import QuizBrain
from data import question_data as qd
from question_model import Question

question_bank = []


for item in qd:
    text = item["question"]
    answer = item["correct_answer"]
    new_q = Question(q_text=text, q_answer=answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    user_choice = quiz.next_question()

print("You have completed the quiz.")
print(f"Final score: {quiz.score}/{quiz.question_number}\n")
    


# py main.py