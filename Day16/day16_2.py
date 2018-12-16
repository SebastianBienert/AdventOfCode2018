import re

data = open("d:\\AoC2018\\Day16\\day16.txt", "r").readlines()
before = []
instructions = []
after = []

for line in data:
    if line[0] == 'B':
        reg = re.search(r"\[(.+)\]", line).group(1).split(',')
        before.append({ i: int(c.strip()) for i, c in enumerate(reg)} )
    if line[0] == 'A':
        reg = re.search(r"\[(.+)\]", line).group(1).split(',')
        after.append({ i: int(c.strip()) for i, c in enumerate(reg)} )
    if line[0].isdigit():
        reg = line.split()
        instructions.append([int(c) for c in reg])

registers = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0
}

def addr(registers, a, b, c):
    registers[c] = registers[a] + registers[b]
def addi(register, a, b, c):
    registers[c] = registers[a] + b
def mulr(registers, a, b, c):
    registers[c] = registers[a] * registers[b]
def muli(register, a, b, c):
    registers[c] = registers[a] * b
def banr(registers, a, b, c):
    registers[c] = registers[a] & registers[b]
def bani(register, a, b, c):
    registers[c] = registers[a] & b
def borr(registers, a, b, c):
    registers[c] = registers[a] | registers[b]
def bori(registers, a, b, c):
    registers[c] = registers[a] | b
def setr(registers, a, b, c):
    registers[c] = registers[a]
def seti(registers, a, b, c):
    registers[c] = a
def gtir(registers, a, b, c):
    registers[c] = 1 if a > registers[b] else 0
def gtri(registers, a, b, c):
    registers[c] = 1 if registers[a] > b else 0
def gtrr(registers, a, b, c):
    registers[c] = 1 if registers[a] > registers[b] else 0
def eqir(registers, a, b, c):
    registers[c] = 1 if a == registers[b] else 0
def eqri(registers, a, b, c):
    registers[c] = 1 if registers[a] == b else 0
def eqrr(registers, a, b, c):
    registers[c] = 1 if registers[a] == registers[b] else 0
def load_values_to_register(values):
    for x in values:
        registers[x] = values[x]
def is_dic_equal(values):
    for x in values:
        if values[x] != registers[x]:
            return False
    return True

functions = [addr, addi,
            mulr, muli,
            banr, bani,
            borr, bori,
            setr, seti,
            gtir, gtri, gtrr,
            eqir, eqri, eqrr]

counter = 0
result = 0

chose_func = ""
solved_registers = { i : set() for i, f in enumerate(functions)}
for x in range(0, len(before)):
    counter = 0
    for f in functions:
        load_values_to_register(before[x])
        f(registers, instructions[x][1], instructions[x][2], instructions[x][3])
        if is_dic_equal(after[x]):
            solved_registers[instructions[x][0]].add(f.__name__)
            chosen_func = f.__name__


##SOLVING:
solved_registers = { k : list(v) for k,v in solved_registers.items()}
result = { i : "" for i, f in enumerate(functions)}
def process_registers(result, solved_registers):
    for k, list_of_regs in solved_registers.items():
        if len(list_of_regs) == 1:
            result[k] = list_of_regs[0]
            delete_register_from_dict(list_of_regs[0], solved_registers)
            break
def delete_register_from_dict(name, registers):
    for key, value in registers.items():
        if name in value:
            value.remove(name)
def print_dict(dict):
    for k, r in dict.items():
        print("{} : {}".format(k, r))

for i in range(0, 16):
    process_registers(result, solved_registers)

## HAVE RESULTS:
second_task = []
for line in open("d:\\AoC2018\\Day16\\day16_2.txt", "r").readlines():
    if line[0].isdigit():
        reg = line.split()
        second_task.append([int(c) for c in reg])

print_dict(result)
load_values_to_register({
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0
})
for instruction in second_task:
    ins = result[instruction[0]]
    locals()[ins](registers, instruction[1], instruction[2], instruction[3])

print(registers)


    