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
    pairs.append(x)
    y = ast.literal_eval(y)
    pairs.append(y)


def compare(left, right):
    print(f"COMPARE {left} vs {right}")
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print("Left side is smaller, so inputs are in the right order")
            return 1
        if left > right:
            print("Right side ran out of items, so inputs are not in the right order")
            return -1
    if isinstance(left, list) and isinstance(right, list):
        for l, r in itertools.zip_longest(left, right):
            if l is None:
                print("Left side ran out of items, so inputs are in the right order")
                return 1
            if r is None:
                print("Right side ran out of items, so inputs are not in the right order")
                return -1
            res = compare(l, r)
            if res == 0:
                continue
            return res
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    return 0


pairs.append([[2]])
pairs.append([[6]])

from functools import cmp_to_key

x = sorted(pairs, key=cmp_to_key(compare), reverse=True)
print((x.index([[2]]) + 1) * (x.index([[6]]) + 1))
