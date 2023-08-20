arr = [input() for _ in range(int(input()))]

res, max_h = [], 0
for i in range(5):
    h = 0
    for a in arr:
        if a[i] == "Y":
            h += 1

    if max_h < h:
        res = [i + 1]
        max_h = h
    elif max_h == h:
        res.append(i + 1)
print(*res, sep=",")

