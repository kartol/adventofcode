puzzle = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
res = 0
for rs in puzzle.split('\n'):
    first = rs[:len(rs) // 2]
    second = rs[len(rs) // 2:]
    x = set(first).intersection(set(second))
    ch = x.pop()
    val = ord(ch) - 96 if ch.islower() else ord(ch) - 38
    res += val

print(res)
