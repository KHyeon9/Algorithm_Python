n, k = map(int, input().split())
nums = list(map(int, input().split()))
count = [0] * (max(nums) + 1)
left, right, result = 0, 0, 0
while right < n:
    if count[nums[right]] < k:
        count[nums[right]] += 1
        right += 1
    else:
        count[nums[left]] -= 1
        left += 1
    result = max(right - left, result)
print(result)