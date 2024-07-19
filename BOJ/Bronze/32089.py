while True:
    n = int(input())

    if n == 0:
        break

    a_list = list(map(int, input().split()))
    res = 0

    for i in range(n - 2):
        res = max(res, sum(a_list[i:i + 3]))

    print(res)
