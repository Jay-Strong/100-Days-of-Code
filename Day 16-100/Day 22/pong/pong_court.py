from turtle import Turtle

class Court(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pensize(3)
        self.speed(0)
        self.teleport(0, 290)
        self.seth(270)
        
    def draw_centerline(self: object) -> None:
        for _ in range(29):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
