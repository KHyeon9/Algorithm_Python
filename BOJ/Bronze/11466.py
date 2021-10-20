h, w = map(int, input().split())

if h > w:
    if h > w * 3:
        r = w

    elif h > w * 1.5:
        r = h / 3

    else:
        r = w / 2

else:
    if w > h * 3:
        r = h

    elif w > h * 1.5:
        r = w / 3

    else:
        r = h / 2

print(round(r, 3))