from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.forward()


def backward():
    tim.backward()



screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")



screen.exitonclick()

# py main.py