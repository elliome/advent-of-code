import math, time

with open('./input.txt') as f:
    input = f.read().splitlines()

start = time.time()

WIDTH = len(input[0])
CHECK_STRING = "XMAS"
check_count = 0
input = "".join(input)

VERTICAL_END = (WIDTH * len(CHECK_STRING))
HORIZONTAL_END = len(CHECK_STRING)

VERTICAL_STEP = WIDTH
HORIZONTAL_STEP = 1

SOUTH_END = VERTICAL_END
NORTH_END = VERTICAL_END * -1
WEST_END = HORIZONTAL_END
EAST_END = HORIZONTAL_END * -1

SOUTH_STEP = VERTICAL_STEP
NORTH_STEP = VERTICAL_STEP * -1
WEST_STEP = HORIZONTAL_STEP
EAST_STEP = HORIZONTAL_STEP * -1

def checkAll (index, string):
    count = 0
    count += checkWest(index, string)
    count += checkEast(index, string)
    count += checkSouth(index, string)
    count += checkNorth(index, string)
    count += checkNorthWest(index, string)
    count += checkNorthEast(index, string)
    count += checkSouthWest(index, string)
    count += checkSouthEast(index, string)

    return count

def abstractCheckDirection (index, string, end, step = None):
    new_end = index + end if index + end > 0 else 0
    new_index = index + 1 if index % 10 == 0 and index <= 30 else index
    if (string[new_index : new_end : step]) == CHECK_STRING:
        return 1
    
    return 0

def westBoundrySafe (index):
    x = index - ((math.floor(index / WIDTH)) * WIDTH)
    return x < WIDTH - 3

def eastBoundrySafe (index):
    x = index - ((math.floor(index / WIDTH)) * WIDTH)
    return x > 2

def checkWest (index, string):
    if not westBoundrySafe(index): return 0

    return abstractCheckDirection(index, string, WEST_END, WEST_STEP)

def checkEast (index, string):
    if not eastBoundrySafe(index): return 0
    return abstractCheckDirection(index, string, EAST_END, EAST_STEP)

def checkSouth (index, string):
    return abstractCheckDirection(index, string, SOUTH_END, SOUTH_STEP)

def checkNorth (index, string):
    return abstractCheckDirection(index, string, NORTH_END, NORTH_STEP)

def checkNorthWest (index, string):
    if not westBoundrySafe(index): return 0
    return abstractCheckDirection(index, string, NORTH_END + WEST_END, NORTH_STEP + WEST_STEP)

def checkNorthEast (index, string):
    if not eastBoundrySafe(index): return 0
    return abstractCheckDirection(index, string, NORTH_END + EAST_END, NORTH_STEP + EAST_STEP)

def checkSouthWest (index, string):
    if not westBoundrySafe(index): return 0
    return abstractCheckDirection(index, string, SOUTH_END + WEST_END, SOUTH_STEP + WEST_STEP)

def checkSouthEast (index, string):
    if not eastBoundrySafe(index): return 0
    return abstractCheckDirection(index, string, SOUTH_END + EAST_END, SOUTH_STEP + EAST_STEP)

for index, char in enumerate(input):
    check_count += checkAll(index, input)

print()
print(check_count)
print(f"{round((time.time() - start) * 1000, 5)}ms")