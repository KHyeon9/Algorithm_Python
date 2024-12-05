line = input().split("(")
station, sub = line[0], line[1][:-1] if len(line) == 2 else ""

print(station)
print(sub if len(sub) != 0 else "-")