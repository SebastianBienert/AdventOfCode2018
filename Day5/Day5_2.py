
data = open("day5.txt", "r").readline()

def is_same_letter_pair(first, second):
    return abs(ord(first) - ord(second)) == 32


def remove_adjacent(data):
    for (index, letter) in enumerate(data):
        if index == len(data) - 1:
            return False, data
        if is_same_letter_pair(letter, data[index + 1]):
            return True, data[: index] + data[index + 2:]
    
    
def process_input(letter, data):
    iter = 0
    changes = True
    output = data.replace(letter,'').replace(letter.upper(),'')
    while(changes):
        changes, output = remove_adjacent(output)
        if iter % 10000 == 0:
            print(len(output))
        iter += 1
    return len(output)
    

dic = dict()   
for letter in [chr(l) for l in range(97, 97 + 26)]:
    output = process_input(letter, data)
    print("LETTER: {0}, result: {1}".format(letter, output))
    dic[letter] = output

max_key = max(dic, key=lambda k: dic[k])
print(dic[max_key])