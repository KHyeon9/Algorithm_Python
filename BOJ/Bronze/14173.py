x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

xmax = max(x1, x2, x3, x4)
ymax = max(y1, y2, y3, y4)
xmin = min(x1, x2, x3, x4)
ymin = min(y1, y2, y3, y4)

if xmax - xmin > ymax - ymin:
    print((xmax - xmin) ** 2)

else:
    print(( ymax - ymin) ** 2)
