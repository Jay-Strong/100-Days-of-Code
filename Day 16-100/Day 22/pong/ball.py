from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.shape("square")
        self.seth(90)