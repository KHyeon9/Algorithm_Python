n, t = map(int, input().split())
a = list(map(int, input().split()))
r = 0
for i in range(n):
    t -= a[i]
    if t >= 0:
        r += 1

    elif t < 0:
        r = i
        break

print(r)