n, m = map(int, input().split())

res = min(n + m, min(n, m) * 2 + 1)

print(res)