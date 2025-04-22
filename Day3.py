print("Welcome to Treasure Island!")
user_response = input("Your mission is to find the treasure.\nYou're at a crossroad. Where do you want to go?\nType 'left' or 'right'\n").lower()

if user_response == "left":
    print("You've come to a lake. There's an island in the middle.")
    action = input("Type 'wait' to wait for a boat or 'swim' to swim across.\n").lower()
    
    if action == "wait":
        print("You arrive at the island unharmed. There's a house with 3 doors.")
        door_choice = input("One red, one yellow, and one blue. Which color do you choose?\n").lower()
        
        match door_choice:
            case "red":
                print("It's a room full of fire. Game Over.")
            case "yellow":
                print("You found the treasure! You Win! 🏆")
            case "blue":
                print("You enter a room of beasts. Game Over.")
            case _:
                print("Invalid choice. Game Over.")
    
    elif action == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("Invalid choice. Game Over.")

elif user_response == "right":
    print("You fell into a hole. Game Over.")
else:
    print("Invalid direction. Game Over.")