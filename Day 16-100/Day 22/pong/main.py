from turtle import Screen
from scoreboard import Scoreboard as sb
from paddle import Paddle
from pong_court import Court
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

court = Court()
court.draw_centerline()
paddle = Paddle()
sb_left = sb.goto()
screen.update()

screen.exitonclick()

# py main.py