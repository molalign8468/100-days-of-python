import tkinter
import pandas
import random

# -------------------Constants----------------#
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
flip_timer = None

#------------------MAIN FUNCIONLITY---------------#

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/amharic_word.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="Amharic", fill="white")
    canvas.itemconfig(card_word, text=current_card["Amharic"], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

#-------------------UI----------------#
window = tkinter.Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=0)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(2, weight=1)

# Load images
try:
    right_icon = tkinter.PhotoImage(file="./images/right.png")
    wrong_icon = tkinter.PhotoImage(file="./images/wrong.png")
    card_front = tkinter.PhotoImage(file="./images/card_front.png")
    card_back = tkinter.PhotoImage(file="./images/card_back.png")
except tkinter.TclError:
    print("Image files not found. Please ensure 'right.png', 'wrong.png', 'card_front.png', and 'card_back.png' are in the './images/' directory.")
    right_icon = None
    wrong_icon = None
    card_front = None
    card_back = None
    right_btn_text = "✅"
    wrong_btn_text = "❌"
else:
    right_btn_text = ""
    wrong_btn_text = ""

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=1, column=1)

right_btn = tkinter.Button(image=right_icon, text=right_btn_text, font=("Arial", 24), relief="flat", highlightthickness=0, command=is_known)
right_btn.grid(row=2, column=2, sticky="E")

wrong_btn = tkinter.Button(image=wrong_icon, text=wrong_btn_text, font=("Arial", 24), relief="flat", highlightthickness=0, command=next_card)
wrong_btn.grid(row=2, column=0, sticky="W")

next_card()

window.mainloop()