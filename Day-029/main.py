import tkinter
from tkinter import messagebox
import random
import pyperclip

# create random password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# save credentials to txt file
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEMail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website},{email},{password} \n")
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)

# UI Setup
WindowApp = tkinter.Tk()
WindowApp.title("Password Manager")
WindowApp.config(padx=20, pady=20)

# logo
CanvasApp = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
CanvasApp.create_image(100, 100, image=logo_img)
CanvasApp.grid(row=0, column=1)

# label
website_label = tkinter.Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password: ")
password_label.grid(row=3, column=0)

# entry
website_entry = tkinter.Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "email@test.com")
password_entry = tkinter.Entry(width=40)
password_entry.grid(row=3, column=1)

# buttons
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=50, command=save)
add_button.grid(row=4, column=1, columnspan=2)

WindowApp.mainloop()