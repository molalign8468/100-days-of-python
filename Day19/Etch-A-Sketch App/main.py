from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_clock_wise():
    tim.right(10)
def move_counter():
    tim.left(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_clock_wise,"d")
screen.onkey(move_counter,"a")
screen.onkey(clear,"c")


screen.listen()
screen.exitonclick()