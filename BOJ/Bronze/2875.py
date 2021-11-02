n, m, k = list(map(int, input().split()))

r = min(min(n//2, m), (n + m - k) // 3)

print(r)
