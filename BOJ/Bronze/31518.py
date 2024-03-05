n = int(input())
cnt = 0

for _ in range(3):
    nums = list(map(int, input().split()))

    if 7 in nums:
        cnt += 1

print(777 if cnt >= 3 else 0)