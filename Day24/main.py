with open("./input/Letters/starting_letter.txt") as text:
    template = text.read()
with open("./input/Names/invited_names.txt") as names:
    #name = names.read()
    list_of_names = names.readlines()

for name in list_of_names:
    new_letter = template.replace("name",name.strip())
    letters = open(f"./output/ReadyToSend/letter_for_{name.strip()}.doc",mode="w")
    letters.write(new_letter)
    

