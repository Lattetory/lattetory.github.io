# 251008 Day 29 of Python

# Day 19-1 Project
# Making the Etch a sketch project

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun= move_forward) 
screen.onkey(key="s", fun= move_backward) 
screen.onkey(key="a", fun= turn_right) 
screen.onkey(key="d", fun= turn_left) 
screen.onkey(key="c", fun= clear_screen)
# 이때 move_forward 뒤에 () 붙이지 않는다 
# > 저 괄호안에서 함수 실행 할 것이 아니기때문
# 즉, 이름만 전달하기 때문에!
# 고차함수 = 다른 함수를 입력으로 받아들이고 함수의 본문 안에서 함께 작동
screen.exitonclick()