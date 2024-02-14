a, b = 0, 0
line = input()
for i in range(0, len(line), 2):
    if line[i] == "A":
        a += int(line[i + 1])
    else:
        b += int(line[i + 1])

print("A" if a > b else "B")