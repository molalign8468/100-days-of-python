from art import logo
import os

bidders= {}


while True:
    name = input("What is your name \n")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    is_there_other = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if is_there_other == 'yes':
        os.system('cls')
        continue
    else:
        max_bid = 0
        winner = ""
        for key in bidders:
            if bidders[key] > max_bid:
                winner = max(bidders, key=lambda x: bidders[x])
                max_bid = bidders[winner]
                print(f"The winner is {winner} with a bid of ${max_bid}")
                
        break

