import turtle

ALLGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,300)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Score: {self.score}", align=ALLGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()