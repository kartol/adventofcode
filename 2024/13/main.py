from typing import NamedTuple

import numpy as np


class Coords(NamedTuple):
    x: int
    y: int


class Machine(NamedTuple):
    button_a: Coords
    button_b: Coords
    final_coords: Coords


def parse_button(line):
    return Coords(int(line[line.find("X+") + 2 : line.find(",")]), int(line[line.find("Y+") + 2 :]))


def parse_prize(line):
    return Coords(int(line[line.find("X=") + 2 : line.find(",")]), int(line[line.find("Y=") + 2 :]))


def parse_input(puzzle_input):
    machines = []
    for machine in puzzle_input.split("\n\n"):
        a, b, p = machine.split("\n")
        machines.append(
            Machine(
                button_a=parse_button(a),
                button_b=parse_button(b),
                final_coords=parse_prize(p),
            )
        )
    return machines


def part_one(puzzle_input):
    machines = parse_input(puzzle_input)
    s = 0
    for machine in machines:
        y = np.linalg.solve(
            np.matrix([machine.button_a, machine.button_b], dtype=int).T, np.array(machine.final_coords, dtype=int)
        )
        price = np.dot(y, (3, 1))
        if np.isclose(y, np.round(y)).all():
            s += price
    print(int(s))


def part_two(puzzle_input):
    machines = parse_input(puzzle_input)
    s = 0
    for machine in machines:
        b = 10000000000000 + np.array(machine.final_coords, dtype=int)
        X = np.matrix([machine.button_a, machine.button_b], dtype=int).T
        a = np.linalg.solve(X, b)
        a = np.round(a).astype(int)
        if ((X @ a) == b).all():
            price = np.dot(a, (3, 1))
            s += price
    print(int(s))


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example)
    part_one(puzzle.input)

    part_two(puzzle.example)
    part_two(puzzle.input)
