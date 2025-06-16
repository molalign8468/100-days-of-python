import turtle as tr
import random

timmy = tr.Turtle()
tr.colormode(255)
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")
# colors =["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]



direction = [0,90,180,270]
while True:
    # timmy.color(random.choice(colors))
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    timmy.pencolor((r, g, b))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))




screen = tr.Screen()
screen.exitonclick()