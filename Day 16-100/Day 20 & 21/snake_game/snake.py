import turtle

class Snake:
    def __init__(self) -> None:
        self.segments = []

        for num in range(3):
            new_segment = turtle.Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto((-20 * num), 0)
            self.segments.append(new_segment)


    def turn_left(self) -> None:
        self.segments[0].left(90)


    def turn_right(self) -> None:
        self.segments[0].right(90)



    def move_snake(self) -> None:
        turtle.onkey(fun=self.turn_left, key="Left")
        turtle.onkey(fun=self.turn_right, key="Right")
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)