import re
import numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Point:
    def __init__(self, id , line):
        reg = re.search(r"^position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>$", line)
        self.x = int(reg.group(1))
        self.y = int(reg.group(2))
        self.vx = int(reg.group(3))
        self.vy = int(reg.group(4))
        self.id = id
    def __str__(self):
        return "#{4} X: {0}, Y: {1}, Vx: {2}, Vy: {3}".format(self.x, self.y, self.vx, self.vy, self.id)
    def __repr__(self):
        return "#{4} X: {0}, Y: {1}, Vx: {2}, Vy: {3}".format(self.x, self.y, self.vx, self.vy, self.id)

s = 0
def update(i, points, scat):
    speed = 300
    ys = [point.y for point in points]
    global s

    if all([abs(point.x) < 238 for point in points]):
        speed = 0.005
        print(s)
        print(max([ys.count(y) for y in ys]))
    elif all([abs(point.x) < 400 for point in points]):
        speed = 0.25
    elif any([abs(point.x) < 1000 for point in points]):
        speed = 25
        
    if max([ys.count(y) for y in ys]) > 15:
        speed = 0.001
        print(s)
    x = []
    y = []
    for point in points:
        point.x += point.vx * speed
        point.y += point.vy * speed
        x.append(point.x)
        y.append(point.y)

    s += speed
    data = numpy.stack((x,y), axis=1)
    scat.set_offsets(data)

points = [Point(i, x) for i, x in enumerate(open("day10.txt", "r").readlines())]
fig, ax = plt.subplots()
x = [point.x for point in points]
y = [point.y for point in points]
scat = ax.scatter(x, y)
animation = FuncAnimation(fig, update, frames=range(100),
fargs=(points, scat))
plt.show()