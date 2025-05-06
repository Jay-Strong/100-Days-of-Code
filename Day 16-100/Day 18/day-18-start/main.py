import turtle as t
from random import randint, choice

tim = t.Turtle()
# tim.shape("turtle")
# tim.color("turquoise1", "chartreuse1")

screen = t.Screen()
t.colormode(255)


def random_color() -> tuple:
    color_code = []
    for _ in range(3):
        num = randint(0, screen.colormode())
        color_code.append(num)
    return tuple(color_code)


def draw_shape(num_sides: int) -> None:
    color = random_color()
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
    directions = [0, 90, 180, 270]
    tim.speed(0)
    tim.width(15)
    for i in range(250):
        tim.pencolor(random_color())
        tim.seth(choice(directions))
        tim.forward(30)
    tim.penup()
    tim.home()


def spirograph(gap: int) -> None:
    tim.speed(0)
    for i in range(0, 361, gap):
        tim.pencolor(random_color())
        tim.seth(i)
        tim.circle(100)


# draw_dashed_line()

# for i in range(3, 11):
#     draw_shape(i)

# random_walk()

spirograph(5)

screen.exitonclick()


# py main.py
