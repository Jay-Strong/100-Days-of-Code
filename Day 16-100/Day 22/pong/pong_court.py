from turtle import Turtle

class Court(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shape("square")
        self.pensize(8)
        self.speed(0)
        self.goto(0, 290)
        self.seth(270)
        self.draw_centerline()


    def draw_centerline(self) -> None:
        for _ in range(40):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20) 
    

    # def draw_centerline(self) -> None:
    #     for _ in range(29):
    #         self.stamp()
    #         self.forward(50)
