from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
all_turtles = []


for num in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto((-20 * num), 0)
    all_turtles.append(new_turtle)


screen.exitonclick()

# py main.py