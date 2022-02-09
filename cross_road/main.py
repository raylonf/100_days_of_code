import random

from player import Player
from turtle import Screen
from cars import Car
from time import sleep
from scoreboard import *

CHOICE = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
n = 0

cars = []
screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)

screen.tracer(0)

score = Scoreboard()
p1 = Player()
screen.listen()
screen.onkey(p1.moveup, 'Up')
screen.onkey(p1.movedown, 'Down')
level = 1


def gerar_cars():
    for _ in range(random.choice(CHOICE[n:])):
        car = Car()
        car.pass_level(level)
        cars.append(car)


games_on = True
while games_on:
    screen.update()
    sleep(0.05)
    gerar_cars()
    for car in cars:
        car.move()

    if p1.ycor() == 280:
        score.passLevel()
        level += 1
        n += 1
        p1.goto(0, -280)

    for car in cars:
        if p1.distance(car) < 20:
            gameover = GameOver()
            games_on = False

    if level == 11:
        fin = Finish()
        games_on = False

screen.exitonclick()
