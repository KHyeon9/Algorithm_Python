t = 1
while 1:
    l = int(input())
    if l == 0:
        break

    n = int(input())
    print(f"User {t}")
    for _ in range(n):
        w = int(input())
        print("%.5f" % (w * l / 100000))
    t += 1