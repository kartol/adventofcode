from collections import defaultdict, deque


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
    seq_price = {}
    d = deque(maxlen=4)

    price_number = number % 10
    previous_price_number = price_number
    for _ in range(n_iters):
        number = next_number(number)
        price_number = number % 10
        diff = price_number - previous_price_number
        d.append(diff)
        if len(d) == 4:
            seq = tuple(d)
            if seq not in seq_price:
                seq_price[tuple(d)] = price_number
        previous_price_number = price_number
    return seq_price


def part_two(puzzle_input, n_iters):
    sequences = defaultdict(int)
    for line in puzzle_input.splitlines():
        for seq, price in solve_number(int(line), n_iters).items():
            sequences[seq] += price
    print(max(sequences.values()))


if __name__ == "__main__":
    import puzzle

    part_two(puzzle.example, 100)
    part_two(puzzle.example3, 2000)
    part_two(puzzle.input, 2000)
