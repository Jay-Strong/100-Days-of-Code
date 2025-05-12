from scoreboard import Scoreboard
from food import Food
from snake import Snake
from turtle import Screen
from random import randint as ri
import time

screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.update()

game_is_on = True

while game_is_on:
    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.add_point()
        scoreboard.refresh()
        snake.add_segment()
    screen.update()
    time.sleep(0.2)
    snake.move_snake()
    

screen.exitonclick()

# py main.py