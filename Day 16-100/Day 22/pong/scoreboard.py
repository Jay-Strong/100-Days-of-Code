from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Cascadia Code", 40, "normal")
RIGHT_SB_POS = (70, 230)
LEFT_SB_POS = (-70, 230)

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        

    def create_scoreboard(self, position: tuple) -> None:
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.refresh()
        

    def refresh(self) -> None:
        self.clear()
        self.score_text = f"{self.score}"
        self.write(self.score_text, False, ALIGNMENT, FONT)


class LeftScore(Scoreboard):
    def __init__(self) -> None:
        super().__init__()
        position = LEFT_SB_POS
        self.create_scoreboard(position)


class RightScore(Scoreboard):
    def __init__(self) -> None:
        super().__init__()
        position = RIGHT_SB_POS
        self.create_scoreboard(position)


