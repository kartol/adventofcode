def parse_input(puzzle_input):
    lst = []
    for line in puzzle_input.split("\n"):
        lst.append([int(each) for each in line.split()])
    return lst


def price_row(row):
    deltas = [x - y for x, y in zip(row, row[1:])]
    if not (all(delta > 0 for delta in deltas) or all(delta < 0 for delta in deltas)):
        return 0
    if any(delta == 0 or abs(delta) > 3 for delta in deltas):
        return 0

    return 1


def part_one(puzzle_input):
    lst = parse_input(puzzle_input)
    s = 0
    for row in lst:
        s += price_row(row)
    print(s)


def part_two(puzzle_input):
    lst = parse_input(puzzle_input)
    s = 0
    for row in lst:
        p = price_row(row)
        if p == 0:
            for i, _ in enumerate(row):
                p = price_row(row[:i] + row[i + 1 :])
                if p == 1:
                    break
        s += p
    print(s)


if __name__ == "__main__":
    from puzzle import input

    part_one(input)
    part_two(input)
