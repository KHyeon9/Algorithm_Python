for _ in range(int(input())):
    s = input()
    res = s[0]
    for i in s[1:]:
        if i != res[-1]:
            res += i
    print(res)
