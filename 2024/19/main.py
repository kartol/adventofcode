from functools import cache


class Collection:
    def __init__(self, stripes) -> None:
        self.stripes = stripes

    @cache
    def is_in_collection(self, towel: str) -> bool:
        if towel == "":
            return True
        return any(self.is_in_collection(towel[len(stripe) :]) for stripe in self.stripes if towel.startswith(stripe))


def parse_input(puzzle_input):
    stripes, towels = puzzle_input.split("\n\n")
    return stripes.split(", "), towels.split("\n")


def part_one(puzzle_input):
    stripes, towels = parse_input(puzzle_input)
    collection = Collection(stripes)
    print(sum(int(collection.is_in_collection(towel)) for towel in towels))


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example)
    part_one(puzzle.input)
