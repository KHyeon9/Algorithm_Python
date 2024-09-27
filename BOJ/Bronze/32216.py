n, k, t0 = map(int, input().split())
d_list = list(map(int, input().split()))
t, res = t0, 0

for d in d_list:
    if t < k:
        t = t + d + abs(t - k)
    elif t > k:
        t = t + d - abs(t - k)
    else:
        t = t + d

    res += abs(t - k)

print(res)
