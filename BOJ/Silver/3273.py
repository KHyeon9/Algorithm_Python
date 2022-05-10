n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
start, end = 0, n - 1
cnt = 0
while start < end:
    num_sum = nums[start] + nums[end]
    if num_sum > x:
        end -= 1
    elif num_sum < x:
        start += 1
    else:
        cnt += 1
        start += 1
        end -= 1

print(cnt)
