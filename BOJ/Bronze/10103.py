t = int(input())
r1 = r2 = 100

for i in range(t):
    c, s = list(map(int, input().split()))

    if c > s:
        r2 -= c

    elif c < s:
        r1 -= s

print(r1)
print(r2)