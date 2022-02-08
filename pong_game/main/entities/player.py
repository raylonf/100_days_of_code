from turtle import Turtle


def posicao_player(posicao):

    if posicao == 'left':
        return -480

    elif posicao == 'right':
        return 480


class Player(Turtle):

    def __init__(self, posicao):
        super(Player, self).__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.penup()
        self.setposition(posicao_player(posicao), 0)

    def up(self):
        if self.ycor() > 220:
            pass
        else:
            x = self.xcor()
            new_y = self.ycor() + 50
            self.goto(x, new_y)

    def down(self):
        if self.ycor() < -220:
            pass
        else:
            x = self.xcor()
            new_y = self.ycor() - 50
            self.goto(x, new_y)
