a, b = map(int, input().split())
r = 0
inc = 1
for i in range(b, -1, -1):
    r += inc
    inc += a - 2
print(r)