import numpy
import re

def processLine(line):
    reg = re.search(r'(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
    return (int(reg.group(1)), int(reg.group(2))
    , int(reg.group(3)), int(reg.group(4)), int(reg.group(5)))

def incrementMarixSlice(x, y, width, height):
    for xCord in range(x, x + width):
        for yCord in range(y, y + height):
            fabric[xCord, yCord] += 1


fileData = open("day3.txt","r")
lines = [x.strip() for x in fileData.readlines()]

fabric = numpy.zeros((1000, 1000))

for line in lines:
    id, x, y, width, height = processLine(line)
    incrementMarixSlice(x, y, width, height)
    # print(id, x, y, width, height)

result = numpy.count_nonzero(fabric >= 2)
print("Result: {0}".format(result))
