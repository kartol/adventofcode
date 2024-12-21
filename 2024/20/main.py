from collections import defaultdict, deque
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

    def set(self, coords: Coords, val):
        self.grid[coords.y][coords.x] = val

    def at(self, coords: Coords):
        return self.grid[coords.y][coords.x]

    def is_in_bound(self, coords):
        return 0 <= coords.x < len(self.grid) and 0 <= coords.y < len(self.grid[0])

    def get_neighbors(self, position: Coords):
        neighbors = []
        for delta in [
            Coords(0, -1),
            Coords(1, 0),
            Coords(0, 1),
            Coords(-1, 0),
        ]:
            next = position + delta
            if self.is_in_bound(next) and self.at(next) != "#":
                neighbors.append(next)
        return neighbors


def parse_input(puzzle_input):
    grid = [list(line) for line in puzzle_input.split("\n")]
    return Grid(grid)


def bfs(grid, starting_position: Coords, end_coords: Coords):
    q = deque()
    visited = set()
    visited.add(starting_position)
    q.append((starting_position, [starting_position]))
    while q:
        current_position, path = q.popleft()
        if current_position == end_coords:
            return path
        for next in grid.get_neighbors(current_position):
            if next not in visited:
                visited.add(next)
                q.append((next, path + [next]))
    raise ValueError()


def solve(puzzle_input, cheat_price, min_cheat_score):
    grid = parse_input(puzzle_input)
    start_position = None
    end_coords = None
    for y, line in enumerate(grid.grid):
        for x, each in enumerate(line):
            if each == "S":
                start_position = Coords(x, y)
            if each == "E":
                end_coords = Coords(x, y)

    if start_position is None or end_coords is None:
        return

    path = bfs(grid, start_position, end_coords)

    d = defaultdict(int)
    s = 0
    for i, a in enumerate(path):
        for j, b in enumerate(path):
            distance = abs(a.x - b.x) + abs(a.y - b.y)
            if distance <= cheat_price:
                saves = j - i - distance
                if saves >= min_cheat_score:
                    s += 1
                    d[saves] += 1
    print(s)
    print({key: d[key] for key in sorted(d)})


if __name__ == "__main__":
    import puzzle

    solve(puzzle.example, 2, 0)
    solve(puzzle.input, 2, 100)
    solve(puzzle.example, 20, 50)
    solve(puzzle.input, 20, 100)
