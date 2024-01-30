for _ in range(int(input())):
    l, d = map(int, input().split(':'))
    l_win, d_win = 0, 0

    for i in range(10):
        for j in range(10):
            if l + i > d + j:
                l_win += 1
            elif l + i < d + j:
                d_win += 1
            else:
                if i > d:
                    l_win += 1
                elif i < d:
                    d_win += 1

    print(l_win, d_win)