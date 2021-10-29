n, l, d = map(int, input().split())

i = 1
r = 0

while i * d <= (l + 5) * n - 5:
    if l <= (i * d) % (l + 5) <= l + 4:
        r = i * d
        break
    else:
        i += 1

if r == 0:
    r = ((l + 5) * n - 5) // d + 1
    print(r * d)

else:
    print(r)