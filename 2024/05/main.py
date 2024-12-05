from black.trans import defaultdict


def parse_input(puzzle_input):
    rules_input, prints_input = puzzle_input.split("\n\n")
    rules = []
    for rule in rules_input.split("\n"):
        x, y = rule.split("|")
        rules.append((int(x), int(y)))

    updates_list = []
    for printing in prints_input.split("\n"):
        updates = [int(each) for each in printing.split(",")]
        updates_list.append(updates)

    return rules, updates_list


def part_one(puzzle_input):
    rules, updates_list = parse_input(puzzle_input)

    rule_dict = defaultdict(set)
    for x, y in rules:
        rule_dict[x].add(y)

    s = 0
    for updates in updates_list:
        printed = set()
        for update in updates:
            if printed.intersection(rule_dict[update]):
                break
            printed.add(update)
        else:
            s += updates[len(updates) // 2]

    print(s)


def find_broken_rule(updates, rule_dict):
    printed = set()
    for update in updates:
        if x := printed.intersection(rule_dict[update]):
            return update, list(x)[0]
        printed.add(update)


def swap(lst, x, y):
    idx_x = lst.index(x)
    idx_y = lst.index(y)
    lst[idx_x] = y
    lst[idx_y] = x


def price(updates, rule_dict):
    while broken_rule := find_broken_rule(updates, rule_dict):
        x, y = broken_rule
        swap(updates, x, y)

    return updates[len(updates) // 2]


def part_two(puzzle_input):
    rules, updates_list = parse_input(puzzle_input)

    rule_dict = defaultdict(set)
    for x, y in rules:
        rule_dict[x].add(y)

    s = 0
    for updates in updates_list:
        if not find_broken_rule(updates, rule_dict):
            continue
        s += price(updates, rule_dict)

    print(s)


if __name__ == "__main__":
    from puzzle import input

    part_one(input)
    part_two(input)
