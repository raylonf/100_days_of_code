from turtle import Turtle
import random
r = (10, 9, 8, 7, -7, -8, -9, -10)
rand = random.choice(r)
rand2 = random.choice(r)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.x_move = rand
        self.y_move = rand2

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.y_move *= -1

    def rebound(self):
        self.x_move *= -1


