# 251008 Day 29 of Python

# Day 18 Project
# Making the Hirst painting project

import turtle as t
import random

t.colormode(255)

color_list = [(202, 164, 109), (238, 240, 245),(150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19)]

# 내가 찾은 답! 
# tim = t.Turtle()
# tim.shape("circle")
# tim.shapesize()
# xpos = -250
# ypos = -250
# tim.teleport(xpos, ypos)
# tim.speed("fastest")

# for a in range(10):
#     ypos += 50
#     for i in range(9):
#         new_color = random.choice(color_list)
#         tim.color(new_color)
#         tim.stamp()
#         tim.penup()
#         tim.fd(50)
#         tim.pendown()
#         tim.stamp()
#     if ypos < 250:
#         tim.left(90)
#         tim.teleport(-250, ypos)
#         tim.right(90)

# 정답 _ dot 이 있었구나~ 
# 그럼 dot 으로 다시 해본다 > 별차이 없구나 > 그냥 정답 적는다

tim = t.Turtle()
tim.speed("fastest")
tim.setheading(225) # teleport 말고 직접 가는법이군
tim.penup()
tim.hideturtle() # 포인트 숨기기
tim.forward(300)
tim.setheading(0)
number_of_dots = 100 # 아.. 이렇게 범위를 정해주면 되는군

for dot_count in range(1, number_of_dots + 1): 
    tim.dot(20, random.choice(color_list))
    tim.fd(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500) # 와.. 그냥 직접 다 가는구나.. 난 왜 teleport 썼냥..
        tim.setheading(0)


screen = t.Screen()
screen.screensize(300, 300)
screen.exitonclick()
