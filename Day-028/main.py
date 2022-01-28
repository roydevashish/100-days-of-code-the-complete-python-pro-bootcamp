import math
import tkinter

# Constant
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Reset Timer
def Reset():
    WindowApp.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# Start Timer
def StartTimer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        Count(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        Count(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        Count(work_sec)
        title_label.config(text="Work", fg=GREEN)

# Countdown
def Count(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = WindowApp.after(1000, Count, count - 1)
    else:
        StartTimer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            mark += "O"
        check_mark.config(text=marks)

# UI Setup
WindowApp = tkinter.Tk()
WindowApp.title("Pomodoro")
WindowApp.config(padx=100, pady=50, bg=YELLOW)

title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=1)

tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=StartTimer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=Reset)
reset_button.grid(row=2, column=2)

check_mark = tkinter.Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

WindowApp.mainloop()