import puzzle

cubes_max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def set_possible(cube_set):
    for each in cube_set.split(', '):
        amount, color = each.split(' ')
        if int(amount) > cubes_max[color]:
            return False
    return True

def solve_line(line):
    game, line = line.split(': ')
    game_id = game.split(' ')[1]
    possible = [set_possible(cube_set) for cube_set in line.split('; ')]
    if all(possible):
        return int(game_id)
    return 0

def main():
    s = 0
    for line in puzzle.input.split("\n"):
        s += solve_line(line)
    print(s)


if __name__ == "__main__":
    main()
