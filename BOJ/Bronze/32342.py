for _ in range(int(input())):
    s = input()
    res = 0

    for i in range(len(s) - 2):
        if s[i:i+3] == "WOW":
            res += 1

    print(res)