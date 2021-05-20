import turtle
turtle.speed(20)
turtle.shape('turtle')
corner = 360


def turtle_circle():
    for i in range(180):
        turtle.forward(2)
        turtle.left(2)
    for i in range(180):
        turtle.forward(2)
        turtle.right(2)


for i in range (3):
    turtle.left(corner)
    turtle_circle()
    corner /= 6
    if corner < 45:
        corner = 45

turtle.mainloop()
