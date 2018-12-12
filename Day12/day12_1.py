rules = { x.split()[0] : x.split()[2] for x in open("d:\\AoC2018\\Day12\\day12.txt", "r").readlines() }
initial_state = "##.......#.######.##..#...#.#.#..#...#..####..#.##...#....#...##..#..#.##.##.###.##.#.......###....#"
padding = 50
state = '.' * padding + initial_state + '.' * padding

zero_index = padding
generation = 20

for k in range(0, generation):
    next_state = ".."
    for i in range(2, len(state)):
        processing = state[i - 2 : i + 3]
        if processing in rules:
            next_state += rules[processing]
        else:
            next_state += '.'
    state = next_state

result = 0
for i, c in enumerate(state):
    if c == '#':
        result += i - padding

print(result)