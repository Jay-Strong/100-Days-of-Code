import turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20
RIGHT_POS = (350, 0)
LEFT_POS = (-350, 0)

class Paddle(turtle.Turtle):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.moving_up = False
        self.moving_down = False
        self.goto(position)

    def start_up(self):
        self.moving_up = True


    def stop_up(self):
        self.moving_up = False


    def start_down(self):
        self.moving_down = True


    def stop_down(self):
        self.moving_down = False
        

    def up(self) -> None:
        if self.ycor() < 241:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self) -> None:
        if self.ycor() > -240:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)


    def move(self) -> None:
        if self.moving_up:
            self.up()

        if self.moving_down:
            self.down()

