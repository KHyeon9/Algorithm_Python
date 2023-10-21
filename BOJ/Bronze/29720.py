n, m, k = map(int, input().split())

r_min = max(n - (m * k), 0)
r_max = n - m * (k - 1) - 1

print(r_min, r_max)