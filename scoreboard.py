from turtle import Turtle
from snake import Snake
ALIGN = "center"
FONT = ('courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition (-50, 270)
        self.color("blue")
        self.score = 0
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)

    def gameover(self):
        self.setposition(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def scoreadd(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)
