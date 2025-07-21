import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_list = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter a Word: ").upper()
letter_characters = [char for char in user_input]
phonetic_codes = [new_list[char] for char in letter_characters]
print(phonetic_codes)