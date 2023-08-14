for _ in range(int(input())):
    nums = list(map(int, input().split()))
    prev = nums[0]
    res = 0

    for n in nums[1:-1]:
        if prev * 2 < n:
            res += n - 2 * prev
        prev = n

    print(res)