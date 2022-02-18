import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
BLUE = '#008e89'
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ''
timer = None
# text='✓',


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_layout.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')

    global reps, marks
    reps = 0
    marks = ''
    check_layout.config(text=marks)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_time_break = SHORT_BREAK_MIN * 60
    long_tim_break = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        timer_layout.config(text='Work', fg=GREEN)
    elif reps % 8 != 0:
        count_down(short_time_break)
        timer_layout.config(text='Break', fg=PINK)
    else:
        count_down(long_tim_break)
        timer_layout.config(text='Break', fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        global marks
        if reps % 2 != 0:
            marks += '✓'
        check_layout.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro time')
window.config(padx=50, pady=50, bg=BLUE)

canvas = Canvas(width= 207, height=230, bg=BLUE, highlightthickness=0)
image_tomato = PhotoImage(file='tomato.png')
canvas.create_image(107, 117, image=image_tomato)
timer_text = canvas.create_text(107, 142, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=2, column=2)

timer_layout = Label(text='Timer', bg=BLUE, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
timer_layout.grid(row=1, column=2)

start_button = Button(text='Start', command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(row=3, column=3)

check_layout= Label(bg=BLUE, fg=RED, font=(25))
check_layout.grid(row=4, column=2)


window.mainloop()