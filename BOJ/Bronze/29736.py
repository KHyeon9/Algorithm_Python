a, b = map(int, input().split())
k, x = map(int, input().split())

res = min(k + x, b) - max(k - x, a) + 1
print(res if res > 0 else "IMPOSSIBLE")