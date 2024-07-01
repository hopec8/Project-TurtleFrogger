from turtle import Turtle, Screen
from starting_turtle import StartingTurtle
from car import Car
from scoreboard import Scoreboard
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
STARTING_POSITION_Y = -280
FINISH_LINE_Y = 280
STARTING_SPEED = 1
SPAWN_INTERVAL = 50
SPAWN_DECREASE = 5
COLLISION_DISTANCE = 25

screen = Screen()
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)
screen.title("Turtle Crossing")

car_list = []
turtle = StartingTurtle()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")
screen.onkey(turtle.move_back, "Down")

def play():
    game_on = True
    random_interval = SPAWN_INTERVAL
    car_speed = STARTING_SPEED

    while game_on:
        screen.update()
        if turtle.ycor() > 280:
            scoreboard.level_up()
            scoreboard.update_score()
            turtle.turtle_reset()
            car_speed += 1
            random_interval -= SPAWN_DECREASE
        for each_car in car_list:
            each_car.move(car_speed)
            if turtle.distance(each_car) < COLLISION_DISTANCE:
                scoreboard.game_over()
                game_on = False
        random_chance = random.randint(1, random_interval)
        if random_chance == 1:
            new_car = Car()
            car_list.append(new_car)

play()

screen.exitonclick()