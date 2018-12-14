data = [3, 7]

first_elf_index = 0
second_elf_index = 1

def get_new_elements(x, y):
    return [int(d) for d in str(x + y)]

def find_match(data, input):
    toString = "".join([str(x) for x in data])
    return toString.find(input) != -1

input = "430971"

print(data, first_elf_index % len(data), second_elf_index % len(data))
found = False
while not found:
    data.extend(get_new_elements(data[first_elf_index % len(data)], data[second_elf_index % len(data)]))
    first_elf_index = (first_elf_index + data[first_elf_index] + 1) % len(data)
    second_elf_index = (second_elf_index + data[second_elf_index] + 1) % len(data)
    found = find_match(data[-10:], input)
    if len(data) % 1000000 == 0:
        print(len(data))

print(len(data) - len(input) - 1)

