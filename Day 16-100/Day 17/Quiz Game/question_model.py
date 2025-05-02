from data import question_data as qd

class Question():
    def __init__(self: object, index: int) -> None:
        self.index = index
        self.text = qd[index]["text"]
        self.answer = qd[index]["answer"]

q1 = Question(0)

print(q1.text)

# py question_model.py