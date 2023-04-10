while 1:
    try:
        nums = list(map(int, input().split()))
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(nums[i] * nums[i + 1])
            elif i == len(nums) - 1:
                result.append(nums[i - 1] * nums[i])
            else:
                result.append(nums[i - 1] * nums[i] * nums[i + 1])
        print(*result)

    except EOFError:
        break