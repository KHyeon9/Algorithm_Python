while True:
    s, w, p = map(float, input().split())

    if s == w == p:
        break

    res = []

    if s <= 4.5 and w >= 150 and p >= 200:
        res.append("Wide Receiver")
    if s <= 6 and w >= 300 and p >= 500:
        res.append("Lineman")
    if s <= 5.0 and w >= 200 and p >= 300:
        res.append("Quarterback")
    if len(res) == 0:
        res.append("No positions")

    print(*res)