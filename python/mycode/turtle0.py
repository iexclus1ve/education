import turtle
turtle.shape('turtle')
turtle.pensize(3)
turtle.color('red', 'black')
# turtle.speed(20)


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
    turtle.goto(-24, 0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(72)
    turtle.forward(144)
    for i in range(4):
        turtle.right(144)
        turtle.forward(144)
    turtle.end_fill()


david()
star()
turtle.hideturtle()
turtle.mainloop()
