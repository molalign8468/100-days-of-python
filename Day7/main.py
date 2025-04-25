import random
from hangman_word import word_list
from hangman_art import stages, logo

lives = 6
print(logo)

chosen_word = random.choice(word_list)
correct_letters = [] 
display = ["_"] * len(chosen_word)  

print("Word to guess: " + " ".join(display))

game_over = False

while not game_over:
    print(f"\n**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed '{guess}'")
        continue  

    if guess in chosen_word:
        correct_letters.append(guess)
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

    print("Word to guess: " + " ".join(display))

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")
    elif lives == 0:
        game_over = True
        print(f"*********************** IT WAS '{chosen_word}'! YOU LOSE **********************")

    print(stages[lives])