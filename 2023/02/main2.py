import functools
import operator

import puzzle

def game_power(line):
    cubes_max = {
        "red": 1,
        "green": 1,
        "blue": 1,
    }
    for cube_set in line.split('; '):
        for each in cube_set.split(', '):
            amount, color = each.split(' ')
            if int(amount) > cubes_max[color]:
                cubes_max[color] = int(amount)
    return functools.reduce(operator.mul, cubes_max.values(), 1)

def solve_line(line):
    line = line.split(': ')[1]
    return game_power(line)

def main():
    s = 0
    for line in puzzle.input.split("\n"):
        s += solve_line(line)
    print(s)


if __name__ == "__main__":
    main()
