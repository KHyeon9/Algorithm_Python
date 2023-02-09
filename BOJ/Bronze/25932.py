t = int(input())
for i in range(t):
    nums = list(map(int, input().split()))
    Mack = True if 18 in nums else False
    Zack = True if 17 in nums else False
    print(*nums)
    if Mack and Zack:
        print("both")
    elif Mack:
        print("mack")
    elif Zack:
        print("zack")
    else:
        print("none")
    if i != t - 1:
        print()