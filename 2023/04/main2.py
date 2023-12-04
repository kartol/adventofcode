import numpy as np

import puzzle

def price_card(card):
    _, rhs = card.split(': ')
    numbers, winning_numbers = rhs.split(' | ')
    numbers = [int(n) for n in numbers.split()]
    winning_numbers = [int(n) for n in winning_numbers.split()]
    return len(set(numbers) & set(winning_numbers))


def main():
    puzzle_input = puzzle.input
    arr = np.ones(len(puzzle_input.split('\n')), dtype=np.int32)
    for i, card in enumerate(puzzle_input.split('\n')):
        number_of_copies = price_card(card)
        arr[i+1: i+1+number_of_copies] += arr[i]
    print(arr.sum())

if __name__ == "__main__":
    main()
