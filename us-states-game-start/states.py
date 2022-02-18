import turtle

class State(turtle.Turtle):

    def __init__(self):
        super(State, self).__init__()
        self.hideturtle()
        self.penup()
        self.color('black')