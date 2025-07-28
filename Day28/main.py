import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TEXT_MARK = "✅" 
reps = 0
timer = None 

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    window.after_cancel(timer) 
    reps = 0 
    canvas.itemconfig(timer_text, text="00:00") 
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="") 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1 

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0: 
        count = long_break_sec
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0: 
        count = short_break_sec
        timer_label.config(text="Short Break", fg=PINK)
    else: 
        count = work_sec
        timer_label.config(text="Work", fg=GREEN)

    count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, reps

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer() 

        if reps % 2 == 0:
            marks = ""
            work_sessions_completed = math.floor(reps / 2)
            for _ in range(work_sessions_completed):
                marks += TEXT_MARK
            check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Project")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0, columnspan=2)

tomato_image = tkinter.PhotoImage(file="tomato.png") 
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) 
canvas.grid(column=1, row=1, columnspan=2)

# Start Button
start_btn = tkinter.Button(text="Start", bg="#fff", fg="#000", font=(FONT_NAME, 10), highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2) 

# Reset Button
reset_btn = tkinter.Button(text="Reset", bg="#fff", fg="#000", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2) 

# Check Mark Label
check_mark = tkinter.Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15)) 
check_mark.grid(column=1, row=3, columnspan=2) 

window.mainloop()