import turtle as t
import random as r


color_list = [(204, 159, 107), (231, 213, 109), (134, 168, 192), (44, 105, 144), (152, 78, 53), (199, 142, 164), 
              (15, 32, 53), (181, 159, 42), (148, 65, 87), (141, 178, 155), (205, 91, 70), (64, 117, 92), 
              (195, 89, 118), (225, 170, 187), (15, 38, 27), (59, 34, 19), (227, 175, 166), (48, 158, 182), 
              (238, 213, 4), (87, 155, 112), (121, 35, 53), (177, 188, 216), (35, 58, 110), (169, 206, 184),
              (60, 21, 36), (14, 96, 71)]


def hirst_painting(rows=10, cols=10) -> None:
    tom.hideturtle()
    tom.penup()
    tom.speed(0)
    tom.teleport(-230, -300)
    for row in range(rows):
        for col in range(cols):
            color = r.choice(color_list)
            tom.dot(20, color)
            tom.forward(50)
        # Move to the start of the next row
        tom.backward(50 * cols)
        tom.left(90)
        tom.forward(50)
        tom.right(90)
    tom.home()


t.colormode(255)
tom = t.Turtle()
screen = t.Screen()

hirst_painting()

screen.exitonclick()

# py main.py

# =====================================================================================================================
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)