def mix(secret_number, to_mix):
    return secret_number ^ to_mix


def prune(secret_number):
    return secret_number % 16777216


def next_number(secret_number):
    secret_number = prune(mix(secret_number, secret_number << 6))
    secret_number = prune(mix(secret_number, secret_number >> 5))
    secret_number = prune(mix(secret_number, secret_number << 11))
    return secret_number


def solve_number(number, n_iters):
    for _ in range(n_iters):
        number = next_number(number)
        print(number % 10)
    return number


def part_one(puzzle_input, n_iters):
    s = 0
    for line in puzzle_input.splitlines():
        s += solve_number(int(line), n_iters)
    print(s)


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example, 10)
    part_one(puzzle.example2, 2000)
    part_one(puzzle.input, 2000)
