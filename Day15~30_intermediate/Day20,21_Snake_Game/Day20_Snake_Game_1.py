# 251010 Day 31 of Python

# Day 20 Project
# Making the Snake Game 1 project

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("ttette's Snake Game") # 제목
screen.tracer(0) # 애니메이션 효과 끄기 > 뱀이 스르르 움직여보이게끔

# snake_1 = Turtle(shape= "square")
# snake_1.color("white")
# snake_1.penup()

# snake_2 = Turtle(shape= "square")
# snake_2.color("white")
# snake_2.penup()
# snake_2.goto(x= -20, y= 0)

# snake_3 = Turtle(shape= "square")
# snake_3.color("white")
# snake_3.penup()
# snake_3.goto(x= -40, y= 0)

# 를 줄여서 아래처럼

# Make Snakes
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

snake = []

for position in starting_positions:
    new_snake = Turtle(shape= "square")
    new_snake.color("white")
    new_snake.penup()
    new_snake.goto(position)
    snake.append(new_snake)

# Moves Snakes
game_is_on = True
while game_is_on:
    screen.update() # 화면 업데이트 해주기 > 이부분에 해주면 한번에 움직이는것처럼 보임
    time.sleep(0.05)
    
    for snake_num in range(len(snake)-1, 0, -1): 
# 시작부분(맨마지막=몸통의마지막번호=-1(0부터시작이니까)), 끝부분(시작몸통=0), 증가폭(뒤에서앞으로가니까=-1)
        new_x = snake[snake_num - 1].xcor() # 앞 몸통의 x좌표
        new_y = snake[snake_num - 1].ycor() # 앞 몸통의 y좌표
        snake[snake_num].goto(new_x, new_y) # > 앞 몸통의 좌표로 가라 = 움직이게하기
    snake[0].forward(20)

# > 이제 파일 분리해서 다시 정리하기! 

screen.exitonclick()
