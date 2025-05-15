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
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_point()
        scoreboard.refresh()
        snake.extend()
        print(len(snake.segments))

    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    
    

screen.exitonclick()

# py main.py
