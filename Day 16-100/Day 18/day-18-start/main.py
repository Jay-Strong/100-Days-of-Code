from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.shape("turtle")
tim.color("turquoise1", "chartreuse1")

my_screen = Screen()
my_screen.colormode(255)


def select_random_color() -> tuple:
    color_code = ()
    for _ in range(3):
        num = randint(0, 255)
        color_code += (num,)
    return color_code


def draw_shape(num_sides: int) -> None:
    color = select_random_color()
    tim.pencolor(color)
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(angle)


def draw_dashed_line() -> None:
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def random_walk() -> None:
    tim.speed(10)
    tim.width(10)
    
   

# draw_dashed_line()

# for i in range(3, 11):
#     draw_shape(i)


my_screen.exitonclick()


# py main.py
