# import colorgram
# rgb_colores = []
# colores = colorgram.extract('2.jpg', 30)
# for color in colores:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     nuevo_color = (r, g, b)
#     rgb_colores.append(nuevo_color)
# print(rgb_colores)


import turtle as tom
import random

tom.colormode(255)
kame = tom.Turtle()
kame.speed("fastest")
kame.penup()
kame.hideturtle()

lista = [(232, 142, 77), (230, 65, 102), (246, 220, 81), (7, 175, 214), (161, 53, 106), (233, 77, 60), (2, 132, 168), (86, 186, 211), (232, 125, 156), (143, 211, 221), (154, 77, 55), (41, 168, 106), (117, 191, 152), (1, 153, 92), (174, 147, 60), (240, 156, 177), (179, 199, 194), (27, 84, 62), (75, 53, 85), (20, 61, 122), (36, 65, 86), (0, 109, 114), (245, 166, 153), (101, 125, 163), (175, 190, 213)]
kame.setheading(225)
kame.forward(300)
kame.setheading(0)
puntos = 100

for conteo in range(1, puntos + 1):
    kame.dot(20, random.choice(lista))
    kame.forward(50)

    if conteo % 10 == 0:
        kame.setheading(90)
        kame.forward(50)
        kame.setheading(180)
        kame.forward(500)
        kame.setheading(0)


screen = tom.Screen()
screen.exitonclick()


