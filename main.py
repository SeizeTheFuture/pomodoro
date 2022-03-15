import tkinter as tk

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def count_down(count):
    count_min = (count // 60)
    count_sec = (count % 60)
    global timer
    if len(str(count_sec)) >= 2:
        pass
    else:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        count -= 1
        timer = window.after(1000, count_down, count)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.configure(text=marks, fg="green", bg="yellow")
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        timer_label.configure(text = "Break", fg = "pink")
        if reps % 8 == 0:
            count_down(long_break_sec)
        else:
            count_down(short_break_sec)
    else:
        timer_label.configure(text = "Work", fg= "green")
        count_down(work_sec)

def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.configure(text="Timer", fg="green")
    marks=""
    check_marks.configure(text=marks, fg="green", bg="yellow")
    reps = 0

window = tk.Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg="yellow")

canvas = tk.Canvas(width=200, height=224, bg="yellow", highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("verdana", 35, "bold"))
canvas.grid(column=2, row=2)
timer_label = tk.Label(window, text="Timer", font=("courier", 50), fg="green", bg="yellow")
start_button = tk.Button(text="Start", command=start_timer)
reset_button = tk.Button(text="Reset", command=reset)
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)
timer_label.grid(column=2, row=0)
check_marks = tk.Label(text="",fg="green", bg="yellow")
check_marks.grid(column=2, row=4)

window.mainloop()
