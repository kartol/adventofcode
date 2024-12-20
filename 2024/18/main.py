from collections import deque
from typing import NamedTuple


class Coords(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y)


def is_in_bounds(max_x, max_y, position):
    return 0 <= position.x < max_x and 0 <= position.y < max_y


def get_neighbors(position):
    neighbors = []
    for delta in [
        Coords(1, 0),
        Coords(0, 1),
        Coords(-1, 0),
        Coords(0, -1),
    ]:
        neighbors.append(position + delta)
    return neighbors


def bfs(max_x, max_y, starting_position, ending_position, coords):
    q = deque()
    visited: set = set()
    visited.add(starting_position)
    q.append((starting_position, [starting_position]))
    while q:
        current_position, path = q.popleft()
        if current_position == ending_position:
            return path
        for next in get_neighbors(current_position):
            if not is_in_bounds(max_x, max_y, next):
                continue
            if next in coords:
                continue
            if next not in visited:
                visited.add(next)
                q.append((next, path + [next]))
    return visited


def parse_input(puzzle_input):
    coords = []
    for each in puzzle_input.splitlines():
        x, y = each.split(",")
        coords.append(Coords(int(x), int(y)))
    return coords


def part_one(puzzle_input, max_x, max_y, sim_bytes):
    coords = parse_input(puzzle_input)[:sim_bytes]
    path = bfs(max_x, max_y, Coords(0, 0), Coords(max_x - 1, max_y - 1), coords)
    print(len(path) - 1)


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example, 7, 7, 12)
    part_one(puzzle.input, 71, 71, 1024)
