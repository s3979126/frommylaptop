import turtle
win = turtle.Screen()
turtle1 = turtle.Turtle()
turtle1.pen(pencolor="yellow", fillcolor="yellow")
win.bgcolor("red")
turtle1.speed(10)
def draw_shape(sides_long, joints):
    turtle1.penup()
    turtle1.goto(-sides_long/2, 50)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(joints):
        turtle1.forward(sides_long)
        turtle1.right(180 - 180 / joints)
    turtle1.end_fill()
    win.exitonclick()
