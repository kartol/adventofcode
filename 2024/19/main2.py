from functools import cache


class Collection:
    def __init__(self, stripes) -> None:
        self.stripes = stripes

    @cache
    def is_in_collection(self, towel: str) -> int:
        if towel == "":
            return 1
        return sum(self.is_in_collection(towel[len(stripe) :]) for stripe in self.stripes if towel.startswith(stripe))


def parse_input(puzzle_input):
    stripes, towels = puzzle_input.split("\n\n")
    return stripes.split(", "), towels.split("\n")


def part_two(puzzle_input):
    stripes, towels = parse_input(puzzle_input)
    collection = Collection(stripes)
    print(sum(collection.is_in_collection(towel) for towel in towels))


if __name__ == "__main__":
    import puzzle

    part_two(puzzle.example)
    part_two(puzzle.input)
