import math
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
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


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer(window, timer_text, canvas, title_label, check_mark_label):
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def on_start_click(window, timer_text, canvas, title_label, check_mark_label):
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(window, timer_text, title_label, canvas, work_sec, check_mark_label)
        title_label.config(text="Work", fg=GREEN)
    elif reps % 8 != 0:
        count_down(window, timer_text, title_label, canvas, short_break_sec, check_mark_label)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(window, timer_text, title_label, canvas, long_break_sec, check_mark_label)
        title_label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(window, timer_text, title_label, canvas, count, check_mark_label):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, window, timer_text, title_label, canvas, count - 1, check_mark_label)
    else:
        on_start_click(window, timer_text, canvas, title_label, check_mark_label)
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
def main():
    window = tkinter.Tk("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
    title_label.grid(row=0, column=1)

    check_mark_label = tkinter.Label(text="", fg=GREEN, bg=YELLOW)
    check_mark_label.grid(row=3, column=1)

    start_button = tkinter.Button(text="Start", command=lambda: on_start_click(window, timer_text, canvas, title_label,
                                                                               check_mark_label))
    start_button.grid(row=2, column=0)

    reset_button = tkinter.Button(text="Reset", command=lambda: reset_timer(window, timer_text, canvas, title_label,
                                                                            check_mark_label))
    reset_button.grid(row=2, column=2)

    tomato_img = tkinter.PhotoImage(file="tomato.png")

    canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(row=1, column=1)

    window.mainloop()


if __name__ == "__main__":
    main()
