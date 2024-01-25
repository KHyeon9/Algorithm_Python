for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    alpa = list("abcdefghijklmnopqrstuvwxyz")
    res = []

    for num in nums:
        temp = alpa.pop(num)
        alpa.insert(0, temp)
        res.append(temp)

    print(*res, sep="")