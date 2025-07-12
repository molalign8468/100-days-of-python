from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebord import Scoreboard
import time

TOP_WALL_Y = 280
BOTTOM_WALL_Y = -280

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) 



paddle1 = Paddle(350,0)
paddle2 = Paddle(-350,0)

ball = Ball()
scoreboard = Scoreboard()


screen.listen()  
screen.onkey(paddle1.go_up, "Up")    
screen.onkey(paddle1.go_down, "Down") 

screen.onkey(paddle2.go_up, "w")    
screen.onkey(paddle2.go_down, "s") 


game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.1) 
    ball.move()
    if ball.ycor() > TOP_WALL_Y or ball.ycor() < BOTTOM_WALL_Y:
        ball.bounce_y()
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        scoreboard.player2_point() if ball.xcor() > 0 else scoreboard.player1_point()
        ball.bounce_x()

    if ball.xcor() > 390 :
        ball.reset_position()
        scoreboard.reset_score()
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.reset_score()

screen.exitonclick()