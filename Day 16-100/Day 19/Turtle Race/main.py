from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []
race_is_on = False



for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:

    for turtle in all_turtles:
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            race_is_on = False
            if turtle.fillcolor() == user_bet:
                print(f"You've won! {turtle.fillcolor()} is the winner.")
            else:
                print(f"You've lost! {turtle.fillcolor()} is the winner.")

screen.exitonclick()

# py main.py