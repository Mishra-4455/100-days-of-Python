from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

#---------------------------------------------------DATA FILE--------------------------------------------#

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Japanese_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#------------------------------------------------BUTTON FUNCTION-----------------------------------------#

def next_card():
    global current_card, filp_timer
    window.after_cancel(filp_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_catagory, text=current_card["CATEGORY"], fill="black")
    canvas.itemconfig(card_title, text="Kanji", fill="black")
    canvas.itemconfig(card, image=card_front_img)
    if pandas.isna(current_card["KANJI"]):
        canvas.itemconfig(card_japanese, text="", fill="black")
        canvas.itemconfig(card_kanji, text=current_card["JAPANESE"], fill="black")
    else:
        canvas.itemconfig(card_japanese, text=current_card["JAPANESE"], fill="black")
        canvas.itemconfig(card_kanji, text=current_card["KANJI"], fill="black")
    filp_timer = window.after(5000, func=flip_card)

#---------------------------------------------SAVING TO SEP FILE------------------------------------------#

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#------------------------------------------------FLIPPING CARD--------------------------------------------#

def flip_card():
    global current_card
    canvas.itemconfig(card, image= card_back_img)
    canvas.itemconfig(card_catagory, fill="white")
    canvas.itemconfig(card_title, text="Romaji + English Meaning", fill="white")
    canvas.itemconfig(card_japanese, text=current_card["ENGLISH"], fill="white")
    canvas.itemconfig(card_kanji, text=current_card["ROMAJI"], fill="white")

#----------------------------------------------------UI SETUP--------------------------------------------#

#Display screen for everything
window = Tk()
window.title("Flashy")
window.config(padx= 50, pady=50, bg=BACKGROUND_COLOR)

filp_timer = window.after(3000, func=flip_card)

#flash card front
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
card_catagory = canvas.create_text(400, 60, text="Catagory", font=("Ariel", 20, "italic"))
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_kanji = canvas.create_text(400, 280, text="Kanji", font=("Ariel", 60, "bold"))
card_japanese = canvas.create_text(400, 350, text="japanese", font=("Ariel", 25))
canvas.grid(column=0, row=0, columnspan=2)

#Right button
right_img = PhotoImage(file="images/right.png")
correct = Button(image=right_img, highlightthickness=0, command=is_known)
correct.grid(column=1, row=1)

#wrong button
wrong_img = PhotoImage(file="images/wrong.png")
incorrect = Button(image=wrong_img, highlightthickness=0, command=next_card)
incorrect.grid(column=0, row=1)

next_card()

window.mainloop()