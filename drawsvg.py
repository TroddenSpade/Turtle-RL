from svgpathtools import svg2paths
import numpy as np
import turtle

w, h = 1400, 1400

s = turtle.Screen()
turtle.screensize(canvwidth=w, canvheight=h, bg=None)

t = turtle.Turtle()


paths, attributes = svg2paths('output3.svg')

points = []
for pa in paths:
    for l in pa:
        p0 = [l.start.real, l.start.imag]
        p1 = [l.end.real, l.end.imag]
        points.append([p0, p1])

points = np.array(points)
points -= points.mean()
# scale = max(w/2,h/2) / max(abs(points.min()), abs(points.max()))
# points *= scale
points *= np.array([1, -1])

print(max(abs(points.min()), abs(points.max())))

for p in points:
    p0, p1 = p
    t.penup()
    t.goto(p0)
    t.pendown()
    t.goto(p1)

turtle.done()