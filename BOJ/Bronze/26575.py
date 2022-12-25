for _ in range(int(input())):
    d, f, p = input().split()
    if f[0] == '.':
        f = "0" + f
    if p[0] == '.':
        p = "0" + p
    print("$%.2f" % round(float(d) * float(f) * float(p),2))