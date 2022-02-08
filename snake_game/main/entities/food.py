from turtle import Turtle
import random

LIST_RANDOM = []
for c in range(-280, 280, 10):
    LIST_RANDOM.append(c)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.local()
        self.shapesize(stretch_len=0.3, stretch_wid= 0.3)
        self.speed(0)
        self.local()
        self.x = 0
        self.y = 0

    def local(self):
        self.x = random.choice(LIST_RANDOM)
        self.y = random.choice(LIST_RANDOM)
        self.setposition(self.x, self.y)



