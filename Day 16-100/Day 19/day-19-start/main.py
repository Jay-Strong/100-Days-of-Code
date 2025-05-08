from turtle import Turtle, Screen


def move_forward() -> None:
    tim.forward(10)


tim = Turtle()
screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key="space")


screen.exitonclick()

# py main.py