from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Lucida Console", 40, "normal")
RIGHT_SB_POS = (70, 230)
LEFT_SB_POS = (-70, 230)
CENTER_SB_POSITION = (0, 0)


class Scoreboard(Turtle):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.score = 0
        
        self.create_scoreboard(position)


    def refresh(self) -> None:
        self.clear()
        self.score_text = f"{self.score}"
        self.write(self.score_text, False, ALIGNMENT, FONT)


    def create_scoreboard(self, position: tuple) -> None:
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.refresh()
        

    def add_point(self) -> None:
        self.score += 1
        self.refresh()
         
    def game_over(self, winner) -> None:
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.game_over_text = f"Game Over. {winner} is the winner!"
        self.write(self.game_over_text, False, ALIGNMENT, FONT)
        self.refresh()