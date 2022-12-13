puzzle = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


class Noop:
    def __init__(self):
        pass

    def __iter__(self):
        yield


class Add:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        yield
        yield self.x


instructions = []

for instruction in puzzle.split('\n'):
    match instruction.split():
        case ['noop']:
            instructions.append(Noop())
        case ['addx', n]:
            n = int(n)
            instructions.append(Add(n))

display = [['.', ] * 41 for _ in range(6)]
cd = display[0]
x = 1
cycle = 1
for instruction in instructions:
    for val in instruction:
        if cycle in [40, 80, 120, 160, 200]:
            cd = display[cycle // 40]
        sprite = [x, x + 1, x + 2]
        if any(each == cycle % 40 for each in sprite):
            cd[cycle % 40] = '#'
        if val is not None:
            x += val
        cycle += 1
for each in display:
    print(*each[1:], sep='')
