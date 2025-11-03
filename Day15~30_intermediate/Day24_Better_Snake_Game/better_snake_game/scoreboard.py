from turtle import Turtle
ALIGN = "center" 
FONT = ("Courier", 18, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg= f"Score = {self.score} High Score: {self.high_score}", align= ALIGN, font= FONT) 

    def reset(self): # high score
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/data.txt", mode= "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def scoring(self):
        self.score += 1
        self.update_scoreboard()


