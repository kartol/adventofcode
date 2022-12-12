puzzle = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
for i in range(14, len(puzzle)):
    if len(set(puzzle[i - 14:i])) == 14:
        print(i)
        break
