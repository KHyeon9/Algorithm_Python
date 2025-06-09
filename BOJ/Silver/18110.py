from sys import stdin
input = stdin.readline

def round_sol(num):
    return int(num + 0.5)

n = int(input())
if n:
    cut = round_sol(n * 0.15)
    level = sorted([int(input()) for _ in range(n)])[cut:n-cut]
    print(round_sol(sum(level) / (n - 2 * cut)))
else:
    print(0)