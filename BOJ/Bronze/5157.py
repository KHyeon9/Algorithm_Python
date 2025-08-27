for t in range(int(input())):
    C, B, n, r = map(int, input().split())
    bailout = list(map(int, input().split()))
    res = 0

    for _ in range(n):
        ci, bi = map(int, input().split())
        if ci in bailout:
            res += bi * r // 100

    print(f"Data Set {t + 1}:")
    print(res)
    print()