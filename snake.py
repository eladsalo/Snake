from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "right"

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        new_segments = Turtle("square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def move(self):
        for num in range(len(self.segments)-1, 0, -1):
            self.segments[num].goto(self.segments[num-1].xcor(), self.segments[num-1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.direction != "down":
            self.head.setheading(UP)
            self.move()
            self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.head.setheading(DOWN)
            self.move()
            self.direction = "down"

    def right(self):
        if self.direction != "left":
            self.head.setheading(RIGHT)
            self.move()
            self.direction = "right"

    def left(self):
        if self.direction != "right":
            self.head.setheading(LEFT)
            self.move()
            self.direction = "left"

    # another way to start again the game
    def reset(self):
        for seg in self.segments:
            self.segments.clear(1000, 1000)
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "right"


