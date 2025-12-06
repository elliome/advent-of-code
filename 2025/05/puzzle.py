import time
from typing import List, Dict

with open('input.txt') as f:
    lines: List[str] = f.read().splitlines()

start_time: float = time.time()
valid_id_ranges: List[tuple[int, int]] = []
ids_end_index = 0
part_1_count = 0


def is_id_valid(id_number: int) -> int:
    for low, high in valid_id_ranges:
        if low <= id_number <= high:
            return 1

    return 0


for i, line in enumerate(lines):
    if line == "":
        ids_end_index = i
        break
    start, end = line.split('-')

    valid_id_ranges.append((int(start), int(end)))

for i in range(ids_end_index + 1, len(lines)):
    part_1_count += is_id_valid(int(lines[i]))

print(f"Part 1: {part_1_count} {time.time() - start_time}s")
start_time = time.time()

has_changed = True
while has_changed:
    has_changed = False
    for index_1, valid_id_range in enumerate(valid_id_ranges):
        start, end = valid_id_range
        for index_2, second_valid_id_range in enumerate(valid_id_ranges):
            if valid_id_range == second_valid_id_range:
                continue

            second_start, second_end = second_valid_id_range

            if start <= second_start <= end <= second_end:
                valid_id_ranges[index_1] = (start, second_end)
                valid_id_ranges.remove(second_valid_id_range)
                has_changed = True
                break
            elif end >= second_end >= start >= second_start:
                valid_id_ranges[index_1] = (second_start, end)
                valid_id_ranges.remove(second_valid_id_range)
                has_changed = True
                break
            elif second_start >= start and second_end <= end:
                valid_id_ranges.remove(second_valid_id_range)
                has_changed = True
                break

        if has_changed:
            break

count = 0

valid_id_ranges = list(set(valid_id_ranges))
for start, end in valid_id_ranges:
    count += (end + 1) - start

print(f"Part 2: {count} {time.time() - start_time}s")

