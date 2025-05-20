from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Cascadia Code", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self: object, location: tuple) -> None:
        super().__init__()
        RIGHT = (70, 230)
        LEFT = (-70, 230)
        self.score = 0
        self.create_scoreboard(location)

        

    def create_scoreboard(self: object, location: tuple) -> None:
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(location)
        self.refresh()
        
    

    def refresh(self: object) -> None:
        self.clear()
        self.score_text = f"{self.score}"
        self.write(self.score_text, False, ALIGNMENT, FONT)


    # def scoreboard(self: object, location: tuple = LEFT) -> None:
    #     self.goto(location)
          

