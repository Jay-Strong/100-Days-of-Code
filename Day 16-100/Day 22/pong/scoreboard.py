from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Cascadia Code", 18, "normal")
RIGHT = (40, 270)
LEFT = (-40, 270)

class Scoreboard(Turtle):
    def __init__(self: object) -> None:
        super().__init__()
        

    def create_scoreboard(self: object, location: int) -> None:
        self.penup()
        self.hideturtle()
        self.color("white")
        self.refesh()
    

    def refresh(self: object) -> None:
        self.clear()
        self.write(self.score, False, ALIGNMENT, FONT)


    def left_scoreboard(self: object, location: tuple = LEFT) -> None:
        self.left_scoreboard = Turtle()
          

