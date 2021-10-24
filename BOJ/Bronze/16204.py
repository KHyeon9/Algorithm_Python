n, m, k = map(int, input().split())

fx = n - m
bx = n - k

print(min(m, k) + min(fx, bx))