import turtle
turtle.shape('turtle')
turtle.pensize(3)
turtle.color('purple', 'green')
# turtle.speed(20)


def david():
    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(50)
            turtle.right(360 / 3)
        turtle.end_fill()
        turtle.forward(50)
        turtle.left(360 / 6)


david()
turtle.hideturtle()
turtle.mainloop()
