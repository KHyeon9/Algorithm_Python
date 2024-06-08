from itertools import combinations

nums = sorted(list(map(int, input().split())))
n = int(input())
res = []

for com in combinations(nums, 2):
    if sum(com) == n and com not in res:
        res.append(com)
        print(*com)

print(len(res))