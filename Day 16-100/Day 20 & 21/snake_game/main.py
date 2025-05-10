from food import Food
from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()

snake = Snake()
food = Food()

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.goto(food.new_location)
   
    

screen.exitonclick()

# py main.py