for _ in range(int(input())):
    s = input()

    sum1 = 0
    for n in s:
        sum1 += int(n)
    sum2 = int(s[-3:]) * 10
    res = sum1 + sum2

    if res < 1000:
        res += 1000
    print(str(res)[-4:])