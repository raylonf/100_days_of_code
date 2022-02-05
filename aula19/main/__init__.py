import turtle
import turtle as tur
import random

list_turtles = []
colors = ['red', 'pink', 'blue', 'green', 'brown', 'purple']
y = -170
for x in range(6):
    tim = tur.Turtle()
    tim.shape('turtle')
    tim.penup()
    tim.color(colors[x])
    tim.setposition(-220, y)
    y += 70
    list_turtles.append(tim)


speeds = (0, 10)
screen = tur.Screen()
# tom = tur.Turtle()
# tom.shape('turtle')
# tom.color('yellow')
# tata = tur.Turtle()
# tata.shape('circle')
# tata.color('red')
# tom.setposition(-150, 0)
# tata.setposition(-150, -20)
#
# def move_forwards():
#     tim.fd(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def move_right():
#     tim.right(10)
#
# def move_left():
#     tim.left(10)
#
# def clean():
#     tim.penup()
#     tim.clear()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forwards, 'w')
# screen.onkey(move_backwards, 's')
# screen.onkey(move_left  , 'a')
# screen.onkey(move_right, 'd')
# screen.onkey(clean, 'c')
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Faça a sua aposta', prompt='Em qual cor de tartaruga você aposta na vitória?')
is_race = True
winner = ''
while is_race:
    for turtle in list_turtles:
        turtle.fd(random.choice(speeds))

        if turtle.xcor() == 220:
            winner = turtle.color()[0]
            print(winner)
            is_race = False

if user_bet == winner:
    screen.textinput(title='Parabens, você é muito bom de apostas!!', prompt='')
else:
    screen.textinput(title='Não foi dessa vez, quem sabe na proxima!', prompt='')
screen.exitonclick()
