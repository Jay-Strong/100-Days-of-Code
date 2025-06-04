from turtle import Turtle
from random import randint, choice

SERVE_TO_LEFT = randint(120, 240)
SERVE_TO_RIGHT = randint(-60, 60)

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.is_left = False
        self.is_right = False
        # self.penup()
        self.color("white")
        self.shape("square")
        self.seth(SERVE_TO_RIGHT)
        self.speed(1)
     

    def serve_right(self) -> None:
        self.seth(SERVE_TO_RIGHT)
        self.is_right = True
        self.is_left = False
        self.forward(100)
    
    
    def serve_left(self) -> None:
        self.seth(SERVE_TO_LEFT)
        self.is_left = True
        self.is_right = False
        self.forward(100)

    def start_game(self) -> None:
        self.serve_options = [self.serve_right, self.serve_left]
        self.serve_choice = choice(self.serve_options)
        self.serve_choice()
        self.forward(100)

