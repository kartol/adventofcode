import numpy as np

puzzle = """30373
25512
65332
33549
35390"""
grid_len = len(puzzle.split('\n'))
grid = [[int(n) for n in each] for each in puzzle.split('\n')]
grid = np.array(grid)


def is_visible(grid, x, y):
    mask = grid >= grid[x, y]
    if (
            sum(mask[x + 1:, y]) == 0
            or sum(mask[:x, y]) == 0
            or sum(mask[x, y + 1:]) == 0
            or sum(mask[x, :y]) == 0
    ):
        return True
    return False


count = 0
for i in range(0, grid_len):
    for j in range(0, grid_len):
        if is_visible(grid, i, j):
            count += 1

print(count)
