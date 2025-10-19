from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update() 
    car_manager.create_car()
    car_manager.car_move()

    # Detect collision with car
    for car in car_manager.all_cars: # 아하 전체 카 ~
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()
    # 밑 코드 대신 위 코드로 
    # if player.ycor() > 290:
    #     car_manager.reset_position()
    #     player.reset_position()



screen.exitonclick()

