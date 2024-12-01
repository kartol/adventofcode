def parse_input(puzzle_input):
    lst1, lst2 = [], []
    for line in puzzle_input.split("\n"):
        x, y = line.split()
        lst1.append(int(x))
        lst2.append(int(y))
    return lst1, lst2

def part_one(puzzle_input):
    lst1, lst2 = parse_input(puzzle_input)

    lst1 = sorted(lst1)
    lst2 = sorted(lst2)

    s = 0
    for x, y in zip(lst1, lst2):
        s += abs(x-y)
    print(s)


def part_two(puzzle_input):
    lst1, lst2 = parse_input(puzzle_input)

    s = 0
    for each in lst1:
        cnt = lst2.count(each)
        s += each * cnt
    print(s)

if __name__ == '__main__':
    from puzzle import input1
    part_one(input1)
    part_two(input1)
