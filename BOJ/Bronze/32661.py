max_res, min_res = 0, 1e9

for _ in range(int(input())):
    p = int(input())

    max_res = max(max_res, p)
    min_res = min(min_res, p)

print(max(0, min_res - max_res // 2))
