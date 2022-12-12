puzzle = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

map, instructions = puzzle.split('\n\n')
map = map.split('\n')
map_len = max(int(each) for each in map[-1].split('   '))
columns = {c: [] for c in range(map_len)}
map = map[:-1]
for floor in map:
    for i in range(map_len):
        ch = floor[i * 4 + 1]
        if ch != ' ':
            columns[i].append(ch)

for instruction in instructions.split('\n'):
    match instruction.split(' '):
        case ["move", x, "from", a, "to", b]:
            a = int(a) - 1
            b = int(b) - 1
            x = int(x)
            move = columns[a][:x][::-1]
            columns[a] = columns[a][x:]
            columns[b] = move + columns[b]

for each in columns.values():
    print(each[0], end='')
