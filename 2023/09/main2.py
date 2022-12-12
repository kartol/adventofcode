puzzle = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


def distance_x(x, y):
    return x.x - y.x


def distance_y(x, y):
    return x.y - y.y


class Point:
    def __init__(self, x, y, child=None, val='H'):
        self.x = x
        self.y = y
        self.child = child
        self.val = val
        self.visited = set()

    def move_right(self):
        self.y += 1
        if self.child is not None:
            self.child.parent_moved(self)

    def move_left(self):
        self.y -= 1
        if self.child is not None:
            self.child.parent_moved(self)

    def move_up(self):
        self.x -= 1
        if self.child is not None:
            self.child.parent_moved(self)

    def move_down(self):
        self.x += 1
        if self.child is not None:
            self.child.parent_moved(self)

    def parent_moved(self, parent):
        delta_x = distance_x(parent, self)
        delta_y = distance_y(parent, self)
        match abs(delta_x), abs(delta_y):
            case 2, 0:
                self.x += 1 if delta_x > 0 else -1
            case 0, 2:
                self.y += 1 if delta_y > 0 else -1
            case (2, 1) | (1, 2) | (2, 2):
                self.x += 1 if delta_x > 0 else -1
                self.y += 1 if delta_y > 0 else -1
        self.visited.add((self.x, self.y))
        if self.child is not None:
            self.child.parent_moved(self)


class Grid:
    def __init__(self):
        last_tail = None
        tails = []
        for each in range(9, 0, -1):
            tail = Point(x=15, y=11, child=last_tail, val=str(each))
            tails.append(tail)
            last_tail = tail
        self.tails = tails
        self.head = Point(x=15, y=11, child=self.tails[-1])
        self.grid = []

    def render(self):
        self.grid = [26 * ['.', ] for _ in range(21)]
        for tail in self.tails:
            self.grid[tail.x][tail.y] = tail.val
        self.grid[self.head.x][self.head.y] = self.head.val

    def move_right(self):
        self.head.move_right()

    def move_left(self):
        self.head.move_left()

    def move_up(self):
        self.head.move_up()

    def move_down(self):
        self.head.move_down()

    def print(self):
        self.render()
        for each in self.grid:
            print(*each)
        print()


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

# grid.print()
print(len(grid.tails[0].visited))
