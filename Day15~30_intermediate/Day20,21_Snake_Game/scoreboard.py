from turtle import Turtle
ALIGN = "center" # 이렇게 상수로 빼주면 수정하기 쉬워짐
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.clear()
        self.hideturtle()
        self.update_scoreboard()
        # self.write(arg= f"Score = {self.score}", move= False, align= "center", font=("Arial", 12, "normal")) # 항목 생략도 가능

    def update_scoreboard(self):
        self.write(arg= f"Score = {self.score}", align= ALIGN, font= FONT) 

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align= ALIGN, font= FONT) 


    def scoring(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        # self.write(arg= f"Score = {self.score}", move= False, align= "center", font=("Arial", 12, "normal")) 



