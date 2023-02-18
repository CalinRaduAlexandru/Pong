from turtle import Turtle, Screen, time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
l_score = Scoreboard()
r_score = Scoreboard()


screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True

ball = Ball()

while game_on:
    time.sleep(ball.movement)
    screen.update()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 75 and ball.xcor() > 320 or \
            ball.distance(l_paddle) < 75 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        l_score.l_win()
        ball.reset_position()

    elif ball.xcor() < -400:
        r_score.r_win()
        ball.reset_position()












screen.exitonclick()
