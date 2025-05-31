n, d, k = map(int, input().split())
stars = list(map(int, input().split()))

max_star = max(stars)
now, res = 0, 0

for i in range(d):
    now += max_star
    if now > k:
        now = max_star
        res += 1

print(res)