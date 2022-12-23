import turtle
from PIL import ImageGrab

def getter(root, widget):
    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    return ImageGrab.grab().crop((x, y, x1, y1))

s = turtle.Screen()
turtle.screensize(canvwidth=None, canvheight=None, bg=None)

t = turtle.Turtle()
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

t.goto(100,100)
t.home()

t.circle(60)

t.dot(10)

turtle.done()