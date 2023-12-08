import puzzle


def main():
    puzzle_input = puzzle.input
    times = [int(each) for each in puzzle_input.split("\n")[0].split(":")[1].split()]
    distances = [int(each) for each in puzzle_input.split("\n")[1].split(":")[1].split()]

    answer = 1
    for time, record_distance in zip(times, distances):
        s = 0
        for i in range(time):
            travel_for = time - i
            velocity = i
            distance = travel_for * velocity
            if distance > record_distance:
                s += 1

        answer *= s

    print(answer)

if __name__ == "__main__":
    main()
