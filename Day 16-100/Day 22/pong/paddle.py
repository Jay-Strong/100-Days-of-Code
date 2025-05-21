import turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20
LEFT_PADDLE_POS = [(-370, -40), (-370, -20), (-370, 0), (-370, 20), (-370, 40)]
RIGHT_PADDLE_POS = [(370, -40), (370, -20), (370, 0), (370, 20), (370, 40)]


class Paddle(turtle.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.segments = []
        

    def create_paddle(self, positions: list[tuple]) -> None:
        for position in positions:
            self.add_segment(position=position)
        self.head = self.segments[0]
        self.tail = self.segments[-1]

       


    def add_segment(self, position: tuple) -> None:
        self.new_segment = turtle.Turtle(shape="square")
        self.new_segment.color("white")
        self.new_segment.penup()
        self.new_segment.goto(position)
        self.new_segment.seth(UP)
        self.segments.append(self.new_segment)
        

    
    def up(self) -> None:
        for seg_num in self.segments:
            seg_num.forward(MOVE_DISTANCE)


    def down(self) -> None:
        for seg_num in self.segments:
            seg_num.back(MOVE_DISTANCE)


    def move(self) -> None:
        turtle.onkey(fun=self.up, key="Up")
        turtle.onkey(fun=self.down, key="Down")

        


    # def move(self) -> None:
    #     turtle.onkey(fun=self.up, key="Up")
    #     turtle.onkey(fun=self.down, key="Down")
    #     for seg_num in range(len(self.segments) - 1, 0, -1):
    #         new_x = self.segments[seg_num - 1].xcor()
    #         new_y = self.segments[seg_num - 1].ycor()
    #         self.segments[seg_num].goto(new_x, new_y)
    #     self.head.forward(MOVE_DISTANCE)


class LeftPaddle(Paddle):
    def __init__(self) -> None:
        super().__init__()
        self.positions = LEFT_PADDLE_POS
        self.create_paddle(self.positions)



class RightPaddle(Paddle):
    def __init__(self) -> None:
        super().__init__()
        self.positions = RIGHT_PADDLE_POS
        self.create_paddle(self.positions)
