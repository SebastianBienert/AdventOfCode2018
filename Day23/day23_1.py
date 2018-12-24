import re

data = [ line for line in open("d:\\AoC2018\\Day23\\day23.txt", "r").readlines()]
nanobots = []
for line in data:
    reg = re.search(r"^pos=<([\d,-]+)>, r=(\d+)$", line)
    coords = [int(cord) for cord in reg.group(1).split(',')]
    print(coords)
    nanobots.append( (coords, int(reg.group(2))))

def manattan_distance(first, second):
    return abs(first[0] - second[0]) + abs(first[1] - second[1]) + abs(first[2] - second[2])

maximum = max(nanobots, key=lambda k: k[1])

counter = 0
for bot in nanobots:
    if manattan_distance(bot[0], maximum[0]) <= maximum[1]:
        counter += 1

print(counter)