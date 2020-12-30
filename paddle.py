from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.pos_sqr = []

    #Create_paddle will proceed to create segments that will be part of the paddle.
    #Segments will be 20 x 20 pixels and will be created from initial_position, substracting on the y axis as they
    #are being created.

    def create_paddle(self, initial_position):
        for position in range(5):
            new_segment = Turtle(shape='square')
            new_segment.speed(0)
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(initial_position)
            initial_position = (initial_position[0], initial_position[1]-20)
            self.segments.append(new_segment)

    # Once all paddle segments are created, segment[0] will lead movement when moving up.
    # We will create a temporary position list and store all current positions.
    # Once segment[0] moves up (heading = 90 and forward of 20 pixels) ,
    # then all remaining segments will move to the position of segment in front of them(1->0, 2->1, 3->2 and 4->3).
    # We will clean the pos[] list , since don't want any position to be stored at the end of the movement.
    # Same logic for move_down(), but reversed having segment[4] as the lead.

    def move_up(self):

        if self.segments[0].position()[1] < 260:
            pos = []
            self.segments[0].setheading(90)
            for i in range(0, len(self.segments)):
                pos.append(self.segments[i].position())
            self.segments[0].forward(20)
            for j in range(1, len(self.segments)):
                self.segments[j].goto(pos[j-1])
            pos.clear()


    def move_down(self):
        if self.segments[4].position()[1] > -260:
            pos = []
            self.segments[4].setheading(270)
            for i in range(0, len(self.segments)):
                pos.append(self.segments[i].position())
            self.segments[-1].forward(20)
            for j in range(len(self.segments)-1, 0, -1):
                self.segments[j-1].goto(pos[j])
            pos.clear()