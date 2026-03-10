import turtle
import random

class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("Yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomX = random.randint(-575, 575)
        randomY = random.randint(-300, 300)
        self.goto(randomX,randomY)


