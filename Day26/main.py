import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_list = {row.letter: row.code for (index, row) in data.iterrows()}


has_finished = True
while has_finished:
    user_input = input("Enter a Word: ").upper()
    letter_characters = [char for char in user_input]
    try: 
        phonetic_codes = [new_list[char] for char in letter_characters]
    except KeyError as error_msg:
        print("sorry, only letters in the alphabet please")
    else:
        print(phonetic_codes)
        has_finished=False


