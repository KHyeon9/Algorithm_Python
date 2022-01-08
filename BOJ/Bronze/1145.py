nums = sorted(list(map(int, input().split())))
MIN = nums[0]
while 1:
    cnt = 0
    for i in nums:
        if MIN % i == 0:
            cnt += 1
    if cnt >= 3:
        print(MIN)
        break
    MIN += 1
