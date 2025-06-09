from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed(1)
        self.x_move = 10
        self.y_move = 10


    def move(self) -> None:
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def wall_bounce(self) -> None:
        self.y_move *= -1


    def paddle_bounce(self) -> None:
        self.x_move *= -1
