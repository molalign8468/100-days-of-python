import tkinter
import random
from tkinter import messagebox, END 
import pyperclip
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():   
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(text=password)
    return password

def set_random_password():
    password_input.delete(0, END) 
    password_input.insert(0, generate_password())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if not website or not username or not password:
        messagebox.showerror("Error", "Empty fields are not acceptable, please provide all input.")
        return

    response = messagebox.askokcancel(title="Confirm Details",
                                      message=f"Please confirm the entered details:\n\n"
                                              f"Website: {website}\n"
                                              f"Username: {username}\n"
                                              f"Password: {password}\n\n"
                                              f"Is this correct?")
    if response: 
        try:
            with open("password.txt", "a", encoding="utf-8") as content:
                content.write(f"{website} | {username} | {password}\n")
        except IOError:
            messagebox.showerror("Error", "Could not write to file. Check file permissions.")
        else:
            messagebox.showinfo("Success", "Password saved successfully!")
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus() 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0) 
try:
    image = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=image) 
except tkinter.TclError:
    messagebox.showwarning("Image Warning", "logo.png not found. Application will run without logo.")
    canvas.create_text(100, 100, text="LOGO\nMissing", font=("Arial", 16, "bold"), fill="grey")
canvas.grid(row=0, column=1, columnspan=2, pady=20) 

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0, sticky="W", pady=2)

username_label = tkinter.Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky="W", pady=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0, sticky="W", pady=2)

# Entry widgets
website_input = tkinter.Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW", pady=2)
website_input.focus() 

username_input = tkinter.Entry(width=40)
username_input.grid(row=2, column=1, columnspan=2, sticky="EW", pady=2)
username_input.insert(0, "molalign@gmail.com")

password_input = tkinter.Entry(width=21) 
password_input.grid(row=3, column=1, sticky="EW", pady=2)

# Buttons
generator_btn = tkinter.Button(text="Generate Password", command=set_random_password)
generator_btn.grid(row=3, column=2, sticky="EW", padx=5, pady=2) 

add_btn = tkinter.Button(text="Add", width=36, command=add_password) 
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW", pady=10)

window.mainloop()