while 1:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    a = list(map(int, input().split()))
    cost = m // n
    result = 0

    for i in a:
        if cost <= i:
            result += cost
        else:
            result += i
    print(result)