import turtle
def drawing_setup(pen_color,fill_color, win_color):
    win = turtle.Screen()
    turtle1 = turtle.Turtle()
    turtle1.pen(pencolor=pen_color, fillcolor=fill_color)
    win.bgcolor(win_color)
    turtle1.speed(10)