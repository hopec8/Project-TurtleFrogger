from turtle import Turtle


class StartingTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def move(self):
        self.forward(20)

    def move_back(self):
        self.backward(20)

    def turtle_reset(self):
        self.goto(0, -280)
