import time
from typing import List

with open('input.txt') as f:
    lines: List[str] = f.read().splitlines()


start_time = time.time()
processed_sums:List[List[str]] = []
part_1_total = 0

for line in lines:
    counter = 0
    for item in line.split(' '):
        if item == '':
            continue

        if counter >= len(processed_sums):
            processed_sums.append([item])
        else:
            if item.isdigit():
                processed_sums[counter].append(item)
            else:
                processed_sums[counter].append(item)

        counter += 1

def find_sum_of_problems(sums: List[List[str]]) -> int:
    grand_total = 0
    for single_sum in sums:
        total = 0
        operator = "*"

        for value in reversed(single_sum):
            if value == "+":
                operator = "+"
                continue
            elif value == "*":
                operator = "*"
                total += 1
                continue

            if not value.isdigit():
                break

            if operator == "+":
                total += int(value)
            elif operator == "*":
                total *= int(value)

        grand_total += total

    return grand_total

print(f"{find_sum_of_problems(processed_sums)}, {time.time() - start_time}")

# Part 2
start_time = time.time()
columns: List[str] = []
for line in lines:
    for index, char in enumerate(line):
        if index >= len(columns):
            columns.append(char)
        else:
            columns[index] += char

mode: str = "+"
grand_total: int = 0
total: int = 0

for item in columns:
    if item.strip() == "":
        continue

    if '+' in item:
        grand_total += total
        mode = "+"
        total = int(item[0:-1].strip())
        continue
    elif '*' in item:
        grand_total += total
        mode = "*"
        total = int(item[0:-1].strip())
        continue

    if mode == '+':
        total += int(item.strip())
    elif mode == '*':
        total *= int(item.strip())
grand_total += total

print(f"{grand_total}, {time.time() - start_time}")
