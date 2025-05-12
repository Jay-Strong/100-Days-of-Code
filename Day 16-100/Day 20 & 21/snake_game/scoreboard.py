from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.score_text = f"Score: {self.score}"
        self.update()
        


    def update(self) -> None:
        self.clear()
        self.score += 1
        self.write(self.score_text, False, "center", ("Arial", 10, "normal"))