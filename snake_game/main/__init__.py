from turtle import Turtle, Screen
from entities.snake import Snake
from entities.food import Food
from entities.scoreboard import Scoreboard, GameOver
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while True:
    screen.update()
    score.print_scoreboard()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 5:
        food.local()
        snake.eat_food()
        score.make_point()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gameover = GameOver()
        break

    if snake.check_not_collision() == False:
        gameover = GameOver()
        break


screen.exitonclick()