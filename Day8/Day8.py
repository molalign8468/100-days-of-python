from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def generate_shifted(shift):
    return [alphabet[(i + shift) % 26] for i in range(len(alphabet))]



def encrypt(text,shift):
    shifted_alphabet = generate_shifted(shift)
    encrypted_word = ""
    
    for char in text :
        if not char == ' ':
            index_of_shifted_leter = alphabet.index(char)
            encrypted_word+=shifted_alphabet[index_of_shifted_leter]
        else:
            encrypted_word+=" "
    return encrypted_word

def decrypt(text,shift):
    shifted_alphabet = generate_shifted(shift)
    decrypted_word = ""
    for char in text :
        if not char == ' ':
            index_of_shifted_leter = shifted_alphabet.index(char)
            decrypted_word+=alphabet[index_of_shifted_leter]
        else:
            decrypted_word+=" "

    return decrypted_word


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

    if direction == 'decode':
        print(decrypt(text,shift))
    if direction == 'encode':
        print(encrypt(text,shift))
    whant_coun= input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if whant_coun == 'no':
        print("Good By")
        break




















