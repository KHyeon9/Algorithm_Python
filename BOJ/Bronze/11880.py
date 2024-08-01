from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    line = list(map(int, input().split()))
    res = []

    for i in range(3):
        res.append(line[i] ** 2 + (sum(line) - line[i]) ** 2)

    print(min(res))