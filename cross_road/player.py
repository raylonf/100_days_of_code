from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.color('white')
        self.penup()
        self.shape('turtle')
        self.seth(90)
        self.setposition(0, -280)

    def moveup(self):
        self.fd(20)

    def movedown(self):
        self.back(20)

