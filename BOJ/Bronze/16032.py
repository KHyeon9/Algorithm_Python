while True:
    n = int(input())

    if n == 0:
        break

    nums = list(map(int, input().split()))
    avg = sum(nums) / len(nums)
    res = 0

    for num in nums:
        if num <= avg:
            res += 1

    print(res)
