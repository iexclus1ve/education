import turtle
import math
turtle.shape('turtle')
turtle.pensize(3)
turtle.color('red', 'black')
turtle.speed(3)
c = 240
r = c / 2 * math.pi
d = r * 2
l = (2 * r) * math.sin(108 * math.pi / 180)


def david():
    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(36)
            turtle.right(360 / 3)
        turtle.end_fill()
        turtle.forward(36)
        turtle.left(360 / 6)


def star():
    turtle.penup()
    turtle.pendown()
    # turtle.begin_fill()
    turtle.left(108)
    turtle.forward(l)
    for i in range(4):
        turtle.right(144)
        turtle.forward(l)
    # turtle.end_fill()


def circle():
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.circle(r)
    turtle.penup()
    # turtle.home()
    # turtle.goto(0, r)
    turtle.pendown()
    turtle.end_fill()
circle()
star()
turtle.penup()
turtle.home()
turtle.pendown()
david()
turtle.hideturtle()
turtle.mainloop()
