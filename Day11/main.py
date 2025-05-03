import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)


player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card(), deal_card()]

def adjust_aces(hand):
    """Convert 11 to 1 if hand busts with an Ace"""
    while sum(hand) > 21 and 11 in hand:
        ace_index = hand.index(11)
        hand[ace_index] = 1


player_bust = False
while True:
    player_total = sum(player_hand)
    print(f"\nYour cards: {player_hand}, current score: {player_total}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    if player_total > 21:
        player_bust = True
        break

    action = input("Type 'y' to hit, 'n' to stand: ").lower()
    if action == 'y':
        player_hand.append(deal_card())
        adjust_aces(player_hand)
    else:
        break


dealer_bust = False
if not player_bust:
    while sum(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        adjust_aces(dealer_hand)
    
    dealer_total = sum(dealer_hand)
    if dealer_total > 21:
        dealer_bust = True


print(f"\nFinal hands:")
print(f"Your hand: {player_hand}, total: {sum(player_hand)}")
print(f"Dealer's hand: {dealer_hand}, total: {sum(dealer_hand)}")

if player_bust:
    print("You bust! Dealer wins!")
elif dealer_bust:
    print("Dealer busts! You win!")
else:
    if sum(player_hand) > sum(dealer_hand):
        print("You win!")
    elif sum(player_hand) == sum(dealer_hand):
        print("Draw!")
    else:
        print("Dealer wins!")