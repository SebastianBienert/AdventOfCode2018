import re
import numpy

fileData = open("day4.txt","r")
lines = [x.strip() for x in fileData.readlines()]

def get_guard_id(line):
    return int(re.search(r"(\d+)", line).group(1))

def get_line_type(line):
    if line.startswith("Guard"):
        return "Start"
    if line.startswith("falls"):
        return "FallAsleep"
    if line.startswith("wakes"):
        return "WakeUp"

def process_line(line):
    id = 0
    reg = re.search(r"^\[(.+) (\d+):(\d+)\] (.+)$", line)
    lineType = get_line_type(reg.group(4))
    if lineType == "Start":
        id = get_guard_id(reg.group(4))
    return id, lineType, int(reg.group(3))

def fill_time_array(array, start, end):
    for index, element in enumerate(array[start:end]):
        array[start + index] += 1

guardTimes = dict()
currentGuard = 0
startSleep = 0

lines.sort()
for line in lines:
    id, lineType, time = process_line(line)
    if lineType == "Start":
        currentGuard = id
        if not currentGuard in guardTimes:
            guardTimes[currentGuard] = numpy.zeros(60)
    if lineType == "FallAsleep":
        startSleep = time
    if lineType == "WakeUp":
        fill_time_array(guardTimes[currentGuard], startSleep, time)

maxGuard = max(guardTimes, key= lambda k: numpy.amax(guardTimes[k]))        
maxMinute = numpy.argmax(guardTimes[maxGuard])
print("Guard {0}, minute: {1}, RESULT: {2}".format(maxGuard, maxMinute, maxGuard*maxMinute))