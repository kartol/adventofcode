from enum import IntEnum
from typing import ClassVar


class Instruction(IntEnum):
    adv = 0
    bxl = 1
    bst = 2
    jnz = 3
    bxc = 4
    out = 5
    bdv = 6
    cdv = 7


class Registers:
    A: ClassVar[int] = 0
    B: ClassVar[int] = 0
    C: ClassVar[int] = 0


def combo_operand(operand) -> int:
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return Registers.A
    if operand == 5:
        return Registers.B
    if operand == 6:
        return Registers.C
    raise ValueError("???")


def run_instruction(instruction: Instruction, operand):
    match instruction:
        case Instruction.adv:
            # A / (2 ** COMBO)
            Registers.A = int(Registers.A / 2 ** combo_operand(operand))
        case Instruction.bxl:
            Registers.B = Registers.B ^ operand
        case Instruction.bst:
            Registers.B = combo_operand(operand) % 8
        case Instruction.jnz:
            if Registers.A == 0:
                return None
            return operand
        case Instruction.bxc:
            Registers.B = Registers.B ^ Registers.C
        case Instruction.out:
            print(combo_operand(operand) % 8, end=",")
        case Instruction.bdv:
            Registers.B = int(Registers.A / 2 ** combo_operand(operand))
        case Instruction.cdv:
            Registers.C = int(Registers.A / 2 ** combo_operand(operand))
    return None


def parse_input(puzzle_input):
    regs, program = puzzle_input.split("\n\n")
    a, b, c = regs.splitlines()
    a = int(a.removeprefix("Register A: "))
    b = int(b.removeprefix("Register B: "))
    c = int(c.removeprefix("Register C: "))
    program = [int(each) for each in program.removeprefix("Program: ").split(",")]
    return program, a, b, c


def part_one(puzzle_input):
    program, a, b, c = parse_input(puzzle_input)
    Registers.A = a
    Registers.B = b
    Registers.C = c

    instruction_pointer = 0
    while instruction_pointer < len(program) - 1:
        instruction = Instruction(program[instruction_pointer])
        operand = program[instruction_pointer + 1]
        jump = run_instruction(instruction, operand)
        if jump is None:
            instruction_pointer += 2
        else:
            instruction_pointer = jump
    print()


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example)
    part_one(puzzle.input)
