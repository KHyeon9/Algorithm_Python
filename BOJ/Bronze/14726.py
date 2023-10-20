for _ in range(int(input())):
    num = input()
    res = ""

    for i in range(len(num)):
        if i % 2 != 0:
            res += num[i]
        else:
            n = int(num[i]) * 2
            if n >= 10:
                temp = str(n)
                n = int(temp[0]) + int(temp[1])

            res += str(n)
    sum_res = sum(list(map(int, res)))

    print("T" if sum_res % 10 == 0 else "F")



