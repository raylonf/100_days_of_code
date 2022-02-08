from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pong_nets = []
        self.score_p1 = 0
        self.score_p2 = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.setposition(0, 250)
        self.view_points()

    def point(self, pos):
        if pos == 'left':
            self.score_p1 += 1
            self.clear()
            self.view_points()

        elif pos == 'right':
            self.score_p2 += 1
            self.clear()
            self.view_points()

        else:
            return 'error '

    def pong_net(self):
        for y in range(-300, 300, 30):
            net = Turtle()
            net.hideturtle()
            net.penup()
            net.setposition(x=0, y=y)
            net.color('white')
            net.write('|\n'
                      '|', font=('Arial', 8, 'bold'))
            self.pong_nets.append(net)

    def view_points(self):
        self.write(arg=f'{self.score_p1}              {self.score_p2}', move=False, align='center',
                   font=('TimesNewRoman', 30, 'bold'))