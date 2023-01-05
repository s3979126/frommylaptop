import turtle

def drawing_setup(pen_color,fill_color, win_color):
    win = turtle.Screen()
    turtle1 = turtle.Turtle()
    turtle1.pen(pencolor=pen_color, fillcolor=fill_color)
    win.bgcolor(win_color)
    turtle1.speed(10)
def draw_shape(sides_long, joints):
    drawing_setup("red", "blue", "blue")
    turtle1.penup()
    turtle1.goto(-sides_long/2, 50)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(joints):
        turtle1.forward(sides_long)
        turtle1.right(180 - 180 / joints)
    turtle1.end_fill()
    win.exitonclick()
draw_shape(500,5)
