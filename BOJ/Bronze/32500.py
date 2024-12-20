from collections import defaultdict

lottery = defaultdict(int)
n = int(input())

for _ in range(n * 10):
    nums = list(map(int, input().split()))
    for num in nums:
        lottery[num] += 1

res = [num for num, cnt in lottery.items() if cnt > n * 2]

if res:
    print(" ".join(map(str, sorted(res))))
else:
    print(-1)