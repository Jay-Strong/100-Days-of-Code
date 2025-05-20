from turtle import Turtle

class Court(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shape("square")
        self.pensize(3)
        self.speed(0)
        self.goto(0, 280)
        self.seth(270)
        
    def draw_centerline(self: object) -> None:
        for _ in range(29):
            # self.pendown()
            self.stamp()
            self.forward(50)
            # self.penup()
            # self.forward(10)
            
