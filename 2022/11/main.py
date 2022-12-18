class Item:
    def __init__(self, wl):
        self.wl = wl


class Monkey:
    def __init__(self, items: list[int], operation, test):
        self.items: list[Item] = [Item(it) for it in items]
        self.operation = operation
        self.test = test
        self.inspect_rate = 0

    def inspects(self, item):
        self.inspect_rate += 1
        self.operation(item)
        item.wl = item.wl // 3

    def test_item(self, item):
        self.test(item)

    def remove_items(self):
        self.items = []


class Monkeys:
    def __init__(self):
        self.monkeys: list[Monkey] = []

    def add_monkey(self, monkey):
        self.monkeys.append(monkey)
        return self

    def pass_item(self, monkey_no, item):
        self.monkeys[monkey_no].items.append(item)

    def __iter__(self):
        return iter(self.monkeys)


monkeys = Monkeys()


def test_wrap(x, m1, m2):
    def test(item):
        if item.wl % x == 0:
            monkeys.pass_item(m1, item)
        else:
            monkeys.pass_item(m2, item)

    return test


def operation_wrap(op):
    def operation(item):
        item.wl = op(item.wl)

    return operation


monkeys.add_monkey(
    Monkey(
        items=[91, 58, 52, 69, 95, 54],
        operation=operation_wrap(lambda x: x * 13),
        test=test_wrap(7, 1, 5),
    )
).add_monkey(
    Monkey(
        items=[80, 80, 97, 84],
        operation=operation_wrap(lambda x: x * x),
        test=test_wrap(3, 3, 5),
    )
).add_monkey(
    Monkey(
        items=[86, 92, 71],
        operation=operation_wrap(lambda x: x + 7),
        test=test_wrap(2, 0, 4),
    )
).add_monkey(
    Monkey(
        items=[96, 90, 99, 76, 79, 85, 98, 61],
        operation=operation_wrap(lambda x: x + 4),
        test=test_wrap(11, 7, 6),
    )
).add_monkey(
    Monkey(
        items=[60, 83, 68, 64, 73],
        operation=operation_wrap(lambda x: x * 19),
        test=test_wrap(17, 1, 0),
    )
).add_monkey(
    Monkey(
        items=[96, 52, 52, 94, 76, 51, 57],
        operation=operation_wrap(lambda x: x + 3),
        test=test_wrap(5, 7, 3),
    )
).add_monkey(
    Monkey(
        items=[75],
        operation=operation_wrap(lambda x: x + 5),
        test=test_wrap(13, 4, 2),
    )
).add_monkey(
    Monkey(
        items=[83, 75],
        operation=operation_wrap(lambda x: x + 1),
        test=test_wrap(19, 2, 6),
    )
)

for round in range(20):
    for monkey in monkeys:
        for i, item in enumerate(monkey.items):
            monkey.inspects(item)
            monkey.test_item(item)
        monkey.remove_items()

m = sorted(monkeys.monkeys, key=lambda x: x.inspect_rate)
print(m[-2].inspect_rate * m[-1].inspect_rate)
