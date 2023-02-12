from turtle import  Turtle
import random


def random_place():
    x_place = random.randint(-280, 280)
    y_place = random.randint(-280, 280)
    tuple_place = (x_place, y_place)
    return tuple_place


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random_place())


