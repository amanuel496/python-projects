#import colorgram
import random
import turtle as t

# colors_list = colorgram.extract('image.jpg', 2**32)
#
# number_of_colors = len(colors_list)
# print(number_of_colors)
# color_palette = []
# for item in colors_list:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     rgb = (r, g, b)
#     color_palette.append(rgb)
#
# print(color_palette)
t.colormode(255)
colors = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34), (11, 97, 52), (169, 181, 232), (241, 169, 155), (252, 7, 40), (10, 84, 100), (63, 98, 8), (14, 51, 250), (250, 11, 8)]
print(len(colors))
# 10 x 10
# Dot size 20
# Distance 50
tim = t.Turtle()
screen = t.Screen()
tim.up()
tim.setposition((-190, -210))
tim.down()
for i in range(1, 11):
    if i%2 != 0 and i != 1:
        tim.setheading(90)
        tim.up()
        tim.forward(50)
        tim.setheading(0)
        tim.down()
    elif i%2 == 0 and i != 1:
        tim.setheading(90)
        tim.up()
        tim.forward(50)
        tim.setheading(180)
        tim.down()
    for j in range(1, 10):
        tim.dot(20, (colors[random.randint(0,33)]))
        tim.up()
        tim.forward(50)
        tim.down()
        tim.dot(20, (colors[random.randint(0,33)]))
screen.exitonclick()
