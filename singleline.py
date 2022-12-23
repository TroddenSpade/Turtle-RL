import turtle
import numpy as np

NUM_MINS = 5

points = []
f = open("coords.txt", "r")
for l in f:
    arr = l.split()
    points.append([int(arr[1])-360, int(arr[2])-360])

points = np.array(points)
print(points)

idx = 0
order = [points[idx]]
while len(points) > 1:
    p = points[idx]
    points = np.delete(points, idx, 0)
    diffs = np.power(points - p, 2).sum(axis=1)
    args = np.argpartition(diffs, range(min(NUM_MINS, len(points))))
    idx = np.random.choice(args[:NUM_MINS])
    order.append(points[idx])
order.append(order[0])

s = turtle.Screen()
turtle.screensize(canvwidth=720, canvheight=720, bg=None)

t = turtle.Turtle()

for p in order:
    t.goto(p)
    t.dot()

turtle.done()