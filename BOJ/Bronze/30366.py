n, m = map(int, input().split())
a_list = list(map(int, input().split()))
now, res = 0, 0

for a in a_list:
    if now + a > m:
        res += 1
        now = 0
    now += a
    print(res)

