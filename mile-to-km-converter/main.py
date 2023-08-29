import tkinter


def main():
    window = tkinter.Tk()
    window.title("Mile to Km Converter")
    window.minsize(width=300, height=100)
    window.config(padx=20, pady=20)

    miles_input = tkinter.Entry(width=10)
    miles_input.grid(row=0, column=1)

    miles_label = tkinter.Label(text="Miles")
    miles_label.grid(row=0, column=2)
    miles_label.config(padx=10)

    is_equal_label = tkinter.Label(text="Is equal to")
    is_equal_label.grid(row=1, column=0)

    kilometer_result_label = tkinter.Label(text="0")
    kilometer_result_label.grid(row=1, column=1)

    kilometer_label = tkinter.Label(text="Km")
    kilometer_label.grid(row=1, column=2)

    calculate_button = tkinter.Button(text="Calculate",
                                      command=lambda: kilometer_result_label.config(
                                          text=str(round(int(miles_input.get()) * 1.60934))))
    calculate_button.grid(row=2, column=1)

    window.mainloop()


if __name__ == '__main__':
    main()
