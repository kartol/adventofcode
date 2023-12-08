import puzzle


def main():
    puzzle_input = puzzle.input
    time = int("".join(puzzle_input.split("\n")[0].split(":")[1].split()))
    record_distance = int("".join(puzzle_input.split("\n")[1].split(":")[1].split()))
    answer = 0
    for i in range(time):
        travel_for = time - i
        velocity = i
        distance = travel_for * velocity
        if distance > record_distance:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
