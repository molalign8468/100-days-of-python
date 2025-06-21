from turtle import Turtle, Screen
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
FINISH_LINE = 230
START_LINE = -230
NUM_TURTLES = 5
COLORS = ["red", "green", "blue", "purple", "orange"]
Y_SPACING = 40
START_Y = -80

def setup_screen():
    """Configure the game screen"""
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Turtle Race")
    return screen

def create_turtle(color, y_position):
    """Create and position a turtle"""
    turtle = Turtle("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(START_LINE, y_position)
    return turtle

def setup_racers():
    """Create all racing turtles"""
    return [create_turtle(COLORS[i], START_Y + i * Y_SPACING) 
            for i in range(NUM_TURTLES)]

def get_user_bet(screen):
    """Prompt user for their bet"""
    return screen.textinput("Make your bet", 
                          f"Which turtle will win? ({', '.join(COLORS)}): ").lower()

def race(racers, user_bet):
    """Run the race and determine winner"""
    while True:
        for racer in racers:
            racer.forward(random.randint(1, 10))
            if racer.xcor() >= FINISH_LINE:
                winner_color = racer.pencolor()
                display_result(winner_color, user_bet)
                return winner_color

def display_result(winner, user_bet):
    """Show race results on screen"""
    result = Turtle()
    result.hideturtle()
    result.penup()
    
    if winner == user_bet:
        result.write("You won!", align="center", font=("Arial", 24, "bold"))
    else:
        result.write(f"You lose! {winner.capitalize()} won", 
                   align="center", font=("Arial", 20, "normal"))
    

    result.goto(0, SCREEN_HEIGHT//2 - 40)
    result.write(f"Winner: {winner.capitalize()}", 
               align="center", font=("Arial", 16, "italic"))

def main():
    """Main game function"""
    screen = setup_screen()
    racers = setup_racers()
    user_bet = get_user_bet(screen)
    
    if user_bet and user_bet in COLORS:
        winner = race(racers, user_bet)
    else:
        print("Invalid bet. Game canceled.")
    
    screen.exitonclick()

if __name__ == "__main__":
    main()