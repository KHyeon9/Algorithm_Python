for _ in range(int(input())):
    n = int(input())
    res = 0
    while n != 6174:
        temp = list(str(n))
        n = int("".join(sorted(temp, reverse=True))) - int("".join(sorted(temp)))
        res += 1

        if n < 1000:
            n = int(str(n) + "0" * (4 - len(str(n))))
    print(res)