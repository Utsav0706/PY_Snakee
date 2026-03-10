import turtle

ALIGNMENT = "center"
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
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)