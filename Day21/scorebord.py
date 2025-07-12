from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard display."""
        self.clear()
        self.goto(-100, 260)
        self.write(f"{self.score1}", align="center", font=("Courier", 24, "normal"))
        self.goto(100, 260)
        self.write(f"{self.score2}", align="center", font=("Courier", 24, "normal"))

    def player1_point(self):
        """Increments Player 1's score by 1."""
        self.score1 += 1
        self.update_scoreboard()

    def player2_point(self):
        """Increments Player 2's score by 1."""
        self.score2 += 1
        self.update_scoreboard()
    def reset_score(self):
        """Resets both players' scores to zero."""
        self.score1 = 0
        self.score2 = 0
        self.update_scoreboard()