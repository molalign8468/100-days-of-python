from art import logo
import os

print(logo)
bidders= {}


while True:
    name = input("What is your name \n")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    is_there_other = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if is_there_other == 'yes':
        os.system('cls')
        continue
    elif is_there_other == 'no':
        max_bid = 0
        winner = ""
        for key in bidders:
            if bidders[key] > max_bid:
                winner = max(bidders, key=lambda x: bidders[x])
                max_bid = bidders[winner]
                print(f"The winner is {winner} with a bid of ${max_bid}")
                
        break
    else:
        print("Invalid input ")
        continue

