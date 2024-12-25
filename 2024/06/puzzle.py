import math, time, random, copy
from enum import Enum
from time import sleep
from typing import Tuple

start = time.time()

with open('./input.txt') as f:
    puzzle_input = f.read()

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Directions(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)

class Cell:
    def __init__(self, char: str | None = None, is_visited: bool = False) -> None:
        self.is_visited = False
        self.previously_visited_by_directions = []

        if is_visited:
            self.is_visited = True

        if char == "#":
            self.isWall = True
        else:
            self.isWall = False

    def __str__(self) -> str:
        if self.is_visited:
            if len(self.previously_visited_by_directions) == 0:
                return "X"
            elif len(self.previously_visited_by_directions) == 1:
                return Bcolors.OKBLUE + "X" + Bcolors.ENDC
            elif len(self.previously_visited_by_directions) == 2:
                return Bcolors.WARNING + "X" + Bcolors.ENDC
            elif len(self.previously_visited_by_directions) == 3:
                return Bcolors.WARNING + "X" + Bcolors.ENDC
            elif len(self.previously_visited_by_directions) == 3:
                return Bcolors.FAIL + "X" + Bcolors.ENDC
            else:
                return "?"

        if self.isWall:
            return "#"
        else:
            return "."

class Agent:
    direction: Directions
    _current_cell: Cell | None
    _position: tuple[int, int]

    def __init__(self, char: str, position: tuple[int, int]) -> None:
        self.direction = Directions.NORTH
        self._position = position

    def __str__(self) -> str:
        match self.direction:
            case Directions.NORTH:
                return "^"
            case Directions.EAST:
                return ">"
            case Directions.SOUTH:
                return "⌄"
            case Directions.WEST:
                return "<"
            case _:
                return "?"

    @property
    def position(self):
        return self._position

    def rotate(self):
        if self.direction == Directions.NORTH:
            self.direction = Directions.EAST
        elif self.direction == Directions.EAST:
            self.direction = Directions.SOUTH
        elif self.direction == Directions.SOUTH:
            self.direction = Directions.WEST
        elif self.direction == Directions.WEST:
            self.direction = Directions.NORTH

    @position.setter
    def position(self, value):
        self._position = value


class Grid:
    cells: dict[tuple[int, int], Cell | Agent]
    width: int
    agent: Agent

    def __init__(self, input_string: str) -> None:
        self.cells = {}
        lines = input_string.splitlines()
        self.width = len(lines[0])
        for line_index, line in enumerate(lines):
            for char_index, char in enumerate(line):
                key = (line_index, char_index)
                if char in ["#", "."]:
                    self.cells[key] = Cell(char)
                else:
                    self.cells[key] = Cell(char)
                    self.agent = Agent(char, key)


    def __str__(self) -> str:
        for index, item in enumerate(self.cells):
            if index != 0 and index % self.width == 0:
                print()
            if self.agent.position == item:
                print(self.agent, end="")
            else:
                print(self.cells[item], end="")
        return ""

    def calculate_agent_path(self):
        should_continue = True
        while should_continue:
            should_continue, is_loop = self.update_agent()
            # print(self)
            pass

    def check_for_loop_in_agent_path(self) -> bool:
        should_continue = True
        while should_continue:
            should_continue, is_loop = self.update_agent()

            if is_loop:
                return is_loop
            pass

    def update_agent(self) -> tuple[bool, bool]:
        new_position: tuple[int, int] = tuple(map(lambda y, x: x + y, self.agent.position, self.agent.direction.value))
        old_position = self.agent.position

        if new_position in self.cells:
            if self.cells[new_position].isWall:
                self.agent.rotate()
                return True, False

            if self.agent.direction in self.cells[new_position].previously_visited_by_directions or len(self.cells[new_position].previously_visited_by_directions) > 4:
                return False, True

            self.cells[old_position].is_visited = True
            self.cells[old_position].previously_visited_by_directions.append(self.agent.direction)
            self.agent.position = new_position

            return True, False
        else:
            self.cells[self.agent.position] = Cell(is_visited=True)
            return False, False

    def get_visited_cells(self):
        visited = 0
        for cell in self.cells:
            if isinstance(self.cells[cell], Cell) and self.cells[cell].is_visited:
                visited += 1

        return visited

    def update_cell(self, pos: tuple[int, int], cell:Cell):
        self.cells[pos] = cell

grid = Grid(puzzle_input)
print(grid)

grid.calculate_agent_path()
print(grid, grid.get_visited_cells())

# sleep(10)

# Part 2

puzzle_input_list = list(puzzle_input)

loop_count = 0

for index, char in enumerate(list(puzzle_input_list)):
    if char == '.':
        puzzle_input_list_copy = puzzle_input_list[::1]
        puzzle_input_list_copy[index] = "#"
        temp_grid = Grid("".join(puzzle_input_list_copy))
        if temp_grid.check_for_loop_in_agent_path():
            loop_count += 1
        # print(temp_grid)
        if index % 10 == 1:
            print(f'====================== { round(int(index) / len(list(puzzle_input_list)) * 100, 2)}% | {loop_count} =======================')