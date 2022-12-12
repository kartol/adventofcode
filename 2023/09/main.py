from collections import namedtuple

puzzle = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

Point = namedtuple('Point', ['x', 'y'])


def distance(x, y):
    return abs(x.x - y.x) > 1 or abs(x.y - y.y) > 1


class Grid:
    def __init__(self):
        self.head, self.tail = Point(x=4, y=0), Point(x=4, y=0)
        self.grid = [6 * [0, ] for _ in range(5)]

    def move_right(self):
        self.move(self.head._replace(y=self.head.y + 1))

    def move_left(self):
        self.move(self.head._replace(y=self.head.y - 1))

    def move_up(self):
        self.move(self.head._replace(x=self.head.x - 1))

    def move_down(self):
        self.move(self.head._replace(x=self.head.x + 1))

    def move(self, head):
        if distance(head, self.tail):
            self.tail = self.head
        self.head = head
        self.grid[self.tail.x][self.tail.y] = 1

    def print(self):
        self.grid[self.tail.x][self.tail.y] = 1
        print(*self.grid, sep='\n')


grid = Grid()
for command in puzzle.split('\n'):
    match command.split(' '):
        case ['U', n]:
            n = int(n)
            for _ in range(n):
                grid.move_up()
        case ['D', n]:
            n = int(n)
            for _ in range(n):
                grid.move_down()
        case ['L', n]:
            n = int(n)
            for _ in range(n):
                grid.move_left()
        case ['R', n]:
            n = int(n)
            for _ in range(n):
                grid.move_right()

grid.print()
acc = 0
for e in grid.grid:
    for x in e:
        acc += x
print(acc)
