from turtle import Turtle, Screen

red = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

red.color("red")
red.shape("turtle")
user_bet = screen.textinput(title="Make Your Bet!", prompt="Which turtle will win the race? Enter a color: ")
red.penup()
red.goto(x=-230, y=-100)
# red.teleport(x=-230, y=-100)
print(user_bet)
screen.exitonclick()

# py main.py