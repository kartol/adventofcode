def parse_input(puzzle_input):
    grid = []
    for line in puzzle_input.split("\n"):
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    return grid


def is_on_grid(grid, position):
    if position[0] < 0 or position[1] < 0:
        return False
    if position[0] >= len(grid) or position[1] >= len(grid[0]):
        return False
    return True


def part_one(puzzle_input):
    grid = parse_input(puzzle_input)

    current_direction = "^"
    current_position = (0, 0)
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == current_direction:
                current_position = (i, j)
                grid[i][j] = "."

    move_map = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }
    visited = set()
    while is_on_grid(grid, current_position):
        next_position = tuple(x + y for x, y in zip(current_position, move_map[current_direction]))
        if not is_on_grid(grid, next_position):
            break
        next_char = grid[next_position[0]][next_position[1]]
        if next_char == ".":
            current_position = next_position
            visited.add(current_position)
        else:
            directions = list(move_map)
            current_direction = directions[(directions.index(current_direction) + 1) % len(directions)]

    print(len(visited))


def detect_loop(grid, current_position, current_direction):
    move_map = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }
    visited = set()
    while is_on_grid(grid, current_position):
        next_position = tuple(x + y for x, y in zip(current_position, move_map[current_direction]))
        if not is_on_grid(grid, next_position):
            break
        next_char = grid[next_position[0]][next_position[1]]
        if next_char == ".":
            current_position = next_position
            if (current_position, current_direction) in visited:
                return True
            visited.add((current_position, current_direction))
        else:
            directions = list(move_map)
            current_direction = directions[(directions.index(current_direction) + 1) % len(directions)]

    return False


def part_two(puzzle_input):
    grid = parse_input(puzzle_input)

    current_direction = "^"
    current_position = (0, 0)
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == current_direction:
                current_position = (i, j)
                grid[i][j] = "."

    loops = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if grid[i][j] == ".":
                grid[i][j] = "#"
                loops += detect_loop(grid, current_position, current_direction)
                grid[i][j] = "."

    print(loops)


if __name__ == "__main__":
    from puzzle import input

    part_one(input)
    part_two(input)
