for _ in range(int(input())):
    s = input()
    res = 0
    for i in s:
        if i == ' ':
            continue
        res += ord(i) - 64
    if res == 100:
        print("PERFECT LIFE")
    else:
        print(res)