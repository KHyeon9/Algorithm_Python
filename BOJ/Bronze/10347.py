incoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    line = list(input().split())

    if line[0] == "0":
        break

    n = int(line[0])
    line = line[1]
    res = ""

    for w in line:
        p = (incoding.index(w) + n) % len(incoding)
        res += incoding[p]

    print(res[::-1])
