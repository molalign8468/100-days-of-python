import tkinter as tk
import random
import pyperclip
import json
from tkinter import messagebox, END

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
PASSWORD_FILE = "password.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a random password and copies it to the clipboard."""
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(LETTERS) for _ in range(nr_letters)]
    password_list.extend([random.choice(SYMBOLS) for _ in range(nr_symbols)])
    password_list.extend([random.choice(NUMBERS) for _ in range(nr_numbers)])

    random.shuffle(password_list)
    password = "".join(password_list)

    pyperclip.copy(password)
    return password

def set_random_password():
    """Sets a newly generated password into the password input field."""
    password_input.delete(0, END)
    password_input.insert(0, generate_password())
    messagebox.showinfo(title="Password Generated", message="Password copied to clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    """Retrieves input, validates, confirms, and saves password data to JSON."""
    website = website_input.get().strip()
    username = username_input.get().strip()
    password = password_input.get().strip()

    if not website or not username or not password:
        messagebox.showerror("Error", "All fields are required. Please provide all input.")
        return

    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    response = messagebox.askokcancel(
        title="Confirm Details",
        message=f"Please confirm the entered details:\n\n"
                f"Website: {website}\n"
                f"Username: {username}\n"
                f"Password: {password}\n\n"
                f"Is this correct?"
    )

    if response:
        try:
            with open(PASSWORD_FILE, "r", encoding="utf-8") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}
        except json.JSONDecodeError:
            data = {}
            messagebox.showwarning("File Warning", f"'{PASSWORD_FILE}' was empty or corrupted. Starting new data.")

        data.update(new_data)
        with open(PASSWORD_FILE, "w", encoding="utf-8") as data_file:
            json.dump(data, data_file, indent=4)

        messagebox.showinfo("Success", "Password saved successfully!")
        website_input.delete(0, END)
        password_input.delete(0, END)
        website_input.focus()
    else:
        messagebox.showinfo("Cancelled", "Password saving cancelled.")

# ---------------------------- SEARCH FUNCTIONALITY ------------------------------- #
def search_password():
    """Searches for a website's credentials and displays them."""
    item_to_search = website_input.get().strip()

    if not item_to_search:
        messagebox.showwarning("Search Error", "Please enter a website to search.")
        return

    try:
        with open(PASSWORD_FILE, "r", encoding="utf-8") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File Error", message="No data file found. Please add some passwords first.")
        return
    except json.JSONDecodeError:
        messagebox.showerror(title="File Error", message=f"'{PASSWORD_FILE}' is corrupted or empty. Cannot search.")
        return

    if item_to_search in data:
        username = data[item_to_search]["username"]
        password = data[item_to_search]["password"]
        messagebox.showinfo(
            title=item_to_search,
            message=f"Email: {username}\nPassword: {password}"
        )
        pyperclip.copy(password) # Copy found password to clipboard
        messagebox.showinfo("Password Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror(title="Not Found", message=f"No details found for '{item_to_search}'.")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
try:
    image = tk.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=image)
except tk.TclError:
    messagebox.showwarning("Image Warning", "logo.png not found. Application will run without logo.")
    canvas.create_text(100, 100, text="LOGO\nMissing", font=("Arial", 16, "bold"), fill="grey")
canvas.grid(row=0, column=1, columnspan=2, pady=20)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, sticky="W", pady=2)

username_label = tk.Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky="W", pady=2)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky="W", pady=2)

# Entry widgets
website_input = tk.Entry(width=21)
website_input.grid(row=1, column=1, sticky="EW", pady=2)
website_input.focus()

username_input = tk.Entry(width=40)
username_input.grid(row=2, column=1, columnspan=2, sticky="EW", pady=2)
username_input.insert(0, "molalign@gmail.com") 

password_input = tk.Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW", pady=2)

# Buttons
generator_btn = tk.Button(text="Generate Password", command=set_random_password)
generator_btn.grid(row=3, column=2, sticky="EW", padx=5, pady=2)

add_btn = tk.Button(text="Add", width=36, command=add_password)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW", pady=10)

search_button = tk.Button(text="Search", command=search_password) 
search_button.grid(row=1, column=2, sticky="EW", padx=5, pady=2)

window.mainloop()