n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

if n > m:
    b_list += [0] * (n - m)
elif m > n:
    a_list += [0] * (m - n)

res = 0
for i in range(max(n, m)):
    res = max(res, b_list[i] - a_list[i])

print(res)