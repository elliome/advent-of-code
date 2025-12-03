import time
from typing import List

with open('input.txt') as f:
    lines: List[str] = f.read().splitlines()

start_time:float = time.time()
start_time_total:float = time.time()

part_1_sum:int = 0
part_2_sum:int = 0

for line in lines:
    highest:int = -1
    second_highest:int = -1

    for index,char in enumerate(line):
        num:int = int(char)

        if num > highest and index != len(line)-1:
            highest = num
            second_highest = -1
        elif num > second_highest:
            second_highest = num

    part_1_sum+= int(f"{highest}{second_highest}")

print(f"Part 1 {part_1_sum}")
print(time.time()-start_time)
start_time = time.time()

for line in lines:
    digits:List[int] = []
    for char in line:
        digits.append(int(char))

    position = 0
    while len(digits) > 12:
        if digits[position] < digits[position + 1]:
            digits.remove(digits[position])
            position = 0
            continue

        position += 1

        if position == len(digits) - 1:
            digits = digits[:12]
            break

    part_2_sum += int("".join(map(str, digits)))


print(f"Part 2 {part_2_sum}")
print(time.time()-start_time)
print(time.time()-start_time_total)