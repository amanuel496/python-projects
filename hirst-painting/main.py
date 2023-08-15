import colorgram
import random
import turtle as t


def extract_colors():
    colors_list = colorgram.extract('image.jpg', 2**32)  # Not sure how many colors are there so
                                                            # gave a large number to include all of them
    color_palette = []
    for item in colors_list:
        r = item.rgb.r
        g = item.rgb.g
        b = item.rgb.b
        rgb = (r, g, b)
        color_palette.append(rgb)

    return color_palette


def remove_unwanted_colors(colors_list, size_to_remove):
    for i in range(size_to_remove):
        del colors_list[i]
    updated_color_list = colors_list

    return updated_color_list


def draw_painting(pen):
    pen.up()
    pen.setposition((-190, -210))  # Set the starting position
    pen.down()
    for i in range(1, 11):
        if i % 2 != 0 and i != 1:
            pen.setheading(90)
            pen.up()
            pen.forward(50)
            pen.setheading(0)
            pen.down()
        elif i % 2 == 0 and i != 1:
            pen.setheading(90)
            pen.up()
            pen.forward(50)
            pen.setheading(180)
            pen.down()
        for j in range(1, 10):
            pen.dot(20, (colors[random.randint(0, 33)]))
            pen.up()
            pen.forward(50)
            pen.down()
            pen.dot(20, (colors[random.randint(0, 33)]))


colors = remove_unwanted_colors(extract_colors(), 4)  # Remove the first 4 colors since they're close to white

t.colormode(255)  # Default colormode is set to 0
tim = t.Turtle()

draw_painting(tim)
t.Screen().exitonclick()
