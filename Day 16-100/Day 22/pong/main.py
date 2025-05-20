from turtle import Screen
from scoreboard import LeftScore as ls, RightScore as rs, Scoreboard as sb
from paddle import Paddle
from pong_court import Court
import time

RIGHT_SB_POS = (70, 230)
LEFT_SB_POS = (-70, 230)
LEFT_PADDLE_POS = [(-370, -40), (-370, -20), (-370, 0), (-370, 20), (-370, 40)]
RIGHT_PADDLE_POS = [(370, -40), (370, -20), (370, 0), (370, 20), (370, 40)]


screen = Screen()
screen.setup(width = 800, height = 600)
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

court = Court()
left_sb = ls()
right_sb = rs()
left_paddle = Paddle(positions=LEFT_PADDLE_POS)
right_paddle = Paddle(positions=RIGHT_PADDLE_POS)
screen.update()


screen.exitonclick()

# py main.py
