import itertools

import numpy as np

import puzzle


def main():
    puzzle_input = puzzle.input
    grid = []
    i = 0
    for line in puzzle_input.split("\n"):
        row = []
        for each in line:
            if each == "#":
                i += 1
            row.append(0 if each == "." else i)
        grid.append(row)

    grid = np.array(grid)
    new_columns = np.argwhere(np.sum(grid, axis=0) == 0)
    new_rows = np.argwhere(np.sum(grid, axis=1) == 0)

    dist = 0
    indices = np.argwhere(grid > 0)
    for i1, i2 in itertools.combinations(indices, 2):
        x = ((min(i1[0], i2[0]) < new_rows) & (max(i1[0], i2[0]) > new_rows)).sum()
        x += ((min(i1[1], i2[1]) < new_columns) & (max(i1[1], i2[1]) > new_columns)).sum()

        dist += abs(i1[0] - i2[0]) + abs(i1[1] - i2[1]) + x * (1000000 - 1)

    print(dist)


if __name__ == "__main__":
    main()
