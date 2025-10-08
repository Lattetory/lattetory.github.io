# 251008 Day 29 of Python

# Day 19-2 Project
# Making the Turtle racing game project

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400) # 키워드인자 적어주면 알아보기편함
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: (in rainbowcolor) ")
colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]
ypos = -100
all_turtles = []

for turtul_index in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtul_index])
    new_turtle.penup()
    new_turtle.goto(x= -230, y= ypos)
    ypos += 35
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230: # xcor = x위치값인가봄
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turrle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turrle is the winner!")

        rand_distance = random.randint(0, 10) # 0 ~ 10
        turtle.forward(rand_distance)

screen.exitonclick()


