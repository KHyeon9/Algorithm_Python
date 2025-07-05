a = int(input())
n, m = map(int, input().split())

if n > m:
    n, m = m, n

n /= a

print(n * 2 if n * 2 < m else m)