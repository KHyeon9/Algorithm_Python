n, m = map(int, input().split())
res = 1

for _ in range(n):
    deck = int(input())
    if deck == 0:
        deck = 1
    res *= deck
print(res % m)