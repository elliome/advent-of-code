import time
from math import floor
from typing import List

with open('input.txt') as f:
    lines: List[str] = f.read().splitlines()

start_time = time.time()

lock_position: int = 50
times_unlocked_part_1: int = 0
times_unlocked_part_2: int = 0

for line in lines:
    direction = line[0]
    amount = int(line[1:])

    if amount >= 100:
        turns = floor(amount / 100)
        times_unlocked_part_2 += turns
        amount -= turns * 100

    if direction == "R":
        if lock_position + amount >= 100:
            if lock_position != 0 and lock_position + amount != 100:
                times_unlocked_part_2 += 1
            lock_position -= 100
        lock_position += amount
    else:
        if lock_position - amount < 0:
            if lock_position != 0 and lock_position - amount != 0:
                times_unlocked_part_2 += 1
            lock_position += 100
        lock_position -= amount

    if lock_position == 0:
        times_unlocked_part_1 += 1
        times_unlocked_part_2 += 1


print(f"Part 1: {times_unlocked_part_1}")
print(f"Part 2: {times_unlocked_part_2} {round((time.time() - start_time), 6)}")