import turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle:
    def __init__(self: object, positions: list[tuple]) -> None:
        self.segments = []
        self.paddle = self.create_paddle(positions=positions)
        self.head = self.segments[0]


    def create_paddle(self, positions: list[tuple]) -> None:
        for position in positions:
            self.add_segment(position=position)


    def add_segment(self: object, position: tuple) -> None:
        self.new_segment = turtle.Turtle(shape="square")
        self.new_segment.color("white")
        self.new_segment.penup()
        self.new_segment.goto(position)
        self.segments.append(self.new_segment)

    
    def up(self: object) -> None:
        self.head.seth(UP)
        self.forward(MOVE_DISTANCE)


    def down(self: object) -> None:
        self.head.seth(DOWN)
        self.forward(MOVE_DISTANCE)


    def move(self: object) -> None:
        turtle.onkey(fun=self.up, key="Up")
        turtle.onkey(fun=self.down, key="Down")