for _ in range(int(input())):
    num = input()
    res = []
    now_num = num[0]
    cnt = 0
    for n in num:
        if now_num != n:
            res.append([str(cnt), now_num])
            now_num = n
            cnt = 1
            continue
        cnt += 1
    res.append([str(cnt), now_num])
    res_line = ""
    for el in res:
        res_line += el[0] + el[1]

    print(res_line)
