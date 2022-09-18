while 1:
    s = input()
    if s == '#':
        break
    res = 0
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        res += (i + 1) * (ord(s[i]) - ord('A') + 1)
    print(res)