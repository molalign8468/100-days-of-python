# Rock bit scissors
# Scissors bit Paper
# Paper bit Rock
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_choices = ['rock', 'paper', 'scissors']
gestures = [rock, paper, scissors]  
computer_index = random.randint(0, 2)
computer_choice = game_choices[computer_index]

while True:
    try:
        my_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
        if 0 <= my_index <= 2:
            break
        else:
            print("Invalid input. Please enter 0, 1, or 2.")
    except ValueError:
        print("Please enter a number!")

my_choice = game_choices[my_index]

print(f"\nYou chose:\n{gestures[my_index]}")
print(f"Computer chose:\n{gestures[computer_index]}")

if my_choice == computer_choice:
    print("Draw!")
elif (
    (my_choice == "rock" and computer_choice == "scissors") or
    (my_choice == "scissors" and computer_choice == "paper") or
    (my_choice == "paper" and computer_choice == "rock")
):
    print("You win!")
else:
    print("You lose!")