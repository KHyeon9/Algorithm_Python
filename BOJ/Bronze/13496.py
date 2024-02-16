for t in range(1, int(input()) + 1):
    n, s, d = map(int, input().split())
    res = 0

    for _ in range(n):
        d_i, v_i = map(int, input().split())

        if s * d >= d_i:
            res += v_i

    print(f"Data Set {t}:")
    print(res)
    print()