from turtle import Turtle
import random

INITIAL_POSITION = [0, 0]
INITIAL_HEADING = [0,180]

#As soon as the ball is initiated, it will go to INITIAL_POSITION and pick a random heading from INITIAL_HEADING, so
#it can start moving either to the left or right side once moves() method is called.

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(1)
        self.penup()
        self.goto(INITIAL_POSITION)
        self.setheading(random.choice(INITIAL_HEADING))

    def moves(self):
        self.forward(20)
        #printing ball.heading to verify movement.
        #print(self.heading())
