for _ in range(int(input())):
    s = input()
    g_cnt = s.count('g') + s.count('G')
    b_cnt = s.count('b') + s.count('B')
    if g_cnt > b_cnt:
        print(s + " is GOOD")
    elif g_cnt < b_cnt:
        print(s + " is A BADDY")
    else:
        print(s + " is NEUTRAL")
