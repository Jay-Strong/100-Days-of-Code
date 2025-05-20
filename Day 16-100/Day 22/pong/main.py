from turtle import Screen
from scoreboard import Scoreboard as sb
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
court.draw_centerline()
left_sb = sb(location=LEFT_SB_POS)
right_sb = sb(location=RIGHT_SB_POS)
left_paddle = Paddle(positions=LEFT_PADDLE_POS)
right_paddle = Paddle(positions=RIGHT_PADDLE_POS)
screen.update()


screen.exitonclick()

# py main.py
