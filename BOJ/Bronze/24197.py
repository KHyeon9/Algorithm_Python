n, m = map(int, input().split())
position = list(map(int, input().split()))
now, res = 1, 0

for p in position:
    res += min((now - p + n) % n, (p - now + n) % n)
    now = p

print(res)