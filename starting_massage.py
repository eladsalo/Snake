from turtle import Turtle
import time

FONT = 30
ALIGNMENT = "center"


class StartingMassage(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 100)
        self.color("green")
        self.hideturtle()
        self.write("Be ready", True, align=ALIGNMENT, font=("Ariel", FONT, "normal"))
        time.sleep(1)
        self.clear()
        self.goto(0, 100)
        time.sleep(0.1)
        self.write("The game will start in", True, align=ALIGNMENT, font=("Ariel", FONT, "normal"))
        time.sleep(1)
        self.clear()
        self.goto(0, 100)
        time.sleep(0.1)
        self.write("3", True, align=ALIGNMENT, font=("Ariel", FONT+10, "normal"))
        time.sleep(1)
        self.clear()
        self.goto(0, 100)
        self.write("2", True, align=ALIGNMENT, font=("Ariel", FONT+10, "normal"))
        time.sleep(1)
        self.clear()
        self.goto(0, 100)
        self.write("1", True, align=ALIGNMENT, font=("Ariel", FONT+10, "normal"))
        time.sleep(1)
        self.clear()
        self.goto(0, 100)
        self.write("Go!", True, align=ALIGNMENT, font=("Ariel", FONT+10, "normal"))
        time.sleep(0.3)
        self.clear()
