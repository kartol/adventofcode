from collections import Counter
from functools import cmp_to_key

import puzzle

base_price = {
    "A": 13, "K": 12, "Q": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1
}


class Hand:
    def __init__(self, cards: str, bid):
        self.cards_counter = sorted(Counter(cards).items(), key=lambda x: x[1], reverse=True)
        self.cards = cards
        self.bid = bid

    @property
    def strength_order(self):
        joker_id = self.cards.find("J")
        if joker_id != -1:
            return max(Hand(self.cards[:joker_id] + c + self.cards[joker_id + 1:], 0).strength_order for c in
                       list(base_price.keys())[:-1])
        if self.cards_counter[0][1] == 5:
            return 7
        if self.cards_counter[0][1] == 4:
            return 6
        if self.cards_counter[0][1] == 3 and self.cards_counter[1][1] == 2:
            return 5
        if self.cards_counter[0][1] == 3:
            return 4
        if self.cards_counter[0][1] == 2 and self.cards_counter[1][1] == 2:
            return 3
        if self.cards_counter[0][1] == 2:
            return 2
        return 1


def compare(hand: Hand, other_hand: Hand):
    if hand.strength_order == other_hand.strength_order:
        for card, other_card in zip(hand.cards, other_hand.cards):
            if card == other_card:
                continue
            return base_price[card] - base_price[other_card]
    return hand.strength_order - other_hand.strength_order


def main():
    hands = []
    for line in puzzle.input.split("\n"):
        hand, bid = line.split()
        hands.append(Hand(hand, int(bid)))

    x = sorted(hands, key=cmp_to_key(compare))
    answer = 0
    for i, hand in enumerate(x, 1):
        answer += hand.bid * i
    print(answer)


if __name__ == "__main__":
    main()
