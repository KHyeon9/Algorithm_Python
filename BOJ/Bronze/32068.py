for _ in range(int(input())):
    l, r, s = map(int, input().split())
    l_res, r_res = (s - l) * 2 + 1, (r - s) * 2
    print(l_res if l_res < r_res else r_res)