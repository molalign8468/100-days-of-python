import turtle
import time
from snake import Snake
from Food import Food
from scorebord import ScoreBoard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game (OOP)")
screen.tracer(0) 

scoreBoard = ScoreBoard()

snake = Snake()
food = Food()
print(food.pos())
print(snake.head.distance(food))



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move() 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreBoard.reset()
        snake.reset()

    if snake.head.distance(food) < 15:
        print("Collision!")
        snake.extend()
        food.refresh()
        scoreBoard.inc_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreBoard.reset()
            snake.reset()
        

screen.exitonclick()