import colorgram
import turtle  as tr
import random
colors = colorgram.extract("image.jpg",30)
color_list = []
for i in range(len(colors)):
    color = colors[i]
    rgb = color.rgb
    r,g,b = rgb
    single_rgb = (r,g,b)
    color_list.append(single_rgb)



tim = tr.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tr.colormode(255)

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
no_of_dot = 100
for dot_count in range(1,no_of_dot+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = tr.Screen()
screen.exitonclick()
