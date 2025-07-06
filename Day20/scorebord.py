from turtle import Turtle 
from snake import Snake

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle): 
    def __init__(self):
        super().__init__() 
        self.score = 0     
        self.goto(0, 250)  
        self.color("white") 
        self.hideturtle() 
        self.penup()      
        self.refresh()    
    def refresh(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1  
        self.clear()      
        self.refresh()    
    def game_over(self):
        self.goto(0,0)
        self.write("Game over ")