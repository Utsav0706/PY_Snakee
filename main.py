import turtle
import time
import snake
import food

screen = turtle.Screen()
screen.setup(width=1200, height=750)
screen.bgcolor("black")
screen.title("My Snake 😁")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()















screen.exitonclick()