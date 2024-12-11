from collections import defaultdict


def part_one(puzzle_input, blinks):
    stones = [int(each) for each in puzzle_input.split(" ")]

    new_stones = []
    for i in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) >= 2 and len(str(stone))%2==0:
                str_stone = str(stone)
                len_str_stone = len(str(stone))
                new_stones.extend([int(str_stone[:len_str_stone//2]), int(str_stone[len_str_stone//2:])])
            else:
                new_stones.append(stone*2024)
        stones = new_stones
    
    print(len(new_stones))


def part_two(puzzle_input, blinks):
    stones = [int(each) for each in puzzle_input.split(" ")]
    stone_dict = defaultdict(int)
    for stone in stones:
        stone_dict[stone] += 1

    new_dict = defaultdict(int)
    for i in range(blinks):
        new_dict = defaultdict(int)
        for stone, counter in stone_dict.items():
            if stone == 0:
                new_dict[1] += counter
            elif len(str(stone))%2:
                new_dict[stone*2024] += counter
            else:
                str_stone = str(stone)
                len_str_stone = len(str(stone))
                new_dict[int(str_stone[:len_str_stone//2])] += counter
                new_dict[int(str_stone[len_str_stone//2:])] += counter
        stone_dict = new_dict
    
    print(sum(x for x in new_dict.values()))


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example,6)
    part_one(puzzle.example,25)
    part_one(puzzle.input,25)
    
    part_two(puzzle.example,6)
    part_two(puzzle.example,25)
    part_two(puzzle.input,25)
    part_two(puzzle.input,75)
