from turtle import Screen
from entities.player import Player
from entities.scoreboard import Scoreboard
from entities.ball import Ball
import time

board = Screen()
board.setup(height=600, width=1000)
board.bgcolor('black')
board.title('Pong Game')

board.tracer(0)
score = Scoreboard()
score.pong_net()
p1 = Player(posicao='left')
p2 = Player(posicao='right')
ball = Ball()

board.listen()
board.onkey(p1.up, 'w')
board.onkey(p1.down, 's')

board.onkey(p2.up, 'Up')
board.onkey(p2.down, 'Down')

while True:
    board.update()
    ball.move()

    if ball.xcor() >= 465 and ball.distance(p2) < 60 or ball.xcor() <= -465 and ball.distance(p1) < 60:
        ball.rebound()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce()

    if ball.xcor() > 470:
        score.point(pos='left')
        ball.home()
        ball.rebound()

    if ball.xcor() < -470:
        score.point(pos='right')
        ball.home()
        ball.rebound()

    if score.score_p1 == 10 or score.score_p2 == 10:
        break

    time.sleep(0.02)
board.exitonclick()

