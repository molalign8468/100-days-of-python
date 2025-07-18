from turtle import Turtle 
from snake import Snake

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle): 
    def __init__(self):
        super().__init__() 
        self.score = 0   
        self.high_score=0  
        self.goto(0, 250)  
        self.color("white") 
        self.hideturtle() 
        self.penup()      
        self.refresh()    
    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.high_score}", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score=0
        self.refresh()

    def inc_score(self):
        self.score += 1  
        self.refresh()    
  