import numpy

size = 300
grid = numpy.zeros((size + 1,size + 1, size + 1))

def calculatePowerLevel(x, y, grid_serial_number):
    rackID = x + 10
    xd = (((rackID * y + grid_serial_number) ) * rackID // 100 ) % 10
    return xd - 5

def fillGrid(grid):
    for x in range(1, size + 1):
        print(x)
        for y in range(1, size + 1):
            for z in range(1, size + 1):
                if (x + z) < size + 1 and x < size and (y + z) < size + 1:
                    horizontal = grid[x + z, y : (y + z + 1),0]
                    vertical = grid[x: x + z, y + z,0]
                    grid[x,y,z] = grid[x,y, z - 1] + sum(horizontal) + sum(vertical)
                else:
                    break

for x in range(1, size + 1):
    for y in range(1, size + 1):
        grid[x,y,0] = calculatePowerLevel(x,y, 1723)

fillGrid(grid)
index = numpy.argmax(grid)
result = numpy.unravel_index(index, (size + 1, size + 1, size + 1))
print("REUSLT: {0},{1},{2}", result[0], result[1], result[2] + 1)
