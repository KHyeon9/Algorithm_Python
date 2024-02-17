arr = ["zilch", "double", "double-double", "triple-double"]
for _ in range(int(input())):
    nums = list(map(int, input().split()))
    res = 0

    for n in nums:
        if n >= 10:
            res += 1

    print(*nums)
    print(arr[res])
    print()