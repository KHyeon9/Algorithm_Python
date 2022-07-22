res = 1e9
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a <= b:
        res = min(res, b)
print(res if res != 1e9 else -1)