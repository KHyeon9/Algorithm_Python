n = int(input())
n_list = list(map(int, input().split()))
res = 0

for i in range(n):
    x, y = map(int, input().split())

    if n_list[i]:
        res += y - x if y - x > 0 else 0

print(res)