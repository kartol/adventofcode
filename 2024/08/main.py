from collections import defaultdict
from itertools import permutations


def parse_input(puzzle_input):
    grid = []
    antennas = defaultdict(list)
    for i, line in enumerate(puzzle_input.split("\n")):
        row = []
        for j, char in enumerate(line):
            row.append(char)
            if char == ".":
                continue
            antennas[char].append((i, j))
        grid.append(row)
    return grid, antennas


def part_one(puzzle_input):
    grid, antennas = parse_input(puzzle_input)

    def is_in_bounds(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])

    antinodes = set()
    for same_f_antennas in antennas.values():
        for pair in permutations(same_f_antennas, 2):
            delta = tuple([x - y for x, y in zip(*pair)])
            antinode = (pair[0][0] + delta[0], pair[0][1] + delta[1])
            if not is_in_bounds(antinode[0], antinode[1]):
                continue
            antinodes.add(antinode)
    print(len(antinodes))


def part_two(puzzle_input):
    grid, antennas = parse_input(puzzle_input)

    def is_in_bounds(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])

    antinodes = set()
    for same_f_antennas in antennas.values():
        for pair in permutations(same_f_antennas, 2):
            delta = tuple([x - y for x, y in zip(*pair)])
            antinode = pair[0]
            while is_in_bounds(antinode[0], antinode[1]):
                antinodes.add(antinode)
                antinode = (antinode[0] + delta[0], antinode[1] + delta[1])
    print(len(antinodes))


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.input)
    part_two(puzzle.input)
