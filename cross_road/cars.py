from turtle import Turtle
import random

COLORS = ('white', 'pink', 'yellow', 'brown', 'green', 'orange', 'red')
INITIAL_POSITION = (random.randint(-260, 260))


class Car(Turtle):

    def __init__(self):
        super(Car, self).__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setposition(300, random.randint(-240, 260))
        self.moviment = 5

    def move(self):
        new_mov_x = self.xcor() + self.moviment
        y = self.ycor()
        self.goto(new_mov_x, y)

    def pass_level(self, level):
        x = 4 * level
        self.moviment = x * -1
