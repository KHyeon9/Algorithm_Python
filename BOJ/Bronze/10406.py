w, n, p = map(int, input().split())
h = list(map(int, input().split()))
r = 0

for i in range(p):
    if w <= h[i] <= n:
        r += 1

print(r)
