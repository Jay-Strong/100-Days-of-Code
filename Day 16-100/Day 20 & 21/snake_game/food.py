from turtle import Turtle
from random import randint as ri

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("blue")
        self.speed(0)
        x_coord = ri(-575, 575)
        y_coord = ri(-575, 575)
        self.goto(x_coord, y_coord)

# py food.py