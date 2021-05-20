#! /usr/bin/env python3
import turtle
import math

turtle.shape('triangle')
turtle.pensize(3)
turtle.color('red', 'black')

turtle.speed(3)
c = 240  # Длина окружности
r = c / 2 * math.pi  # Радиус окружности
d = r * 2  # Диаметр окружности
corner = (360 / 5)  # Угол пятиконечной звезды
l = (2 * r) * math.sin(corner * math.pi / 180)  # Длина хорды
david_len = 36  # Длина стороны треугольника звезды Давида


def david():
    turtle.penup()
    turtle.home()
    turtle.goto(-david_len / 2, -david_len / 2)
    turtle.pendown()
    for step in range(6):
        for i in range(3):
            turtle.forward(david_len)
            turtle.right(360 / 3)
        turtle.forward(36)
        turtle.left(360 / 6)


def star():
    turtle.left(corner)
    turtle.forward(l)
    for i in range(4):
        turtle.left(corner * 2)
        turtle.forward(l)


def circle():
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.circle(r)
    turtle.penup()
    turtle.pendown()
    turtle.end_fill()


circle()
star()
david()
turtle.hideturtle()
turtle.mainloop()
