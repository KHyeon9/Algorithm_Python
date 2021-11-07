while 1:
    time1, time2 = input().split()
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    if h1 == m1 == h2 == m2 == 0:
        break
    t = (h1 + h2) * 60 + m1 + m2
    d = t // 1440
    h = t // 60 % 24
    m = t % 60
    if d == 0:
        print("%02d:%02d" % (h, m))
    else:
        print("%02d:%02d +%d" % (h, m, d))