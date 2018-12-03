fileData = open("day2.txt","r")
lines = [x.strip() for x in fileData.readlines()]

def process_line(line):
    twoLettersFlag = 0
    threeLettersFlag = 0
    for letter in line:
        if twoLettersFlag == 0 and line.count(letter) == 2:
            twoLettersFlag = 1
        if threeLettersFlag == 0 and line.count(letter) == 3:
            threeLettersFlag = 1

    return twoLettersFlag, threeLettersFlag
        
twoLettersCount = 0
threeLettersCount = 0

for line in lines:
    (twoLetters, threeLetters) = process_line(line)
    twoLettersCount += twoLetters
    threeLettersCount += threeLetters

print("TWO: {0}, THREE: {1}, RESULT: {2}".format(twoLettersCount, threeLettersCount, twoLettersCount*threeLettersCount))

