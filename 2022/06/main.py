puzzle = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
for i in range(4, len(puzzle)):
    if len(set(puzzle[i - 4:i])) == 4:
        print(i)
        break
