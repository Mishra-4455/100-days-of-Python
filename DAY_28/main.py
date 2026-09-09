from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00") 
    lable.config(text= "Timer")
    tick.config(text= "")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    REPS += 1

    if REPS % 8 == 0:
        lable.config(text=" BREAK ", fg=RED)
        countdown(long_break_sec)
    elif REPS % 2 == 0:
        lable.config(text="BREAK", fg=PINK)
        countdown(short_break_sec)
    else:
        lable.config(text="WORK", fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    count_mins = count // 60
    count_secs = count % 60
    if(count_secs < 10):
        count_secs = f"0{count_secs}"
    if(count_mins < 10):
        count_mins = f"0{count_mins}"
        
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count>0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(REPS//2):
            mark += "✔"
        tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 26, "bold"), fill="white")
canvas.grid(column=1, row=1)

lable = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 60), padx=10, pady=10, bg=YELLOW, highlightthickness=0)
lable.grid(column= 1, row=0)

start = Button(text="Start", width=3)
start.grid(column=0, row=2)
start.config(command= start_timer)

reset = Button(text="Reset", width=3)
reset.grid(column=2, row=2)
reset.config(command= reset_timer)

tick = Label(fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW, highlightthickness=0)
tick.grid(column=1, row=3)

window.mainloop()