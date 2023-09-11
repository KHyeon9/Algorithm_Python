while True:
    n = int(input())

    if n == 0:
        break

    nums = ''.join(input().split())
    res = 0

    for i in range(n):
        if nums[i: i + 4] == "2020":
            res += 1

    print(res)