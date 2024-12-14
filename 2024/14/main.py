import time
from typing import NamedTuple

import numpy as np
from termcolor import colored


class Coords(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y)

    def __rmul__(self, other):
        return Coords(self.x * other, self.y * other)


class Robot(NamedTuple):
    coords: Coords
    velocity: Coords


def render(coords: list[Coords], grid_x, grid_y):
    grid = [[0 for _ in range(grid_x)] for _ in range(grid_y)]
    for coord in coords:
        grid[coord.y % grid_y][coord.x % grid_x] += 1
    return grid

def print_grid(grid):
    for line in grid:
        for each in line:
            if each != 0:
                print(colored(each, "green", on_color="on_green"), end="")
            else:
                print(each, end="")
        print()

def parse_input(puzzle_input):
    robots = []
    for machine in puzzle_input.split("\n"):
        p, v = machine.split(" ")
        p, v = p[2:], v[2:]
        p = p.split(",")
        v = v.split(",")
        robots.append(
            Robot(
                coords=Coords(x=int(p[0]), y=int(p[1])),
                velocity=Coords(x=int(v[0]), y=int(v[1])),
            )
        )
    return robots


def part_one(puzzle_input, grid_x, grid_y):
    robots = parse_input(puzzle_input)
    coords = []
    for robot in robots:
        coords.append(robot.coords + 100 * robot.velocity)
    grid = render(coords, grid_x, grid_y)
    np_grid = np.array(grid)
    grid_half_x = grid_x // 2
    grid_half_y = grid_y // 2

    print(
        np.sum(np_grid[:grid_half_y, :grid_half_x])
        * np.sum(np_grid[:grid_half_y, grid_half_x + 1 :])
        * np.sum(np_grid[grid_half_y + 1 :, :grid_half_x])
        * np.sum(np_grid[grid_half_y:, grid_half_x + 1 :])
    )

def scan_grid(np_grid):
    mask = np_grid==0
    cs = np_grid.cumsum(axis=1)
    out = cs-np.maximum.accumulate(np.where(mask, cs, 0), axis=1)
    return np.max(out) >= 10

def part_two(puzzle_input, grid_x, grid_y):
    robots = parse_input(puzzle_input)

    seconds = 0
    while True:
        seconds += 1
        coords = []
        for robot in robots:
            coords.append(robot.coords + seconds * robot.velocity)
        grid = render(coords, grid_x, grid_y)
        np_grid = np.array(grid)
        
        if scan_grid(np_grid):
            grid_half_x = grid_x // 2
            grid_half_y = grid_y // 2
            print_grid(grid)
    
            print(
                np.sum(np_grid[:grid_half_y, :grid_half_x])
                * np.sum(np_grid[:grid_half_y, grid_half_x + 1 :])
                * np.sum(np_grid[grid_half_y + 1 :, :grid_half_x])
                * np.sum(np_grid[grid_half_y:, grid_half_x + 1 :])
            )
            print(f"{seconds=}")
            input()


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example, 11, 7)
    part_one(puzzle.input, 101, 103)
    
    part_two(puzzle.input, 101, 103)
