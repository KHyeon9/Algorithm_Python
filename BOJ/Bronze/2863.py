a, b = map(int, input().split())
c, d = map(int, input().split())
m = 0

for i in range(4):
    s = a / c + b / d

    if m < s:
        m = s
        r = i

    a, b, c, d = c, a, d, b

print(r)