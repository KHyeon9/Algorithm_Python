while True:
    h1, m1, h2, m2 = map(int, input().split())

    if h1 == h2 == m1 == m2 == 0:
        break

    now = h1 * 60 + m1
    next = h2 * 60 + m2
    if next < now:
        next += 1440
    print(next - now)