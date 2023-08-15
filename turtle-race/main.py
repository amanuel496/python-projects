from turtle import Turtle, Screen
from random import randint


def create_list_of_turtle():
    turtles = []
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(6):
        turtles.append(Turtle(shape="turtle"))
        turtles[i].color(colors[i])

    return turtles


def align_turtles(turtles_list):
    initial_x = -230
    initial_y = -100
    turtles_list[0]. penup()
    turtles_list[0].goto(x=initial_x, y=initial_y)

    for _ in range(1, 6):
        turtles_list[_].penup()
        turtles_list[_].goto(initial_x, y=-100 + 40 * _)


def main():

    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    list_of_turtles = create_list_of_turtle()

    align_turtles(list_of_turtles)

    is_game_on = True
    while is_game_on:
        for turtle in list_of_turtles:
            distance = randint(0, 10)
            turtle.forward(distance)
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                    is_game_on = False
                    break
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                    is_game_on = False
                    break

    screen.exitonclick()


main()
