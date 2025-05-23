from turtle import Turtle
from random import randint

SERVE_TO_LEFT = randint(120, 240)
SERVE_TO_RIGHT = randint(-60, 60)

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        # self.penup()
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=5)
        # self.shape("square")
        # self.seth(SERVE_TO_LEFT)
        self.seth(SERVE_TO_RIGHT)
        self.speed(1)
        self.forward(600)