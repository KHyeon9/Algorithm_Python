for _ in range(int(input())):
    s = list(input().split())
    r = float(s.pop(0))
    for i in range(len(s)):
        if s[i] == '@':
            r *= 3
        elif s[i] == '%':
            r += 5
        elif s[i] == '#':
            r -= 7
    print('%0.2f' % r)