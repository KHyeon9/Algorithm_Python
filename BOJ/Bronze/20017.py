n, m, a = map(int, input().split())
b_list = list(map(int, input().split()))
res = 0

for i in range(n * m - m):
    if 2 * b_list[i] < b_list[i + m]:
        res += a

print(res)