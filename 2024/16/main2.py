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


def get_path(parent, start_coords, end_coords):
    path = [end_coords]
    while path[-1] != start_coords:
        path.append(parent[path[-1]])
    return path


def dijkstra(grid, start_coords, end_coords):
    prices = defaultdict(lambda: 1e10)
    visited: set[Coords] = set()
    visited.add(start_coords)

    q = [(0, start_coords, [start_coords])]
    while q:
        price, current_position, path = heapq.heappop(q)
        if current_position.x == end_coords.x and current_position.y == end_coords.y:
            yield price, path
        for next, step_price in grid.get_neighbors(current_position):
            next_price = price + step_price
            if next not in visited or next_price <= prices[next]:
                visited.add(next)
                prices[next] = next_price
                heapq.heappush(q, (next_price, next, path + [next]))
    raise ValueError("there is no path to the end coords")


def part_two(puzzle_input):
    grid = parse_input(puzzle_input)
    start_coords = None
    end_coords = None
    for y, line in enumerate(grid.grid):
        for x, each in enumerate(line):
            if each == "S":
                start_coords = Coords(x, y, Direction.right)
            if each == "E":
                end_coords = Coords(x, y, Direction.up)

    paths = set()
    lowest_price = None
    for price, path in dijkstra(grid, start_coords, end_coords):
        if lowest_price is None:
            lowest_price = price
        if price > lowest_price:
            break
        paths.update(path)

    for each in paths:
        grid.set(each, "O")

    s = 0
    for line in grid.grid:
        for each in line:
            if each == "O":
                s += 1
    print(s)


if __name__ == "__main__":
    import puzzle

    part_two(puzzle.example)
    part_two(puzzle.example2)
    part_two(puzzle.example3)
    part_two(puzzle.input)
