from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.goto(-240, 260)
        self.color('white')
        self.level = 1
        self.showLevel()

    def showLevel(self):
        self.clear()
        self.write(f'Level {self.level}', move=False, align='left', font=('Arial', 14, 'italic'))

    def passLevel(self):
        self.level += 1
        self.showLevel()


class GameOver(Turtle):

    def __init__(self):
        super(GameOver, self).__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.write('GAME OVER', align='center', font=('Currier', 18))


class Finish(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.write('CONGRATULATIONS', align='center', font=('Currier', 18))