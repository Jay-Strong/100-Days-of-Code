import turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in START_POSITIONS:
            new_segment = turtle.Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    def right(self) -> None:
        self.head.seth(0)


    def up(self) -> None:
        self.head.seth(90)


    def left(self) -> None:
        self.head.seth(180)


    def down(self) -> None:
        self.head.seth(270)



    def move_snake(self) -> None:
        turtle.onkey(fun=self.right, key="Right")
        turtle.onkey(fun=self.up, key="Up")
        turtle.onkey(fun=self.left, key="Left")
        turtle.onkey(fun=self.down, key="Down")
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)