import numpy as np

puzzle = """30373
25512
65332
33549
35390"""
grid_len = len(puzzle.split('\n'))
grid = [[int(n) for n in each] for each in puzzle.split('\n')]
grid = np.array(grid)


def calculate_score(mask):
    if len(mask) == 0:
        return 0
    mask = np.roll(mask, 1)
    mask[0] = False
    mask = ~(mask.cumsum() >= 1)
    return mask.sum()


def get_score(grid, x, y):
    mask = grid >= grid[x, y]
    ret = 1
    for sub in [
        mask[x + 1:, y],  # down
        mask[:x, y][::-1],  # up
        mask[x, y + 1:],  # right
        mask[x, :y][::-1],  # left
    ]:
        ret *= calculate_score(sub)
    return ret


max_score = 0
for i in range(0, grid_len):
    for j in range(0, grid_len):
        score = get_score(grid, i, j)
        if score > max_score:
            max_score = score

print(max_score)
