from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generator():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    S_letters = [choice(letters) for _ in range(1, randint(8,10)+1)]
    S_numbers = [choice(numbers) for _ in range(1, randint(2,4)+1)]
    S_symbols = [choice(symbols) for _ in range(1, randint(2,4)+1)]

    S = S_letters + S_numbers + S_symbols
    shuffle(S)

    String = "".join(S)
    pyperclip.copy(String)
    passw.delete(0, END)
    passw.insert(0, String)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web.get()
    email = ema.get()
    password = passw.get()

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty.")
    else:
        is_ok = messagebox.askyesno(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n    Save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} -|- {email} -|- {password}\n")
            web.delete(0,END)
            passw.delete(0,END)
            web.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("--Password Manager--")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
lock_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= lock_png)
canvas.grid(column=1, row=0)

website = Label(text= "Website:")
website.grid(column=0, row=1)

web = Entry(width=36)
web.grid(column=1, row=1, columnspan=2)
web.focus()

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

ema = Entry(width=36)
ema.insert(0, "mishraabhinav445@gmail.com")
ema.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

passw = Entry(width=20)
passw.grid(column=1, row=3)

gen = Button(text="Generate password", width=13, height=1)
gen.config(command=generator)
gen.grid(column=2, row=3)

add = Button(text="Add", width=34, height=1)
add.config(command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()