from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

for _ in range(n):
    s, t = map(int, input().split())

total = 0

for _ in range(m):
    t, p = map(int, input().split())
    total += p

print(f"{total / n:.4f}")