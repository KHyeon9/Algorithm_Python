n, a, b, c = map(int, input().split())

if n == 1:
    res = 0
elif min(a, b, c) != c:
    res = min(a, b) * (n - 1)
else:
    res = min(a, b) + c * (n - 2)

print(res // 100, res % 100)