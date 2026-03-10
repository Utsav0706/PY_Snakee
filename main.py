import turtle
import time

screen = turtle.Screen()
screen.setup(width=1200, height=750)
screen.bgcolor("black")
screen.title("My Snake 😁")

starting_position = [(0,0) ,(-20,0), (-40,0)]

snakes = []

for position in starting_position:
    snake = turtle.Turtle("square")
    snake.penup()
    snake.color("white")
    snake.goto(position)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for snake in snakes:
        snake.forward(20)















screen.exitonclick()