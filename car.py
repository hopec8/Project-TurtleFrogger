from turtle import Turtle
import random


colors = ['red1', 'orange', 'yellow1', 'green1', 'cyan2', 'blueviolet']

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(colors))
        self.penup()
        self.setheading(180)
        self.goto(280, (random.randrange(-240, 280, 25)))

    def move(self, speed):
        self.forward(speed)



