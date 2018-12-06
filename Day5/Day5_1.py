
data = open("day5.txt", "r").readline()

def is_same_letter_pair(first, second):
    return abs(ord(first) - ord(second)) == 32


def remove_adjacent(data):
    for (index, letter) in enumerate(data):
        if index == len(data) - 1:
            return False, data
        if is_same_letter_pair(letter, data[index + 1]):
            return True, data[: index] + data[index + 2:]
    
    
changes = True
output = data
iter = 0
print(len(output))
while(changes):
    changes, output = remove_adjacent(output)
    if iter % 1000 == 0:
        print(len(output))
    iter += 1
print(len(output))