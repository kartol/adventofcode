import puzzle


def find_digit(line):
    for char in line:
        if char.isdigit():
            return char
    raise ValueError("no digit found")


def main():
    s = 0
    for line in puzzle.input.split("\n"):
        fist_digit = find_digit(line)
        last_digit = find_digit(line[::-1])
        s += int(fist_digit + last_digit)
    print(s)


if __name__ == "__main__":
    main()
