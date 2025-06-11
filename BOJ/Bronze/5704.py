alpa = []
for i in range(26):
    alpa.append(chr(97 + i))

while True:
    line = list(set(input().replace(" ", "")))

    if line[0] == "*":
        break

    line.sort()
    print("Y" if line == alpa else "N")
