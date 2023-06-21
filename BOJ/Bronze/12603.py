for t in range(int(input())):
    c = int(input())
    n = int(input())
    prices = list(map(int, input().split()))
    flag = False
    res1, res2 = 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] + prices[j] == c:
                flag = True
                res1 = i + 1
                res2 = j + 1
                break
        if flag:
            break
    print(f"Case #{t + 1}: {res1} {res2}")
