for _ in range(int(input())):
    line = input()
    res = ""
    now = line[0]
    cnt = 1

    for el in line[1:]:
        if el != now:
            res += str(cnt) + " " + now + " "
            now = el
            cnt = 1
            continue
        cnt += 1
    res += str(cnt) + " " + now

    print(res)
