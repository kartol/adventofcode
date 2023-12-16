import itertools

import puzzle
import numpy as np

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
    for column in new_columns[::-1]:
        column = column[0]
        grid = np.insert(grid, column, values=0, axis=1)
    for row in new_rows[::-1]:
        row = row[0]
        grid = np.insert(grid, row, values=0, axis=0)

    dist = 0
    indices = np.argwhere(grid > 0)
    for i1, i2 in itertools.combinations(indices, 2):
        dist += abs(i1[0] - i2[0]) + abs(i1[1] - i2[1])
    print(dist)


if __name__ == "__main__":
    main()
