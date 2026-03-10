import turtle

screen = turtle.Screen()
screen.setup(width=1200, height=750)
screen.bgcolor("black")
screen.title("My Snake 😁")


snake1 = turtle.Turtle("square")
snake1.color("white")

snake2 = turtle.Turtle("square")
snake2.color("white")
snake2.goto(-20,0)

snake3 = turtle.Turtle("square")
snake3.color("white")
snake3.goto(-40,0)

screen.exitonclick()