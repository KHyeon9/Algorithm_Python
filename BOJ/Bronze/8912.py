for _ in range(int(input())):
    n = int(input())
    sell_list = list(map(int, input().split()))
    res = 0
    for i in range(n):
        for j in range(i):
            if sell_list[j] <= sell_list[i]:
                res += 1
    print(res)

