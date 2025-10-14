from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10 # 이거 이용하려했지만 렉걸리는듯?

class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # 차가 1/6 확률로 만들어지게 함 _ 이런방법이 있었다니..
        random_chance = random.randint(1, 6) 
        if random_chance == 1:
            new_car = Turtle(shape= "square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len= 2, stretch_wid= 1)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)


    def car_move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE) # 와.. backward 로 하면 됐네..
            # new_x = self.xcor() - MOVE_DISTANCE # 이게 아니라..
            # # self.move_speed *= 0.9
            # self.goto(new_x, self.ycor())

    # def reset_position(self):
    #     self.move_speed *= 0.7

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
