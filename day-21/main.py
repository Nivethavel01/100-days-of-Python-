from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

score = ScoreBoard()
ball = Ball()

game_is_on = True

while game_is_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    #Detect collision on the top & bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        print("Ball hit the wall")
        ball.bounce()

    #Detect collision on the paddle
    if (ball.xcor() > 320 and  ball.distance(r_paddle) < 70) or (ball.xcor() > -320 and  ball.distance(l_paddle) < 70)  :
        print("Ball hit the paddle")
        ball.paddle_bounce()

    #Detect if r_paddle misses the ball
    if ball.xcor() > 380 :
        score.increase_score_r()
        ball.reset()

    #Detect if l_paddle misses the ball 
    if ball.xcor() < -380:
        score.increase_score_l()
        ball.reset()

screen.exitonclick()