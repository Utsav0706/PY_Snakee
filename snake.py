import turtle

STARTING_POSITION = [(0,0) ,(-20,0), (-40,0)]
MOVE_SPEED = 20

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            snake = turtle.Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(position)
            self.snakes.append(snake)

    def move_snake(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            newX = self.snakes[snake_num - 1].xcor()
            newY = self.snakes[snake_num - 1].ycor()

            self.snakes[snake_num].goto(newX, newY)

        self.snakes[0].forward(MOVE_SPEED)