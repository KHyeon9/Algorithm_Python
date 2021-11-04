a = list(map(int, input().split()))
a.sort()
n1 = a[1] - a[0]
n2 = a[2] - a[1]


if n1 == n2:
    print(a[2] + n1)

else:
    if n1 < n2:
        print(a[1] + n1)

    else:
        print(a[0] + n2)