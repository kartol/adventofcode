from collections import deque


class Position(tuple):
    def __add__(self, other):
        return Position((self[0] + other[0], self[1] + other[1]))


def parse_input(puzzle_input):
    grid = []
    trailheads = []
    for i, line in enumerate(puzzle_input.split("\n")):
        row = []
        for j, char in enumerate(line):
            row.append(char)
            if char == "0":
                trailheads.append(Position((i, j)))
        grid.append(row)
    return grid, trailheads


def is_in_bounds(grid, position):
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])

def get_neighbors(grid, position):
    neighbors = []
    for delta in [
        Position((1, 0)),
        Position((0, 1)),
        Position((-1, 0)),
        Position((0, -1)),
    ]:
        if is_in_bounds(grid, n := position + delta):
            neighbors.append(n)
    return neighbors


def bfs(grid, starting_position):

    q = deque()
    visited = set(starting_position)
    q.append(starting_position)
    counter = 0
    while q:
        current_position = q.popleft()
        current_value = int(grid[current_position[0]][current_position[1]])
        for x in get_neighbors(grid, current_position):
            if grid[x[0]][x[1]] == ".":
                continue
            val = int(grid[x[0]][x[1]])
            if x not in visited and val == current_value + 1:
                visited.add(x)
                q.append(x)
                if val == 9:
                    counter += 1
    return counter


def part_one(puzzle_input):
    grid, trailheads = parse_input(puzzle_input)
    s = 0
    for trailhead in trailheads:
        s += bfs(grid, trailhead)
    print(s)



def bfs_2(grid, starting_position):
    q = deque()
    q.append(starting_position)
    counter = 0
    while q:
        current_position = q.popleft()
        current_value = int(grid[current_position[0]][current_position[1]])
        for x in get_neighbors(grid, current_position):
            if grid[x[0]][x[1]] == ".":
                continue
            val = int(grid[x[0]][x[1]])
            if val == current_value + 1:
                q.append(x)
                if val == 9:
                    counter += 1
    return counter

def part_two(puzzle_input):
    grid, trailheads = parse_input(puzzle_input)
    s = 0
    for trailhead in trailheads:
        s += bfs_2(grid, trailhead)
    print(s)


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example2)
    part_one(puzzle.input)
    part_two(puzzle.example3)
    part_two(puzzle.input)
