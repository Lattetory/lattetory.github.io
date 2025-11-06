# 251010,13 Day 31,34 of Python

# Day 20 Project
# Making the Snake Game 1 project

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("ttette's Snake Game") 
screen.tracer(0) 

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scoring()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    # for snake1 in snake.snakes:
    #     if snake1 == snake.head:
    #         pass
    #     elif snake.head.distance(snake1) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    # 를 슬라이싱으로 줄여서 쓸 수 있음
    for snake1 in snake.snakes[1:]:
        if snake.head.distance(snake1) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
