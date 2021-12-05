while 1:
    try:
        s = input()
        s2 = input()
    except EOFError:
        break
    r = []
    for i in s:
        if i in s2:
            if min(s.count(i), s2.count(i)) > r.count(i):
                r.append(i)
    print(''.join(sorted(r)))