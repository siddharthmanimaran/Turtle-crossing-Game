from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level =1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.write(f"Level:{self.level}",font=FONT)
    def level_up(self):
        self.clear()
        self.level+=1
        self.write(f"Level:{self.level}",font=FONT)

    def game_end(self):
        self.color("red")
        self.goto(0,0)
        self.write("Game Over...",font=FONT,align="center")

