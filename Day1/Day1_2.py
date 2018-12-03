fileData = open("day1.txt","r")
lines = [x.strip() for x in fileData.readlines()]

def processLine(line, currentSum):
    if line[0] == '+':
        currentSum += int(line[1:])
    else:
        currentSum -= int(line[1:])
    return currentSum

iter = 0
sum = 0
seenFrequences = set([sum])

while True:
    sum = processLine(lines[iter % len(lines)], sum)
    if sum in seenFrequences:
        print("RESULT: {0}".format(sum))
        break
    else:
        seenFrequences.add(sum)
    iter += 1


