import numpy
grid = numpy.zeros((301,301))

def calculatePowerLevel(x, y, grid_serial_number):
    rackID = x + 10
    xd = (((rackID * y + grid_serial_number) ) * rackID // 100 ) % 10
    return xd - 5

def calculateTotalPower(x,y, grid):
    s = 0
    if x + 2 >= 300 or y + 2 >= 300:
        return 0
    for fx in range(x, x+3):
        for fy in range(y, y+3):
            s += grid[fx,fy]
    return s

for x in range(1, 301):
    for y in range(1, 301):
        grid[x,y] = calculatePowerLevel(x,y, 18)

result = 0
rx = 0
ry = 0
for x in range(1, 301):
    for y in range(1, 301):
        current = calculateTotalPower(x,y, grid)
        if current > result:
            result = current
            rx = x
            ry = y

print(result, rx, ry)