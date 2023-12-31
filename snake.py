from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)



    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("white")
        self.segments.append(new_segment)

    def extend(self):
        #Add segment after every food.
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:  # Avoid reversing direction
            self.head.setheading(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:  # Avoid reversing direction
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:  # Avoid reversing direction
            self.head.setheading(RIGHT)

    def move_down(self):
        if self.head.heading() != UP:  # Avoid reversing direction
            self.head.setheading(DOWN)
