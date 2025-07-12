from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x_position,y_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_position,y_position)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 290:  
            self.goto(self.xcor(), new_y)  
    def go_down(self):
        new_y = self.ycor() - 20
        if new_y < 290:  
            self.goto(self.xcor(), new_y) 
    
