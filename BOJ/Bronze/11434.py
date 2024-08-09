for t in range(int(input())):
    n, w, e = map(int, input().split())
    res = 0

    for _ in range(n):
        ww, we, ew, ee = map(int, input().split())
        res += max(w * ww + e * ew, w * we + e * ee)

    print(f"Data Set {t + 1}:")
    print(res)
    print()