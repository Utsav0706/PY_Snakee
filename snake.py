import turtle

STARTING_POSITION = [(0,0) ,(-20,0), (-40,0)]
MOVE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.addnew(position)

    def move_snake(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            newX = self.snakes[snake_num - 1].xcor()
            newY = self.snakes[snake_num - 1].ycor()

            self.snakes[snake_num].goto(newX, newY)

        self.head.forward(MOVE_SPEED)

    def addnew(self, position):
        snake = turtle.Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snakes.append(snake)

    def extend(self):
        self.addnew(self.snakes[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

