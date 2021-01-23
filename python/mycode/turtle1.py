import turtle
x, y = 2, 2
turtle.shape('turtle')
turtle.speed(1000)
turtle.left(90)
for i in range(3):
    for i in range(180):
        turtle.forward(x)
        turtle.left(y)
    for i in range(180):
        turtle.forward(x)
        turtle.right(y)
    x += 0.2
