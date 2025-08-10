line = list(input().split("()"))
print("correct" if len(line[0]) == len(line[1]) else "fix")