n, m = map(int, input().split())

s = list(map(int, input().split())) + [0] * m

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(n + m):
        s[i] -= t[j]
        s[j] += t[j]

print(*s)
