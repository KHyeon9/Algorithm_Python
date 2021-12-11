n, t = map(int, input().split())
r = 0
a = []

for i in range(n):
    a.append(int(input()))

for i in range(n - 1):
    if a[i] - t >= a[i + 1]:
        r += 1

print(r)