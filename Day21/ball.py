from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0) 
        self.x_move = 10 
        self.y_move = 10  
       

    def move(self):
        """Moves the ball based on its current x_move and y_move values."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Changes the vertical direction of the ball (bounces off top/bottom)."""
        self.y_move *= -1 

    def bounce_x(self):
        """Changes the horizontal direction of the ball (bounces off paddles)."""
        self.x_move *= -1
    def reset_position(self):
        """Resets the ball to the center of the screen."""
        self.goto(0, 0)
        self.bounce_x()