from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def generate_shifted(shift):
    return [alphabet[(i + shift) % 26] for i in range(len(alphabet))]

def Ceasar_Cipher(text,shift,direction):
    shifted_alphabet = generate_shifted(shift)
    shifted_word = ""
    for char in text:
        if direction == 'encode':
             if not char == ' ':
                 index_of_shifted_leter = alphabet.index(char)
                 shifted_word+=shifted_alphabet[index_of_shifted_leter]
             else:
                 shifted_word+=" "
        if direction == 'decode':
            if not char == ' ':
                 index_of_shifted_leter = shifted_alphabet.index(char)
                 shifted_word+=alphabet[index_of_shifted_leter]
            else:
                 shifted_word+=" "
    return shifted_word
        




while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to exit:\n").lower()
    if direction == 'exit':
        print("Good By")
        break
    if direction not in ["encode","decode"]:
        print("Invalid input pleas try again")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    print(f"Here's the {direction} result: {Ceasar_Cipher(text,shift,direction)}")
    want_toCont= input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if want_toCont == 'no':
        print("Good By")
        break




















