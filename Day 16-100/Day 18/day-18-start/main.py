import turtle as t
from random import randint, choice

tim = t.Turtle()
# tim.shape("turtle")
# tim.color("turquoise1", "chartreuse1")

screen = t.Screen()
t.colormode(255)


def select_random_color() -> tuple:
    color_code = []
    for _ in range(3):
        num = randint(0, screen.colormode())
        color_code.append(num)
    return tuple(color_code)


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
    directions = [0, 90, 180, 270]
    tim.speed(0)
    tim.width(15)
    for i in range(250):
        tim.pencolor(select_random_color())
        tim.seth(choice(directions))
        tim.forward(30)
    tim.penup()
    tim.home()



# draw_dashed_line()

# for i in range(3, 11):
#     draw_shape(i)

random_walk()

screen.exitonclick()


# py main.py
