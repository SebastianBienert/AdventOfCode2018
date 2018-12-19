import sys

data = [list(line.strip()) for line in open("d:\\AoC2018\\Day18\\day18.txt", "r").readlines()]
# print(data)


def get_adjacent_numbers(data, x, y):
    adjacent = list()
    if y > 0:
        adjacent.append(data[y - 1][x])
        if x > 0:
            adjacent.append(data[y-1][x-1])
        if x < len(data[y]) - 1:
            adjacent.append(data[y-1][x + 1])
    if y < len(data) - 1:
        adjacent.append(data[y + 1][x])
        if x > 0:
            adjacent.append(data[y+1][x-1])
        if x < len(data[y]) - 1:
            adjacent.append(data[y+1][x + 1])
    if x > 0:
        adjacent.append(data[y][x-1])
    if x < len(data[y]) - 1:
        adjacent.append(data[y][x + 1])

    open_ground = adjacent.count('.')
    trees = adjacent.count('|')
    lumberyard = adjacent.count('#')

    return open_ground, trees, lumberyard

def print_data(data):
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            sys.stdout.write(data[y][x])
        sys.stdout.write('\n')

# print(get_adjacent_numbers(data, 0,0))

minutes = 10000000

for m in range(0, minutes):
    # print("\n")
    copy = [row[:] for row in data]
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            op_ground, tree, lumber = get_adjacent_numbers(data, x,y)
            if copy[y][x] == '.' and tree >= 3:
                copy[y][x] = '|'
            elif copy[y][x] == "|" and lumber >= 3:
                copy[y][x] = '#'
            elif copy[y][x] == '#' and not (lumber >= 1 and tree >= 1):
                copy [y][x] = '.'
    data = copy
    # if m % 10 == 0:
    sum_open = sum(line.count('.') for line in data)
    sum_trees = sum(line.count('|') for line in data)
    sum_lumber = sum(line.count('#') for line in data)
    print("RESULT {} : {} {} {}".format(m + 1, sum_open, sum_trees, sum_lumber))
    # print_data(data)
    
# sum_open = sum(line.count('.') for line in data)
# sum_trees = sum(line.count('|') for line in data)
# sum_lumber = sum(line.count('#') for line in data)
            
# print("RESULT : {}".format(sum_trees * sum_lumber))