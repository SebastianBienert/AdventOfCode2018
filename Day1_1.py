fileData = open("data/day1.txt","r")

sum = 0
for line in [x.strip() for x in fileData.readlines()]:
    if line[0] == '+':
        sum += int(line[1:])
    else:
        sum -= int(line[1:])

print(sum)

