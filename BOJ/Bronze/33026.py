n = int(input())
line = input()
res = -1

for i in range(1, n):
    flag1 = line[:i].count("L") != line[i:].count("L")
    flag2 = line[:i].count("O") != line[i:].count("O")

    if flag1 and flag2:
        res = i
        break

print(res)
