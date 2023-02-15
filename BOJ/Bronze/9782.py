case = 0
while 1:
    case += 1
    nums = list(map(float, input().split()))
    if nums[0] == 0:
        break
    nums = nums[1:]
    lenth = len(nums) // 2
    res = nums[lenth] if len(nums) % 2 == 1 else (nums[lenth] + nums[lenth - 1]) / 2

    print(f"Case {case}: {res}")