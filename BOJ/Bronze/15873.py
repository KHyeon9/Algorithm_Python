a = list(map(int, input()))

if len(a) == 2:
    print(a[0] + a[1])

elif len(a) == 3:
    if a[1] == 0:
        print(10 + a[2])

    elif a[2] == 0:
        print(10 + a[0])
else:
    print("20")