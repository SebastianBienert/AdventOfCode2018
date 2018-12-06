import numpy
import sys

lines = open("day6.txt", "r").readlines()
points = { index+1 : ( int(line.split(',')[0].strip()), int(line.split(',')[1].strip()) ) for (index,line) in enumerate(lines) }

def manhattan_distance(first, second):
    return abs(first[0] - second[0]) + abs(first[1] - second[1])

def init_plane(plane, points):
        for x in range(0, plane.shape[0]):
                for y in range(0, plane.shape[1]):
                        if sum([manhattan_distance((y,x), point) for index, point in points.items()]) < 10000:
                            plane[x,y] = 1

maxY = points[int(max(points, key=lambda k: points[k][1]))][1]
maxX = points[int(max(points, key=lambda k: points[k][0]))][0]
plane = numpy.zeros((maxY + 1, maxX + 1), dtype=numpy.int8)
init_plane(plane, points)
print("RESULT: ", numpy.count_nonzero(plane == 1))
