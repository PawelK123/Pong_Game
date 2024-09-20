from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
speed = 0.1
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
r_Paddle = Paddle((350,0))
l_Paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()
    screen.listen()
    screen.onkey(r_Paddle.go_up, "Up")
    screen.onkey(r_Paddle.go_down, "Down")
    screen.onkey(l_Paddle.go_up, "w")
    screen.onkey(l_Paddle.go_down, "s")
    time.sleep(speed)
    ball.move()
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with the paddle
    if ball.distance(r_Paddle) < 50 and ball.xcor() > 320 or ball.distance(l_Paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed -= 0.01
    if speed == 0:
        speed = 0.01


    # Detect R paddle misses
    if ball.xcor() > 400:
        ball = Ball()
        ball.x_move *= -1
        ball.y_move *= -1
        scoreboard.l_point()
        speed = 0.1
    # Detect L paddle misses
    elif ball.xcor() < -400:
        ball = Ball()
        scoreboard.p_point()
        speed = 0.1














screen.exitonclick()
