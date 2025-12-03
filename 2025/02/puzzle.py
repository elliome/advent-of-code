import time
from typing import List

start_time = time.time()
with open('input.txt') as f:
    lines:List[str] = f.read().split(',')

sum_part_1:int = 0
sum_part_2:int = 0

def find_part_2_matches(input:int) -> int :
    input_string = str(input)
    length = len(str(input_string))
    half_length = int(length / 2) + 1

    for i in range(1, half_length):
        first_part = input_string[:i]
        matches = True
        for j in range(i, length, i):
            if input_string[j: j+i] != first_part:
                matches = False
                break

        if matches:
            return input

    return 0

for line in lines:
    start, end = line.split('-')
    for i in range(int(start), int(end) + 1):
        sum_part_2 += find_part_2_matches(i)
        num:str = str(i)
        line_length:int = len(num)
        if line_length % 2 == 0:
            if num[0:line_length//2] == num[line_length//2:]:
                sum_part_1 += int(num)

print(f"Part 1: {sum_part_1}")
print(f"Part 2: {sum_part_2}")
print(f"Time: {round((time.time() - start_time), 4)}s")

