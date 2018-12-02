fileData = open("data/day2.txt","r")
lines = [x.strip() for x in fileData.readlines()]

#FIXED LENGTH
def logicalAndString(first, second):
    result = ""
    for index, letter  in enumerate(first):
        if letter == second[index]:
            result += first[index]
        else:
            result += '0'
    return result


for index, line in enumerate(lines):
    for secondLine in lines[index:]:
        andResult = logicalAndString(line, secondLine)
        if andResult.count('0') == 1:
            result = andResult.replace('0', '')
            print("RESULT: {0}".format(result))
    
