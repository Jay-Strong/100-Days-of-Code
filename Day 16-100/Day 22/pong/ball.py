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


    def bounce(self) -> None:
        self.y_move *= -1



    # def serve_ball(self) -> None:
    #     if self.is_right and not self.is_left:
    #         self.seth(left)
    #     else:
    #         self.seth(right)
    #     self.forward(MOVE_DISTANCE)

     
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

