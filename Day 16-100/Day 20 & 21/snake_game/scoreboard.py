from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Cascadia Code", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.goto(0, 270)
        self.refresh()


    def game_over(self) -> None:
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("Game Over 🙁", False, ALIGNMENT, FONT)

        

    def add_point(self) -> int:
        self.score += 1
        self.refresh()
        return self.score


    def refresh(self) -> None:
        self.score_text = f"Score: {self.score}"
        self.clear()
        self.write(self.score_text, False, ALIGNMENT, FONT)