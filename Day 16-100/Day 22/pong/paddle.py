import turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20
START_POSITIONS = [(-280, -40), (-280, -20), (-280, 0), (-280, 20), (-280, 40)]
# START_POSITIONS_RIGHT = [(-20, 270), (0, 270), (-40, 270)]

class Paddle:
    def __init__(self: object) -> None:
        self.segments = []
        self.paddle = self.create_paddle()
        self.head = self.segments[0]


    def create_paddle(self) -> None:
        for position in START_POSITIONS:
            self.add_segment(position=position)


    def add_segment(self: object, position: tuple) -> None:
        self.new_segment = turtle.Turtle(shape="square")
        self.new_segment.color("white")
        self.new_segment.penup()
        self.new_segment.goto(position)
        self.segments.append(self.new_segment)

    
    def up(self: object) -> None:
        self.head.seth(UP)


    def down(self: object) -> None:
        self.head.seth(DOWN)
        self.forward(MOVE_DISTANCE)


    



        