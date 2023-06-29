from turtle import Turtle, Screen
screen = Screen()
import time

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

START_POSITIONS =  [(0, 0), (-20, 0), (-40, 0)] #these two are constants, hence the all caps and bein up here.
MOVE_DISTANCE = 20

class Snake:
    def __init__(self): #when we create the snake object, the stuff under this initializer happens.
        self.segments = [] #need to use "self" when creating a class.
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):

        # creating a for loop that causes the snake to move continously
        for seg_num in range(len(self.segments) - 1, 0, -1):  # (start, stop, step)
            new_x = self.segments[seg_num - 1].xcor()  # getting the x and y coords of the square infront of it.
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # tell the square to go to those coords
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
            self.move()


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()



    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()



