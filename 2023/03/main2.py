puzzle = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
res = 0
all_rs = puzzle.split('\n')
i = 0
while i < len(all_rs) // 3:
    rs = all_rs[i * 3:(i + 1) * 3]
    i += 1
    x = set(rs[0])
    for each in rs:
        x = x.intersection(set(each))
    ch = x.pop()
    val = ord(ch) - 96 if ch.islower() else ord(ch) - 38
    res += val

print(res)
