from turtle import Turtle
FONT = 20
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = 0
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {0}", True, align=ALIGNMENT, font=("Ariel", FONT, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"score: {self.score}", True, align=ALIGNMENT, font=("Ariel", FONT, "normal"))

    def reset(self):
        self.score = 0





