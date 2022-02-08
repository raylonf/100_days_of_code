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
