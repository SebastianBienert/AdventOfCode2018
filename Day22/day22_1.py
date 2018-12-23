import numpy
import sys
data = [list(line.strip()) for line in open("day22.txt").readlines()]
depth = 11109
x_target = 9
y_target = 731
geologic_coords = numpy.zeros( (y_target + 1, x_target + 1) )

def get_erosion_level(x,y, geologic_coords, depth):
    return (geologic_coords[y][x] + depth) % 20183

for y in range(0, y_target + 1):
    for x in range(0, x_target + 1):
        if (x == x_target and y == y_target) or (y == 0 and x == 0):
            geologic_coords[y][x] = 0
        elif y == 0:
            geologic_coords[y][x] = x * 16807
        elif x == 0:
            geologic_coords[y][x] = y * 48271
        else:
            geologic_coords[y][x] = get_erosion_level(x - 1,y, geologic_coords, depth) * get_erosion_level(x,y - 1, geologic_coords, depth)

cave = numpy.chararray( (y_target + 1, x_target + 1), unicode = True )
result = 0
for y in range(0, y_target + 1):
    for x in range(0, x_target + 1):
        level = get_erosion_level(x,y, geologic_coords, depth)
        if level % 3 == 0:
            cave[y][x] = '.'
        elif level % 3 == 1:
            cave[y][x] = '='
            result += 1
        else:
            cave[y][x] = '|'
            result += 2


# for y in range(0, len(cave)):
#     for x in range(0, len(cave[y])):
#         sys.stdout.write(str(cave[y][x]))
#     sys.stdout.write('\n')

print(result)