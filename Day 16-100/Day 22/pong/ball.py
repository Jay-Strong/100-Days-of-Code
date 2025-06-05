from turtle import Turtle
from random import randint, choice

LEFT_HEADING = randint(120, 240)
RIGHT_HEADING = randint(-60, 60)
MOVE_DISTANCE = 20

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.is_left = False
        self.is_right = False
        # self.penup()
        self.color("white")
        self.shape("circle")
        self.speed(1)


    def move(self) -> None:
        new_x = self.xcor() - MOVE_DISTANCE
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x, new_y)

    def serve_ball(self) -> None:
        self.seth(LEFT_HEADING)
        self.forward(MOVE_DISTANCE)
     
# ==========================================================================================
    # def serve_right(self) -> None:
    #     self.seth(SERVE_TO_RIGHT)
    #     self.is_right = True
    #     self.is_left = False
    #     self.forward(MOVE_DISTANCE)
    
    
    # def serve_left(self) -> None:
    #     self.seth(SERVE_TO_LEFT)
    #     self.is_left = True
    #     self.is_right = False
    #     self.forward(MOVE_DISTANCE)

    # def start_game(self) -> None:
    #     self.serve_options = [self.serve_right, self.serve_left]
    #     self.serve_choice = choice(self.serve_options)
    #     self.serve_choice()
    #     self.forward(MOVE_DISTANCE)

