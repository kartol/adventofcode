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
    symbols = []
    number_registry = NumberRegistry()
    for i, line in enumerate(puzzle_input.split("\n")):
        for j, char in enumerate(line):
            if char.isdigit():
                number_registry.update(char)
            elif char == '.':
                number_registry.reset()
            else:
                # special symbol
                number_registry.reset()
                symbols.append((i, j))
            matrix[i, j] = number_registry.current_id()
    ids = set()
    for (i, j) in symbols:
        ids.update(set(matrix[i - 1:i + 2, j - 1:j + 2].reshape(-1)))

    s = 0
    for id in ids:
        s += number_registry.all_numbers[id].value()

    print(s)

if __name__ == "__main__":
    main()
