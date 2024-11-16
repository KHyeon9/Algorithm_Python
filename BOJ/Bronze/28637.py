for _ in range(int(input())):
    s = input()
    res = s[0].lower()

    for w in s[1:]:
        if w.isupper():
            res += "_" + w.lower()
            continue
        res += w

    print(res)
