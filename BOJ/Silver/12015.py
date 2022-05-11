def binary(arr, target, s, e):
    while s < e:
        mid = (s + e) // 2
        if target <= arr[mid]:
            e = mid
        elif target > arr[mid]:
            s = mid + 1
    return e


n = int(input())
nums = list(map(int, input().split()))
dp = [0]
for num in nums:
    if dp[-1] < num:
        dp.append(num)
    else:
        p = binary(dp, num, 0, len(dp) - 1)
        dp[p] = num
print(len(dp) - 1)