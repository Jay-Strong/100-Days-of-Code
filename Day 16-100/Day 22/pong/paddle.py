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
        self.moving_up = False
        self.moving_down = False
        

    def create_paddle(self, positions: list[tuple]) -> None:
        for position in positions:
            self.add_segment(position=position)

       
    def add_segment(self, position: tuple) -> None:
        self.new_segment = turtle.Turtle(shape="square")
        self.new_segment.color("white")
        self.new_segment.penup()
        self.new_segment.goto(position)
        self.new_segment.seth(UP)
        self.segments.append(self.new_segment)

    
    def start_up(self):
        self.moving_up = True


    def stop_up(self):
        self.moving_up = False


    def start_down(self):
        self.moving_down = True


    def stop_down(self):
        self.moving_down = False
        

    def up(self) -> None:
        for seg_num in self.segments:
            seg_num.forward(MOVE_DISTANCE)


    def down(self) -> None:
        for seg_num in self.segments:
            seg_num.back(MOVE_DISTANCE)


    def move(self) -> None:
        if self.moving_up:
            self.up()
        if self.moving_down:
            self.down()


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
