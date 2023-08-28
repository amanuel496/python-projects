import turtle
import pandas as pd

ALIGNMENT = "center"
FONT = ('Courier', 10, 'normal')


def main():
    state_name = turtle.Turtle()
    state_name.up()
    state_name.shape("square")
    state_name.shapesize(stretch_wid=1, stretch_len=4)
    state_name.pencolor("black")
    state_name.fillcolor("white")
    screen = turtle.Screen()
    screen.title("U.S States Game")
    img = "blank_states_img.gif"
    screen.addshape(img)
    turtle.shape(img)
    data = pd.read_csv("50_states.csv")

    state = data["state"].to_list()
    x_point = data["x"].to_list()
    y_point = data["y"].to_list()

    map_dict = {}
    for i in range(50):
        map_dict[state[i]] = (x_point[i], y_point[i])

    user_input = screen.textinput("Guess the State", "What's another state's name?").title()
    score = 0
    while True:
        if user_input in map_dict:
            screen.tracer(0)
            state_name.goto(map_dict[user_input])
            state_name.write(user_input, True, ALIGNMENT, FONT)
            state_name.hideturtle()
            screen.update()
            score += 1
            if score == 50:
                break

        user_input = screen.textinput(f"{score}/50 States Correct", "What's another state's name?").title()

    screen.mainloop()


if __name__ == "__main__":
    main()
