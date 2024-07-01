from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-250, 270)
        self.write(arg=f"Level: {self.level}", align="center", font=("American Typewriter", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg= "Game over.", align="center", font=("American Typewriter", 24, "normal"))

    def level_up(self):
        self.level += 1

    def update_score(self):
        self.clear()
        self.goto(-250, 270)
        self.write(arg=f"Level: {self.level}", align="center", font=("American Typewriter", 20, "normal"))


