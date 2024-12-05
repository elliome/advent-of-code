import math, time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

with open('./input.txt') as f:
    puzzle_input = f.read().splitlines()

start = time.time()

WIDTH = len(puzzle_input[0])
CHECK_STRING = "XMAS"
check_count = 0
puzzle_input = "".join(puzzle_input)

VERTICAL_STEP = WIDTH
HORIZONTAL_STEP = 1


def check_all(_index, puzzle_string, check_string=CHECK_STRING):
    count = 0
    count += check_west(_index, puzzle_string, check_string)
    count += check_east(_index, puzzle_string, check_string)
    count += check_south(_index, puzzle_string, check_string)
    count += check_north(_index, puzzle_string, check_string)
    count += check_north_west(_index, puzzle_string, check_string)
    count += check_north_east(_index, puzzle_string, check_string)
    count += check_south_west(_index, puzzle_string, check_string)
    count += check_south_east(_index, puzzle_string, check_string)

    return count

def check_crosses(_index: int, puzzle_string: str, check_string:str) -> int:
    if _index % WIDTH == 0:
        print()

    if _index < WIDTH:
        return 0

    if _index - (math.floor(_index / WIDTH) * WIDTH) == 0:
        return 0

    if _index - (math.floor(_index / WIDTH) * WIDTH) == WIDTH - 1:
        return 0

    if _index > len(puzzle_string) - WIDTH:
        return 0

    if puzzle_string[_index] != "A":
        return 0

    _char = puzzle_string[_index]

    top_left = puzzle_string[_index + (HORIZONTAL_STEP * -1) + (VERTICAL_STEP * -1)]
    top_right = puzzle_string[_index + HORIZONTAL_STEP + (VERTICAL_STEP * -1)]
    center = _char
    bottom_left = puzzle_string[_index + (HORIZONTAL_STEP * -1) + VERTICAL_STEP]
    bottom_right = puzzle_string[_index + HORIZONTAL_STEP + VERTICAL_STEP]

    top_left_to_bottom_right = top_left + center + bottom_right
    top_right_to_bottom_left = top_right + center + bottom_left

    if top_right_to_bottom_left in [check_string, check_string[::-1]] and top_left_to_bottom_right in [check_string, check_string[::-1]]:
        return 1

    return 0

def abstract_check_direction(_index, puzzle_string, end, step=None, check_string=CHECK_STRING):
    new_end = _index + end if _index + end > 0 else 0
    new_index = _index + 1 if _index % 10 == 0 and _index <= 30 else _index
    if (puzzle_string[new_index: new_end: step]) in [check_string, check_string[::-1]]:
        return 1

    return 0


def west_boundary_safe(_index: int, check_string: str) -> bool:
    x = _index - ((math.floor(_index / WIDTH)) * WIDTH)
    return x < WIDTH - (len(check_string) - 1)


def east_boundary_safe(_index:int, check_string: str):
    x = _index - ((math.floor(_index / WIDTH)) * WIDTH)
    return x > (len(check_string) - 2)


def check_west(_index, puzzle_string, check_string):
    if not west_boundary_safe(_index, check_string): return 0

    return abstract_check_direction(
        _index,
        puzzle_string,
        len(check_string),
        HORIZONTAL_STEP,
        check_string
    )


def check_east(_index, puzzle_string, check_string):
    if not east_boundary_safe(_index, check_string): return 0
    return abstract_check_direction(
        _index,
        puzzle_string,
        len(check_string) * -1,
        HORIZONTAL_STEP * -1,
        check_string
    )


def check_south(_index, puzzle_string, check_string):
    return abstract_check_direction(
        _index,
        puzzle_string,
        WIDTH * len(check_string),
        VERTICAL_STEP,
        check_string
    )


def check_north(_index, puzzle_string, check_string):
    return abstract_check_direction(
        _index,
        puzzle_string,
        (WIDTH * len(check_string)) * -1,
        VERTICAL_STEP * -1,
        check_string
    )


def check_north_west(_index, puzzle_string, check_string):
    if not west_boundary_safe(_index, check_string): return 0
    return abstract_check_direction(
        _index,
        puzzle_string,
        ((WIDTH * len(check_string)) * -1) + len(check_string),
        (VERTICAL_STEP * -1) + HORIZONTAL_STEP,
        check_string
    )


def check_north_east(_index, puzzle_string, check_string):
    if not east_boundary_safe(_index, check_string): return 0
    return abstract_check_direction(
        _index,
        puzzle_string,
        ((WIDTH * len(check_string)) * -1) + (len(check_string) * -1),
        (VERTICAL_STEP * -1) + (HORIZONTAL_STEP * -1),
        check_string
    )


def check_south_west(_index, puzzle_string, check_string):
    if not west_boundary_safe(_index, check_string): return 0
    return abstract_check_direction(
        _index,
        puzzle_string,
        (WIDTH * len(check_string)) + len(check_string),
        VERTICAL_STEP + HORIZONTAL_STEP,
        check_string
    )


def check_south_east(_index, puzzle_string, check_string):
    if not east_boundary_safe(_index, check_string): return 0
    return abstract_check_direction(
        _index,
        puzzle_string,
        (WIDTH * len(check_string)) + (len(check_string) * -1),
        VERTICAL_STEP + (HORIZONTAL_STEP * -1),
        check_string
    )

for index, char in enumerate(puzzle_input):
    if char == 'X':
        check_count += check_all(index, puzzle_input, CHECK_STRING)

pt_two_check_count = 0

for index, char in enumerate(puzzle_input):
    if char == 'A':
        pt_two_check_count += check_crosses(index, puzzle_input, "MAS")

print(check_count)
print(pt_two_check_count)
print(f"{round((time.time() - start) * 1000, 5)}ms")
