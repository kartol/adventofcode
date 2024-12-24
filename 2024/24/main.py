import operator


def parse_input(puzzle_input):
    init_state, gates = puzzle_input.split("\n\n")

    init_states = {}
    for each in init_state.splitlines():
        wire_name, wire_value = each.split(": ")
        init_states[wire_name] = int(wire_value)

    gates_dict = {}
    for gate in gates.splitlines():
        x, output_wire = gate.split(" -> ")
        input_wire_1, operation, input_wire_2 = x.split(" ")
        if operation == "AND":
            op = operator.and_
        elif operation == "XOR":
            op = operator.xor
        elif operation == "OR":
            op = operator.or_
        else:
            raise ValueError(f"not supported {operation=}")
        gates_dict[output_wire] = (input_wire_1, op, input_wire_2)

    return init_states, gates_dict


def get_wire_value(init_states, gates_dict, output_wire):
    if output_wire in init_states:
        return init_states[output_wire]
    gate = gates_dict[output_wire]
    return gate[1](get_wire_value(init_states, gates_dict, gate[0]), get_wire_value(init_states, gates_dict, gate[2]))


def part_one(puzzle_input):
    init_states, gates_dict = parse_input(puzzle_input)
    output_wires = []
    for output_wire in gates_dict:
        if output_wire.startswith("z"):
            output_wires.append(output_wire)

    output_wires = sorted(output_wires, key=lambda x: -int(x[1:]))
    number = []
    for output_wire in output_wires:
        number.append(str(get_wire_value(init_states, gates_dict, output_wire)))

    print(int("".join(number), 2))


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example)
    part_one(puzzle.example2)
    part_one(puzzle.input)
