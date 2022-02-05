"""from turtle import Screen, Turtle

timmy_turtle = Turtle()
#timmy_turtle.shapesize('user')
timmy_turtle.shape('turtle')
timmy_turtle.color('blue', 'red')
timmy_turtle.fd(150)
timmy_turtle.left(180)
timmy_turtle.fd(300)

for _ in range(35):
    timmy_turtle.left(175)
    timmy_turtle.fd(300)
for _ in range(30):
    timmy_turtle.left(132)
    timmy_turtle.fd(300)
    
scren = Screen()
scren.exitonclick()"""
    
import turtle as t 
import random 

tim = t.Turtle()
t.colormode(255)


colors = ['red', 'blue', 'pink', 'violet', 'brown', 'yellow', 'green']
direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g ,b)
    return color


def make_geometric(x):
    tim.color(random.choice(colors))    
    for _ in range(x):
        tim.fd(50)
        tim.seth(360 / x)

def random_walk(x):
    tim.shape('circle')
    tim.pensize(15)
    tim.speed(0)
    for _ in range(x):
        tim.pencolor(random_color())
        tim.fd(30)
        tim.right(random.choice(direction))

def make_circle(y, x):
    tim.home()
    tim.speed(0)
    for _ in range(x):
        tim.pencolor(random_color())
        tim.circle(y)
        tim.right(360 / x)

        
        
'''for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown ()'''
    

'''tim.penup()
tim.right(180)
tim.fd(150)
tim.right(90)
tim.fd(100)
tim.right(90)
tim.pendown()
for x in range(3, 25):
    make_geometric(x)'''

'''tim.speed(0)
tim.speed(0)
tim.speed(0)
tim.speed(0)

random_walk(300)'''

make_circle(100, 100)

screen = t.Screen()
screen.exitonclick()















