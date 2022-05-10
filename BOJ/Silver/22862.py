n, k = map(int, input().split())
nums = list(map(int, input().split()))
right = 0
cnt, jump = 0, 0
result = 0
for left in range(n):
    while jump <= k and right < n:
        if nums[right] % 2 == 0:
            cnt += 1
            result = max(result, cnt)
        else:
            jump += 1
        right += 1
    if nums[left] % 2 == 0:
        cnt -= 1
    else:
        jump -= 1
print(result)