from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

def convert():
    S = float(text_box.get())
    conv = str(round(S*1.609, 3))
    converter_text.config(text=conv)

text_box = Entry()
text_box.grid(column=1, row=0)
text_box.config(width=9)

unit = Label(text="Miles")
unit.grid(column=2, row=0)

t = Label(text="is equal to")
t.grid(column=0, row=1)

converter_text = Label(text="0")
converter_text.grid(column=1, row=1)

unit2 = Label(text="Km")
unit2.grid(column=2, row=1)

button = Button(text="Calculate")
button.grid(column=1, row=2)
button.config(command= convert)

window.mainloop()