import itertools

import puzzle
import tqdm


def is_correct(record, numbers):
    x = tuple(len(each) for each in record.split('.') if len(each))
    return x == numbers


def main():
    puzzle_input = puzzle.input
    s = 0
    for line in tqdm.tqdm(puzzle_input.split("\n")):
        lhs, numbers = line.split()
        numbers = tuple(int(n) for n in numbers.split(','))

        missing_springs = sum(numbers) - sum(each == "#" for each in lhs)
        missing_parts = sum(each == "?" for each in lhs)
        comb = ["#", ] * missing_springs + ["."] * (missing_parts - missing_springs)
        for perm in set(itertools.permutations(comb, len(comb))):
            new_lhs = lhs[:]
            for each in perm:
                new_lhs = new_lhs.replace("?", each, 1)
            s += int(is_correct(new_lhs, numbers))

    print(s)


if __name__ == "__main__":
    main()
