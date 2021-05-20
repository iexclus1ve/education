import turtle
turtle.shape('turtle')
turtle.speed(20)


def spider():
    corner = (int(360 / 12))
    for i in range(12):
        turtle.right(corner)
        turtle.forward(150)
        turtle.stamp()
        turtle.home()
        corner += int(360 / 12)



def spiral():
    step = 0.01
    while True:
        turtle.left(3.6)
        turtle.forward(step)
        step += 0.01


spiral()
turtle.mainloop()