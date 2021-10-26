x, l, r = map(int, input().split())

if x <= l <= r:
    print(l)

elif l <= x <= r:
    print(x)

elif l <= r <= x:
    print(r)