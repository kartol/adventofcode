puzzle = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

solutions = 0
for line in puzzle.split('\n'):
    sequences = [[int(x) for x in each.split('-')] for each in line.split(',')]
    first_assignments = set(range(sequences[0][0], sequences[0][1] + 1))
    second_assignments = set(range(sequences[1][0], sequences[1][1] + 1))
    if first_assignments.intersection(second_assignments):
        solutions += 1

print(solutions)
