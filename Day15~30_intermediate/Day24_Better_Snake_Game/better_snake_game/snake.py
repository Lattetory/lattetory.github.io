from turtle import Screen, Turtle
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20 # 맨위로 적어줌으로써 수정시 용이하게 함
UP = 90
DOWN = 270
LEFT = 180 # 서로 반대방향으로 향할수없게
RIGHT = 0

class Snake():
    # Moves Snakes
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
    
    # make a snake 1
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    # make a snake 2
    def add_segment(self, position): 
            new_snake = Turtle(shape= "square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.snakes.append(new_snake)
    
    def reset(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear() # snakes 의 리스트 전부 삭제
        self.create_snake() # 새로 생성
        self.head = self.snakes[0] # haed 정해주기

    # add a new segment(snake) to the snake.
    def extend(self):
        self.add_segment(self.snakes[-1].position()) # 마지막 snake 뒤에 추가



    # Moves Snakes
    def move(self):
        global snakes
        for snake_num in range(len(self.snakes)-1, 0, -1): 
            new_x = self.snakes[snake_num - 1].xcor() 
            new_y = self.snakes[snake_num - 1].ycor() 
            self.snakes[snake_num].goto(new_x, new_y) 
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN: # 서로 반대방향으로 갈수없게
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




