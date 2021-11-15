while 1:
    M, A, B = map(int, input().split())
    if M == A == B == 0:
        break
    A = A / 3600
    B = B / 3600
    hh = round(abs(M / A - M / B))
    ss = hh % 60
    hh //= 60
    mm = hh % 60
    hh //= 60
    print("{}:{:02}:{:02}".format(hh, mm, ss))
