n, m = map(int, input().split())

for i in range(max(n, m) - min(n, m) - 1, -2, -1):
    print(max(n, m) - i)
