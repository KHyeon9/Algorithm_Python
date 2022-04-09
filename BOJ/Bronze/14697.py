a, b, c, n = map(int, input().split())
result = False

for i in range(n // c + 1):
    for j in range(n // b + 1):
        for k in range(n // a + 1):
            if a * k + b * j + c * i == n:
                result = True
if result:
    print(1)
else:
    print(0)