from collections import defaultdict
from enum import IntEnum
from typing import NamedTuple
import heapq


class Direction(IntEnum):
    up = 0
    right = 1
    down = 2
    left = 3


class Coords(NamedTuple):
    x: int
    y: int
    rotation: Direction

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y, self.rotation)

    def rotate_right(self):
        return Coords(self.x, self.y, (self.rotation + 1) % 4)

    def rotate_left(self):
        return Coords(self.x, self.y, (self.rotation + 3) % 4)


class Grid:
    def __init__(self, grid):
        self.grid = grid

    def print(self):
        for line in self.grid:
            print(*line, sep="")

    def set(self, coords: Coords, val):
        self.grid[coords.y][coords.x] = val

    def at(self, coords: Coords):
        return self.grid[coords.y][coords.x]

    def get_neighbors(self, coords: Coords):
        neighbors = []
        if coords.rotation == Direction.up:
            delta = Coords(0, -1, Direction.up)
        elif coords.rotation == Direction.right:
            delta = Coords(1, 0, Direction.right)
        elif coords.rotation == Direction.down:
            delta = Coords(0, 1, Direction.down)
        elif coords.rotation == Direction.left:
            delta = Coords(-1, 0, Direction.left)

        if self.at(coords + delta) != "#":
            neighbors.append((coords + delta, 1))

        neighbors.append((coords.rotate_left(), 1000))
        neighbors.append((coords.rotate_right(), 1000))
        return neighbors


def parse_input(puzzle_input):
    grid = [list(line) for line in puzzle_input.split("\n")]
    return Grid(grid)


def dijkstra(grid, start_coords, end_coords):
    prices = defaultdict(lambda: 1e10)
    visited: set[Coords] = set()
    visited.add(start_coords)

    q = [(0, start_coords)]
    while q:
        price, current_position = heapq.heappop(q)
        if current_position.x == end_coords.x and current_position.y == end_coords.y:
            return price
        for next, step_price in grid.get_neighbors(current_position):
            next_price = price + step_price
            if next not in visited or next_price < prices[next]:
                visited.add(next)
                prices[next] = next_price
                heapq.heappush(q, (next_price, next))
    raise ValueError("there is no path to the end coords")


def part_one(puzzle_input):
    grid = parse_input(puzzle_input)
    start_coords = None
    end_coords = None
    for y, line in enumerate(grid.grid):
        for x, each in enumerate(line):
            if each == "S":
                start_coords = Coords(x, y, Direction.right)
            if each == "E":
                end_coords = Coords(x, y, Direction.up)

    price = dijkstra(grid, start_coords, end_coords)
    print(price)


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example)
    part_one(puzzle.example2)
    part_one(puzzle.example3)
    part_one(puzzle.input)
