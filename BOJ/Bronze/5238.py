for _ in range(int(input())):
    nums = list(map(int, input().split()))
    n = nums[0]
    nums = nums[1:]
    flag = True

    for i in range(2, n):
        if nums[i - 2] + nums[i - 1] != nums[i]:
            flag = False
            break
    print("YES" if flag else "NO")