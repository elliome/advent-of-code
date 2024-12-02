with open('input.txt') as f:
    reports = list(map(lambda n : n.split(" "), f.read().splitlines()))


def isNumbersSafe (a, b):
    return abs(a - b) not in range (1, 4)

def isLevelsSafe (levels):
    prevLevel = -1
    direction = ""
    
    for index, level in enumerate(levels):
        if prevLevel != -1:
            if isNumbersSafe(int(level), prevLevel):
                return False, index

        if (direction == "" and prevLevel != -1):
            if int(level) > prevLevel:
                direction = 'asc'
            else:
                direction = 'desc'
        
        if (direction == 'asc'):
            if int(level) < prevLevel:
                return False, index
        elif (direction == 'desc'):
            if int(level) > prevLevel:
                return False, index

        prevLevel = int(level)
    
    return True, -1

# Part 1

safeReportCount = 0

for report in reports:
    if isLevelsSafe(report)[0]:
        safeReportCount += 1

print(safeReportCount)

# Part 2 

safeReportCount = 0

for report in reports:
    isSafe, unsafeIndex = isLevelsSafe(report)
    if isSafe:
        safeReportCount += 1
    else:
        for i in range(len(report)):
            tempReport = report[:]
            tempReport.pop(i)
            if (isLevelsSafe(tempReport)[0]):
                safeReportCount += 1
                break
    

print(safeReportCount)