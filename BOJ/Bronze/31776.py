res = 0

for _ in range(int(input())):
    t = list(map(int, input().split()))
    if sum(t) == -3:
        continue

    for i in range(3):
        if t[i] == -1:
            t[i] = 121

    if t[0] <= t[1] <= t[2]:
        res += 1

print(res)