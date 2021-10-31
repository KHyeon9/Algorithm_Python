p = 0
r = 0

for i in range(10):
    a, b = map(int, input().split())
    p += b - a

    if r < p:
        r = p

print(r)