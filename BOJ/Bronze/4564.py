while 1:
    num = int(input())
    if num == 0:
        break
    res = [num]
    while 1:
        n = 1
        if len(str(num)) == 1:
            break
        for i in str(num):
            n *= int(i)

        res.append(n)
        num = n
    print(*res)
