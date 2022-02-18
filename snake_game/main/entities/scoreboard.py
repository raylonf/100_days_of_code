from turtle import Turtle
import os

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
        self.high_score = 0
        self.load_score()

    def make_point(self):
        self.score += 1

    def print_scoreboard(self):
        self.clear()
        return self.write(arg=f'Your Score : {self.score}  High score: {self.high_score}', move=False, align=ALLIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.print_scoreboard()
        self.save_score()

    def load_score(self):
        if not os.path.exists('score.txt'):
            return
        with open('score.txt', 'r') as f:
            self.high_score = int(f.read())


    def save_score(self):
        x = self.high_score
        with open('score.txt', 'w') as f:
            f.write(str(x))


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.clear()
        self.hideturtle()
        self.penup()
        self.setposition(0, 40)
        self.write(arg='Game Over', move=False, align=ALLIGN, font=FONT)


    # def restart(self):
    #     start = Turtle()
    #     start.color('blue')
    #     start.hideturtle()
    #     start.penup()
    #     start.setposition(-40, 0)
    #     start.write(arg='Start', move=False, align=ALLIGN, font=FONT)
    #
    #     end = Turtle()
    #     end.color('red')
    #     end.hideturtle()
    #     end.penup()
    #     end.setposition(40, 0)
    #     end.write(arg='End', move=False, align=ALLIGN, font=FONT)
    #
    #     if start.onclick(fun=None, btn=1, add=None):
    #         return True
    #
    #     if end.onclick(fun=None, btn=1, add=None):
    #         return False
