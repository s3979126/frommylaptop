import turtle
win = turtle.Screen()
win.bgcolor("navy blue")
tito = turtle.Turtle()
tess = turtle.Turtle()

tess.forward(900)
tito.color("red")
tito.pensize(9)
t=30
win2 = turtle.Screen()
win2.bgcolor("crimson")
for i in range(314):
    tito.forward(15)
    tito.left(t)

win2.exitonclick()
win.exitonclick()