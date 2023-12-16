from enum import StrEnum, auto

import puzzle


class Directions(StrEnum):
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()


connects_to = {
    "|": [Directions.UP, Directions.DOWN],
    "-": [Directions.LEFT, Directions.RIGHT],
    "L": [Directions.UP, Directions.RIGHT],
    "J": [Directions.LEFT, Directions.UP],
    "7": [Directions.LEFT, Directions.DOWN],
    "F": [Directions.RIGHT, Directions.DOWN],
    ".": [],
    "S": [Directions.UP, Directions.RIGHT, Directions.DOWN, Directions.LEFT],
}


def new_coords(x, y, direction):
    if direction == Directions.RIGHT:
        return x + 1, y
    if direction == Directions.LEFT:
        return x - 1, y
    if direction == Directions.UP:
        return x, y - 1
    return x, y + 1


def is_connected(grid, x, y, direction):
    pipe = grid[y][x]
    coords = new_coords(x, y, direction)
    pipe_new = grid[coords[1]][coords[0]]
    if direction == Directions.RIGHT:
        return (
                (Directions.RIGHT in connects_to[pipe])
                and (Directions.LEFT in connects_to[pipe_new])
        )
    if direction == Directions.LEFT:
        return (
                (Directions.LEFT in connects_to[pipe])
                and (Directions.RIGHT in connects_to[pipe_new])
        )
    if direction == Directions.UP:
        return (
                (Directions.UP in connects_to[pipe])
                and (Directions.DOWN in connects_to[pipe_new])
        )
    return (
            (Directions.DOWN in connects_to[pipe])
            and (Directions.UP in connects_to[pipe_new])
    )


def main():
    puzzle_input = puzzle.input
    first_line = puzzle_input.split("\n")[0]
    grid = [[".", ] * (len(first_line) + 2)]
    for i, line in enumerate(puzzle_input.split("\n"), 1):
        row = ["."]
        for j, each in enumerate(line, 1):
            row.append(each)
            if each == "S":
                s = (i, j)
        row.append(".")
        grid.append(row)
    grid.append([".", ] * (len(first_line) + 2))

    x, y = s[1], s[0]

    i = 0
    stop = False
    while not stop:
        if i == 3:
            grid[s[0]][s[1]] = "S"
        for direction in Directions:
            if is_connected(grid, x, y, direction=direction):
                grid[y][x] = "."
                x, y = new_coords(x, y, direction)
                if grid[y][x] == "S":
                    stop = True
                i += 1
                break

    print(i // 2)


if __name__ == "__main__":
    main()
