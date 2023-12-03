import numpy as np

import puzzle


class Number:
    def __init__(self, val=''):
        self.val = val

    def update(self, char: str):
        self.val += char

    def value(self):
        return int(self.val)


class NumberRegistry:
    def __init__(self):
        self.current_number = None
        self.all_numbers = [Number('0')]

    def update(self, char: str):
        if self.current_number is None:
            self.current_number = Number()
        self.current_number.update(char)

    def reset(self):
        if self.current_number is not None:
            self.all_numbers.append(self.current_number)
            self.current_number = None

    def current_id(self):
        if self.current_number is None:
            return 0
        return len(self.all_numbers)


def main():
    puzzle_input = puzzle.input
    matrix = np.zeros((len(puzzle_input.split("\n")), len(puzzle_input.split("\n")[0])), dtype=np.int32)
    gears = []
    number_registry = NumberRegistry()
    for i, line in enumerate(puzzle_input.split("\n")):
        for j, char in enumerate(line):
            if char.isdigit():
                number_registry.update(char)
            elif char == '.':
                number_registry.reset()
            elif char == '*':
                # special symbol
                number_registry.reset()
                gears.append((i, j))
            else:
                number_registry.reset()
            matrix[i, j] = number_registry.current_id()

    s = 0
    for (i, j) in gears:
        numbers = set(matrix[i - 1:i + 2, j - 1:j + 2].reshape(-1)) - {0, }
        if len(numbers) != 2:
            continue
        values = [number_registry.all_numbers[n].value() for n in numbers]
        s += values[0] * values[1]

    print(s)


if __name__ == "__main__":
    main()
