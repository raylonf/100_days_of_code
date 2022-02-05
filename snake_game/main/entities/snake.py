from turtle import Turtle


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.len_snake_init = 3
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.direction = 'right'

    def create_snake(self):
        z = 0
        for _ in range(self.len_snake_init):
            snake = Turtle('square')
            snake.penup()
            snake.color('white')
            snake.setposition(z, 0)
            snake.shapesize(stretch_len=0.5, stretch_wid=0.5)
            z -= 10
            self.snake_body.append(snake)

    def move(self):

        for t in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[t - 1].xcor()
            new_y = self.snake_body[t - 1].ycor()
            self.snake_body[t].goto(new_x, new_y)

        self.head.fd(10)

    def up(self):
        if self.direction != 'down':
            self.head.seth(90)
            self.direction = 'up'

    def down(self):
        if self.direction != 'up':
            self.head.seth(270)
            self.direction = 'down'

    def right(self):
        if self.direction != 'left':
            self.head.seth(0)
            self.direction = 'right'

    def left(self):
        if self.direction != 'right':
            self.head.seth(180)
            self.direction = 'left'

    def eat_food(self):
        snake = Turtle('square')
        snake.penup()
        snake.color('white')
        snake.setposition(self.snake_body[1].position())
        snake.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.snake_body.insert(-1, snake)

    #Check not collision on tail
    def check_not_collision(self):
        for s in range(2, len(self.snake_body)):
            if self.head.distance(self.snake_body[s]) < 5:
                return False