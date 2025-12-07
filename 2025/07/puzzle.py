import os
import time
from typing import List, Dict

with open('input.txt') as f:
    lines: List[str] = f.read().splitlines()

start_time = time.time()

grid: Dict[tuple[int,int], str] = {}
queue: List[tuple[int,int]] = []
start: tuple[int,int] = (0,0)

def print_grid():
    for _y in range(len(lines)):
        for _x in range(len(lines[x])):
            print(grid[_x,_y], end='')
        print()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid[(x, y)] = char
        if char == 'S':
            queue.append((x, y))
            start = (x, y)


class Node:
    def __init__(self, position: tuple[int,int]):
        self.children = []
        self.position = position
        self.cached_total_children = -1
        return

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_count_of_all_children(self):
        if self.cached_total_children > -1:
            return self.cached_total_children

        count = 2 - len(self.children)

        for child in self.children:
            count += child.get_count_of_all_children()

        self.cached_total_children = count

        return count


    def __str__(self) -> str:
        return f"{self.position}, with {len(self.children)} children"


split_count = 0

while len(queue):
    x, y = queue.pop()
    if (x, y+1) not in grid:
        continue

    if grid[(x, y+1)] == '.':
        grid[(x, y+1)] = '|'
        queue.append((x, y+1))
    elif grid[(x, y+1)] == '^':
        split_count += 1
        grid[(x-1, y+1)] = '|'
        queue.append((x-1, y+1))
        grid[(x+1, y+1)] = '|'
        queue.append((x+1, y+1))


print(f"Part 1{split_count} {time.time() - start_time}s")
nodes: Dict[tuple[int,int], Node] = {}

queue = [start]
nodes[start] = Node(start)

while len(queue):
    x, y = queue.pop()
    if (x, y+1) not in grid:
        continue
    if len(nodes[x, y].get_children()):
        continue

    if len(nodes.values()) == 1:
        for _y in range(y, len(lines)):
            if grid[(x, _y)] == '^':
                nodes[x, _y] = Node((x, _y))
                nodes[x, y].add_child(nodes[x, _y])
                queue.append((x, _y))
                break
    else:
        for _y in range(y, len(lines)):
            if grid[(x - 1, _y)] == '^':
                if (x - 1, _y) not in nodes:
                    nodes[x - 1, _y] = Node((x - 1, _y))
                queue.append((x - 1, _y))
                nodes[x, y].add_child(nodes[x - 1, _y])
                break
        for _y in range(y, len(lines)):
            if grid[(x + 1, _y)] == '^':
                if (x + 1, _y) not in nodes:
                    nodes[x + 1, _y] = Node((x + 1, _y))
                nodes[x, y].add_child(nodes[x + 1, _y])
                queue.append((x + 1, _y))
                break

print(f"Part 2{nodes[start].get_children()[0].get_count_of_all_children()} {time.time() - start_time}s")
