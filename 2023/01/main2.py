import puzzle

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_substr(line, substr):
    try:
        return line.index(substr)
    except ValueError:
        return len(line) + 1


def find_digit(line, reverse=False):
    found_min = "0"
    index_min = len(line) + 1
    for digit_str, digit in digits.items():
        if reverse:
            digit_str = digit_str[::-1]
        index = min(find_substr(line, digit_str), find_substr(line, digit))
        if index < index_min:
            index_min = index
            found_min = digit
    if index_min == len(line) + 1:
        raise ValueError("no digit found")
    return found_min


def main():
    s = 0
    for line in puzzle.input.split("\n"):
        fist_digit = find_digit(line)
        last_digit = find_digit(line[::-1], reverse=True)
        s += int(fist_digit + last_digit)
    print(s)


if __name__ == "__main__":
    main()
