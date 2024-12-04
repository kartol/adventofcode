def parse_input(puzzle_input):
    grid = []
    for line in puzzle_input.split("\n"):
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    return grid


def read_indices(grid, i, j, x_dir, y_dir):
    txt = ""
    try:
        for x, y in zip(x_dir, y_dir):
            if i + x < 0 or j + y < 0:
                break
            txt += grid[i + x][j + y]
    except IndexError as e:
        return ""
    return txt


def price_index(grid, i, j):
    directions = [
        [[0, 1, 2, 3], [0, 0, 0, 0]],
        [[0, -1, -2, -3], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [0, 1, 2, 3]],
        [[0, 0, 0, 0], [0, -1, -2, -3]],
        [[0, 1, 2, 3], [0, 1, 2, 3]],
        [[0, 1, 2, 3], [0, -1, -2, -3]],
        [[0, -1, -2, -3], [0, -1, -2, -3]],
        [[0, -1, -2, -3], [0, 1, 2, 3]],
    ]

    cnt = 0
    for x_dir, y_dir in directions:
        if read_indices(grid, i, j, x_dir, y_dir) == "XMAS":
            cnt += 1

    return cnt


def part_one(puzzle_input):
    grid = parse_input(puzzle_input)

    s = 0
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            s += price_index(grid, i, j)

    print(s)


def find_mas(grid, i, j):
    diag1 = read_indices(grid, i, j, [-1, 0, 1], [-1, 0, 1])
    diag2 = read_indices(grid, i, j, [1, 0, -1], [-1, 0, 1])
    if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
        return 1

    return 0


def part_two(puzzle_input):
    grid = parse_input(puzzle_input)

    s = 0
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            s += find_mas(grid, i, j)

    print(s)


if __name__ == "__main__":
    from puzzle import input

    part_one(input)
    part_two(input)
