# TODO .#1 Create the screen -- DONE
# TODO .#2 Create and move paddle -- DONE
# TODO .#3 Create another paddle -- DONE
# TODO. #4 Create the ball and make it move -- DONE
# TODO. #5 Detect collision with wall and bounce -- DONE
# TODO. #6 Detect collision with Paddle -- DONE
# TODO. #7 Detect when paddle misses -- DONE
# TODO. #8 Keep Score -- DONE

from turtle import Screen
from paddle import Paddle
from scoreboard import Score
from ball import Ball
import time

#Setting up screen properties
screen = Screen()
screen.screensize(canvheight=400, canvwidth=600, bg="black")
screen.title("Python Pong Game")

#Turning screen animation off
screen.tracer(0)

#Setting up Scoreboard and field
scoreboard = Score()
line = Score()
line.draw_game_field()

#Setting up the paddles
initial_position_l = [-300, 40 ]
initial_position_r = [300, 40 ]
l_paddle = Paddle()
r_paddle = Paddle()
l_paddle.create_paddle(initial_position_l)
r_paddle.create_paddle(initial_position_r)

#Setting up the ball.
ball = Ball()

#Initializing the game while loop.
game = True

#Making screen to listen to keyboard "keys" to execute command inside of loop to move_up or move_down.
screen.listen()

game = True

while game == True:

    screen.update()
    time.sleep(0.1)
    #Calling Ball moves() method to get the ball moving.
    ball.moves()
    screen.onkey(fun=l_paddle.move_up, key='w')
    screen.onkey(fun=l_paddle.move_down, key='s')
    screen.onkey(fun=r_paddle.move_up, key='Up')
    screen.onkey(fun=r_paddle.move_down, key='Down')

#Collision with left Paddle
    if ball.distance(l_paddle.segments[0]) < 20:
        ball.setheading(60)
    elif ball.distance(l_paddle.segments[1]) < 20:
        ball.setheading(30)
    elif ball.distance(l_paddle.segments[2]) < 20:
        ball.setheading(0)
    elif ball.distance(l_paddle.segments[3]) < 20:
        ball.setheading(330)
    elif ball.distance(l_paddle.segments[4]) < 20:
        ball.setheading(300)

#Collision with right Paddle
    if ball.distance(r_paddle.segments[0]) < 20:
        ball.setheading(120)
    elif ball.distance(r_paddle.segments[1]) < 20:
        ball.setheading(150)
    elif ball.distance(r_paddle.segments[2]) < 20:
        ball.setheading(180)
    elif ball.distance(r_paddle.segments[3]) < 20:
        ball.setheading(210)
    elif ball.distance(r_paddle.segments[4]) < 20:
        ball.setheading(240)

#Wall collision rules when ball moving from right to left
    if ball.heading() == 120 and ball.position()[1] > 260:
        ball.setheading(210)
    elif ball.heading() == 150 and ball.position()[1] >260:
        ball.setheading(240)
    elif ball.heading() == 210 and ball.position()[1] < -260:
        ball.setheading(120)
    elif ball.heading() == 240 and ball.position()[1] < -260:
        ball.setheading(150)

#Wall collision rules when ball moving from left to right
    elif ball.heading() == 60 and ball.position()[1] > 260:
        ball.setheading(330)
    elif ball.heading() == 30 and ball.position()[1] > 260:
        ball.setheading(300)
    elif ball.heading() == 330 and ball.position()[1] < -260:
        ball.setheading(60)
    elif ball.heading() == 300 and ball.position()[1] < -260:
        ball.setheading(30)

#Score track
    if ball.position()[0] > 320:
        scoreboard.increase_score_left()
        ball.goto(0, 0)
        ball.setheading(0)

    if ball.position()[0] < -320:
        scoreboard.increase_score_right()
        ball.goto(0, 0)
        ball.setheading(0)

#Keeping screen visible
screen.exitonclick()