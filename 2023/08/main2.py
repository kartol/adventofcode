from math import lcm

import puzzle


def main():
    instructions, edges = puzzle.input.split("\n\n")

    connections = {}
    starting_nodes = []
    ending_nodes = []
    for edge in edges.split("\n"):
        s, rhs = edge.split(" = ")
        l, r = rhs[1:-1].split(', ')
        connections[s] = (l, r)
        if s[-1] == "A":
            starting_nodes.append(s)
        if s[-1] == "Z":
            ending_nodes.append(s)

    distances = []
    for current in starting_nodes:
        i = 0
        while current not in ending_nodes:
            direction = instructions[i % len(instructions)]
            current = connections[current][0] if direction == "L" else connections[current][1]
            i += 1
        distances.append(i)

    print(lcm(*distances))


if __name__ == "__main__":
    main()
