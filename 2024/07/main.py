from itertools import product

def parse_input(puzzle_input):
    equations = []
    for line in puzzle_input.split("\n"):
        y, rest = line.split(": ")
        y = int(y)
        equations.append((y, [int(each) for each in rest.split(" ")]))
        
    return equations


def evaluate(terms, operators):
    val = terms[0]
    for term, operator in zip(terms[1:], operators):
        if operator == "+":
            val += term
        if operator == "*":
            val *= term
        if operator == "|":
            val = int(str(val) + str(term))
    return val
    

def part_one(puzzle_input):
    equations = parse_input(puzzle_input)
    s = 0
    for y, terms in equations:
        for operators in product("+*", repeat=len(terms)-1):
            val = evaluate(terms, operators)
            if val != y:
                continue
            s += val
            break
    print(s)


def part_two(puzzle_input):
    equations = parse_input(puzzle_input)
    s = 0
    for y, terms in equations:
        for operators in product("+*|", repeat=len(terms)-1):
            val = evaluate(terms, operators)
            if val != y:
                continue
            s += val
            break
    print(s)



if __name__ == "__main__":
    from puzzle import input

    part_one(input)
    part_two(input)
