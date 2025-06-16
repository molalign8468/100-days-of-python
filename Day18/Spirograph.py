import turtle as tr
import random

timmy = tr.Turtle()
tr.colormode(255)
timmy.shape("turtle")
timmy.pensize(1)
timmy.speed("fastest")
while True:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    timmy.pencolor((r,g,b))
    timmy.circle(100)
    timmy.left(10)
    print(timmy.heading())
    if timmy.heading() == 350.0:
        break

    




screen = tr.Screen()
screen.exitonclick()