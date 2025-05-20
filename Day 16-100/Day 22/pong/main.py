from turtle import Screen
from scoreboard import LeftScore as ls, RightScore as rs
from paddle import LeftPaddle as lp, RightPaddle as rp
from pong_court import Court
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

court = Court()
left_sb = ls()
right_sb = rs()
left_paddle = lp()
right_paddle = rp()
screen.update()
time.sleep(0.15)
left_paddle.move()

screen.exitonclick()

# py main.py
