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
for x in range(0, len(before)):
    counter = 0
    for f in functions:
        load_values_to_register(before[x])
        f(registers, instructions[x][1], instructions[x][2], instructions[x][3])
        if is_dic_equal(after[x]):
            counter += 1
    if counter >= 3:
        result += 1

print(result)



