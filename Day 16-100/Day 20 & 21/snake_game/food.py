from turtle import Turtle
from random import randint as ri

class Food(Turtle):
    def __init__(self: object) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self: object) -> None:
        self.new_location = (ri(-280, 280), ri(-280, 280))
        self.goto(self.new_location)

# py food.py