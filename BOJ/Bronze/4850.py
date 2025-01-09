while True:
    try:
        n, w, d, res = map(int, input().split())

        total_cnt = (n * (n - 1)) // 2
        total_weight = total_cnt * w
        dif_weight = total_weight - res
        answer = dif_weight // d

        print(answer if answer != 0 else n)

    except EOFError:
        break
