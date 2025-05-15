import turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self) -> None:
        for position in START_POSITIONS:
            self.add_segment(position=position)


    def add_segment(self: object, position: tuple) -> None:
        new_segment = turtle.Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self: object) -> None: 
        self.add_segment(self.segments[-1].position())
        
    


    def right(self: object) -> None:
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)


    def up(self: object) -> None:
        if self.head.heading() != DOWN:
            self.head.seth(UP)


    def left(self: object) -> None:
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)


    def down(self: object) -> None:
        if self.head.heading() != UP:
            self.head.seth(DOWN)



    def move_snake(self: object) -> None:
        turtle.onkey(fun=self.right, key="Right")
        turtle.onkey(fun=self.up, key="Up")
        turtle.onkey(fun=self.left, key="Left")
        turtle.onkey(fun=self.down, key="Down")
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)