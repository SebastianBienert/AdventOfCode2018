
from collections import Counter
rules = { x.split()[0] : x.split()[2] for x in open("d:\\AoC2018\\Day12\\day12.txt", "r").readlines() }
initial_state = "##.......#.######.##..#...#.#.#..#...#..####..#.##...#....#...##..#..#.##.##.###.##.#.......###....#"
padding = 700
state = '.' * padding + initial_state + '.' * padding

zero_index = padding
generation = 300

def calculateResult(state):
    result = 0
    for i, c in enumerate(state):
        if c == '#':
            result += i - padding
    return result

result = list()
for k in range(0, generation):
    next_state = ".."
    for i in range(2, len(state)):
        processing = state[i - 2 : i + 3]
        if processing in rules:
            next_state += rules[processing]
        else:
            next_state += '.'
    state = next_state
    result.append((k, calculateResult(state)))

print(result)
diffs = list()
for i, r in enumerate(result):
    if i != 0:
        diffs.append(result[i][1] - result[i - 1][1])

print(Counter(result))
print(Counter(diffs))

print("RESULT: ", (result[100][1]) + 40 * (50000000000 - 101) )