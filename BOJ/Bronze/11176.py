for _ in range(int(input())):
    e, n = map(int, input().split())
    res = 0

    for _ in range(n):
        b = int(input())

        if b > e:
            res += 1
    print(res)