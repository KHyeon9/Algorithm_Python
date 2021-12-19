n = list(map(int, input().split()))

r = sum(n) - max(n) - min(n)

print(r)