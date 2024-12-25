from typing import NamedTuple


class LockSmth(NamedTuple):
    x1: int
    x2: int
    x3: int
    x4: int
    x5: int

    def __add__(self, other):
        return LockSmth(
            self.x1 + other.x1,
            self.x2 + other.x2,
            self.x3 + other.x3,
            self.x4 + other.x4,
            self.x5 + other.x5,
        )


def is_key(key_string):
    return "#" in key_string.split("\n")[-1]


def parse_lock_smth(key_string):
    columns = list(zip(*key_string.split("\n")))
    return LockSmth(*(column.count("#") - 1 for column in columns))


def parse_inpt(puzzle_input):
    keys = []
    locks = []
    for each in puzzle_input.split("\n\n"):
        lock_smth = parse_lock_smth(each)
        if is_key(each):
            keys.append(lock_smth)
        else:
            locks.append(lock_smth)
    return keys, locks


def fits(x: LockSmth):
    for each in x:
        if each > 5:
            return False
    return True


def part_one(puzzle_input):
    keys, locks = parse_inpt(puzzle_input)

    s = 0
    for key in keys:
        for lock in locks:
            s += int(fits(key + lock))
    print(s)


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example)
    part_one(puzzle.input)
