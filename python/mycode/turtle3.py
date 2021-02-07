import turtle
turtle.speed(10)


def eternity(x, y):
    for i in range(180):
        turtle.forward(x)
        turtle.left(y)
    for i in range(180):
        turtle.forward(x)
        turtle.right(y)


turtle.left(90)
d = 2
for eternity_count in range(10):
    eternity(d, 2)
    d += 0.2
turtle.mainloop()
