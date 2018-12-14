data = [3, 7]

first_elf_index = 0
second_elf_index = 1

def get_new_elements(x, y):
    return [int(d) for d in str(x + y)]


input = 430971

print(data, first_elf_index % len(data), second_elf_index % len(data))
while len(data) < input + 10:
    data.extend(get_new_elements(data[first_elf_index % len(data)], data[second_elf_index % len(data)]))
    first_elf_index = (first_elf_index + data[first_elf_index] + 1) % len(data)
    second_elf_index = (second_elf_index + data[second_elf_index] + 1) % len(data)
    # print(data, first_elf_index % len(data), second_elf_index % len(data))

print("".join([str(x) for x in data[input:input + 10]]))

