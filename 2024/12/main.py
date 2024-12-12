from collections import deque, defaultdict


class Position(tuple):
    def __add__(self, other):
        return Position((self[0] + other[0], self[1] + other[1]))


def is_in_bounds(grid, position):
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])


def get_neighbors(position):
    neighbors = []
    for delta in [
        Position((1, 0)),
        Position((0, 1)),
        Position((-1, 0)),
        Position((0, -1)),
    ]:
        neighbors.append(position + delta)
    return neighbors


def bfs(grid, starting_position):
    plant = grid[starting_position[0]][starting_position[1]]
    q = deque()
    visited: set[Position] = set()
    visited.add(starting_position)
    fences = set()
    q.append(starting_position)
    while q:
        current_position = q.popleft()
        for x in get_neighbors(current_position):
            if not is_in_bounds(grid, x):
                fences.add((current_position, x))
                continue
            if grid[x[0]][x[1]] != plant:
                fences.add((current_position, x))
                continue
            if x not in visited:
                visited.add(x)
                q.append(x)
    return visited, fences


def part_one(puzzle_input):
    grid = [[each for each in line] for line in puzzle_input.split("\n")]

    s = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            position = Position((i, j))
            if position in visited:
                continue
            area, fences = bfs(grid, position)
            visited.update(area)
            s += len(area) * len(fences)
    print(s)


def price_fence(fences):
    v_fences = [fence for fence in fences if fence[0][0] == fence[1][0]]
    h_fences = [fence for fence in fences if fence[0][1] == fence[1][1]]
    
    grouped_v_fences = defaultdict(list)
    for fence in v_fences:
        grouped_v_fences[(fence[1][1], fence[0][1])].append(fence[1][0])
        
    grouped_h_fences = defaultdict(list)
    for fence in h_fences:
        grouped_h_fences[(fence[1][0], fence[0][0])].append(fence[1][1])
        
    v_fences = [sorted(fences) for fences in grouped_v_fences.values()]
    h_fences = [sorted(fences) for fences in grouped_h_fences.values()]
    
    def price_lst(lst):
        s = 0
        prev_val = lst[0]
        for val in lst:
            if val == prev_val + 1:
                prev_val= val
                continue
            prev_val = val
            s += 1
        return s
    
    sides = 0
    for lst in v_fences + h_fences:
        sides += price_lst(lst)

    return sides


def part_two(puzzle_input):
    grid = [[each for each in line] for line in puzzle_input.split("\n")]

    s = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            position = Position((i, j))
            if position in visited:
                continue
            area, fences = bfs(grid, position)
            visited.update(area)
            s += len(area) * price_fence(fences)
    print(s)


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example)
    part_one(puzzle.example2)
    part_one(puzzle.input)

    print("===============")

    part_two(puzzle.example)
    part_two(puzzle.example2)
    part_two(puzzle.example3)
    part_two(puzzle.example4)
    part_two(puzzle.input)
