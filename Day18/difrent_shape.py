import turtle as tr
import random

timmy = tr.Turtle()
timmy.color('red','yellow')
timmy.shape("turtle")

colors =["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]



# angle of triangle = 360 / 3
# angle or rectangle = 360/4
# angle of pentagon = 360 /5

starter = 3

while starter < 10:
    for i in range(starter):
        timmy.forward(100)
        timmy.pencolor(random.choice(colors))
        timmy.left(360/starter)
    starter+=1








screen = tr.Screen()
screen.exitonclick()