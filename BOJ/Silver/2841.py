from sys import stdin
input = stdin.readline

strings = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

n, m = map(int, input().split())
res = 0

for _ in range(n):
    s, f = map(int, input().split())

    while True:
        if len(strings[s]) > 0 and strings[s][-1] == f:
            break

        res += 1

        if not len(strings[s]) or strings[s][-1] < f:
            strings[s].append(f)
            break
        else:
            t = strings[s].pop()

print(res)