m, h = map(int, input().split())
res = 0

for _ in range(int(input())):
    c, b = map(int, input().split())

    res += c * m if c * m > b * h else b * h

print(res)