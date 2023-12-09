import puzzle


def main():
    instructions, edges = puzzle.input.split("\n\n")

    connections = {}
    for edge in edges.split("\n"):
        s, rhs = edge.split(" = ")
        l, r = rhs[1:-1].split(', ')
        connections[s] = (l, r)

    current = "AAA"
    i = 0
    while current != "ZZZ":
        direction = instructions[i % len(instructions)]
        current = connections[current][0] if direction == "L" else connections[current][1]
        i += 1
    print(i)


if __name__ == "__main__":
    main()
