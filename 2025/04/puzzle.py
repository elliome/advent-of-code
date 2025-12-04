import time
from typing import List, Dict

with open('input.txt') as f:
    lines: List[str] = f.read().splitlines()

start_time:float = time.time()
grid:Dict[tuple[int,int], int] = {}
part_1_sum:int = 0
part_2_sum:int = 0

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid[x,y] = 1 if char == '@' else 0


for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == ".":
            continue

        neighbours: List[int] = []

        for relative_x in range(x + -1,  x + 2):
            for relative_y in range(y + -1,  y + 2):
                if (relative_x,relative_y) in grid:
                    neighbours.append(grid[relative_x,relative_y])

        if sum(neighbours) - 1 < 4:
            part_1_sum += 1

print(f"Part 1 {part_1_sum} in {time.time()-start_time} seconds")
start_time = time.time()

has_removed_one:bool = True
while has_removed_one:
    has_removed_one = False
    inp = list(grid.values())
    for i, char in enumerate(inp):
        y = i // len(lines[0])
        x = i - y * len(lines[0])

        if char == 0:
            continue

        neighbour_count:int = 0

        for relative_x in range(x + -1,  x + 2):
            for relative_y in range(y + -1,  y + 2):
                if (relative_x,relative_y) in grid:
                    neighbour_count += grid[relative_x,relative_y]
        if neighbour_count - 1 < 4:
            part_2_sum += 1
            grid[x,y] = 0
            has_removed_one = True

print(f"Part 2 {part_2_sum} in {time.time()-start_time} seconds")