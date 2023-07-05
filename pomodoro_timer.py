from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_set = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    screen.after_cancel(timer_set)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    timer_check.config(text=" ")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    work_min = int(entry.get()) * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break)
        timer.config(text="Break", fg=PINK)

    else:
        count_down(work_min)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    minutes = str(count_min)
    count_sec = int(count % 60)
    if len(minutes) == 1:
        minutes = f"0{minutes}"
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{count_sec}")
    if count > 0:
        global timer_set
        timer_set = screen.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            timer_check.config(text="✅")
        else:
            timer_check.config(text=" ")


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro Timer")
screen.minsize(width=310, height=300)
screen.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 108, image=tomato_img)
timer_text = canvas.create_text(100, 128, text="00:00", font=(FONT_NAME, 32, "bold"), fill="White")
canvas.grid(row=1, column=1)

entry = Entry(width=10, bg="white", highlightthickness=0, fg="black")
entry.insert(END, string="Enter Time")
entry.focus()
entry.grid(row=4, column=1)

timer = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer.grid(row=0, column=1)
timer.config(pady=15)

start = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)
start.config(pady=-10, padx=-8)


reset = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)
reset.config(pady=-10, padx=-8)

timer_check = Label(text=" ", bg=YELLOW, fg="black", font=30)
timer_check.grid(row=2, column=1)

screen.mainloop()
