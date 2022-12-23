import ast
import itertools

puzzle = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
pairs = []
for pair in puzzle.split('\n\n'):
    x, y = pair.split('\n')
    x = ast.literal_eval(x)
    y = ast.literal_eval(y)
    pairs.append((x, y))


def compare(left, right):
    print(f"COMPARE {left} vs {right}")
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print("Left side is smaller, so inputs are in the right order")
            return True
        if left > right:
            print("Right side ran out of items, so inputs are not in the right order")
            return False
    if isinstance(left, list) and isinstance(right, list):
        for l, r in itertools.zip_longest(left, right):
            if l is None:
                print("Left side ran out of items, so inputs are in the right order")
                return True
            if r is None:
                print("Right side ran out of items, so inputs are not in the right order")
                return False
            res = compare(l, r)
            if res is None:
                continue
            return res
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)


s = 0
for i, (left, right) in enumerate(pairs, 1):
    if compare(left, right) is True:
        s += i

print(s)
