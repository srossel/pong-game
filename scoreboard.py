from turtle import Turtle
INIT_X = 0
INIT_Y = 280


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.goto(x=INIT_X, y=INIT_Y)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.score_left}        {self.score_right}", False, align="center", font=("Arial", 48, "normal"))

    def increase_score_left(self):
        self.score_left = self.score_left + 1
        self.clear()
        self.update_scoreboard()
    def increase_score_right(self):
        self.score_right = self.score_right + 1
        self.clear()
        self.update_scoreboard()

    #game_over logic haven't been implemented yet.

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", False, align="center", font=("Arial", 24, "normal"))

    def draw_game_field(self):
        self.penup()
        self.goto(0, 250)
        self.setheading(270)
        for i in range(13):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.goto(0, -270)
        self.pendown()
        self.goto(300, -270)
        self.goto(300,270)
        self.goto(-300,270)
        self.goto(-300,-270)
        self.goto(0,-270)
        self.penup()
        self.goto(0,-360)
        self.hideturtle()

