import numpy as np
import tqdm


def parse_input(puzzle_input):
    connections = []
    for line in puzzle_input.splitlines():
        connections.append(line.split("-"))
    return connections


best_result = []


def find_for_combination(matrix, combination, from_index):
    global best_result
    if matrix[..., combination][combination, ...].all():
        if len(combination) > len(best_result):
            best_result = combination
    else:
        return

    for idx, val in list(enumerate(np.nonzero(matrix[combination][0])[0]))[from_index:]:
        if val not in combination:
            find_for_combination(matrix, combination + [val], idx + 1)


def part_one(puzzle_input):
    connections = parse_input(puzzle_input)

    computers = set()
    for connection in connections:
        computers.update(connection)

    computers = sorted(list(computers))
    matrix = np.eye(len(computers))
    for a, b in connections:
        idx_a = computers.index(a)
        idx_b = computers.index(b)
        matrix[idx_a, idx_b] = 1
        matrix[idx_b, idx_a] = 1

    for k in tqdm.tqdm(range(len(computers))):
        find_for_combination(matrix, [k], 0)

    print(",".join([computers[each] for each in best_result]))


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.input)
