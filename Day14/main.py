import random
import os
from data import data
import art

opponent_A = random.choice(data)
opponent_B = random.choice(data)

def who_has_bigger(A,B):
    '''Compare Both celebrity's '''
    if A > B:
      return "a"
    elif A< B:
       return "b"
result = who_has_bigger(opponent_A["follower_count"],opponent_B["follower_count"])

score = 0
isGame_over = False

while not isGame_over:
   print(art.logo)
   print(f"Compare A: {opponent_A["name"]}, a {opponent_A["description"]}, from {opponent_A["country"]}.")
   print(art.vs)
   print(f"Compare B: {opponent_B["name"]}, a {opponent_B["description"]}, from {opponent_B["country"]}.")
   user_in = input("Who has more followers? Type 'A' or 'B': ").lower()



   if user_in == result :
     score+=1
     print(f"Correct! Current score: {score}\n")
     opponent_A = opponent_B
     opponent_B = random.choice(data)
     os.system('clear')

     result = who_has_bigger(opponent_A["follower_count"],opponent_B["follower_count"])

   else:
      isGame_over = True
      print(f"\nSorry, that's wrong. Final score: {score}")
      
print("Game Over!")




