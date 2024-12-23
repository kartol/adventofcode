import itertools


def parse_input(puzzle_input):
    connections = []
    for line in puzzle_input.splitlines():
        connections.append(line.split("-"))
    return connections


def any_starts_with(triplet, letter):
    return any(each.startswith(letter) for each in triplet)


def is_interconnected(computers, triplet):
    for a, b in itertools.combinations(triplet, 2):
        if a not in computers[b]:
            return False
        if b not in computers[a]:
            return False
    return True


def part_one(puzzle_input):
    connections = parse_input(puzzle_input)

    computers = {}
    for a, b in connections:
        computer_a = {}
        computer_b = {}
        if a in computers:
            computer_a = computers[a]
        else:
            computers[a] = computer_a
        if b in computers:
            computer_b = computers[b]
        else:
            computers[b] = computer_b

        computer_a[b] = computer_b
        computer_b[a] = computer_a

    s = 0
    for triplet in itertools.combinations(computers, 3):
        if any_starts_with(triplet, "t") and is_interconnected(computers, triplet):
            s += 1
    print(s)


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example)
    part_one(puzzle.input)
