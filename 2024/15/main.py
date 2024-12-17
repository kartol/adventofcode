from typing import NamedTuple


class Coords(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y)


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

    def switch(self, coords: Coords, coords2: Coords):
        x = self.at(coords)
        y = self.at(coords2)
        self.set(coords, y)
        self.set(coords2, x)


def parse_input(puzzle_input):
    grid, instructions = puzzle_input.split("\n\n")
    grid = [list(line) for line in grid.split("\n")]
    return Grid(grid), [instruction for instruction in instructions if instruction != "\n"]


def part_one(puzzle_input):
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
        move = robot_coords + delta
        if grid.at(move) == "O":
            # try to move the box
            lookup = Coords(move.x, move.y)
            while grid.at(lookup) == "O":
                lookup = lookup + delta
            if grid.at(lookup) == ".":
                grid.switch(lookup, move)
        if grid.at(move) == ".":
            grid.switch(robot_coords, move)
            robot_coords = move

    grid.print()

    s = 0
    for y, line in enumerate(grid.grid):
        for x, each in enumerate(line):
            if each == "O":
                s += x + 100 * y
    print(s)


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example)
    part_one(puzzle.example2)
    part_one(puzzle.input)
