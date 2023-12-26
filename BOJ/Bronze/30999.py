n, m = map(int, input().split())
res = 0

for _ in range(n):
    line = input()

    if len(line) / 2 < line.count("O"):
        res += 1

print(res)