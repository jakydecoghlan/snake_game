from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition (0, 270)
        self.color("white")
        self.score()



    def score(self):
        self.write("Score = ", align="left")


