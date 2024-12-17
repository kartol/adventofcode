from collections import deque
from typing import NamedTuple


class Coords(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coords(self.x - other.x, self.y - other.y)


class Grid:
    def __init__(self, grid):
        self.grid = grid

    def print(self):
        for line in self.grid:
            print(*line, sep="")

    def at(self, coords: Coords):
        return self.grid[coords.y][coords.x]

    def set(self, coords: Coords, val):
        self.grid[coords.y][coords.x] = val

    def is_movable(self, coords: Coords):
        return self.at(coords) == "[" or self.at(coords) == "]" or self.at(coords) == "@"

    def is_block(self, coords: Coords):
        return self.at(coords) == "#"


def parse_input(puzzle_input):
    grid_input, instructions = puzzle_input.split("\n\n")

    def make_larger(x):
        if x == "@":
            return "@."
        if x == "O":
            return "[]"
        return 2 * x

    grid = []
    for line in grid_input.split("\n"):
        grid_line = []
        for each in line:
            grid_line.extend(make_larger(each))
        grid.append(grid_line)
    return Grid(grid), [instruction for instruction in instructions if instruction != "\n"]


def part_two(puzzle_input):
    grid, instructions = parse_input(puzzle_input)

    robot_coords = Coords(0, 0)
    for y, line in enumerate(grid.grid):
        for x, each in enumerate(line):
            if each == "@":
                robot_coords = Coords(x, y)

    for instruction in instructions:
        if instruction == "<":
            delta = Coords(-1, 0)
        elif instruction == ">":
            delta = Coords(1, 0)
        elif instruction == "^":
            delta = Coords(0, -1)
        else:
            delta = Coords(0, 1)

        moving_parts = set()
        to_expand = deque()
        to_expand.append(robot_coords)
        
        while to_expand:
            c = to_expand.popleft()
            if grid.is_movable(c):
                moving_parts.add(c)
                if instruction == "^" or instruction == "v":
                    if grid.at(c) == "[":
                        x = c + Coords(1, 0)
                        if x not in moving_parts:
                            to_expand.append(x)
                    elif grid.at(c) == "]":
                        x = c + Coords(-1, 0)
                        if x not in moving_parts:
                            to_expand.append(x)
                x = c + delta
                if x not in moving_parts:
                    to_expand.append(x)
                    
        is_blocked = any(grid.is_block(each + delta) for each in list(moving_parts))
        if is_blocked:
            continue

        chars = []
        for each in moving_parts:
            chars.append(grid.at(each))

        robot_coords = robot_coords + delta

        for each, char in zip(moving_parts, chars):
            grid.set(each + delta, char)
            if each - delta not in moving_parts:
                grid.set(each, ".")

    grid.print()

    s = 0
    for y, line in enumerate(grid.grid):
        for x, each in enumerate(line):
            if each == "[":
                s += x + 100 * y
    print(s)


if __name__ == "__main__":
    import puzzle

    part_two(puzzle.example)
    part_two(puzzle.example2)
    part_two(puzzle.input)
    part_two(puzzle.example3)
