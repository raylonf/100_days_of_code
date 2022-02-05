from turtle import Turtle

ALLIGN = 'center'
FONT = ('Currier', 12, 'italic')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.color('white')

    def make_point(self):
        self.score += 1

    def print_scoreboard(self):
        self.clear()
        return self.write(arg=f'Your Score : {self.score}', move=False, align=ALLIGN, font=FONT)

class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.clear()
        self.hideturtle()
        self.penup()
        self.write(arg= 'Game Over', move=False, align=ALLIGN, font=FONT)