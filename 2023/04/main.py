import puzzle

def price_card(card):
    _, rhs = card.split(': ')
    numbers, winning_numbers = rhs.split(' | ')
    numbers = [int(n) for n in numbers.split()]
    winning_numbers = [int(n) for n in winning_numbers.split()]
    return int(2**(len(set(numbers) & set(winning_numbers)) - 1))


def main():
    s = 0
    for card in puzzle.input.split('\n'):
        s += price_card(card)
    print(s)

if __name__ == "__main__":
    main()
