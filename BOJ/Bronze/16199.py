y, m, d = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if m2 > m:
    r = y2 - y

elif m2 == m:
    if d2 >= d:
        r = y2 - y

    else:
        r = y2 - y - 1

else:
    r = y2 - y - 1


print(r)
print(y2 - y + 1)
print(y2 - y)