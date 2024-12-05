import re


def part_one(puzzle_input):
    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\))", puzzle_input)
    s = 0
    for match in matches:
        x, y = [int(each) for each in match[4:-1].split(",")]
        s += x * y
    print(s)


def part_two(puzzle_input):
    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))", puzzle_input)

    active = True
    s = 0
    for match in matches:
        if match == "do()":
            active = True
            continue
        if match == "don't()":
            active = False
            continue

        if not active:
            continue

        x, y = [int(each) for each in match[4:-1].split(",")]
        s += x * y
    print(s)


if __name__ == "__main__":
    from puzzle import input

    part_one(input)
    part_two(input)
