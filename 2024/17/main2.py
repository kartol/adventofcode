from dataclasses import dataclass
from enum import IntEnum


class Instruction(IntEnum):
    adv = 0
    bxl = 1
    bst = 2
    jnz = 3
    bxc = 4
    out = 5
    bdv = 6
    cdv = 7


@dataclass
class Registers:
    A: int = 0
    B: int = 0
    C: int = 0


class Computer:
    def __init__(self, a, b, c):
        self.output = []
        self.registers = Registers(a, b, c)

    def combo_operand(self, operand) -> int:
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.registers.A
        if operand == 5:
            return self.registers.B
        if operand == 6:
            return self.registers.C
        raise ValueError("???")

    def run_program(self, program):
        instruction_pointer = 0
        while instruction_pointer < len(program) - 1:
            instruction = Instruction(program[instruction_pointer])
            operand = program[instruction_pointer + 1]
            jump = self.run_instruction(instruction, operand)
            if jump is None:
                instruction_pointer += 2
            else:
                instruction_pointer = jump
        return self.output

    def run_instruction(self, instruction: Instruction, operand):
        match instruction:
            case Instruction.adv:
                self.registers.A >>= self.combo_operand(operand)
            case Instruction.bxl:
                self.registers.B ^= operand
            case Instruction.bst:
                self.registers.B = self.combo_operand(operand) % 8
            case Instruction.jnz:
                if self.registers.A == 0:
                    return None
                return operand
            case Instruction.bxc:
                self.registers.B ^= self.registers.C
            case Instruction.out:
                self.output.append(self.combo_operand(operand) % 8)
            case Instruction.bdv:
                self.registers.B = self.registers.A >> self.combo_operand(operand)
            case Instruction.cdv:
                self.registers.C = self.registers.A >> self.combo_operand(operand)
        return None


def parse_input(puzzle_input):
    regs, program = puzzle_input.split("\n\n")
    a, b, c = regs.splitlines()
    a = int(a.removeprefix("Register A: "))
    b = int(b.removeprefix("Register B: "))
    c = int(c.removeprefix("Register C: "))
    program = [int(each) for each in program.removeprefix("Program: ").split(",")]
    return program, a, b, c


def part_two(puzzle_input):
    program, _, b, c = parse_input(puzzle_input)
    candidates = list(range(8))
    for digit in range(1, 16 + 1):
        new_candidates = []
        for candidate in candidates:
            for i in range(8):
                a = (candidate << 3) + i
                computer = Computer(a, b, c)
                output = computer.run_program(program)
                if output[-digit:] == program[-digit:]:
                    new_candidates.append(a)
        candidates = new_candidates

    a = min(candidates)
    print(a)
    computer = Computer(a, b, c)
    print(*computer.run_program(program), sep=",")


if __name__ == "__main__":
    import puzzle

    part_two(puzzle.input)
